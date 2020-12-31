from discord import Embed
import os
from config import DESCRIPTIONS, PREFIX

HELP = Embed(title="Jederu Blackmarket | Help", description="Snap je nou weer niet hoe het werkt?")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        HELP = HELP.add_field(name=PREFIX + filename[:-3], value=DESCRIPTIONS[filename[:-3]])
