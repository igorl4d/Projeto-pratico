def amostra_msg(input_text):

    msg_usuario = str(input_text).lower()

    if msg_usuario in ("oi", "ola", "Bom dia", "Boa tarde", "Boa noite"):
        return "Olá, eu sou o bot da Wedev, para me usar basta digitar /iniciar! :)"

    if msg_usuario in ("iniciar"):
        return "Talvez você quis dizer /iniciar?"

    if msg_usuario in ("ajuda"):
        return "Talvez você quis dizer /ajuda?"

    else:
        return "Não te entendi, digite /ajuda para receber ajuda"
