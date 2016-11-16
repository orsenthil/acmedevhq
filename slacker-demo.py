import os

from slacker import Slacker

slack = Slacker(os.environ.get('SLACK_BOT_TOKEN'))

slack.chat.post_message('#general', 'Hello There!')
