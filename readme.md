# **Test ApiCloud**

1. **FastApi:**

Diante de uma breve pesquisa, resolvi utilizar a FastApi como framework, de acordo com informações que encontrei tem  
uma rápida resposta e uma fácil utilização.

2. **Pydantic (BaseModel):**

Utilizei a biblioteca do Pydantic(BaseModel), para fazer a leitura de um Json. Pydantic e uma biblioteca em si para  
próprio Python para fazer a validação dos dados, no caso a entrada do Json do próprio teste.

3. **Postman:**

Como no Python não teria como fazer uma 'interface', utilizei o postman para testar e utilizar a Api. Postman tem uma  
praticidade de teste de entrada e saída em vários modelos de dados e uma deles e o que eu precisava como Json.

4. **Arquivos/Pastas:**

Bom, após prestar atenção no algoritmo inteiro e como teria que ficar o resultado final. E a 'possível' criação de  
varios arquivos **'.py'**, resolvi fazer uma breve pesquisa em questão de separação de pastas/arquivos, como não  
tendo experiência com design patterns. Vi alguns vídeos e resolvi separar **('rules')** que seria as regras de uso e  
as **('dtos')** que seria as entradas e saídas.

## Considerando o Aprendizado:

Sem expêriencia na área do Python muito válida, tive algumas dificuldades na utilização dos construtores/métodos e os  
métodos privados. Muita pesquisa e tiração de dúvidas com alguns amigos da área. Consegui efetuar a execução
basicamente  
perfeita do Projeto solicitado para o Teste. Após aprender e consegui entender realmente como funcionava tive
facilidade  
de executar os passos restantes que faltava. Como iniciante as vezes só lendo não consigo aprender, mas na execução  
consigo replicar os passos e tendo a maioria das vezes sucesso.

## Utilização API.

No terminal, digite.

     1º - python get-pip.py
     
     2º - pip install -r requirements.txt  

Nos próprios arquivos do sistema, tem um **requirements.txt**, passando as duas bibliotecas que foram utilizadas na  
criação da api.

Para execução do projeto.

     uvicorn router:app --reload
