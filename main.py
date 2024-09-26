#Clse bot para crear bots de discord
import discord
import random
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def info_contaminación(ctx):
    await ctx.send(f'La contaminación ambiental es la presencia de componentes nocivos en el medio ambiente y que, por tanto, son perjudiciales para los seres vivos.')
    await ctx.send(f'Exsisten tres tipos principales de contaminación:')
    await ctx.send(f'Contaminación del suelo')
    with open(f'images/img_c1.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)

    await ctx.send(f'Contaminación del hídrica o del agua')
    with open(f'images/img_c2.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)

    await ctx.send(f'Contaminación atmosférica o del aire')
    with open(f'images/img_c3.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)

@bot.command()
async def info_desechos(ctx):
    await ctx.send(f'Los desechos se pueden clasificar en desechos peligrosos y no peligrosos.')
    await ctx.send(f'Como su nombre lo indica los desechos peligrosos son dañinos y debemos evitar manipularlos, los desechos que si podemos usar son los no peligrosos')
    with open(f'images/img_d1.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    
    await ctx.send(f'Dentro de los desechos no peligrosos hay otras tres clasificaciones')
    with open(f'images/img_d2.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)

@bot.command()
async def manualidades_espacio(ctx):
    await ctx.send(f'Hay tres dificultades de manualidades sobre el espacio:')
    await ctx.send(f'Para la dificultad facil puedes usar el comando $espacio_facil')
    await ctx.send(f'Para la dificultad media puedes usar el comando $espacio_medio')
    await ctx.send(f'Para la dificultad dificil puedes usar el comando $espacio_dificil')

@bot.command()
async def espacio_facil(ctx):
    with open(f'images/holograma.jpg', 'rb') as f:
       picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un holograma hecho de discos reciclados, para hacerlo solo tienes que seguir estos pasos:')
    with open(f'images/holograma_t.jpg', 'rb') as f:
       picture = discord.File(f) 
    await ctx.send(file=picture)


@bot.command()
async def espacio_medio(ctx):
    with open(f'images/sistema.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un sistema solar que puedes hacer con carton reciclado o papel, este es el tutorial:')
    with open(f'images/sistema_t.jpg', 'rb') as f:
       picture = discord.File(f) 
    await ctx.send(file=picture)

@bot.command()
async def espacio_dificil(ctx):
    with open(f'images/modulo.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un modulo lunar de apollo 11 hecho con carton, el tutorial lo encuentras en este enlace: https://youtu.be/D2V6Bi96rv4?si=6an1kF6l3n3PzR3N:')


@bot.command()
async def manualidades_utiles(ctx):
    await ctx.send(f'Hay tres dificultades de manualidades útiles:')
    await ctx.send(f'Para la dificultad facil puedes usar el comando $utiles_facil')
    await ctx.send(f'Para la dificultad media puedes usar el comando $utiles_medio')
    await ctx.send(f'Para la dificultad dificil puedes usar el comando $utiles_dificil')

@bot.command()
async def utiles_facil(ctx):
    with open(f'images/archivero.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un archivero hecho de cajas de cereal, en esta imagen encuentras cómo hacerlo:')
    with open(f'images/archivero_t.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)

@bot.command()
async def utiles_medio(ctx):
    with open(f'images/organizador.jpg.', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un organizador hecho de rollos de papel higenico, este es el tutorial:')
    with open(f'images/organizador_t.jpg.', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)

@bot.command()
async def utiles_dificil(ctx):
    with open(f'images/portalapizes.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un porta lápizes hecho de papel periodico, estos son los pasos para hacerlo:')
    with open(f'images/portalapizes_t.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)



@bot.command()
async def manualidades_juegos(ctx):
    await ctx.send(f'Hay tres dificultades de juegos reciclados:')
    await ctx.send(f'Para la dificultad facil puedes usar el comando $juegos_facil')
    await ctx.send(f'Para la dificultad media puedes usar el comando $juegos_medio')
    await ctx.send(f'Para la dificultad dificil puedes usar el comando $juegos_dificil')

@bot.command()
async def juegos_facil(ctx):
    with open(f'images/carro.jpg', 'rb') as f:
       picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un carro mobible reciclado, es este enlace están los pasos: https://youtu.be/L75jZNKQNEA?si=Prww4y-ehN4cn2xg')


@bot.command()
async def juegos_medio(ctx):
    with open(f'images/laberinto.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un laberinto hidráulico hecho de cartón, este es el tutorial: https://youtu.be/tixPi19VlsU?si=GDllsCUvYPzf7d5r')


@bot.command()
async def juegos_dificil(ctx):
    with open(f'images/brazo.jpg', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file=picture)
    await ctx.send(f'Este es un brazo mecánico de cartón, el tutorial lo encuantras aquí: https://youtu.be/GTH_Tzg1DmA?si=RFzaJPwn2JVENnUx')

@bot.command()
async def help_(ctx):
    await ctx.send(f'El bot cuenta con estas funciones:')
    await ctx.send(f'-')
    await ctx.send(f'Las funciones de: info_')
    await ctx.send(f'-')
    await ctx.send(f'Estas funciones te explican algunos datos sobre la contaminación y contamos con las siguientes:')
    await ctx.send(f'info_contaminación')
    await ctx.send(f'info_desechos')
    await ctx.send(f'-')
    await ctx.send(f'Las funciones de: manualidades_')
    await ctx.send(f'-')
    await ctx.send(f'Estas funciones te muestran algunos tutoriales de manualidades recicladas, tenemos las siguientes categorías:')
    await ctx.send(f'manualidades_espacio')
    await ctx.send(f'manualidades_utiles')
    await ctx.send(f'manualidades_juegos')   



bot.run("")
