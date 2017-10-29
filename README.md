# disk-usage
Calculate disk usage of given directory

Compatible with Python 2 and Python 3.

### Basic Usage
To list size of all files within the directory `tmp`, enter <br />
`$ python get_disk_usage.py --mnt /tmp`

### Running unit tests
1. Add disk_usage.py file to `PYTHONPATH` <br />
`$ export PYTHONPATH=$PYTHONPATH:/path/to/disk_usage.py`

2. Run unit tests <br />
`$ python test_disk_usage.py`

NOTE: System level testing has been executed with python 2.7 and python 3.6.3
