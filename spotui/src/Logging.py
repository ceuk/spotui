import logging
import os

user_config_dir = os.path.expanduser("~")
filename = user_config_dir + "/.cache/spotui.log"
if not os.path.exists(os.path.dirname(filename)):
  try:
    os.makedirs(os.path.dirname(filename))
  except OSError as exc:  # prevent race condition
    if exc.errno != errno.EEXIST:
      raise
      
# if log file doesn't exist
if not os.path.isfile(filename):
  with open('sample.csv', 'w') as creating_new_log_file: 
    pass
        
logging.basicConfig(filename, filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
