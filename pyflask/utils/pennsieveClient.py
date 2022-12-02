from pennsieve2.pennsieve import Pennsieve
from flask import abort

def connect_pennsieve_client():
    """
        Connects to Pennsieve Python client to the Agent and returns the initialized Pennsieve object.
    """
    try:
        return Pennsieve()
    except Exception as e:
        print(e)
        abort(500, f"Could not connect to the Pennsieve agent: {e}")


def authenticate_user_with_client(ps, selected_account):
    """
        Authenticates the given user with the Pennsieve client.
        Input:
            ps: An initialized Pennsieve object
            selected_account: Pennsieve account to authenticate with
    """
    try:
        ps.user.switch(selected_account)
    except Exception as e:
        abort(400, "Please select a valid Pennsieve account.")

    try:
        ps.user.reauthenticate()
    except Exception as e:
        abort(401, "Could not reauthenticate this account with Pennsieve.")


def get_dataset_id(ps, selected_dataset):
    """
        Returns the dataset ID for the given dataset name.
        Input:
            ps: An initialized Pennsieve object
            selected_dataset: Pennsieve dataset to get the ID for
    """
    try:
        return ps.getDatasets()[selected_dataset]
    except Exception as e:
        abort(400, "Please select a valid Pennsieve dataset.")

