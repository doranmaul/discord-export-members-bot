import discord
from discord.ext import commands
import csv

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents, scope=["bot", "applications.commands"])


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
# Set the commands for your bot
@bot.command()
async def greet(ctx):
    response = 'Hello, I am your discord bot'
    await ctx.send(response)

@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !greet \n !list_command \n !functions \n !export_members'
    await ctx.send(response)

@bot.command()
async def functions(ctx):
    response = 'I am a simple Discord bot for exporting members to csv! I will reply to your command!'
    await ctx.send(response)


@bot.command(name='export_members')
async def export_members(ctx):
    members = ctx.guild.members
    with open('members.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['User ID', 'Username', 'Discriminator', 'Roles'])

        for member in members:
            roles = [role.name for role in member.roles]
            csvwriter.writerow([member.id, member.name, member.discriminator, ', '.join(roles)])

    await ctx.send('Exported members to members.csv')

bot.run('INSERT TOKEN HERE')