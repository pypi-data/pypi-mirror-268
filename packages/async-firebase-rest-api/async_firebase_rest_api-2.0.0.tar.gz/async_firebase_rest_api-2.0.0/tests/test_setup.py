
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


import pytest

async def test_setup_auth(client_app):
	auth = client_app.auth()
	user = await auth.sign_in_anonymous()

	assert await auth.delete_user_account(user['idToken'])


async def test_setup_auth_admin(service_app):
	auth = service_app.auth()
	user = await auth.sign_in_anonymous()

	assert await auth.delete_user_account(user['idToken'])


async def test_setup_db(service_app):
	db = service_app.database().child('firebase_tests')

	assert await db.get()


async def test_setup_storage(client_app):
	storage = client_app.storage()

	with pytest.raises(AttributeError) as exc_info:
		_ = [f async for f in storage.list_files()]
	assert 'bucket' in str(exc_info.value)


async def test_setup_storage_admin(service_app):
	storage = service_app.storage()

	async for _ in storage.list_files():
		break
