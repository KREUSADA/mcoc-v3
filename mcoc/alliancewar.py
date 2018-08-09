import discord
from discord.ext import commands
import json
import requests

BASEPATH = 'https://raw.githubusercontent.com/JasonJW/mcoc-cogs/master/mcocMaps/data/'
ICON_SDF = 'https://raw.githubusercontent.com/JasonJW/mcoc-cogs/master/mcoc/data/sdf_icon.png'
COLLECTOR_ICON='https://raw.githubusercontent.com/JasonJW/mcoc-cogs/master/mcoc/data/cdt_icon.png'
JPAGS = 'http://www.alliancewar.com'
PATREON = 'https://patreon.com/collectorbot'
BOOSTDATA = requests.get('http://www.alliancewar.com/global/ui/js/boosts.json').text
BOOSTS = json.loads(BOOSTDATA)

AW_MAP_PATHS={
'bosskill': {
    'A':[1,2,19,25,46,49,50,53],
    'B':[],
    'C':[3,21,27,41,45,47,51],
    'D':[11,17,22,28,34,36,48],
    'E':[],
    'F':[12,18,24,30,35,37,48],
    'G':[4,7,13,14,31,38,42,52],
    'H':[],
    'I':[6,9,15,14,33,40,44,55]
    },
    'expert':{
    'A':[1,19,25,46,49,50,53],
    'B':[1,2,19,20,26,41,45,47],
    'C':[3,21,27,41,45,47,51],
    'D':[11,17,22,28,34,36,48],
    'E':[10,16,23,29,48],
    'F':[12,18,24,30,35,37,48],
    'G':[4,7,13,14,31,38,42,52],
    'H':[5,8,14,32,39,43,55],
    'I':[6,9,15,14,33,40,44,55]
    },
}

