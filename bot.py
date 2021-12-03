from pyrogram import Client,filters
from random import randint
from gtts import gTTS
import requests,time
import os
app = Client("my_accound",api_id=12721742,api_hash="2a81674bd5e1ccbaed8c07f898d614ca")

@app.on_message((filters.me) & filters.regex("^!pdf "))
def webtopdf(client,message):
    text=message.text
    chat_id=message.chat.id
    name=text.replace("!pdf ","")
    Response=requests.post(f"https://api.codebazan.ir/htmltopdf/?type=json&url=https://{name}")
    tex=Response.json()
    url=tex["result"]["url"]
    pdf=requests.get(url)
    time.sleep(1)
    namefile="test.pdf"
    with open("webtopdf.pdf","wb") as f:
        f.write(pdf.content)
    client.send_document(chat_id,"webtopdf.pdf",reply_to_message_id=message.message_id)
    os.remove("webtopdf.pdf")

@app.on_message((filters.me) & filters.regex("^!proxy$"))
def proxy(client,message):
    messag_id=message.message_id
    Response=requests.post("http://api.codebazan.ir/mtproto/json/") 
    tex=Response.json()
    tex=tex["Result"]
    text=""
    for i in range(0,20):
        server=tex[i]["server"]
        port=tex[i]["port"]
        secret=tex[i]["secret"]
        text+=f"{i+1}- https://t.me/proxy?server={server}&port={port}&secret={secret}\n\n/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=text)

@app.on_message((filters.me) & filters.regex("^!pass "))
def password_gen(client,message):
    text=message.text
    messag_id=message.message_id
    name=text.replace("!pass ","")
    Response=requests.post(f"http://api.codebazan.ir/password/?length={name}")
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=Response.text)

@app.on_message((filters.me) & filters.regex("^!. "))
def strrev(client,message):
    text=message.text
    messag_id=message.message_id
    name=text.replace("!. ","")
    Response=requests.post(f"http://api.codebazan.ir/strrev/?text={name}") 
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=Response.text)

@app.on_message((filters.me) & filters.regex("^!arz$"))
def arz(client,message):
    messag_id=message.message_id
    Response=requests.post("http://api.codebazan.ir/arz/?type=arz")
    tex=Response.json()
    result=""
    for i in range(0,15):
        name=tex[i]["name"]
        price=tex[i]["price"]
        change=tex[i]["change"]
        percent=tex[i]["percent"]
        result+=f"**name:**{name}\n**price:**{price}\n**change:**{change}{percent}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)

@app.on_message((filters.me) & filters.regex("^!font "))
def font(client,message):
    text=message.text
    messag_id=message.message_id
    text=text.replace("!font ","")
    Response=requests.post(f"http://api.codebazan.ir/font/?text={text}")
    tex=Response.json()
    result=""
    for i in tex["result"]:
        font=tex["result"][i]
        result+=f"**{i}:**`{font}`\n\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)
     
@app.on_message((filters.me) & filters.regex("^!fontfa "))
def font(client,message):
    text=message.text
    messag_id=message.message_id
    text=text.replace("!fontfa ","")
    Response=requests.post(f"https://api.codebazan.ir/font/?type=fa&text={text}")
    tex=Response.json()
    result=""
    for i in tex["Result"]:
        font=tex["Result"][i]
        result+=f"**{i}:**`{font}`\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)

@app.on_message((filters.me) & filters.regex("^!logo "))
def logo(client,message):
    text=message.text
    chat_id=message.chat.id
    messag_id=message.message_id
    text=text.replace("!logo ","")
    number=randint(1,110)
    Response=requests.post(f"https://api.codebazan.ir/ephoto/writeText?output=image&effect=create-online-black-and-white-layer-logo-{number}.html&text={text}")
    with open("test.jpg","wb") as f:
        f.write(Response.content)
    client.send_photo(chat_id,"test.jpg",reply_to_message_id=messag_id)
    os.remove("test.jpg")
    
@app.on_message((filters.me) & filters.regex("^!ttr "))
def ttr(client,message):
    text=message.text
    chat_id=message.chat.id
    language=text.split()[0]
    text=text.replace(language,"")
    myobj=gTTS(text=text,lang=language,slow=False)
    myobj.save("test.ogg")
    client.send_audio(chat_id,"test.ogg")
    os.remove('test.ogg')

@app.on_message((filters.me) & filters.regex("^!help$"))
def help(client,message):
    help=""
    help+="**command:**\n!.\n**descriptin:**\nget string and send strrev\n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!arz\n**descriptin:**\nsend list from name , price and change currency\n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!font\n**descriptin:**\ngen name or any thing and send difrent fonts\n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!fontfa\n**descriptin:**\nget persion text and send difrent font\n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!logo\n**descriptin:**\nget text and send logo withe text\n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!ttr\n**descriptin:**\nget language and text so send voice text withe input language \n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!pdf\n**descriptin:**\nget link web and send pdf shot web \n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!proxy\n**descriptin:**\nsend 20 MTproxy for telegram\n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    help+="**command:**\n!pass\n**descriptin:**\nget number and genereat password to len number\n/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=help)
app.run()  # Automatically start() and idle()
