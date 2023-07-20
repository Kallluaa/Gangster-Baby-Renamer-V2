"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 05  ind /🌎 0.1$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 10  ind /🌎 0.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 1000GB
	Price Rs 15  ind /🌎 0.3$  per Month
	
	
	Pay Using Upi I'd ```mekhaleanish@okicici```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mr_kallua"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mr_kallua")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
		text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 05  ind /🌎 0.1$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 10  ind /🌎 0.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 1000GB
	Price Rs 15  ind /🌎 0.3$  per Month
	
	
	Pay Using Upi I'd ```mekhaleanish@okicici```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mr_kallua"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mr_kallua")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
