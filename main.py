import discord
import re
import requests

client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.channel.name.lower() == "creador-canales":
        match = role_pattern.match(message.content)
        if match:
            role1, role2, category_name = match.groups()
            # Get the guild object
            guild = message.guild
            # Get or create the category
            category = discord.utils.get(guild.categories, name=category_name)
            if category is None:
                category = await guild.create_category(category_name)
            # Create the channel
            channel = await guild.create_text_channel(f"{role1}-vs-{role2}", category=category)
            # Get the role objects
            role1_obj = discord.utils.get(guild.roles, name=role1)
            role2_obj = discord.utils.get(guild.roles, name=role2)
            # Set the permissions for the roles
            await channel.set_permissions(role1_obj, read_messages=True, send_messages=True)
            await channel.set_permissions(role2_obj, read_messages=True, send_messages=True)
        else:
            await message.channel.send("El comando no tiene la sintaxis correcta, por favor revisa la sintaxis y vuelve a intentarlo")

client.run("YOUR_BOT_TOKEN")
        



client.run(token)