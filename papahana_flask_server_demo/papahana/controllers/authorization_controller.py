import hashlib
import os

from connexion.exceptions import OAuthProblem
from papahana.controllers import controller_helper as utils
from flask import g, make_response, redirect, request

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


# # TODO check if the WWW3 cookie exists,  get Keck ID,  add the new cookie
def is_authorized():
    """
    sets the session global variable 'authorized'
    """
    apikey = request.cookies.get('ODB-API')

    query = {'api_key': apikey}
    fields = {'keck_id': 1, '_id': 0}

    print(query, fields)
    results = utils.get_fields_by_query(query, fields, 'observerCollect')

    print('is auth', results, apikey)
    if not results:
        g.authorized = False
        raise OAuthProblem('Unauthorized,  API Key does not match records.')

    g.authorized = True
    g.user = None
    g.user = results[0]

    return results[0]


def is_authorized_semid(sem_id):
    keck_id = g.user

    # todo first check the database
    query ={ 'keck_id': keck_id, 'associations': sem_id}
    fields = {'associations': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if results:
        return True

    # not found in database,  check proposals API
    results = utils.get_proposal_ids(keck_id)
    if results and sem_id in results:
        # todo update database
        return True

    # todo then check schedule API

    return False


def hash_key(apikey):
    return hashlib.sha256(str.encode(apikey)).hexdigest()

# def decode_uid(uid_cookie):
#     secret_key =
#     secret_iv =
#
#     key = hashlib.sha256(secret_key.encode('utf-8')).hexdigest()[:32].encode("utf-8")
#     iv = hashlib.sha256(secret_iv.encode('utf-8')).hexdigest()[:16].encode("utf-8")
#
#     # _pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
#     # txt = _pad(userid)
#
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     output = b64encode(cipher.encrypt(uid_cookie.decode("utf-8"))).rstrip(b'=')

    # return output


def check_apikey_auth(api_key, required_scopes):
    """
    function called for the security,  must have a return value

    """
    # TODO check if the WWW3 cookie exists,  get Keck ID,  add the new cookie

    print('type', type(api_key), api_key)

    # TODO use cookie to double check identity
    # userid_cookie = request.cookies.get('www3')
    # print("UID", decode_uid(userid_cookie))

    # hashed_key = hash_key(api_key)
    query = {'api_key': api_key}
    fields = {'keck_id': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if not results:
        raise OAuthProblem('API Key not found')

    g.authorized = True
    try:
        g.user = results[0]['keck_id']
    except KeyError:
        g.user = None

    print('KECK ID', g.user)

    return results[0]


# def _encrypt_apikey(apikey):
#     import hashlib
#     from base64 import b64encode, b64decode, urlsafe_b64encode, urlsafe_b64decode
#     from Crypto.Cipher import AES
#
#     secret_key = '7fm20dm'
#     secret_iv = '03ye2GK9l18'
#
#     key = hashlib.sha256(secret_key.encode('utf-8')).hexdigest()[:32].encode("utf-8")
#     iv = hashlib.sha256(secret_iv.encode('utf-8')).hexdigest()[:16].encode("utf-8")
#
#     _pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
#     txt = _pad(apikey)
#
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     output = b64encode(cipher.encrypt(txt.encode("utf-8"))).rstrip(b'=')
#
#     return output

def get_admin_key():
    query = {'keck_id': -1}
    fields = {'api_key': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    print(results)

    return results[0]['api_key']


def set_apikey_cookie(redirect_url):
    TIMEOUT = 86400
    TMP_APIKEY = get_admin_key()

    print(f'setting key {TMP_APIKEY}')

    res = make_response(redirect(redirect_url, code=302))
    byte_key = str.encode(str(TMP_APIKEY))
    res.set_cookie('ODB-API', byte_key, max_age=TIMEOUT, domain='.keck.hawaii.edu')
    # res.set_cookie('ODB-API', scramble_id, max_age=TIMEOUT, domain='128.171.96.113:50002')

    return res


def generate_api_key():
    """
    Generate a random API key based on os.urandom

    :return: the generated API key
    :rtype: str
    """
    return hashlib.sha256(os.urandom(32)).hexdigest()



