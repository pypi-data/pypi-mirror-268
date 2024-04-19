import contextlib


def get_tokens():
    username = None
    access_token = None
    refresh_token = None
    id_token = None
    with contextlib.suppress(FileNotFoundError):
        with open('.env', 'r') as file:
            for line in file:
                with contextlib.suppress(ValueError):
                    key, value = line.strip().split('=', 1)
                    if key.lower() == 'username':
                        username = value
                    if key.lower() == 'access_token':
                        access_token = value
                    elif key.lower() == 'refresh_token':
                        refresh_token = value
                    elif key.lower() == 'id_token':
                        id_token = value

    if username and access_token and refresh_token and id_token:
        return username, access_token, refresh_token, id_token

    raise ValueError('Tokens not provided')
