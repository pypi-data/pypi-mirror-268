
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


import httpx


def _custom_request():
    """ Async Session using httpx.

    :return: async session
    :rtype: httpx.AsyncClient
    """

    return httpx.AsyncClient()
