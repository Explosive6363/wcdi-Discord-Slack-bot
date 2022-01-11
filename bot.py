import discord
import slackweb
import os
from datetime import datetime, timedelta

token = os.environ['DISCORD_BOT_TOKEN']
webhook = os.environ['WEBHOOK_URL']

client = discord.Client()
slack = slackweb.Slack(url=webhook)

@client.event
async def on_voice_state_update(member, before, after):
    now = datetime.utcnow() + timedelta(hours=9)
    if before.channel == after.channel:
        return
    elif before.channel is None:
        msg = f'{now:%m/%d-%H:%M} に {member.display_name} が {after.channel.name} に参加しました。'
    elif after.channel is None:
        msg = f'{now:%m/%d-%H:%M} に {member.display_name} が {before.channel.name} から退出しました。'
    else:
        msg = f'{now:%m/%d-%H:%M} に {member.display_name} が {before.channel.name} から {after.channel.name} に移動しました。'
    slack.notify(text=msg)

client.run(token)
