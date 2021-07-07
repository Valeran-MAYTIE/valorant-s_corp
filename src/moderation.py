import discord
import datetime
from asyncio import sleep


class Moderation:
    async def deletMessage(self, message):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        if message.author.guild_permissions.manage_messages is True:
            await message.channel.delete_messages(messages)
            return
        await message.channel.send(
            f"""{message.author.mention}
Tu ne peut pas suprimer de message"""
        )

    async def add_bot_role(self, member):
        if member.bot is True:
            guild = self.get_guild(775820548093116478)
            bot = guild.get_role(796364319049908265)
            await member.add_roles(bot)
            return True
        return False

    async def add_vcorp_role(self, member):
        for guild in self.guilds:
            if guild.id == 775820548093116478:
                for role in guild.roles:
                    if role.id == 796356814421098547:
                        vcorpRole = role
        await member.add_roles(vcorpRole)

    async def ban(self, message):
        commande = message.content.split(" ")
        if message.author.guild_permissions.ban_members is False:
            await message.channel.send(
                "{}\nTu ne peut pas ban ".format(message.author.mention)
                + "cette utilisateur"
            )
            return
        if len(commande) >= 2:
            try:
                ban = discord.Object(commande[1])
                await message.guild.ban(ban)
            except discord.HTTPException:
                await message.channel.send(
                    "{}\n Je ne peut pas ban ".format(message.author.mention)
                    + "cette utilisateur"
                )
            except discord.Forbidden:
                await message.channel.send(
                    "{}\n Je ne peut pas ban ".format(message.author.mention)
                    + "cette utilisateur"
                )
        return

    async def unban(self, message):
        commande = message.content.split(" ")
        if message.author.guild_permissions.ban_members is False:
            await message.channel.send(
                "{}\n Je ne peut pas deban ".format(message.author.mention)
                + "cette utilisateur"
            )
            return
        if len(commande) >= 2:
            try:
                ban = discord.Object(commande[1])
                await message.guild.kick(ban)
            except discord.HTTPException:
                await message.channel.send(
                    "{}\n Je ne peut pas deban ".format(message.author.mention)
                    + "cette utilisateur"
                )
            except discord.Forbidden:
                await message.channel.send(
                    "{}\n Je ne peut pas deban ".format(message.author.mention)
                    + "cette utilisateur"
                )
        return

    async def kick(self, message):
        commande = message.content.split(" ")
        if message.author.guild_permissions.kick_members is False:
            await message.channel.send(
                "{}\n Tu ne peut pas kick ".format(message.author.mention)
                + "cette utilisateur"
            )
            return
        if len(commande) >= 2:
            try:
                kick = discord.Object(commande[1])
                await message.guild.kick(kick)
            except discord.HTTPException:
                await message.channel.send(
                    "{}\n Je ne peut pas kick ".format(message.author.mention)
                    + "cette utilisateur"
                )
            except discord.Forbidden:
                await message.channel.send(
                    "{}\n Je ne peut pas kick ".format(message.author.mention)
                    + "cette utilisateur"
                )
        return

    async def jail(self, message):
        if message.author.guild_permissions.administrator == True:
            if len(message.mentions) == 1:
                commmande = message.content.split(" ")
                member = message.mentions[0]
                prinson = message.guild.get_role(824031449145016432)
                prison_voice = message.guild.get_channel(824043211285987338)
                prison_channel = message.guild.get_channel(824030793537290270)
                roles = member.roles

                for role in range(1, len(roles)):
                    await member.remove_roles(roles[role])

                if member.voice != None:
                    if member.voice.channel != None:
                        channel = member.voice.channel
                        await member.move_to(prison_voice)

                await member.add_roles(prinson)

                if len(commmande) != 3:
                    commmande.append(1)

                embedVar = discord.Embed(title="Prison",
                                 description=f"Tu es en prison pendant {commmande[2]} minutes",
                                 color=0x00ff00,
                                 timestamp=datetime.datetime.now())
                await prison_channel.send(f"{member.mention}", embed = embedVar)

                await sleep(60 * int(commmande[2]))

                await member.remove_roles(prinson)

                for role in range(1, len(roles)):
                    await member.add_roles(roles[role])

                member = message.guild.get_member(member.id)
                if member.voice != None:
                    if member.voice.channel != None and channel != None:
                        await member.move_to(channel)
