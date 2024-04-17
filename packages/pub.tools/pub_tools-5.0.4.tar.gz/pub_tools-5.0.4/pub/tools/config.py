import importlib.metadata

NO_VALUE = "<<blank>>"  # special marker
MAX_PUBS = 9000
# Biopython will put a count greater than 200 ids into a post, so we don't need to worry about request size
# But there does seem to be a 9999 limit either from Biopython or from NCBI


VERSION = importlib.metadata.version('pub.tools')
