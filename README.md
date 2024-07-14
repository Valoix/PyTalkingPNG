
# PyTalkingPNG

This is an unfinished project which allows for more twitch integration in your PNG Tubing app writen in python. 



## Features

- **Interactive Twitch Bot**: A custom Twitch bot built using the TwitchIO library, capable of responding to chat commands and interacting with viewers.

- **PNGTuber Visualization**: A graphical interface created with Pygame, displaying an animated character (PNGTuber) that responds to various inputs and commands.

- **Blinking Animation**: The PNGTuber character features a randomized blinking animation, adding lifelike behavior to the display.

- **Voice Activity Detection**: Integration with a voice client to detect and respond to the streamer's voice activity, potentially changing the character's expression when talking.

- **Dynamic Character Transformations**:
  - `!rotate` command: Rotates the character image.
  - `!shrink` command: Temporarily shrinks the character size.

- **Multi-threaded Architecture**: Utilizes threading to run the game loop, voice detection, and Twitch bot concurrently, ensuring smooth performance.

- **Customizable Assets**: Easy to swap out character images for different expressions (normal, blinking, talking) to personalize your PNGTuber.

- **Extensible Command System**: Built-in framework for easily adding new chat commands and interactions.

- **Secure Configuration**: Utilizes a separate file for sensitive information like OAuth tokens and client IDs, promoting better security practices.

This PNGTuber application combines real-time chat interaction, visual animations, and audio responsiveness to create an engaging streaming experience.


## Installation

1. Install dependencies with pip

```bash
  pip3 install -r requirements.txt
```

2. Add your PNG assets into the `assets` folder 
NOTE: The folder must *at least* contain these files:
* A file with open eyes and closed mouth.
* A file with open eyes and open mouth.
* A file with closed eyes and closed mouth.
* A file with closed eyes and open mouth.

3. Edit `game.py` to match your assets file locations (line 39-49)

```bash
  # FOR EXAMPLE:
  normal_image = pygame.image.load("/file/path/to/assets/image.png")
```

4. In `secret.py`, put in your OAUTH token and client id
```bash
def get_twitch_oauth_token():
    OAUTH_TOKEN = "YOUR_TOKEN_HERE"
    return OAUTH_TOKEN

def get_client_id():
    CLIENT_ID = "YOUR_ID_HERE"
    return CLIENT_ID
```

5. In `bot.py` change the `nick` and `initial_channels` to your own twitch username.

6. If I haven't forgotten anything, all that is left is to run the `run_bot.sh` file. 
## Support

For support, contact `valoix` on discord.

