import os
import discord
from dotenv import load_dotenv
from discord import app_commands
from shikanokonokonokokoshitantan import nun

load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print('ログインしました')

@tree.command(
    name="nun",
    description="しかのこのこのここしたんたん",
    #guild=discord.Object(id=GUILD_ID)  # 特定のギルドでのみコマンドを使用可能にする
)
async def hoge(ctx:discord.Interaction):
    output = nun()
    await ctx.response.send_message(output)

client.run(TOKEN)
