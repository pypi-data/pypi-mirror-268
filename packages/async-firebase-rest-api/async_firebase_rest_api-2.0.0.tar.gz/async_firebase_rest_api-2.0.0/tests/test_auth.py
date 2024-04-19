#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


import pytest
import httpx


class TestAuth:

	user = None
	anonymous_user = None

	async def test_sign_in_with_non_existing_account_email_and_password(self, auth, email, password):
		with pytest.raises(httpx.HTTPError) as exc_info:
			await auth.sign_in_with_email_and_password(email, password)
		assert "INVALID_LOGIN_CREDENTIALS" in str(exc_info.value)

	async def test_create_user_with_email_and_password(self, auth, email, password):
		assert await auth.create_user_with_email_and_password(email, password)

	async def test_create_user_with_existing_email_and_password(self, auth, email, password):
		with pytest.raises(httpx.HTTPError) as exc_info:
			await auth.create_user_with_email_and_password(email, password)
		assert "EMAIL_EXISTS" in str(exc_info.value)

	async def test_sign_in_with_email_and_wrong_password(self, auth, email):
		with pytest.raises(httpx.HTTPError) as exc_info:
			await auth.sign_in_with_email_and_password(email, 'WrongPassword123')
		assert "INVALID_LOGIN_CREDENTIALS" in str(exc_info.value)

	async def test_sign_in_with_email_and_password(self, auth, email, password):
		user = await auth.sign_in_with_email_and_password(email, password)
		self.__class__.user = user
		assert user

	async def test_sign_in_anonymous(self, auth):
		user = await auth.sign_in_anonymous()
		self.__class__.anonymous_user = user
		assert user

	async def test_create_custom_token(self, auth):
		with pytest.raises(AttributeError):
			auth.create_custom_token('CreateCustomToken1')

	async def test_create_custom_token_with_claims(self, auth):
		with pytest.raises(AttributeError):
			auth.create_custom_token('CreateCustomToken2', {'premium': True})

	async def test_sign_in_with_custom_token(self, auth):
		with pytest.raises(httpx.HTTPError):
			await auth.sign_in_with_custom_token(None)

	async def test_refresh(self, auth):
		assert await auth.refresh(self.__class__.user.get('refreshToken'))

	async def test_get_account_info(self, auth):
		assert await auth.get_account_info(self.__class__.user.get('idToken'))

	async def test_send_email_verification(self, auth):
		assert await auth.send_email_verification(self.__class__.user.get('idToken'))

	async def test_send_password_reset_email(self, auth):
		assert await auth.send_password_reset_email(self.__class__.user.get('email'))

	@pytest.mark.xfail
	async def test_verify_password_reset_code(self, auth):
		assert await auth.verify_password_reset_code('123456', 'NewTestPassword123')


	async def test_change_email(self, auth, email_2, password):
		with pytest.raises(httpx.HTTPError) as exc_info:
			await auth.change_email(self.__class__.user.get('idToken'), email_2)
		assert "OPERATION_NOT_ALLOWED" in str(exc_info.value)

	async def test_change_password(self, auth,email, password_2):
		user = await auth.change_password(self.__class__.user.get('idToken'), password_2)
		self.__class__.user = None

		assert user
		assert self.__class__.user is None

		user = await auth.sign_in_with_email_and_password(email, password_2)
		self.__class__.user = user

		assert user

	async def test_update_profile_display_name(self, auth):
		new_name = 'Test User'
		user = await auth.update_profile(self.__class__.user.get('idToken'), display_name=new_name)
		assert user
		assert new_name == user['displayName']

	async def test_set_custom_user_claims(self, auth):
		with pytest.raises(AttributeError) as exc_info:
			await auth.set_custom_user_claims(self.__class__.user.get('localId'), {'premium': True})
			await auth.set_custom_user_claims(self.__class__.anonymous_user.get('localId'), {'premium': True})

		assert "'NoneType' object has no attribute 'valid'" in str(exc_info.value)

	async def test_verify_id_token(self, auth):
		with pytest.raises(KeyError) as exc_info:
			claims = await auth.verify_id_token(self.__class__.user.get('idToken'))
			_ = claims['premium']
		assert "'premium'" in str(exc_info.value)

		with pytest.raises(KeyError) as exc_info:
			claims = await auth.verify_id_token(self.__class__.anonymous_user.get('idToken'))
			_ = claims['premium']
		assert "'premium'" in str(exc_info.value)

	async def test_delete_user_account(self, auth):
		assert await auth.delete_user_account(self.__class__.user.get('idToken'))
		assert await auth.delete_user_account(self.__class__.anonymous_user.get('idToken'))


