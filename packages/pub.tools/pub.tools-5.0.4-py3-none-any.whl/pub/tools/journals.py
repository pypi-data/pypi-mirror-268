import csv
import dataclasses
import json
import logging
import os

import requests

logger = logging.getLogger('pub.tools')

JOURNAL_DATA_DIR = os.path.join(os.path.expanduser('~'), '.pubmed')
JOURNAL_DATA_FILE = os.path.join(JOURNAL_DATA_DIR, 'journals.json')

base_path = os.path.dirname(os.path.realpath(__file__))


@dataclasses.dataclass(frozen=True)
class JournalData:
    title: str
    abbr: str
    pissn: str
    eissn: str
    publisher: str
    locator: str
    latest: str
    earliest: str
    freeaccess: str
    openaccess: str
    participation: str
    deposit: str
    url: str


@dataclasses.dataclass(frozen=True)
class AllJournalData:
    atoj: dict[str, str]  # abbreviation -> journal
    jtoa: dict[str, str]  # journal -> abbreviation
    dates: dict[str, tuple[str, str]]  # start and end dates
    full: dict[str, JournalData]


def fetch_journals() -> AllJournalData:
    """
    Gets all journal info from NCBI. This will be cached

    :return: dict
    """
    url = 'https://www.ncbi.nlm.nih.gov/pmc/journals/?format=csv'
    response = requests.get(url, timeout=5.0)
    if response.status_code == 200:

        _atoj = {}
        _jtoa = {}
        dates = {}
        full = {}
        reader = csv.reader(response.text.split('\n'))
        header = False

        for row in reader:
            if not header:
                header = True
                continue
            if row:
                title, abbr, pissn, eissn, publisher, locator, latest, earliest, freeaccess, \
                    openaccess, participation, deposit, url = row
                latest = latest.split(';')[-1]
                earliest = earliest.split(';')[-1]
                _atoj[abbr.lower()] = title
                _jtoa[title.lower()] = abbr
                dates[abbr.lower()] = (earliest, latest)
                full[abbr.lower()] = JournalData(*row)
        return AllJournalData(
            atoj=_atoj,
            jtoa=_jtoa,
            dates=dates,
            full=full
        )


journals = fetch_journals()
try:
    os.makedirs(JOURNAL_DATA_DIR)
except FileExistsError:
    pass
if journals:
    with open(JOURNAL_DATA_FILE, 'w') as f:
        json.dump(dataclasses.asdict(journals), f)
else:
    logger.warning('Falling back to static file for journal/abbreviation information.')
    with open(os.path.join(base_path, 'journals.json'), 'r') as rf:
        with open(JOURNAL_DATA_FILE, 'w') as wf:
            json.dump(rf.read(), wf)


def get_source(cache: bool = False) -> AllJournalData:
    """ get source dictionary of journals and abbreviations

    """
    global journals
    if not cache:
        try:
            journals = fetch_journals()
        except requests.exceptions.HTTPError:
            pass
        except requests.exceptions.ProxyError:
            pass
    return journals


def get_abbreviations(cache: bool = True) -> dict[str, str]:
    """ get the mapping for abbreviation -> journal title

    """
    return get_source(cache).atoj


def get_journals(cache: bool = True) -> dict[str, str]:
    """ get the mapping for journal -> abbreviation

    """
    return get_source(cache).jtoa


def get_dates(cache: bool = True) -> dict[str, tuple[str, str]]:
    """ get date range per journal abbreviation

    :param cache:
    :return: dict
    """
    return get_source(cache).dates


def atoj(abbrv: str, cache: bool = True) -> str:
    """ get journal title from abbreviation

    """
    data = get_abbreviations(cache)
    return data.get(abbrv.lower())


def jtoa(journal: str, cache: bool = True) -> str:
    """ get abbreviation from journal title

    :param journal:
    :param cache:
    :return: str
    """
    data = get_journals(cache)
    return data.get(journal.lower())


def atodates(abbrv: str, cache: bool = True) -> tuple[str, str]:
    """ get date range from journal abbreviation

    :param abbrv:
    :param cache:
    :return:
    """
    data = get_dates(cache)
    return data.get(abbrv.lower())
