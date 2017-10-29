import logging
import os
from pprint import pprint
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def determine_valid_dirname(dirname):
    """
    Check the following criteria to ensure 'dirname' is valid
        - dirname exists
        - dirname is a directory

    If criteria not met, raise an error

    """
    logger.info('Validating mount point')

    # Check dirname exists
    if not os.path.exists(dirname):
        logger.error('Path (%s) does not exist' % dirname)
        sys.exit(1)

    # Check dirname is a directory
    if not os.path.isdir(dirname):
        logger.error('Path (%s) is not a directory' % dirname)
        sys.exit(1)


def get_disk_usage(dirname):
    """
    Gets all files within 'dirname' and determines disk usage

    Returns dictionary of files, e.g

    {
        "files": [
            {"/tmp/foo": 1000},
            {"/tmp/bar": 1000000},
            {"/tmp/buzzz": 42}
            ]
    }

    """
    logger.info('Getting size of files')

    # Initialize disk usage dict
    filesizes = []
    # Walk along every file within 'dirname'
    for root, dirs, files in os.walk(dirname, topdown=False):
        for name in files:
            # Define filename
            fname = os.path.join(root, name)
            # Get size of file (in bytes)
            fsize = os.path.getsize(fname)
            # Append info to list
            filesizes.append({fname: fsize})

    # Return disk usage in expected format
    return {'files': filesizes}


if __name__ == '__main__':
    """
    Take a mount point as an input, return a
    list of all files and their disk usage in bytes

    """
    # Read in arguments
    import argparse
    parser = argparse.ArgumentParser(description='Disk Usage')
    parser.add_argument('--mnt', dest='mnt', action='store',
            required=True, help='Mount point')
    args = parser.parse_args()

    # Check input
    determine_valid_dirname(args.mnt)

    # Get disk usage
    du = get_disk_usage(args.mnt)

    # Print out disk usage
    pprint(du)
