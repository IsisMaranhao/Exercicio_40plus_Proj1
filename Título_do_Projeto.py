'''
Enunciado

Você foi contratado pelo Magazine Luiza para desenvolver um sistema que irá auxiliá-los a escolher os produtos que irão receber desconto na próxima Black Friday.

Para isso, você terá acesso a uma API que fornece alguns dados dos produtos: um ID (identificador único), o preço e a categoria do produto. Uma função pronta irá retornar para você o conjunto de dados já em formato adequado: uma lista de dicionários, onde cada dicionário representa um produto.

Você deverá implementar as funções para listar todas as categorias, listar todos os produtos de uma categoria, identificar o produto mais barato e o mais caro de uma categoria e o top 10 de produtos mais baratos e mais caros de toda a base de dados.

Você pode baixar a base de dados clicando aqui e o código pronto para auxiliá-lo clicando aqui. Renomeie a base de dados para dados.json.

Leia atentamente os comentários no código fornecido. Não modifique a função já pronta e respeite os parâmetros e retorno solicitados nos comentários de cada função que você irá desenvolver.

Atente-se ao prazo de entrega. Você pode entregar o seu exercício fazendo o upload do arquivo .py finalizado.

MENU:

	1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair


'''

dados = [
    {
        "id": "Davi",
        "preco": "1622.50",
        "categoria": "pcs"
    },
    {
        "id": "Junior",
        "preco": "4483.69",
        "categoria": "livros_importados"
    },
    {
        "id": "Isabella",
        "preco": "4427.15",
        "categoria": "pet_shop"
    },
    {
        "id": "Isis",
        "preco": "3229.52",
        "categoria": "eletronicos"
    },
    {
        "id": "Cleide",
        "preco": "3461.74",
        "categoria": "construcao_ferramentas_ferramentas"
    }
]

print(dados,'\n')

for dicionario in dados:
        print(dicionario)

print('\n')

for dicionario in dados:
    if 'preco' in dicionario:
        print(dicionario['preco'])