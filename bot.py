from pyrogram import Client,filters
from random import randint
from gtts import gTTS
import os
app = Client("my_accound",api_id=12721742,api_hash="2a81674bd5e1ccbaed8c07f898d614ca")

@app.on_message((filters.user(618260788) | filters.me) & filters.text)
def media(client, message):
    text=message.text
    text2=text.split()[0]
    text=text.replace(text2,"")
    if text2=="!youvid":
        chat_id=message.chat.id
        bot_results = app.get_inline_bot_results("vid",text)
        app.send_inline_bot_result(chat_id, bot_results.query_id, bot_results.results[randint(0,30)].id)

    elif text2=="!youpic":
        chat_id=message.chat.id
        bot_results = app.get_inline_bot_results("pic",text)
        app.send_inline_bot_result(chat_id, bot_results.query_id, bot_results.results[randint(0,30)].id)

    elif text2=="!yougif":
        chat_id=message.chat.id
        bot_results = app.get_inline_bot_results("gif",text)
        app.send_inline_bot_result(chat_id, bot_results.query_id, bot_results.results[randint(0,30)].id)

    elif text2=="!ttr":
        chat_id=message.chat.id
        message_id=message.message_id
        language=text.split()[0]
        text=text.replace(language,"")
        myobj=gTTS(text=text,lang=language,slow=False)
        myobj.save("test.ogg")
        client.send_audio(chat_id,"test.ogg",reply_to_message_id=message_id)
        os.remove('test.ogg')

    elif text2=="!tts":
        chat_id=message.chat.id
        message_id=message.message_id
        text = message.reply_to_message.text
        language="en"
        myobj=gTTS(text=text,lang=language,slow=False)
        myobj.save("test.ogg")
        client.send_audio(chat_id,"test.ogg",reply_to_message_id=message_id)
        os.remove('test.ogg')
       
    elif text2=="!help":
        help="**command:**\n!youvid\n**descriptin:**\nsearch name video and sending link\n\n\n**command:**\n!youpic\n**descriptin:**\nsearch picture with name and sending picture\n\n\n**command:**\n!yougif\n**descriptin:**\nsearch gif with name and sending gif\n\n\n**command:**\n!ttr\n**descriptin:**\nget text and change to voice and sending voice\n\n\n**command:**\n!tts\n**descriptin:**\nget message reply text and change to voice and sending voice\n\n\n"
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=help)
app.run()  # Automatically start() and idle()
