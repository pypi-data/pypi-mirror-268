
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------

import requests.exceptions
import httpx

def raise_detailed_error(request_object):
	try:
		request_object.raise_for_status()
	except (httpx.HTTPError, requests.exceptions.HTTPError) as e:
		# raise detailed error message
		# TODO: Check if we get a { "error" : "Permission denied." } and handle automatically
		raise httpx.HTTPError(request_object.text) from e
