import discord
from discord.ext import commands
from discord.ext.commands import bot

TOKEN = '[REMOVED]'

# A queue to hold all songs
class Playlist:

    def __init__(self, bot):
        self.songs = []
        self.skipLimit = 3
        self.skipQueue = []
        self.bot = bot
    
    def setSkipLimit(self, limit):
        self.skipLimit = limit

    async def Spot(self, song):
        await self.bot.say('instert Spotify API here')
        return


    @commands.command(pass_context=False, no_pm=True)
    async def addSong(self, song):
        self.songs.append(song)
        return

    @commands.command(pass_context=False, no_pm=True)
    async def removeSong(self, song):
        self.songs.remove(song)
        return
    
    @commands.command(pass_context=False, no_pm=True)
    async def listSongs(self):
        for song in self.songs:
            await self.bot.say(song)
        return

    @commands.command(pass_context=False, no_pm=True)
    async def play(self):
        if len(self.songs) > 0:
            await self.Spot(self.songs.pop(0))
        else:
            await self.bot.say('There are no songs in the Queue.')
        return
    
    @commands.command(pass_context=True, no_pm=True)
    async def skipSong(self, ctx):
        if ctx.message.author.id not in self.skipQueue and len(self.songs) > 0 :

            await self.bot.say('[{0}/{1.skipLimit}] Votes to skip to the current song.'.format(len(self.skipQueue) + 1,self))

            if len(self.skipQueue) == self.skipLimit - 1:
                self.skipQueue.clear()
                await self.bot.say('Skipping this song.')
            else:
                self.skipQueue.append(ctx.message.author.id)

        elif len(self.songs) <= 0:
            await self.bot.say('There are no songs to skip.')
        else:
            await self.bot.say('You have already voted to skip this song.')
        return

SpotBot = discord.Client()
SpotBot = commands.Bot(command_prefix='$', description='A music bot that plays Spotify')
SpotBot.add_cog(Playlist(SpotBot))

@SpotBot.event
async def on_ready():
    print('Logged in as')
    print(SpotBot.user.name)
    print(SpotBot.user.id)
    print('------')

SpotBot.run(TOKEN)



