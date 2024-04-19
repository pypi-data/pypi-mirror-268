#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


import pytest
import asyncio

from firebase import initialize_app
from tests import config
from tests.config import (
	TEST_USER_EMAIL, TEST_USER_PASSWORD,
	TEST_USER_EMAIL_2, TEST_USER_PASSWORD_2
)

@pytest.fixture(scope='session')
def event_loop():
	loop = asyncio.get_event_loop()
	loop.close = lambda: None
	yield loop

@pytest.fixture(scope='session')
async def client_app():
	yield initialize_app(config.SIMPLE_CONFIG)

@pytest.fixture(scope='session')
async def service_app():
	yield initialize_app(config.SERVICE_CONFIG)

@pytest.fixture(scope='session')
def auth(client_app):
	return client_app.auth()

@pytest.fixture(scope='session')
def auth_admin(service_app):
	return service_app.auth()

@pytest.fixture(scope='session')
async def db(service_app):
	# To make it easier to test, we keep the test restricted to firebase_tests
	# Because of the current mutations on calls, we return it as a function.
	try:
		yield lambda: service_app.database().child('firebase_tests')
	finally:
		await service_app.database().child('firebase_tests').remove()

@pytest.fixture(scope='session')
def email():
	return TEST_USER_EMAIL

@pytest.fixture(scope='session')
def email_2():
	return TEST_USER_EMAIL_2

@pytest.fixture(scope='session')
def ds(client_app):
	return client_app.firestore()

@pytest.fixture(scope='session')
def ds_admin(service_app):
	return service_app.firestore()

@pytest.fixture(scope='session')
def password():
	return TEST_USER_PASSWORD

@pytest.fixture(scope='session')
def password_2():
	return TEST_USER_PASSWORD_2

@pytest.fixture(scope='session')
def storage(client_app):
	return client_app.storage()

@pytest.fixture(scope='session')
def storage_admin(service_app):
	return service_app.storage()
