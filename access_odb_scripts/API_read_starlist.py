# use python sessions to create a session that allows the login / cookie
# to persist for multiple requests
import re
import json
import argparse
from requests import Session, packages

packages.urllib3.disable_warnings()

# starlists have a target length
TARGET_NAME_LEN = 15


def parse_args():
    """
    Parse the command line arguments.

    :return: <obj> commandline arguments
    """
    parser = argparse.ArgumentParser(description="Create OBs from Starlist.")

    parser.add_argument("--starlist", type=str, required=True,
                        help="Define the path + filename of starlist.")

    return parser.parse_args()


def get_name_param(line):
    # get the target name,  and the remaining space delimited parameters
    target_name = line[:TARGET_NAME_LEN].rstrip(' ')

    # cut off any comment
    line = line.split('#')[0]

    # get the parameters after the name entry
    line_params = re.split(" +", line[17:])

    return target_name, line_params


def get_coords(line_parms):
    crds = line_parms
    coord_dict = {'ra': f'{crds[0]}:{crds[1]}:{crds[2]}',
                  'dec': f'{crds[3]}:{crds[4]}:{crds[5]}'}

    return coord_dict


def get_ob(metadata_list, url_ob_get):
    ob_id = metadata_list[0]['_id']
    print(f'OB ID = {ob_id}')

    # get the OB by ID
    api_result = api_session.get(url=f'{url_ob_get}?ob_id={ob_id}', verify=False)
    if not api_result:
        print(f'No results from query: {url_ob_get}?ob_id={ob_id}')
        exit()

    ob = api_result.json()
    if 'target' not in ob:
        print('no target component in list,  using next OB')
        ob, metadata_list = get_ob(metadata_list[1:], url_ob_get)

    return ob, metadata_list


def submit_ob(ob, line):
    target_name, line_params = get_name_param(line)
    coords = get_coords(line_params)

    # update name in the OB
    ob['target']['parameters']['target_info_name'] = target_name

    # update coordinates in the OB
    ob['target']['parameters']['target_coord_ra'] = coords['ra']
    ob['target']['parameters']['target_coord_dec'] = coords['dec']

    # send it to the DB
    return api_session.post(url=url_ob_get, json=json.loads(json.dumps(ob)),
                            verify=False)


# ------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------

# parse the command line arguments
args = parse_args()

# connect to the API
api_session = Session()

# Add the login url and API example url
login_url = 'https://www3.keck.hawaii.edu/login/script'
sem_id = '2022B_K111'
api_url = 'https://www3.keck.hawaii.edu/api/ddoi'

# returns all OB metadata for a program (2022B_K111)
url_ob_list = f'{api_url}/semesterIds/{sem_id}/ob/metadata'

# # gets OB by OB Object ID
url_ob_get = f'{api_url}/obsBlocks'

# duplicates OB by Object ID
api_ob_duplicate = f'{api_url}/obsBlocks/duplicate'

# Add your credentials here
# credentials = {'email': 'YourEmail@Address', 'password': 'Observer Login Password'}

# Login and get the two API Cookies: 'ODB-API-KEY'  'ODB-API-UID'
login_result = api_session.post(url=login_url, params=credentials, verify=False)
api_cookies = login_result.json()
api_session.cookies.update(api_cookies)

# Query the ODB API

# get the metadata to know OB IDs
api_result = api_session.get(url=url_ob_list, verify=False)
if not api_result:
    print(f'No results from query: {url_ob_list}')
    exit()

# get the OB information from the Metadata
metadata_list = api_result.json()

# get the OB by ID
ob, metadata_list = get_ob(metadata_list, url_ob_get)

# use OB to submit multiple OBs with updated information from the starlist
starlist = args.starlist
with open(starlist) as file:
    target_lines = file.readlines()
    target_lines = [line.rstrip() for line in target_lines]

# submit an OB for each target in list
for line in target_lines:
    print(line)
    result = submit_ob(ob, line)
    print('post result', result)






