import hashlib
import os
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto import Random

from flask import g, abort, make_response, redirect, request

from papahana import util
from papahana.controllers import controller_helper as utils
from papahana.controllers import observers_utils as obs_utils


def generate_api_key(keck_id):
    """
    check the keck id does not have an api key.  If not,  generate a new one
    and add it to the database.  If it has a key,  abort,  401 unauthorized.
    """
    query = {'keck_id': keck_id}
    fields = {'api_key': 1, '_id': 0}

    results = utils.get_fields_by_query(query, fields, 'observerCollect',
                                        db_name='obs_db')
    if not results:
        doc = {'keck_id': keck_id, 'api_key': '', 'associations': [], 'admin': 0}
        utils.insert_into_collection(doc, 'observerCollect', db_name='obs_db')
    else:
        # if we are here and there is already a key,  abort unauthorized
        try:
            key = results[0]['api_key']
            if key:
                abort(401, f'Unauthorized,  API KEY does not match the records')
        except (KeyError, IndexError):
            abort(401, f'Unauthorized,  error in your observer record -- '
                       f'contact Keck.')

    new_key = generate_new_api_key()

    query = {'keck_id': keck_id}
    fields = {'api_key': new_key}

    utils.update_doc(query, fields, 'observerCollect', db_name='obs_db')

    return new_key


def _pad(unpadded_str):
    """
    Used to pad strings to the AES block size.

    :param unpadded_str:
    :return:
    """
    bs = AES.block_size
    padded = (unpadded_str + (bs - len(unpadded_str) % bs) *
              chr(bs - len(unpadded_str) % bs))

    return padded


def _encrypt_str(plain_str):
    """
    Enryption that can be decrypted simplyin python using the SECRET_KEY.

    :param plain_str: string to be encrypted

    :return: encrypted string
    """
    secret_key = util.config_file_section('apikey')['secret_key']
    key = hashlib.sha256(secret_key.encode()).digest()

    padded_str = _pad(plain_str)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return b64encode(iv + cipher.encrypt(padded_str.encode()))


def decrypt_encoded_str(encoded_str):
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    secret_key = util.config_file_section('apikey')['secret_key']
    key = hashlib.sha256(secret_key.encode()).digest()

    enc = b64decode(encoded_str)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')


def get_admin_key():
    query = {'keck_id': -1}
    fields = {'api_key': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect',
                                        db_name='obs_db')

    return results[0]['api_key']


def generate_new_api_key():
    """
    Generate a random API key based on hashing os.urandom

    :return: the generated API key
    :rtype: str
    """
    return hashlib.sha256(os.urandom(32)).hexdigest()


def check_sem_id_associated(sem_id):
    if not sem_id or not obs_utils.is_semid_associated(sem_id):
        abort(401, f"Unauthorized to access Program: {sem_id}")


def confirm_sem_id_associated(func):
    def inner(*args, **kwargs):
        sem_id = kwargs['sem_id']
        if not obs_utils.is_semid_associated_args(*args, **kwargs):
            abort(401, f"Unauthorized to access Program: {sem_id}")

        if 'user' in kwargs:
            del kwargs['user']
        if 'token_info' in kwargs:
            del kwargs['token_info']

        return func(*args, **kwargs)
    return inner






