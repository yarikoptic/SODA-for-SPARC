


def create_request_headers(ps_or_token):
    """
    Creates necessary HTTP headers for making Pennsieve API requests.
    Input: 
        ps: Pennsieve object for a user that has been authenticated
    """

    if type(ps_or_token) == str:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ps_or_token}",
        }

    user_info = ps_or_token.get_user()
    session_token = user_info["session_token"]
    
    return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {session_token}",
    }
