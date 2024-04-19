import json
import os
from prompt_toolkit import prompt

from depot_api.api.default_api import DefaultApi
from depot_api.api_client import ApiClient, Configuration


class DepotConfig(object):
    DEFAULT_CONFIG_FOLDER = '.depot'
    DEFAULT_CONFIG_FILE = 'config.json'

    def __init__(self, login: str, token: str, endpoint: str, email: str):
        config = Configuration(host=endpoint)
        config.access_token = token
        self.default_api = DefaultApi(ApiClient(config))

        self.login = login
        self.token = token
        self.endpoint = endpoint
        self.email = email

    def api(self) -> DefaultApi:
        return self.default_api

    def save(self):
        config_path = os.path.join(
            os.path.expanduser('~'),
            DepotConfig.DEFAULT_CONFIG_FOLDER,
            DepotConfig.DEFAULT_CONFIG_FILE)

        if not os.path.exists(os.path.dirname(config_path)):
            os.makedirs(os.path.dirname(config_path))

        with open(config_path, 'w') as file:
            file.write(json.dumps({
                'login': self.login,
                'token': self.token,
                'endpoint': self.endpoint,
                'email': self.email
            }))

    @staticmethod
    def default_config_path():
        return os.path.join(
            os.path.expanduser('~'),
            DepotConfig.DEFAULT_CONFIG_FOLDER,
            DepotConfig.DEFAULT_CONFIG_FILE)

    @classmethod
    def from_file(cls, filename: str) -> 'DepotConfig':
        if not os.path.exists(filename):
            return None

        with open(filename, 'r') as file:
            y = json.load(file)
            return cls(**y)

    @classmethod
    def default(cls) -> 'DepotConfig':
        config_path = os.path.join(cls.default_config_path())

        return cls.from_file(config_path)

    @staticmethod
    def create():
        if os.path.exists(DepotConfig.default_config_path()):
            # Ask if the user wants to login again
            r = prompt(
                'You are already logged in. Do you want to log in again? [y/N]: ')
            if r.lower() != 'y':
                return
            with open(DepotConfig.default_config_path(), 'r') as file:
                y = json.load(file)
            default_endpoint = y['endpoint']
            default_login = y['login']
        else:
            default_endpoint = 'https://depot.staging.codedepot.ai'
            default_login = None
        endpoint = prompt(
            f'Enter your API endpoint [{default_endpoint}]: ')
        if not endpoint:
            endpoint = default_endpoint

        if not default_login:
            username = prompt('Enter your login: ')
        else:
            username = prompt(f'Enter your login [{default_login}]: ')
            if not username:
                username = default_login

        # Check if the username is empty TODO: check if the username is valid
        if not username:
            print('Username is required')
            return None

        email = prompt('Enter your email: ')
        # Check if the username is empty TODO: check if the username is valid
        if not email:
            print('Email is required')
            return None

        password = prompt(
            f'Enter the password for {username}: ', is_password=True)
        print('endpoint: ', endpoint)
        default_api = DefaultApi(ApiClient(Configuration(host=endpoint)))

        response = default_api.login_token_post(
            username=email, password=password)
        print(response)

        config = DepotConfig(
            token=response['token'], endpoint=endpoint, login=username, email=email)
        config.save()
        print('The user is logged in, the token is stored at ~/.depot/config.json')
