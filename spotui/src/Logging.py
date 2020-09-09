import logging
import os

user_config_dir = os.path.expanduser("~")
logging.basicConfig(filename=user_config_dir + '/.cache/spotui.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
