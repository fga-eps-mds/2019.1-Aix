import logging

from rasa_core import utils, train, config
from validator import Validator
from rasa_core.agent import Agent
from rasa_core.run import AvailableEndpoints

logger = logging.getLogger(__name__)

utils.configure_colored_logging(loglevel='DEBUG')

import pytest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from bot.train import train_dialogue

def test_train_dialogue(domain_file, model_path, training_folder, policy_config):

    agent_train = train.train_dialogue_model(domain_file=domain_file,
                                      stories_file=training_folder,
                                      output_path=model_path,
                                      policy_config=policy_config,
                                      kwargs={'augmentation_factor': 20,
                                              'validation_split': 0.2, }
                                      )

    policies = config.load(policy_config)

    agent_to_compare = Agent(domain_file,
                  generator=AvailableEndpoints().nlg,
                  action_endpoint=AvailableEndpoints().action,
                  interpreter=None,
                  policies=policies)

    data_load_args, kwargs = utils.extract_args({'augmentation_factor': 20,
                                              'validation_split': 0.2, },
                                                {"use_story_concatenation",
                                                 "unique_last_num_states",
                                                 "augmentation_factor",
                                                 "remove_duplicates",
                                                 "debug_plots"})

    training_data = agent_to_compare.load_data(training_folder,
                                    exclusion_percentage=None,
                                    **data_load_args)
    agent_to_compare.train(training_data, **kwargs)
    agent_to_compare.persist(model_path, False)
    
    assert agent_to_compare == agent_train