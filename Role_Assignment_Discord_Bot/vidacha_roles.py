import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv('bot_config.env')

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
ROLE_ID = int(os.getenv('ROLE_ID'))

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, sync_commands_debug=True)

recruitment_open = False

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Бот {bot.user.name} запущен.')
    print(f'Бот {bot.user.name} запущен и команды синхронизированы.')

def is_guild_owner():
    async def predicate(interaction: discord.Interaction):
        if interaction.user != interaction.guild.owner:
            owner_name = interaction.guild.owner.name
            await interaction.response.send_message(f"Ты не похож на владельца сервера {owner_name}, поэтому тебе нельзя использовать команды.", ephemeral=True)
            return False
        return True
    return discord.app_commands.check(predicate)

@bot.event
async def on_member_join(member):
    global recruitment_open
    if recruitment_open == 'True':
        channel = bot.get_channel(CHANNEL_ID)
        role = discord.utils.get(member.guild.roles, id=ROLE_ID)
        await member.add_roles(role)
        await channel.send(embed=discord.Embed(description=f'User `{member.name}`, has joined the server'))

@bot.tree.command(name="open", description="Открыть набор")
@is_guild_owner()
async def _open(interaction: discord.Interaction):
    global recruitment_open
    recruitment_open = True
    await interaction.response.send_message("Набор открыт! Все новые участники будут получать роль.")

@bot.tree.command(name="close", description="Закрыть набор")
@is_guild_owner()
async def _close(interaction: discord.Interaction):
    global recruitment_open
    recruitment_open = False
    await interaction.response.send_message("Набор закрыт! Новые участники не будут получать роль.")

@bot.tree.command(name="changerole", description="Изменить роль участника")
@is_guild_owner()
async def change_role(interaction: discord.Interaction, member: discord.Member, role_name: str):
    role = discord.utils.get(interaction.guild.roles, name=role_name)
    if not role:
        await interaction.response.send_message(f"Роль '{role_name}' не найдена.", ephemeral=True)
        return

    if role in member.roles:
        await member.remove_roles(role)
        await interaction.response.send_message(f"Роль '{role.name}' была удалена у {member.name}.")
    else:
        await member.add_roles(role)
        await interaction.response.send_message(f"Роль '{role.name}' была добавлена {member.name}.")

@bot.event
async def on_guild_join(guild):
    await bot.tree.sync(guild=guild)

bot.run(TOKEN)
