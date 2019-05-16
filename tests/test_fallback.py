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

def test_should_fallback1(custom_fallback):
	# high confidence
    response = custom_fallback.should_fallback(1, "2")
    assert response == False

def test_should_fallback2(custom_fallback):
	# low confidence
    response = custom_fallback.should_fallback(0.3, "2")
    assert response == True

def test_should_fallback3(custom_fallback):
	# high confidence + last action fallback
    response = custom_fallback.should_fallback(1.0, "action_default_fallback")
    assert response == False

def test_should_fallback4(custom_fallback):
	# low confidence + last action fallback
    response = custom_fallback.should_fallback(0.5, "action_default_fallback")
    assert response == False

def test_should_fallback5(custom_fallback):
	# high confidence + last action None
    response = custom_fallback.should_fallback(1.0, None)
    assert response == False

def test_should_fallback6(custom_fallback):
	# low confidence + last action None
    response = custom_fallback.should_fallback(0.4, None)
    assert response == False


