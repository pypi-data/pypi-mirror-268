import json
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


import re
from dataclasses import dataclass

import httpx
import time

from httpx_sse import aconnect_sse
from stamina import retry

from firebase.database._keep_auth_session import KeepAuthSession

# adapted from https://pypi.org/project/httpx-sse examples
def iter_sse_retrying(url, build_headers):
	last_event_id = ""
	reconnection_delay = 0.0
	session = KeepAuthSession()

	# `stamina` will apply jitter and exponential backoff on top of
	# the `retry` reconnection delay sent by the server.
	@retry(on=httpx.ReadError)
	async def _iter_sse():
		nonlocal last_event_id, reconnection_delay

		time.sleep(reconnection_delay)
		headers = build_headers()

		if last_event_id:
			headers["Last-Event-ID"] = last_event_id

		async with aconnect_sse(session, "GET", url, headers=headers) as event_source:
			async for sse in event_source.aiter_sse():
				last_event_id = sse.id

				if sse.retry is not None:
					reconnection_delay = sse.retry / 1000

				data = json.loads(sse.data)
				yield Event(id=sse.id, event=sse.event, path=data['path'], data=data['data'])

	return _iter_sse()

@dataclass
class Event:
	id: str
	event: str
	path: str
	data: dict[str, str]