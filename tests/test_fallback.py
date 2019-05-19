import logging

import pytest
import os,sys,inspect

from rasa_core import utils
from rasa_core.policies.policy import Policy
from rasa_core.domain import Domain
from rasa_core.trackers import DialogueStateTracker

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from bot.fallback import CustomFallbackPolicy
from bot.fallback import *

@pytest.fixture
def custom_tracker():
    return DialogueStateTracker("default", {})

@pytest.fixture
def custom_domain():
    return Domain({}, [], [], {}, ['action_default_fallback'], [])

@pytest.fixture
def custom_fallback():
    return CustomFallbackPolicy()

def test_standard_featurizer(custom_fallback):
    response = custom_fallback._standard_featurizer()
    assert response == None

def test_init_(custom_fallback):
    response = custom_fallback
    assert response.nlu_threshold == 0.6
    assert response.core_threshold == 0.6
    assert response.fallback_action_name == 'action_default_fallback'
    
def test_should_fallback1(custom_fallback):
	# high confidence
    response = custom_fallback.should_fallback(1, "2")
    assert response == False

	# low confidence
    response = custom_fallback.should_fallback(0.3, "2")
    assert response == True

	# high confidence + last action fallback
    response = custom_fallback.should_fallback(1.0, "action_default_fallback")
    assert response == False

	# low confidence + last action fallback
    response = custom_fallback.should_fallback(0.5, "action_default_fallback")
    assert response == False

	# high confidence + last action None
    response = custom_fallback.should_fallback(1.0, None)
    assert response == False

	# low confidence + last action None
    response = custom_fallback.should_fallback(0.4, None)
    assert response == False

def test_fallback_scores(custom_fallback, custom_domain):
    response = custom_fallback.fallback_scores(custom_domain)
    idx = custom_domain.index_for_action(custom_fallback.fallback_action_name)
    assert response[idx] == 1.2

def test_predict_action_probabilities(custom_fallback, custom_domain, custom_tracker):
    nlu_data = custom_tracker.latest_message.parse_data
    nlu_confidence = nlu_data["intent"].get("confidence", 1.0)
    idx = custom_domain.index_for_action(custom_fallback.fallback_action_name)

    if(custom_fallback.should_fallback(nlu_confidence, custom_tracker.latest_action_name)):
        response = custom_fallback.predict_action_probabilities(custom_tracker, custom_domain)
        assert response[idx] == 1.2
    else:
        response = custom_fallback.predict_action_probabilities(custom_tracker, custom_domain)
        assert response[idx] == 0.6