class TestAuthAdmin:

	user = None
	anonymous_user = None
	custom_token = None
	custom_token_with_claims = None
	custom_user = None
	custom_user_with_claims = None

	async def test_sign_in_with_non_existing_account_email_and_password(self, auth_admin, email, password):
		with pytest.raises(httpx.HTTPError) as exc_info:
			await auth_admin.sign_in_with_email_and_password(email, password)
		assert "INVALID_LOGIN_CREDENTIALS" in str(exc_info.value)

	async def test_create_user_with_email_and_password(self, auth_admin, email, password):
		assert await auth_admin.create_user_with_email_and_password(email, password)

	async def test_create_user_with_existing_email_and_password(self, auth_admin, email, password):
		with pytest.raises(httpx.HTTPError) as exc_info:
			await auth_admin.create_user_with_email_and_password(email, password)
		assert "EMAIL_EXISTS" in str(exc_info.value)

	async def test_sign_in_with_email_and_wrong_password(self, auth_admin, email):
		with pytest.raises(httpx.HTTPError) as exc_info:
			await auth_admin.sign_in_with_email_and_password(email, 'WrongPassword123')
		assert "INVALID_LOGIN_CREDENTIALS" in str(exc_info.value)

	async def test_sign_in_with_email_and_password(self, auth_admin, email, password):
		user = await auth_admin.sign_in_with_email_and_password(email, password)
		self.__class__.user = user
		assert user

	async def test_sign_in_anonymous(self, auth_admin):
		user = await auth_admin.sign_in_anonymous()
		self.__class__.anonymous_user = user
		assert user

	async def test_create_custom_token(self, auth_admin):
		token = auth_admin.create_custom_token('CreateCustomToken1')
		self.__class__.custom_token = token
		assert token

	async def test_create_custom_token_with_claims(self, auth_admin):
		token = auth_admin.create_custom_token('CreateCustomToken2', {'premium': True})
		self.__class__.custom_token_with_claims = token
		assert token

	async def test_sign_in_with_custom_token(self, auth_admin):
		user1 = await auth_admin.sign_in_with_custom_token(self.__class__.custom_token)
		user2 = await auth_admin.sign_in_with_custom_token(self.__class__.custom_token_with_claims)

		self.__class__.custom_user = user1
		self.__class__.custom_user_with_claims = user2

		assert user1
		assert user2

	async def test_get_account_info(self, auth_admin):
		assert await auth_admin.get_account_info(self.__class__.user.get('idToken'))

	async def test_send_email_verification(self, auth_admin):
		assert await auth_admin.send_email_verification(self.__class__.user.get('idToken'))

	async def test_send_password_reset_email(self, auth_admin):
		assert await auth_admin.send_password_reset_email(self.__class__.user.get('email'))

	@pytest.mark.xfail
	async def test_verify_password_reset_code(self, auth_admin):
		assert await auth_admin.verify_password_reset_code('123456', 'NewTestPassword123')

	async def test_update_profile_display_name(self, auth_admin):
		new_name = 'Test User'
		user = await auth_admin.update_profile(self.__class__.user.get('idToken'), display_name=new_name)
		assert user
		assert new_name == user['displayName']

	async def test_set_custom_user_claims(self, auth_admin):
		await auth_admin.set_custom_user_claims(self.__class__.user.get('localId'), {'premium': True})
		await auth_admin.set_custom_user_claims(self.__class__.anonymous_user.get('localId'), {'premium': True})

	async def test_refresh(self, auth_admin):
		self.__class__.user = await auth_admin.refresh(self.__class__.user.get('refreshToken'))
		self.__class__.custom_user = await auth_admin.refresh(self.__class__.custom_user.get('refreshToken'))
		self.__class__.anonymous_user = await auth_admin.refresh(self.__class__.anonymous_user.get('refreshToken'))

	async def test_verify_id_token(self, auth_admin):
		claims = await auth_admin.verify_id_token(self.__class__.user.get('idToken'))
		assert claims['premium'] is True

		claims = await auth_admin.verify_id_token(self.__class__.anonymous_user.get('idToken'))
		assert claims['premium'] is True

		claims = await auth_admin.verify_id_token(self.__class__.custom_user_with_claims.get('idToken'))
		assert claims['premium'] is True

		with pytest.raises(KeyError) as exc_info:
			claims = await auth_admin.verify_id_token(self.__class__.custom_user.get('idToken'))
			_ = claims['premium']
		assert "'premium'" in str(exc_info.value)

	async def test_delete_user_account(self, auth_admin):
		assert await auth_admin.delete_user_account(self.__class__.user.get('idToken'))
		assert await auth_admin.delete_user_account(self.__class__.anonymous_user.get('idToken'))
		assert await auth_admin.delete_user_account(self.__class__.custom_user.get('idToken'))
		assert await auth_admin.delete_user_account(self.__class__.custom_user_with_claims.get('idToken'))
