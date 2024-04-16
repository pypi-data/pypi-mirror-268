import pyrebase
from requests import HTTPError, RequestException

from trail.exception.auth import InvalidCredentialsException
from trail.exception.trail import TrailUnavailableException
from trail.libconfig import libconfig

_user_id_token = None


def authenticate(username, password):
    firebase = pyrebase.initialize_app(
        {
            "apiKey": libconfig.FIREBASE_API_KEY,
            "authDomain": libconfig.FIREBASE_AUTH_DOMAIN,
            "databaseURL": "THIS_IS_NOT_USED",
            "storageBucket": "THIS_IS_NOT_USED",
        }
    )
    auth = firebase.auth()

    try:
        user = auth.sign_in_with_email_and_password(username, password)
    except HTTPError as e:
        # workaround for pyrebase not raising the correct exception
        status_code = e.errno.response.status_code
        if status_code == 400:
            raise InvalidCredentialsException() from e

        raise TrailUnavailableException() from e
    except RequestException as e:
        raise TrailUnavailableException() from e

    return user["idToken"]


def retrieve_id_token() -> str:
    from trail.userconfig import userconfig
    global _user_id_token

    if not _user_id_token:
        _user_id_token = authenticate(userconfig().username, userconfig().password)

    return _user_id_token


def build_auth_header(auth_object=None):
    if auth_object:
        if "email" in auth_object and "api_key" in auth_object:
            return {"X-Api-Key": auth_object["api_key"], "X-User-Email": auth_object["email"]}
        elif "username" in auth_object and "password" in auth_object:
            return {
                "authorization":
                    f"Bearer {authenticate(auth_object['username'], auth_object['password'])}"
            }
    else:
        from trail.userconfig import userconfig
        config = userconfig()
        if config.username and config.api_key:
            return {"X-Api-Key": config.api_key, "X-User-Email": config.username}
        else:
            return {"authorization": f"Bearer {retrieve_id_token()}"}
