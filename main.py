import logging
from os import environ

from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)
from telegram.ext import Updater, CommandHandler

updater = Updater(token=environ.get('API_KEY'), use_context=True)
dispatcher = updater.dispatcher

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized as e:
        logger.error(e)
        # remove update.message.chat_id from conversation list
    except BadRequest as e:
        logger.error(e)
        # handle malformed requests - read more below!
    except TimedOut as e:
        logger.error(e)
    # handle slow connection problems
    except NetworkError as e:
        logger.error(e)
    # handle other connection problems
    except ChatMigrated as e:
        logger.error(e)
    # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError as e:
        logger.error(e)


# handle all other telegram related errors

dispatcher.add_error_handler(error_callback)


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
