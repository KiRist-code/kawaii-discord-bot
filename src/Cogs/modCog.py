import discord
from discord import app_commands
from discord.ext import commands


class ModCog(commands.Bot, commands.GroupCog, name="mod"):
    def __init__(self, bot: commands.Bot, intents: discord.Intents) -> None:
        self.bot = bot
        super().__init__(command_prefix=commands.when_mentioned_or('>'), intents=intents)  # this is now required in this context.

    @app_commands.command(name="ban")
    async def ban(self, interaction: discord.Interaction) -> None:
        """ ban someone """
        await interaction.response.send_message("Hello from sub command 1", ephemeral=True)

    @app_commands.command(name="kick")
    async def kick(self, interaction: discord.Interaction) -> None:
        """ kick someone """
        await interaction.response.send_message("Hello from sub command 2", ephemeral=True)

    @app_commands.command(name="timeout")
    async def timeout(self, interaction: discord.Interaction) -> None:
        """ timeout someone """
        await interaction.response.send_message("Hello from sub command 3", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModCog(bot,discord.Intents.default()), guilds=[discord.Object(id=991693323645497415),discord.Object(id=1044582441521795092)])
