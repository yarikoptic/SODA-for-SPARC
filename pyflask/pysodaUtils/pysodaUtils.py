import subprocess
import re
import sys
from os.path import exists 
import os




def get_agent_installation_location():
    """
        Get the location of the Pennsieve agent installation for Darwin, Linux, and Windows. 
    """
    if sys.platform == "darwin":
        return "/usr/local/bin/pennsieve"

    elif sys.platform.startswith("linux"):
        return "/usr/local/bin/pennsieve"

    elif sys.platform in ["win32", "cygwin"]:
        win_path = os.path.normpath("C:\Program Files (x86)\Pennsieve\pennsieve.exe")
        if exists(win_path): 
            print("Path exists")
            return win_path
        else:
            print("Non x86 path path")
            return os.path.normpath("C:\Program Files\Pennsieve\pennsieve.exe")



def check_agent_installation():
    """
    Check if the Pennsieve agent is installed on the computer. 
    """
    return exists(get_agent_installation_location())
        


def start_agent():
    """
    Start the Pennsieve agent. IMP: Run if agent exists.
    """
    if not check_agent_installation(): 
        raise FileNotFoundError("Pennsieve agent not installed. Please install the agent before running this function.")

    command = [get_agent_installation_location(), "agent"]

    return subprocess.run(command, check=True)

def stop_agent():
    """
    Stops the Pennsieve agent if it is running.
    """

    if not check_agent_installation(): 
        raise FileNotFoundError("Pennsieve agent not installed. Please install the agent before running this function.")

    command = [get_agent_installation_location(), "agent", "stop"]

    return subprocess.run(command, check=True)


def get_agent_version():
    """
        Get the version of the Pennsieve agent installed on the computer.
    """
    # start the agent if it is not running
    start_agent()

    print("Agent started")

    command = [get_agent_installation_location(), "version"]

    version = ""

    while version.find("Error") != -1 or version == "":
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        version = result.stdout

        version = version.decode()

        print(version.find("Error"))

        print(version)
    
    # decode the response 
    version = version.strip()

    return { 'agent_version': version }


def agent_up_to_date():
    
    v = get_agent_version()
    
    # search string for 1.2.2
    # TODO: Improve agent version parsing to check for Agent Version and CLI Version separately. Both need to match.
    if "1.2.2" in v:
        print("Agent is up to date")
        return True
    else:
        print("Agent is not up to date")
        return False



forbidden_characters = '<>:"/\|?*'
def check_forbidden_characters(my_string):
    """
    Check for forbidden characters in file/folder name

    Args:
        my_string: string with characters (string)
    Returns:
        False: no forbidden character
        True: presence of forbidden character(s)
    """
    regex = re.compile(f"[{forbidden_characters}]")
    return regex.search(my_string) is not None or "\\" in r"%r" % my_string


forbidden_characters_bf = '\/:*?"<>'
def check_forbidden_characters_bf(my_string):
    """
    Check for forbidden characters in Pennsieve file/folder name

    Args:
        my_string: string with characters (string)
    Returns:
        False: no forbidden character
        True: presence of forbidden character(s)
    """
    regex = re.compile(f"[{forbidden_characters_bf}]")
    return regex.search(my_string) is not None or "\\" in r"%r" % my_string

