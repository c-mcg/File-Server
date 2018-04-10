from .base import Endpoint

import json

class UserEndpoint(Endpoint):

    def __init__(self):
        self.needs_auth = True

    def handle_request(self, request_handler, server, account, data):

        if account is None:
            return {"error": "Needs auth"}

        return {"name": account.name, "refresh_rate": account.settings["refresh_rate"]}