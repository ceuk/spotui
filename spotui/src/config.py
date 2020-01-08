import os, configparser, errno


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

    # if config file doesn't exist
    if not os.path.isfile(filename):
        _create_default_config(config, filename)

    config.read(filename)

    # check config is valid
    _check_config(config, filename)

    return config


def _create_default_config(configparser, filename):
    configparser.add_section("spotify_api")
    configparser.set("spotify_api", "user_name", "*your spotify username*")
    configparser.set(
        "spotify_api",
        "; register an application here: https://developer.spotify.com/dashboard/login",
    )
    configparser.set("spotify_api", "client_id", "*your application ID*")
    configparser.set("spotify_api", "client_secret",
                     "*your application secret*")
    configparser.set("spotify_api", "redirect_uri",
                     "http://localhost:8888/auth")

    configparser.add_section("other")
    configparser.set("other", "config_version", "1")

    configparser.write(open(filename, "w"))


def _check_config(configparser, filename):
    user_name = configparser.get("spotify_api", "user_name")
    client_id = configparser.get("spotify_api", "client_id")
    client_secret = configparser.get("spotify_api", "client_secret")

    if (client_id == "*your application ID*"
            or client_secret == "*your application secret*"
            or user_name == "*your spotify username*"):
        print("You need to configure: " + filename)
        exit(1)
