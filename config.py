import logging
import os 

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'C:\\project\\slack-bot\\data'
BOT_EXTRA_PLUGIN_DIR = r'C:\\project\\slack-bot\\plugins'

AUTOINSTALL_DEPS = True

BOT_LOG_FILE = BOT_DATA_DIR + '/err.log'
BOT_LOG_LEVEL = logging.DEBUG
BOT_LOG_SENTRY = False
SENTRY_DSN = ''
SENTRY_LOGLEVEL = BOT_LOG_LEVEL

BOT_IDENTITY = {
    'token': os.environ.get('SLACKTOKEN'),
}
BOT_ADMINS = ('@johnw','@403481704','@*' )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!