class AllianceWar:
    """Collector integration for JPAGS' AllianceWar.com."""


    @commands.group(pass_context=True, aliases=['aw',])
    async def alliancewar(self, ctx):
        ''' Commands [WIP]'''

    @alliancewar.command(pass_context=True, name="node")
    async def _node_info(self, ctx, nodeNumber, tier = 'expert'):
        '''Report Node information.'''
        season = 2
        if tier in {'expert','hard','challenger','intermediate','normal','easy'}:

            em = await self.get_awnode_details(ctx = ctx, nodeNumber=nodeNumber,tier=tier, season=season)
            await ctx.send(embed=em)
        else:
            await ctx.send('Valid tiers include: advanced, intermediate, challenger, hard, expert')

    @alliancewar.command(pass_context=True, hidden=True, name="map")
    async def _map(self, ctx, tier = 'expert'):
        '''Report AW track information.'''
        season = 2
        boosturl = 'http://www.alliancewar.com/global/ui/js/boosts.json'
        boosts = json.loads(requests.get(boosturl).text)
        # if boosts is not None:
            # await ctx.send('DEBUG: boosts.json loaded from alliancewar.com')
        tiers = {'expert': discord.Color.gold(),'bosskill': discord.Color.gold(),'hard':discord.Color.red(),'challenger':discord.Color.orange(),'intermediate':discord.Color.blue(), 'advanced':discord.Color.green(), 'normal':discord.Color.green(), 'easy':discord.Color.green()}
        if tier.lower() in tiers:
            mapTitle = 'Alliance War 3.0 {} Map'.format(tier.title())
            if tier.lower()=='advanced' or tier.lower()=='easy':
                tier ='normal'
            mapurl = '{}warmap_3_{}.png'.format(self.basepath,tier.lower())
            em = discord.Embed(color=tiers[tier],title=mapTitle,url=PATREON)
        em.set_image(url=mapurl)
        em.set_footer(text='CollectorDevTeam',icon_url=self.COLLECTOR_ICON)
        await ctx.send(embed=em)



    @alliancewar.command(pass_context=True, hidden=True, name="path", aliases=('tracks','track','paths'))
    async def _path_info(self, ctx, track='A', tier = 'expert'):
        '''Report AW track information.'''
        season = 2
        boosturl = 'http://www.alliancewar.com/global/ui/js/boosts.json'
        boosts = json.loads(requests.get(boosturl).text)
        # if boosts is not None:
            # await ctx.send('DEBUG: boosts.json loaded from alliancewar.com')
        tiers = {'expert':discord.Color.gold(),'hard':discord.Color.red(),'challenger':discord.Color.orange(),'intermediate':discord.Color.blue(),'advanced':discord.Color.green()}
        tracks = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
        if tier in tiers:
            pathurl = 'http://www.alliancewar.com/aw/js/aw_s{}_{}_9path.json'.format(season, tier)
            pathdata = json.loads(requests.get(pathurl).text)
            page_list = []
            for t in tracks:
                em = discord.Embed(color=tiers[tier], title='{} Alliance War Path {}'.format(tier.title(), track), descritpion='', url=JPAGS)
                em.add_field(name='node placeholder',value='boosts placeholders')
                em.add_field(name='node placeholder',value='boosts placeholders')
                em.add_field(name='node placeholder',value='boosts placeholders')
                mapurl = '{}warmap_3_{}.png'.format(self.basepath,tier.lower())
                em.set_image(url=mapurl)
                em.set_footer(icon_url=JPAGS+'/aw/images/app_icon.jpg',text='AllianceWar.com')
                page_list.append(em)

            await self.pages_menu(ctx=ctx, embed_list=page_list, timeout=60, page=tracks[track]-1)

        async def get_awnode_details(self, ctx, nodeNumber, tier, season):
            # boosts = json.loads(requests.get(boosturl).text)
            tiers = {
            'expert':{ 'color' :discord.Color.gold(), 'minis': [27,28,29,30,31,48,51,52,53,55], 'boss':[54]},
            'hard':{ 'color' :discord.Color.red(), 'minis': [48,51,52,53,55], 'boss':[54]},
            'challenger':{ 'color' :discord.Color.orange(), 'minis': [27,28,29,30,31,48,51,52,53,55], 'boss':[54]},
            'intermediate':{ 'color' :discord.Color.blue(), 'minis': [48,51,52,53,55], 'boss':[54]},
            'advanced':{ 'color' :discord.Color.green(), 'minis': [], 'boss':[]}}
            if tier not in tiers:
                jpagstier = 'advanced'
            else:
                jpagstier = tier
                pathurl = 'http://www.alliancewar.com/aw/js/aw_s{}_{}_9path.json'.format(season, jpagstier)
                pathdata = json.loads(requests.get(pathurl).text)
                if int(nodeNumber) in tiers[jpagstier]['minis']:
                    title='{} MINIBOSS Node {} Boosts'.format(tier.title(),nodeNumber)
                elif int(nodeNumber) in tiers[jpagstier]['boss']:
                    title='{} BOSS Node {} Boosts'.format(tier.title(),nodeNumber)
                else:
                    title='{} Node {} Boosts'.format(tier.title(),nodeNumber)
                    em = discord.Embed(color=tiers[jpagstier]['color'], title=title, descritpion='', url=JPAGS)
                    nodedetails = pathdata['boosts'][str(nodeNumber)]
                    for n in nodedetails:
                        title, text = '','No description. Report to @jpags#5202'
                        if ':' in n:
                            nodename, bump = n.split(':')
                        else:
                            nodename = n
                            bump = 0
                            if nodename in BOOSTS:
                                title = BOOSTS[nodename]['title']
                                if BOOSTS[nodename]['text'] is not '':
                                    text = BOOSTS[nodename]['text']
                                    print('nodename: {}\ntitle: {}\ntext: {}'.format(nodename, BOOSTS[nodename]['title'], BOOSTS[nodename]['text']))
                                    if bump is not None:
                                        try:
                                            text = text.format(bump)
                                        except:  #wrote specifically for limber_percent
                                            text = text.replace('}%}','}%').format(bump)  #wrote specifically for limber_percent
                                        print('nodename: {}\ntitle: {}\nbump: {}\ntext: {}'.format(nodename, BOOSTS[nodename]['title'], bump, BOOSTS[nodename]['text']))
                                    else:
                                        text = 'Description text is missing from alliancwar.com.  Report to @jpags#5202.'
                                else:
                                    title = 'Error: {}'.format(nodename)
                                    value = 'Boost details for {} missing from alliancewar.com.  Report to @jpags#5202.'.format(nodename)
                                    em.add_field(name=title, value=text, inline=False)
                                    em.set_footer(icon_url=JPAGS+'/aw/images/app_icon.jpg',text='AllianceWar.com')
                                    return em
    # @commands.command()
    # async def mycom(self, ctx):
        # """This does stuff!"""
        # Your code will go here
        # await ctx.send("I can do stuff!")
