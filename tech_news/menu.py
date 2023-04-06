import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category
)
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12
def analyzer_menu():
    options = input(
           """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""
        )

    match options:
        case '0':
            mensagem = 'Digite quantas notícias serão buscadas:'
            resultado = get_tech_news(int(input()))
            print(resultado)
        case '1':
            mensagem = 'Digite o título:'
            resultado = search_by_title(input(mensagem))
            print(resultado)
        case '2':
            mensagem = 'Digite a data no formato aaaa-mm-dd:'
            resultado = search_by_date(input(mensagem))
            print(resultado)
        case '3':
            mensagem = 'Digite a categoria:'
            resultado = search_by_category(input(mensagem))
            print(resultado)
        case '4':
            top_5_categories()
        case '5':
            print("Encerrando script")
        case _:
            print('Opção inválida', file=sys.stderr)
