import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = "ac")

# tells us when bot is online in console
@bot.event
async def on_ready():
	print("Bot is online.")

# tells us when someone has joined the server
@bot.event
async def on_member_join(member):
	await ctx.send(f"{member} has joined the server!")

# shows server ping command
@bot.command()
async def ping(ctx):
	await ctx.send(f"**Pong!**\nLatency: {round(bot.latency * 1000)}ms")

# calls 'name' a bot command
@bot.command()
async def isabot(ctx, *, name):
	if "327898244703322122" in name or "ac" == name or "AC" == name:
		await ctx.send("no u.")
	else:
		await ctx.send(f"{name} is a bot!")

# 8ball command
@bot.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
	if "327898244703322122" in question or "ac" == question or "AC" == question:
		await ctx.send(f"**Question:** {question}\n**Answer:** If it's a good thing, yes. If it's a bad thing, no.")
	else:
		responses = [
				"It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."]
		await ctx.send(f"**Question:** {question}\n**Answer:** {random.choice(responses)}")

# clear command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
	await ctx.channel.purge(limit=int(amount)+1)

# kick user
@bot.command()
# @commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

# ban user
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)


# @bot.event
# async def on_message(msg):
#     print("{} user has sent a message in {}".format(msg.author.name,msg.channel.name))
#     #whatever you want to do with the XP system

# @bot.command(pass_context=True)
# @commands.has_role("On Leave")
# async def something(ctx, user: discord.Member):
#   role = discord.utils.find(lambda r: r.name == 'Member', ctx.message.server.roles)
#   if role not in user.roles:
#       await bot.say("{} is not muted".format(user))
#   else:
#       await bot.add_roles(user, role)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
	await ctx.bot.logout()


bot.run("NjU5OTIwNzkxNjQ2NzY1MTI2.XgVVUg.7iZYmQCVhL44gElIMvfPIwBR-O0")