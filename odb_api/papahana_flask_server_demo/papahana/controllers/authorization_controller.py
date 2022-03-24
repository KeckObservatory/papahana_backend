from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_bearerAuth(token):
    return {'test_key': 'test_value'}


def decode_token():
    # EXAMPLE: https://github.com/zalando/connexion/tree/master/examples/openapi3/jwt

    return

def get_user_obs_id():
    return
    # url: 'https://www3build.keck.hawaii.edu/userinfo',
    # ip = response.headers["x-my-real-ip"]
    # axios.request({url: 'https://www3build.keck.hawaii.edu/userinfo', method: "get", withCredentials: true,
    #     headers: {'X-My-Real-Ip': ip, },