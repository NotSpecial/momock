# -*- coding: utf-8 -*-

from eve.auth import TokenAuth

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'test'

API_KEY = 'supersecretkey12'


class APIKeyAuth(TokenAuth):
    """Fake api key auth."""

    def check_auth(self, token, allowed_roles, resource, method):
        """Check auth as if API token.

        For simplicity the token is hardcoded above. In a real application
        this would be the API_KEY provided by the API.
        (Therefore in the application it has to be replacable easily.)
        """
        return token == API_KEY


DOMAIN = {
    'users': {
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
        'schema': {
            'firstname': {
                'type': 'string',
                'maxlength': 50,
                'empty': False,
                'nullable': False,
                'required': True},
            'lastname': {
                'type': 'string',
                'maxlength': 50,
                'empty': False,
                'nullable': False,
                'required': True},
            'rfid': {
                'type': 'string',
                'maxlength': 6,
                'empty': False,
                'unique': True,
                'required': True,
                'nullable': False},

        }
    },
    'purchases': {
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
        'authentication': APIKeyAuth,
        'schema': {
            'user_id': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'users',
                    'field': '_id',
                    'embeddable': True},
                'required': True,
                'unique': False},
            'type': {
                'required': False,
                'unique': False,
                'type': 'string',
                'maxlength': 5,
                'nullable': True},
            'slot': {
                'required': False,
                'unique': False,
                'type': 'integer',
                'nullable': True},
            'timestamp': {
                'required': False,
                'unique': False,
                'type': 'datetime',
                'nullable': True},
        }
    }
}
