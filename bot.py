import discord
import os
#import traceback
from datetime import datetime, timedelta


#bot = discord.Bot(command_prefix='/')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
server = os.environ['SERVER_ID']
channel = os.environ['CHANNEL_ID']

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == server and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(channel)
        if before.channel is None:
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None:
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)

#@bot.event
#async def on_command_error(ctx, error):
#    orig_error = getattr(error, "original", error)
#    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#    await ctx.send(error_msg)
#
#@bot.command()
#async def ping(ctx):
#    await ctx.send('pong')

client.run(token)
#bot.run(token)
