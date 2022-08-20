import musicalbeeps
import ldclient
from ldclient.config import Config
import argparse
from dotenv import load_dotenv
import os

def show_message(s):
  print("*** %s" % s)
  print()

# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
    load_dotenv()
    ldclient.set_config(Config(os.environ["ld_api"]))
    client = ldclient.get()

    player = musicalbeeps.Player(volume=0.5, mute_output=False)


    parser = argparse.ArgumentParser()
    parser.add_argument('--user', default='peter'), 

    args = vars(parser.parse_args())
    username = args['user']

    # The SDK starts up the first time ldclient.get() is called.
    if ldclient.get().is_initialized():
        show_message("SDK successfully initialized!")
    else:
        show_message("SDK failed to initialize")
        exit()

    # Set up the user properties. This user should appear on your LaunchDarkly users dashboard
    # soon after you run the demo.
    user = {
        "key": "example-user-key",
        "name": username
    }

    print(user)

    while True:
        flag_value = ldclient.get().variation("octave", user, '4')
        player.play_note('C'+str(flag_value), 0.2)


