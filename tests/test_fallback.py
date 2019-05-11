import logging
import os

import pytest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from bot.fallback import CustomFallbackPolicy


@pytest.fixture
def custom_fallback():
    return CustomFallbackPolicy()


def test_standard_featurizer(custom_fallback):
    response = custom_fallback._standard_featurizer()
    assert response == None


def test_should_fallback(custom_fallback):
    response = custom_fallback.should_fallback(1, "2")
    assert response == False
