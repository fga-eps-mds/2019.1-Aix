import logging
import os

import unittest 

from bot.connector import RocketChatBot, RocketchatHandleMessages, RocketChatInput


# class TestRocketChatInput(unittest.TestCase):

#     # initialization logic for the test suite declared in the test module
#     # code that is executed before all tests in one test run
#     @classmethod
#     def setUpClass(cls):
#         pass

#     # clean up logic for the test suite declared in the test module
#     # code that is executed after all tests in one test run
#     @classmethod
#     def tearDownClass(cls):
#         pass

#     # initialization logic
#     # code that is executed before each test
#     def setUp(self):
#         self.configs = {
#             'user': os.getenv('ROCKETCHAT_BOT_USERNAME'),
#             'password': os.getenv('ROCKETCHAT_BOT_PASSWORD'),
#             'server_url': os.getenv('ROCKETCHAT_URL'),
#         }

#         rocket_chat = RocketChatInput(
#             user=self.configs['user'],
#             password=self.configs['password'],
#             server_url=self.configs['server_url']
#         )


#     # clean up logic
#     # code that is executed after each test
#     def tearDown(self):
#         pass

#     def test_login_rocketchat(self):
#         pass


class TestRocketChatBot(unittest.TestCase):


    # initialization logic
    # code that is executed before each test
    def setUp(self):
        self.configs = {
            'user': os.getenv('ROCKETCHAT_BOT_USERNAME'),
            'password': os.getenv('ROCKETCHAT_BOT_PASSWORD'),
            'server_url': os.getenv('ROCKETCHAT_URL'),
        }


    def test_login_rocketchat(self):
        rocket_chat = RocketChatBot(
            user=self.configs['user'],
            password=self.configs['password'],
            server=self.configs['server_url']
        )

        assert rocket_chat.logged_in


if __name__ == '__main__':
    unittest.main()