from connexion.exceptions import OAuthProblem
from papahana.controllers import controller_helper as utils
from papahana.controllers import authorization_utils as auth_utils
from flask import g, make_response, redirect, request, abort

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_apikey_auth(api_key, required_scopes):
    """
    function called for the security,  must have a return value
    """
    scrambled_api_key = request.cookies.get('ODB-API-KEY')
    scrampled_uid = request.cookies.get('ODB-API-UID')
    keck_id = int(auth_utils.decrypt_encoded_str(scrampled_uid))

    if scrambled_api_key == 'NULL':

        api_key = auth_utils.generate_api_key(keck_id)

        #TODO not working
        auth_utils.update_cookie('ODB-API-KEY', api_key, request.path)
        abort(401, f'Unauthorized - no API key set.  An API Key has been '
                   f'generated.  Please return to Login Page and try again.')
    else:
        api_key = auth_utils.decrypt_encoded_str(scrambled_api_key)

        query = {'api_key': api_key}
        fields = {'keck_id': 1, '_id': 0}
        results = utils.get_fields_by_query(query, fields, 'observerCollect')
        if not results:
            raise OAuthProblem('API Key not found')

        if keck_id != results[0]['keck_id']:
            abort(401, 'Unauthorized,  API KEY and Keck ID do not match our records.')

    g.authorized = True
    g.user = keck_id

    return {'uid': keck_id}


