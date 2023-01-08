import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()


class KawaiiBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('>'), intents=intents)

    async def on_ready(self):
        cogs_path = 'Cogs'
        abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), cogs_path)

        # Add Cogs
        for ext in os.listdir(abs_cogs_path):
            if ext.endswith(".py"):
                await super().load_extension(f"Cogs.{ext.split('.')[0]}")
                print(f'Loaded {ext}')

        bot.tree.copy_global_to(guild=discord.Object(id=1044582441521795092))
        await bot.tree.sync(guild=discord.Object(id=1044582441521795092))

        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = KawaiiBot()


# test command
@bot.tree.command(name="sayhello")
async def sayHello(interaction: discord.Interaction) -> None:
    """ say Hello to Bot """
    await interaction.response.send_message("Hello UwU", ephemeral=True)


# run with TOKEN
content = os.getenv("TOKEN")
bot.run(str(content))
