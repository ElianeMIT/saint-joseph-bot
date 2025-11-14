import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    prayer = """
Hello
Here is my novena:

**Prière à St Joseph de François de Sales dans les situations difficiles**

Glorieux saint Joseph, époux de Marie,
accordez-nous votre protection paternelle,
nous vous en supplions par le Cœur de Jésus-Christ.
Ô vous dont la puissance s'étend à toutes nos nécessités
et sait nous rendre possible les choses les plus impossibles,
ouvrez vos yeux de père sur les intérêts de vos enfants.
Dans l'embarras et la peine qui nous pressent,
nous recourons à vous avec confiance.
Daignez prendre sous votre charitable conduite
cette affaire importante et difficile, cause de notre inquiétude.
Faites que son heureuse issue
soit pour la gloire de Dieu
et contribue au bien de ceux qui veulent le servir fidèlement.
Amen.
"""

    await message.channel.send(prayer)

    await bot.process_commands(message)

bot.run("YOUR_BOT_TOKEN_HERE")
