

import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="+")
invitelink="https://discordapp.com/api/oauth2/authorize?client_id=694812810068361246&permissions=8&scope=bot"

async def owner(ctx):
    return ctx.author.id==621035977892167680

@bot.event
async def on_ready():
	print("Bot is running!")
	game=discord.Game("#FreeFortnite")
	await bot.change_presence(status=discord.Status.online,activity=game)
	
@bot.command()
async def ping(ctx):
	pingtime=bot.latency
	await ctx.send(f"Ping is {pingtime}")

@bot.command()
async def add(ctx,a:int,b:int):
	await ctx.send(a+b)
	
@bot.command()
async def sub(ctx,a:int,b:int):
	await ctx.send(a-b)
	
@bot.command()
async def multiply(ctx,a:int,b:int):
	await ctx.send(a*b)
	
@bot.command()
async def divide(ctx,a:int,b:int):
	await ctx.send(a/b)
		
@bot.command()
async def info(ctx,user:discord.User=None):
	if(user):
		name=f"{user.name}"
		id=f"{user.id}"
		e=discord.Embed(color=0x000000)
		e.add_field(name="Name",value=name)
		e.add_field(name="Id",value=id)
		e.set_footer(text="Made by Dabs Yt#6208")
		await ctx.send(embed=e)

@bot.command()
async def invite(ctx):
	await ctx.send(invitelink)

@bot.command()
@commands.check(owner)
async def kick(ctx,user:discord.Member=None):
    if(user):
        await ctx.send(f"{user.name} was kicked!")
        await user.kick()

               
@bot.command()
@commands.check(owner)
async def ban(ctx,user:discord.Member=None):
    if(user):
        await ctx.send(f"{user.name} was banned!")
        await user.ban()

bot.remove_command("help")
@bot.command()
async def help(ctx):
	e=discord.Embed(color=0x000000)
	e.add_field(name="+ping",value="Shows bot latency")
	e.add_field(name="+add {1} {2}",value="Adds 2 numbers")
	e.add_field(name="+sub {1} {2}",value="Subtracts 2 numbers")
	e.add_field(name="+multiply {1} {2}",value="Multiplies 2 numbers")
	e.add_field(name="+divide {1} {2}",value="Divides 2 numbers")
	e.add_field(name="+info {user}",value="Shows info about a user")
	e.add_field(name="+invite",value="Gives the link to invite this bot")
	e.set_footer(text="Made By Cricket FN")
	await ctx.send(embed=e)
		
bot.run("NzQzODA0MjQ0MTA0MzE1MDAw.XzZ_rw._KMstmMPQ6gQSmL6K34J2FYgDZw")