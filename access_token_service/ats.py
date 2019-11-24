import json
import logging
import os

from jupyterhub.services.auth import HubAuthenticated
from tornado.httpclient import AsyncHTTPClient
import tornado.ioloop
from tornado.web import RequestHandler, Application, authenticated


class AccessTokenHandler(HubAuthenticated, RequestHandler):
    ''' Respond to Access Token requests. '''
    async def _request_token(self, username: str) -> str:
        user_endpoint = f'{self.hub_auth.api_url}/users/{username}'
        headers = {
            'Authorization': f'token {self.hub_auth.api_token}',
        }
        with AsyncHTTPClient as client:
            async with client.get(user_endpoint, headers=headers) as resp:
                return json.loads(resp)

    @authenticated
    async def get(self):
        user = self.get_current_user()
        logging.debug(user)
        user_json = await self._request_token(user['name'])
        logging.debug(user_json)
        return user_json['auth_state']['access_token']


def main():
    prefix = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', '')
    app = Application([
        (prefix + 'oauth_token', AccessTokenHandler),
    ])
    app.listen(8528)
    tornado.ioloop.IOLoop.current().start()
