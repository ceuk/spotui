import os, configparser, errno
from shutil import copy2

def get_config():
    user_config_dir = os.path.expanduser("~")
    config = configparser.ConfigParser(allow_no_value=True)

    filename = user_config_dir + "/.config/spotui/.spotuirc"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # prevent race condition
            if exc.errno != errno.EEXIST:
                raise

    # if config file doesn't exist, create one and stop
    if not os.path.isfile(filename):
        _create_default_config(config, filename)
        print("[ SpoTUI ] " + filename +" has been created!")
        print("[ SpoTUI ] " + " Open it to set up your account")
        exit(1)

    config.read(filename)

    # check config is valid
    _check_config(config, filename)

    return config


def _create_default_config(configparser, filename):
    user_config_dir = os.path.expanduser("~")
    copy2(".spotuirc",  user_config_dir + "/.config/spotui/")


def _check_config(configparser, filename):
    user_name = configparser.get("spotify_api", "user_name")
    client_id = configparser.get("spotify_api", "client_id")
    client_secret = configparser.get("spotify_api", "client_secret")
    
    # file exists, hasn't been changec
    if (client_id == "*your application ID*"
            or client_secret == "*your application secret*"
            or user_name == "*your spotify username*"):
        print("[ SpoTUI ] " + filename +" needs to be edited with appropriate values")
        exit(1)
