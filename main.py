
import telebot
import os 
import random
import json
from dotenv import load_dotenv
from telebot import types,util

load_dotenv()

tempResp = 30
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.my_chat_member_handler()
def my_chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id,"""Olá, sou o BOT oficial do CITIG e fui adicionado a esse grupo.
Não se esqueça de me dar permissão de administrador para que eu possa operar de forma correta.""") # Welcome message, if bot was added to group


@bot.message_handler(commands=["help"])
def ajuda(mensagem):
    # print(mensagem)
    texto = """
    /PM Retorna as Placas de madeira
/PA Retorna as Placas de acrilíco
/CM Retorna as Chapas de madeira
/CA Retorna as Chapas de acrilíco
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["PM"])
def contrato(mensagem):
    bot.send_message(mensagem.chat.id, "PM")

@bot.message_handler(commands=["PA"])
def website(mensagem):
    bot.send_message(mensagem.chat.id, "PA")

@bot.message_handler(commands=["CM"])
def whitepaper(mensagem):
    bot.send_message(mensagem.chat.id, "CM")
    # document=open('arquivo.pdf', 'rb' )
    # bot.send_document(chat_id = mensagem.chat.id, data = document)

@bot.message_handler(commands=["CA"])
def discord(mensagem):
    bot.send_message(mensagem.chat.id, "CA")


def verificar(mensagem):
    return True


@bot.message_handler(commands=["command1","start"])
def ajuda(message):
        texto = """
Escolha uma opção para continuar (Clique no item):
/help retorna os comandos
/PM Retorna as Placas de madeira
/PA Retorna as Placas de acrilíco
/CM Retorna as Chapas de madeira
/CA Retorna as Chapas de acrilíco
Responder qualquer outra coisa não vai funcionar, clique em uma das opções """
        bot.reply_to(message, texto)


bot.infinity_polling(allowed_updates=util.update_types)

