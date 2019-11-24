# Jupyterhub Access Token Service

The Jupyterhub Access Token Service serves an up to date access token for users. It is meant to run on a hub instance using the OAuthenticator.

## Setup

It must run with admin privileges to be able to access the auth_state. The `OAuthenticator.enable_auth_state` must be set to `True` to store the authentication state of the user.

To install, the following service definition can be added to your `jupyterhub_config.py`:

```
c.JupyterHub.services = [
    {
        'name': 'access-token-service',
        'admin': True,
        'command': ['access-token-service'],
    }
]
```
