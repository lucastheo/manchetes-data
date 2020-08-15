# Manchetes

Essa aplicação tem como objetivo coletar a primeira página de diversos jornais e extrair informações dela, assim o transforma o html em dado não visual, um exemplo de dados extraído é as frequências das palavras (most_cited).

## Fase dos dados
Para o desenvolvimento da aplicação foi pensado em 4 estágios de dados. html, json raw, data base e json refined, os algoritmos fazem a informação passar pelos estágios sempre na ordem de html->json raw->data base->json refined.

#### Detalhes dos estágios
* Html: Dados da página armazenados sem nenhum tratamento, após o download.
* Json raw: Separação direta da informação da página sem tratamento nos dados. 
* Data base:Armazena toda informação extraída, algo sólido o qual pode ser reutilizável
* Json refined: Visualizações e junções de dados.

#### Detalhes dos estágios exemplos
* Html: O html da página
* Json raw: Exemplo é extrair todos os trechos de String da página sem extrair informação
* Data base: A frequencia de uma determinada palavra
* Json refined: A frequencia da palavra no dia pelo frequencia da palavra no mes

#### Informação sobre os programas
Os códigos dos algoritmos são executados pelo /automation/main.py de forma garantir o fluxo de dados, ou seja, tudo tem inicio em down_html, passando pela html-to-json-ra, depois json-ra-to-data-base, finalmente chegando em data-base-to-json-re.



