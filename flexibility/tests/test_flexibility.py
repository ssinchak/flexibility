"""
Unit and regression test for the flexibility package.
"""

# Import package, test suite, and other packages as needed

import flexibility

import sys

def test_flexibility_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "flexibility" in sys.modules

   # test = stretch.canvas("hello")
def test_stretch():
    test = flexibility.stretch.canvas("hello")
    assert "h e l l o" == test
