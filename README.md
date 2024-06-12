# project-senai
Banco de Dados para o registro de informações sobre os reagentes do SENAI

## Instalando
Para rodar o aplicativo, é necessário primeiro instalar suas requisições
```
pip install -r requirements.txt
```
Depois, você poderá rodar os programas apropriadamente.

## Usagem
O aplicativo é dividido em dois programas. 

O `user.py` é o programa que é acessado pelo estudante, que irá registrar os gastos de reagentes e mandar para o banco de dados. 

O `adm.py` é o programa que é acessado pelo administrador do laboratório, onde ele terá acesso ao registro de todos os gastos do laboratório e poderá adicionar itens ao estoque.

Para acessar `adm.py`, é necessário login com usuário e senha. Para fins de teste, o programa já vem com o Usuário: *Teste* e Senha: *123456*. Caso queira adicionar um novo Usuário e Senha, pode fazê-lo rodando o programa `create_user.py`.

Caso precise inserir novos Reagentes ao estoque, poderá fazê-lo utilizando a interface de `adm.py`