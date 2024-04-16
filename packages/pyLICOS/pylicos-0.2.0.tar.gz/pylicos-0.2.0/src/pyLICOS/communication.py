import base64
import hashlib

from datetime import datetime
from enum import Enum, auto


class Status(Enum):
    UNKOWN = auto()
    QUEUE = auto()
    RUNNING = auto()
    ERROR = auto()
    DONE = auto()
    CANCELED = auto()


def build_link(adress: str, action: str):
    """

    :param adress:
    :param action:
    :return:
    """

    if adress[-1] == "/":
        adress = adress[:-1]
    if action[0] == "/":
        action = action[1:-1]

    return adress + "/" + action


def add_authentication(header: {}, username: str, password: str):
    """
    Add to the request header the authentication data
    :param header:
    :param username: Username for authentication
    :param password: Password for authentication
    :return:
    """

    client_seconds, client_hash = _auth_values()

    header['Accept'] = "application/json;q=1"
    header['segundos_cliente'] = str(client_seconds)
    header['hash_cliente'] = client_hash

    auth_string = f'{username}:{password}'
    ascii_bytes = auth_string.encode('ascii')
    base64_string = base64.b64encode(ascii_bytes).decode('ascii')

    header['Authorization'] = f'Basic {base64_string}'


def _auth_values():
    client_seconds = _get_ticks(datetime.utcnow())

    secret_word = 'w3b0t1m1x'
    secret_seconds = _get_ticks(datetime(1987, 1, 27, 20, 38, 1, 224000))

    seconds_key = client_seconds - secret_seconds
    string_key = secret_word + str(seconds_key)

    encoded_ascii = string_key.encode('ascii')
    sha512 = hashlib.sha512(encoded_ascii).digest()

    hash_client = base64.encodebytes(sha512).replace(b'\n', b'').decode('ascii')

    return client_seconds, hash_client


def _get_ticks(dt: datetime):
    """
    Get number of ticks elapsed, given a millisecond = 10,000 ticks, since 12:00:00 midnight, January 1, 0001.
    :param dt: datetime to check number of ticks elapsed
    :return: number of ticks elapsed
    """
    fixed_point = datetime(1, 1, 1)
    ticks = int((dt-fixed_point).total_seconds()*10000000)

    return ticks
