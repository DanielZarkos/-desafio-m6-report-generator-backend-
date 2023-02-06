# CNAB Reader

<p>Aplicação com objetivo de interpretar arquivos .txt com informações financeiras (CNAB) via web com soma total de todas as transações e listagem de cada atributo em um código CNAB</p>

## Tecnologias utilizadas:

<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Django Rest Framework</li>
</ul>

## Instruções para rodar localmente

### Requisito:

<ul>
    <li>Python</li>
</ul>

### Clone este repositório

```
git clone git@github.com: https://github.com/DanielZarkos/Cnab_Reader-DanielZarkos
```

### Crie o ambiente virtual em seu terminal

```
python -m venv venv
```

### Inicie o ambiente virtual

#### Windows

###### Abra o PowerShell

```
.\venv\Scripts\activate
```

#### Linux

```
source venv/bin/activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Execute as migrações

```
python manage.py migrate
```

### Inicie o servidor

```
python manage.py runserver
```

#### Para acessar a API coloque o end point

```
/api/cnab/
```
