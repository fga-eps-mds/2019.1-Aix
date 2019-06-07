import pytest
import os
import sys
import inspect
import api_uva




def test_get_params():
    api_uva.get_params()

def test_get_soup():
    api_uva.get_soup()

def test make_login():
    api_uva.make_login()

def test_get_code(path):
    api_uva.get_code()

def test_get_problem():
    api_uva.get_problem()

def test_get_problem_by_id():
    api_uva.get_problem_by_id()

def test_get_problem_by_number():
    api_uva.get_problem_by_number()

def test_submeter_um_problema():
    api_uva.submeter_um_problema()

def test_username_para_userid():
    api_uva.username_para_userid()

def test_resultado_ultima_submissao():
    api_uva.resultado_ultima_submissao()