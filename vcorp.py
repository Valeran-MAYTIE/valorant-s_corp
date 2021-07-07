#!/usr/bin/python3.9
import discord
import os
from dotenv import load_dotenv
from src.MyClient import MyClient


default_intents = discord.Intents.default()
default_intents.members = True
default_intents.voice_states = True
default_intents.invites = True

client = MyClient(default_intents)
load_dotenv()
client.run(os.getenv("TOKEN"))
