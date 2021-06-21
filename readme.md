# **Test ApiCloud**

1. **FastApi:**  
   Diante de uma breve pesquisa, resolvi utilizar a FastApi como framework, de acordo com informações que encontrei tem
   uma rápida resposta e uma fácil utilização.
2. **Pydantic (BaseModel):**
   Utilizei a biblioteca do Pydantic(BaseModel), para fazer a leitura de um Json. Pydantic e uma biblioteca em si para
   próprio Python para fazer a validação dos dados, no caso a entrada do Json do próprio teste.
3. **Postman:**    
   Como no Python não teria como fazer uma 'interface' com a FastApi, utilizei o postman para testar e utilizar a Api.
   Postman tem uma praticidade de teste de entrada e saída em vários modelos de dados e uma deles e o que eu precisava
   como Json.
4. **Tests:**
   No teste para o estágio, necessita de expêriencia em teste unitários, resolvi pesquisar como fazer testes em Python.
   Encontrei um artigo no Google, sobre Pytest e resolvi praticar para desenvolver os testes que necessitava. Consegui
   replicar 2 testes sobre a Api que funcionaram, são eles teste sobre Idade e o teste da velocidade de Internet.
5. **Arquivos/Pastas:**
   Bom, após prestar atenção no algoritmo inteiro e como teria que ficar o resultado final. E a 'possível' criação de
   vários arquivos **'.py'**, resolvi fazer uma breve pesquisa em questão de separação de pastas/arquivos, como não
   tendo experiência com design patterns. Vi alguns vídeos e resolvi separar **('rules')** que seria as regras de uso e
   as **('dtos')** que seria as entradas e saídas e por fim a pasta **('test')** para os testes que realizei.

## Considerando o Aprendizado:

Considerando que sem muita expêriencia em Python ou na área de programação, desenvolvi o teste em 95%. Gostei muito do
aprendizado, onde algumas dificuldades para separação do projeto e a criação dos métodos, após tirar algumas dúvidas,
consegui replicar o pedido da Api. Gostei do desafio onde obtive muita experiência, em pouco tempo. Metodologia de
separação de pastas com classes e funções, me mostrou que um projeto bem organizado e cada (função,método,class) em seu
devido lugar, facilita o entendimento para quem for ler seu código, isso facilita a vida de todos que estão envolvidos
em um tal projeto. Mostrando onde cada item quando necessário está em seu devido lugar.

## Utilização API.

Nos próprios arquivos do sistema, tem um **requirements.txt**, importando as quatro bibliotecas, que foram utilizadas na
criação da Api.

Para instalar as dependências do projeto.

```
1º - python get-pip.py
2º - pipinstall -r requirements.txt 
```

Para execução dos testes no terminal.

```
pytest tests/
```    

Para execução do projeto.

```
uvicorn router:app --reload
```
