import os
import shutil
import unittest

import get_disk_usage

class DiskUsageTestCases(unittest.TestCase):

    def setUp(self):
        # Define testdir
        self.testdir = 'testdir'

    def tearDown(self):
        # Cleanup 'testdir', if present
        if os.path.exists(self.testdir):
            shutil.rmtree(self.testdir)

    def test_determine_valid_dirname_valid(self):
        """ Assert function does not raise error when valid dirname an input"""
        # Get directory the test script is in...
        dirname = os.path.dirname(os.path.abspath(__file__))
        # Call function
        get_disk_usage.determine_valid_dirname(dirname)

    def test_determine_valid_dirname_doesnotexist(self):
        """ Assert function raises error when dirname does not exist"""
        # Define path that does not exist
        dirname = '/pathdoesnotexist'
        # Assert SystemExit raised
        with self.assertRaises(SystemExit) as err:
            get_disk_usage.determine_valid_dirname(dirname)

    def test_determine_valid_dirname_file(self):
        """ Assert function does not raise error when valid dirname an input"""
        # Get directory the test script is in...
        filename = os.path.abspath(__file__)

        # Assert SystemExit raised
        with self.assertRaises(SystemExit) as err:
            get_disk_usage.determine_valid_dirname(filename)

    def test_get_disk_usage_valid(self):
        """ Assert function correctly  """
        # Create testdir
        os.mkdir(self.testdir)
        # Create file with size 'fsize' (in bytes)
        fname = os.path.join(self.testdir,'test.txt')
        fsize = 100
        with open(fname, "wb") as fp:
            fp.seek((100) - 1)
            fp.write('\0')
        # Define the expected disk usage
        du_exp = {'files': [
                {fname: fsize}
            ]}

        du = get_disk_usage.get_disk_usage(self.testdir)
        self.assertEqual(du, du_exp)


if __name__ == "__main__":

    # Run individual test
    #suite = unittest.TestSuite()
    #suite.addTest(DiskUsageTestCases('test_determine_fmap_intendedfor_epi_i'))
    #unittest.TextTestRunner().run(suite)

    unittest.main()
    run_module_suite()
