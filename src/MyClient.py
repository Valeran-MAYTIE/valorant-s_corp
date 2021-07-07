#!/usr/bin/python3.9
from src.voice import Voice
from src.moderation import Moderation
import discord


class MyClient(discord.Client, Voice, Moderation):
    def __init__(self, default_intents):
        discord.Client.__init__(self, intents=default_intents)
        Voice.__init__(self)
        self.invites = list()

    async def on_invite_create(self, invite):
        self.invites = await self.guild.invites()

    async def on_invite_delete(self, invite):
        self.invites = await self.guild.invites()

    async def welcome_message(self, member, inviter):
        welcome_channel: discord.TextChannel = self.get_channel(
            799010937620398101)
        rules_channel: discord.TextChannel = self.get_channel(
            802191231513919508)
        message = "{}\nBienvenue a toi bg va voir {} ".format(
            member.mention,
            rules_channel.mention)
        message += "pour plus d'info sur ce serveur\n"
        message += "Tu as utilisé l'invitation de **{}**".format(
            inviter.name)
        await welcome_channel.send(content=message)

    async def ppdisplay(self, message):
        if len(message.mentions) == 0:
            pp = message.author.avatar_url
            await message.channel.send(pp)
            return
        else:
            for mention in message.mentions:
                pp = mention.avatar_url
                await message.channel.send(pp)
        return

    async def rename_member_count(self):
        count_channel: discord.VoiceChannel = self.get_channel(
            802535294175674419)
        for guild in self.guilds:
            if guild.id == 775820548093116478:
                total_member = guild.member_count
        newname = "Member Count: {}".format(str(total_member))
        await count_channel.edit(name=newname)

    async def emotedisplay(self, message):
        if len(message.stickers) != 0:
            for sticker in message.stickers:
                await message.channel.send(sticker.url)
        return

    async def get_inivter(self):
        new_invite = await self.guild.invites()
        for i in range(len(new_invite)):
            if new_invite[i].uses > self.invites[i].uses:
                return new_invite[i].inviter

    async def on_ready(self):
        self.guild = self.get_guild(775820548093116478)
        self.invites = await self.guild.invites()
        await self.rename_member_count()
        print("Logged as {}!".format(self.user))

    async def on_member_join(self, member):
        bot = await self.add_bot_role(member)
        inviter = await self.get_inivter()
        if bot is False:
            await self.welcome_message(member, inviter)
            await self.add_vcorp_role(member)
        await self.rename_member_count()
        self.invites = await self.guild.invites()

    async def on_member_remove(self, member):
        await self.rename_member_count()

    async def on_voice_state_update(self, member, before, after):
        await self.voicEventTraitment(member, before, after)
        return

    async def on_message(self, message):
        if message.content.startswith("v?"):
            await message.delete()
        if (message.content == "v?reaload"):
            await self.rename_member_count()
        elif message.content.startswith("v?pp"):
            await self.ppdisplay(message)
        elif message.content.startswith("v?emote"):
            await self.emotedisplay(message)
        elif message.content.startswith("v?voice"):
            reponse = await self.voiceCommande(message)
            await message.channel.send(reponse)
        elif message.content.startswith("v?delete"):
            await self.deletMessage(message)
        elif message.content.startswith("v?ban"):
            await self.ban(message)
        elif message.content.startswith("v?unban"):
            await self.unban(message)
        elif message.content.startswith("v?kick"):
            await self.kick(message)
        elif message.content.startswith("v?jail"):
            await self.jail(message)
