import os
from getpass import getpass

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError

from trail.exception.trail import TrailUnavailableException
from trail.libconfig import libconfig
from trail.userconfig import MainConfig
from trail.util import auth

FETCH_ALL_PROJECTS = """
    query {
        allProjects {
            id
            title
            mostRecentExperiment {
                id
            }
        }
    }
"""


def get_user_credentials():
    while True:
        print("Select your authentication method:")
        print("1. Email and API key")
        print("2. Username and password")
        auth_method = input("Please enter the number of your selected method [1/2] (Default: 1): ")
        if auth_method == "" or auth_method == "1":
            email = input("Email: ")
            api_key = input("API Key: ")
            return {"email": email, "api_key": api_key}
        elif auth_method == "2":
            username = input("Username: ")
            password = getpass("Password: ")
            return {"username": username, "password": password}
        else:
            print("Invalid selection. Please enter 1 or 2.")


def select_project_and_parent_experiment(auth_header: dict):
    try:
        transport = AIOHTTPTransport(
            libconfig.gql_endpoint_url,
            headers=auth_header
        )
        client = Client(transport=transport)
        result = client.execute(document=gql(FETCH_ALL_PROJECTS))
        projects = {
            project["id"]: project
            for project in result["allProjects"]
        }
    except TransportQueryError as e:
        raise TrailUnavailableException() from e

    print("Your projects are listed below:\n")
    print("Project ID | Project Title")
    for project in sorted(projects.values(), key=lambda x: x["id"]):
        print(f"{project['id']}     | {project['title']}")

    while True:
        project_id = input("Select a project ID: ")
        if project_id in projects:
            break

    default_experiment_id = projects[project_id].get('mostRecentExperiment', {}).get('id', 'N/A')
    # TODO: validate parent_experiment ID
    parent_experiment_id = input(
        f"Select a parent experiment ID (Default: {default_experiment_id}): ")
    if not parent_experiment_id:
        parent_experiment_id = default_experiment_id

    return project_id, parent_experiment_id


def create_config(auth_object, project_id, parent_experiment_id):
    config = MainConfig(
        os.path.join(os.getcwd(), libconfig.PRIMARY_USER_CONFIG_PATH),
        {
            'username': auth_object['username'] if 'username' in auth_object else auth_object[
                'email'],
            'password': auth_object['password'] if 'password' in auth_object else None,
            'apiKey': auth_object['api_key'] if 'api_key' in auth_object else None,
            'projects': {
                'id': project_id,
                'parentExperimentId': parent_experiment_id
            },
        }
    )
    config.save()


def init_environment():
    print(f"Don't have an account yet? Sign up here: {libconfig.TRAIL_SIGN_UP_URL}\n")

    print("Your configuration file will be stored in the current directory. "
          "Make sure that you are in the root directory of your project.")

    auth_object = get_user_credentials()
    auth_header = auth.build_auth_header(auth_object)
    project_id, parent_experiment_id = select_project_and_parent_experiment(auth_header)
    create_config(auth_object, project_id, parent_experiment_id)

    print("Initialization completed.")
