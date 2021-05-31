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

        copy2(".spotuirc",  filename)
        print("[ SpoTUI ] " + filename +" has been created!")
        print("[ SpoTUI ] " + " Open it to set up your account")
        exit(1)

    config.read(filename)

    # check config is valid
    _check_config(config, filename)

    return config


def _check_config(configparser, filename):
    user_name      = configparser.get("spotify_api", "user_name")
    client_id      = configparser.get("spotify_api", "client_id")
    client_secret  = configparser.get("spotify_api", "client_secret")
    
     # outdated config
    config_version = configparser.get("other", "config_version")
    #TODO: remove this hardcoded config version number
    if int(config_version) < 2:
        print("[ SpoTUI ] " + " config is outdated.")
        print("[ SpoTUI ] " + " Grabbing values and updating . . .")

        nerd_fonts = configparser.get("other", "use_nerd_fonts")

        #copy new file over   
        # TODO: does not copy over comments within the file?? those are necessary 
        copy2(".spotuirc",  filename)
        configparser.read(filename)

        #dump old spotify values in
        configparser.set("spotify_api", "user_name", user_name)
        configparser.set("spotify_api", "client_id", client_id)
        configparser.set("spotify_api", "client_secret", client_secret)
        configparser.set("spotify_api", "use_nerd_fonts", nerd_fonts)
        
        file_ = open(filename, 'w')
        configparser.write(file_)

        #all done
        print("[ SpoTUI ] " + " Done!")
        

    # file exists, hasn't been changed
    if (client_id == "*your application ID*"
            or client_secret == "*your application secret*"
            or user_name == "*your spotify username*"):
        print("[ SpoTUI ] " + filename +" needs to be edited with appropriate values")
        exit(1)

   

