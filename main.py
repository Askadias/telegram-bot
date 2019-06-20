from os import environ

from telebot import TeleBot

app = TeleBot(__name__)


@app.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Command Recieved: {}".format(cmd)
    print(msg+"\n")

    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = "Parrot Says: {}".format(user_msg)
    print(msg+"\n")
    app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = environ.get('API_KEY')
    app.poll(debug=True)
