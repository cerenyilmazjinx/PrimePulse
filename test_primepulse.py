# test_primepulse.py
"""
Tests for PrimePulse module.
"""

import unittest
from primepulse import PrimePulse

class TestPrimePulse(unittest.TestCase):
    """Test cases for PrimePulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimePulse()
        self.assertIsInstance(instance, PrimePulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimePulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
