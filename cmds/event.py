import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import os
import os.path
import json
import random 

with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)
goldList = os.listdir("./image/goldImage")
on9WaterList = os.listdir("./image/on9Water")

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("Hello")
        channel = self.bot.get_channel(int(jdata['Welcome_Channel']))
        await channel.send(f"{member.mention} 入左黎 ! ")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print("Hello")
        channel = self.bot.get_channel(int(jdata['Leave_Channel']))
        await channel.send(f"{member.name} 走左佬 !")

            
    @commands.Cog.listener()
    async def on_message(self,message):

        if message.author == self.bot.user:
            return
        if message.author.bot: 
            return

        for i in jdata["goldenText"]:  #當段野 有"咁你" "錦鯉"etc 會  trigger 
            if i in message.content:
                image = random.choice(goldList)
                await message.channel.send("咁你有咩高見" , file=discord.File("image/goldImage/" + image))
                return

        if message.content in jdata["rubbishWater"]:    #當段野 剩係得"鈴狗""鈴緒on9"會  trigger 
            image = random.choice(on9WaterList)
            await message.channel.send(f"{message.author.mention}", file=discord.File("image/on9Water/" + image))
            return

        if "垃圾殺菇咩" in message.content or "垃圾探女" in message.content: 
            await message.channel.send(f"{message.author.mention} 55ok")
            return

        if "сука" in message.content:
            await message.channel.send("блять")

        if "блять" in message.content:
            await message.channel.send("Пошёл нажуй даун ебаный ебал твою блять семью пидорасов СУКА БЛЯТЬ")
def setup(bot):
    bot.add_cog(event(bot))