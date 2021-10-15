MAJOR = 2
MINOR = 0
MICRO = 'dev'

dev_labels = ['dev', 'alpha', 'beta']

if isinstance(MICRO, str):
    if MICRO in dev_labels:
        version = '{:d}.{:d}{:s}'.format(MAJOR, MINOR, MICRO)
    elif MICRO not in dev_labels:
        version = '{:d}.{:d}.{:s}'.format(MAJOR, MINOR, MICRO)

elif isinstance(MICRO, int):
    version = '{:d}.{:d}.{:d}'.format(MAJOR, MINOR, MICRO)

author = "M. Skocic"
__author__ = 'M. Skocic'

__all__ = ['__package_name__',
           '__version__',
           '__author__',
           '__author_email__',
           '__maintainer__',
           '__maintainer_email__',
           '__copyright__',
           '__license__']

__package_name__ = "PyPEC3"
__version__ = "2.0"
__author__ = "Milan Skocic"
__author_email__ = "milan.skocic@gmail.com"
__maintainer__ = __author__
__maintainer_email__ = __author_email__
__copyright__ = 'Copyright (C) 2014-2021 ' + __author__
__license__ = 'GNU General Public License v3 (GPLv3)'
