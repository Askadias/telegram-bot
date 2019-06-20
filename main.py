from telebot import TeleBot

app = TeleBot(__name__)


@app.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Command Recieved: {}".format(cmd)

    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = '850358969:AAHYS36ztPQR6oJSAQ-pdiapG44XYhQLny8'
    app.poll(debug=True)
