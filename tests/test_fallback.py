import logging
import os

import unittest 

from bot.fallback import CustomFallbackPolicy




class TestFallback(unittest.TestCase):

    def test_standard_featurizer(self):
        response = CustomFallbackPolicy()._standard_featurizer()
        assert response == None


    def test_should_fallback(self):
        response = CustomFallbackPolicy().should_fallback(1, "2")
        assert response == False


if __name__ == '__main__':
    unittest.main()