# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest




class TestArray(unittest.TestCase):

    def test_array(self):
        pass


    

if __name__ == '__main__':
    unittest.main()
