
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


import httpx


class KeepAuthSession(httpx.AsyncClient):
	"""
	A session that doesn't drop Authentication on redirects between domains.
	"""

	def _redirect_headers(self, request, url, method):
		headers = super()._redirect_headers(request, url, method)
		# keep the Authorization header on redirects
		if "Authorization" in request.headers:
			headers["Authorization"] = request.headers["Authorization"]
		return headers


