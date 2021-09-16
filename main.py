from flask import app
from telegram.ext import *
import respostas as R
import requests
import json

API_TL = "1996496100:AAG6NcZMnIw2CGwwHDoLqItRhCtUj04Q6l8"
API_APP = "http://127.0.0.1:5000"

# Definição de comandos


def comando_start(update, context):

    usuario = update.message.from_user
    update.message.reply_text(
        f"Bem vindo, {usuario.first_name}, ao Bot de Teste! Se tiver alguma dúvida , você pode digitar /ajuda. Caso queira se cadastrar no nosso sistema, basta digitar /cadastro")


def comando_help(update, context):

    update.message.reply_text(
        "Comandos possíveis: \n/ajuda, \n/iniciar, \n/cadastro")


def comando_cadastro(update, context):

    usuario = update.message.from_user
    lista = []
    informações = requests.get(f"{API_APP}/info").json()

    # Checa se o id do usuario já se encontra no banco de dados
    for dict in informações["Usuarios"]:
        if usuario.id in dict.values():
            lista.append(usuario.id)

    if len(lista) > 0:
        update.message.reply_text(
            f"Usuário já foi cadastrado!")

    else:
        update.message.reply_text(
            f"Para se cadastrar no nosso sistema, digite /confirmar")


def confirmar_cadastro(update, context):

    usuario = update.message.from_user
    lista = []
    informações = requests.get(f"{API_APP}/info").json()

    # Checa se o id do usuario já se encontra no banco de dados
    for dict in informações["Usuarios"]:
        if usuario.id in dict.values():
            lista.append(usuario.id)

    if len(lista) > 0:
        update.message.reply_text(
            f"Usuário já foi cadastrado!")

    else:
        # Posta informações na API
        resposta = requests.post(
            f"{API_APP}/send/{usuario.first_name}/{usuario.last_name}/{usuario.id}").json()

        texto_resposta = resposta["text"]
        nome_resposta = resposta["Nome"]
        sobrenome_resposta = resposta["Sobrenome"]
        id_telegram_resposta = resposta["id_telegram"]

        update.message.reply_text(
            f"{texto_resposta}\n\nNome: {nome_resposta}\nSobrenome: {sobrenome_resposta}\nId do telegram: {id_telegram_resposta}")


def mensagens(update, context):
    # Acessa as amostras de msgs e suas respostas
    text = str(update.message.text).lower()
    response = R.amostra_msg(text)
    update.message.reply_text(response)


def main():

    updater = Updater(API_TL, use_context=True)
    dp = updater.dispatcher

    # Parametros dos comandos
    dp.add_handler(CommandHandler("start", comando_start))
    dp.add_handler(CommandHandler("iniciar", comando_start))
    dp.add_handler(CommandHandler("ajuda", comando_help))
    dp.add_handler(CommandHandler("help", comando_help))
    dp.add_handler(CommandHandler("cadastro", comando_cadastro))
    dp.add_handler(CommandHandler("confirmar", confirmar_cadastro))
    dp.add_handler(MessageHandler(Filters.text, mensagens))

    # Tempo de resposta do bot
    updater.start_polling(1)


if __name__ == "__main__":
    main()
