from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, ChatType

# Inisialisasi bot
api_id = '28977113'
api_hash = '63bb64a177f438aab3bf92d7371d4f92'
bot_token = '7169782276:AAESklIoVNdHotshUtZO4AYq7wDGq70t9qM'

Bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@Bot.on_chat_member_updated()
async def member_left(client: Client, event: ChatMemberUpdated):
    if event.chat.type == ChatType.CHANNEL:
        old_status = event.old_chat_member.status
        new_status = event.new_chat_member.status
        
        # Check if the user left the channel
        if old_status in ["member", "restricted"] and new_status == "left":
            user_id = event.old_chat_member.user.id
            chat_id = event.chat.id
            try:
                await client.ban_chat_member(chat_id=chat_id, user_id=user_id)
                print(f"User {user_id} has been banned from the channel {chat_id}.")
            except Exception as e:
                print(f"Failed to ban user {user_id} from channel {chat_id}: {e}")

# Menjalankan bot
Bot.run()
