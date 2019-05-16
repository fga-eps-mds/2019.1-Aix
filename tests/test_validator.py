import logging
import os,sys,inspect

import pytest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from bot.validator import str2bool
from bot.validator import Validator

@pytest.fixture
#return validator class
def validator():
    return Validator

#function str2bool
def test_str2bool(validator):
    assert str2bool('yes') == True
    assert str2bool('no') == False

#function search in Validator class
def test_search(validator):
    assert validator.search(validator(), ['este','é','um', 'teste', 'unitário'], 'teste') == True
    assert validator.search(validator(),['este','é','um', 'teste', 'unitário'], 'opa') == False