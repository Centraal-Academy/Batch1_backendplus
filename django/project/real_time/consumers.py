from channels import Group

def ws_message(message):
    message.reply_channel.send({
        "text":message.content["text"],
    })

# def ws_connect(message):
#     Group('users').add(message.reply_channel)

# def ws_disconnect(message):
#     Group('users').discard(message.reply_channel)