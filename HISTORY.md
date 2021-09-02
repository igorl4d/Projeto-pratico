# Projeto_wedev

Projeto desenvolvido para a vaga de desenvolvedor Python Junior. O projeto se trata de um bot do Telegram integrado em uma API desenvolvida com a mico-framework Flask. A API é encarragada de de inserir os dados dos usuários do bot em um banco de dados, assim como retornar informações para esses.

# Tecnologias usadas:

- Python
- Flask
- Sqlite3
- SqlAlchemy

# Funções:

## Main.py

Trata-se do arquivo do bot criado para a aplicação, nesse são determinadas diversas funções de comandos, as quais são chamadas por inputs de texto dos usuários, como /start, /ajuda, etc. Esse arquivo se comunica com os 2 endpoints da API, primeiro faz uma requisição GET, a fim de receber todos os usuários inscritos no banco de dados, e depois, caso o usuário não esteja presente no banco de dados, faz uma requisição POST, passando as informações para a API e recebendo um JSON como retorno.

## APP.py

A API do projeto, possui 2 endpoints, GET e POST. Essa API tem como principal função relacionar o bot com o banco de dados, a requisição GET mostra todas as informações do banco de dados e não recebe nenhum parámetro, já a POST, recebe como parametro as informações do usuário e as insere no banco de dados, retornando um JSON com as informações cadastradas e um texto.

## banco.py

Esse arquivo faz todas as operações relacionadas ao banco de dados e determina o modélo do banco de dados. Possuindo apenas 3 funções: **init()**, a qual checa se já existe um banco de dados, não existindo essa cria um, **query_all()**, essa que retorna todas as informações do banco de dados, e **inserir()**, o qual insere os valores passados para a API no banco de dados.

## resposta.py

Trata-se apenas de um arquivo onde são manipuladas as mensagens do usuário que não são comandos.

# Opiniões Finais:

Fico bastante grato com a oportunidade de participar desse processo seletivo, o teste prático foi bem desafiador, antes desse eu não tinha muita experiência com API's, muito menos com a criação de bots. De toda forma, fico feliz com a participação nesse seletivo antes mesmo da resposta, pois me trouxe conhecimento e desáfio. Novamente obrigado pela oportunidade :)
