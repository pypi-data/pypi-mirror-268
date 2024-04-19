import asyncio
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


import time
import random
import pytest
from contextlib import asynccontextmanager


@pytest.fixture(scope='function')
def db_sa(db):
	# To make it easier to test, we keep the test restricted to firebase_tests
	# Because of the current mutations on calls, we return it as a function.
	name = 'test_%05d' % random.randint(0, 99999)
	yield lambda: db().child(name)

@asynccontextmanager
async def make_append_stream(db):
	l = []

	async def coro():
		async for ev in db.stream():
			l.append(ev)

	# wait a bit before connecting so we don't get events from previous tests
	await asyncio.sleep(0.5)
	async with asyncio.TaskGroup() as tg:
		task = tg.create_task(coro())
		try:
			yield l
		finally:
			task.cancel()





class TestSimpleGetAndPut:
	async def test_simple_get(self, db_sa):
		data = await db_sa().get()
		assert data.val() is None

	async def test_put_succeed(self, db_sa):
		assert await db_sa().set(True)

	async def test_put_then_get_keeps_value(self, db_sa):
		await db_sa().set("some_value")
		data = await db_sa().get()
		assert data.val() == "some_value"

	async def test_put_dictionary(self, db_sa):
		v = dict(a=1, b="2", c=dict(x=3.1, y="3.2"))
		await db_sa().set(v)

		data = await db_sa().get()
		assert data.val() == v

	@pytest.mark.skip
	async def test_put_deeper_dictionary(self, db_sa):
		v = {'1': {'11': {'111': 42}}}
		await db_sa().set(v)

		# gives: assert [None, {'11': {'111': 42}}] == {'1': {'11': {'111': 42}}}
		data = await db_sa().get()
		assert data.val() == v


class TestChildNavigation:
	async def test_get_child_none(self, db_sa):
		data = await db_sa().child('lorem').get()
		assert data.val() is None

	async def test_get_child_after_pushing_data(self, db_sa):
		await db_sa().set({'lorem': "a", 'ipsum': 2})

		data = await db_sa().child('lorem').get()
		assert data.val() == "a"
		data = await db_sa().child('ipsum').get()
		assert data.val() == 2

	async def test_update_child(self, db_sa):
		await db_sa().child('child').update({'c1/c11': 1, 'c1/c12': 2, 'c2': 3})

		data = await db_sa().child('child').child('c1').get()
		assert data.val() == {'c11': 1, 'c12': 2}
		data = await db_sa().child('child').child('c2').get()
		assert data.val() == 3

	async def test_path_equivalence(self, db_sa):
		await db_sa().set({'1': {'11': {'111': 42}}})

		assert (await db_sa().child('1').child('11').child('111').get()).val() == 42
		assert (await db_sa().child('1/11/111').get()).val() == 42
		assert (await db_sa().child('1', '11', '111').get()).val() == 42
		assert (await db_sa().child(1, '11', '111').get()).val() == 42


class TestStreaming:
	async def test_does_initial_call(self, db_sa):
		async with make_append_stream(db_sa()) as l:
			await asyncio.sleep(2)
			assert len(l) == 1

	async def test_responds_to_update_calls(self, db_sa):
		async with make_append_stream(db_sa()) as l:
			# ev 1
			set_data = {"1": "a", "1_2": "b"}
			await db_sa().set(set_data)

			# ev 2
			# wait before update() or it will group the events
			patch_data = {"2": "c"}
			await asyncio.sleep(1)
			await db_sa().update(patch_data)

			# ev 3
			push_data = "3"
			await db_sa().push(push_data)

			await asyncio.sleep(2)
			events = l[:]  # copy

			# race condition
			if len(events) == 4 and events[0].data is None:
				events = events[1:]

			assert len(events) == 3

			assert events[0].event == 'put'
			assert events[0].data == set_data

			assert events[1].event == 'patch'
			assert events[1].data == patch_data

			assert events[2].event == 'put'
			assert events[2].data == push_data


class TestConditionalRequest:
	async def test_conditional_set_succeed(self, db_sa):
		etag = await db_sa().get_etag()
		result = await db_sa().conditional_set({'1': 'a'}, etag)

		data = await db_sa().child('1').get()
		assert data.val() == 'a'

	async def test_conditional_set_fail(self, db_sa):
		etag = '{}123'.format(await db_sa().get_etag())
		result = await db_sa().conditional_set({'2': 'b'}, etag)

		assert 'ETag' in result

	async def test_conditional_remove_succeed(self, db_sa):
		etag = await db_sa().child('1').get_etag()
		result = await db_sa().child('1').conditional_remove(etag)

		data = await db_sa().child('1').get()
		assert data.val() is None

	async def test_conditional_remove_fail(self, db_sa):
		etag = '{}123'.format(await db_sa().get_etag())
		result = await db_sa().conditional_remove(etag)

		assert 'ETag' in result
