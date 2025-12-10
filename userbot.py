from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped

api_id = 20898349
api_hash = "9fdb830d1e435b785f536247f49e7d87"

app = Client("userbot", api_id=api_id, api_hash=api_hash)
call = PyTgCalls(app)

@app.on_message()
async def join_and_set_volume(client, message):
    if message.text == ".joinvc":
        chat_id = message.chat.id

        await call.join_group_call(
            chat_id,
            AudioPiped("input.mp3"),
        )

        await call.change_volume(chat_id, 100)
        await message.reply("Joined VC and volume set to 100")

app.start()
call.start()
print("Userbot running...")
app.idle()
