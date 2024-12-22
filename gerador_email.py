import random
import string

# Lista de nomes brasileiros comuns sem acentos
nomes = [
    "Ana", "Beatriz", "Camila", "Daniela", "Eduarda", "Fernanda", "Gabriela", "Isabela", "Juliana",
    "Larissa", "Mariana", "Natalia", "Patricia", "Raquel", "Sabrina", "Tatiane", "Vanessa", "Yasmin",
    "Alexandre", "Bruno", "Carlos", "Daniel", "Eduardo", "Felipe", "Gustavo", "Henrique", "Igor", "Joao",
    "Leonardo", "Matheus", "Nicolas", "Otavio", "Pedro", "Rafael", "Samuel", "Thiago", "Victor", "William"
]

# Lista de sobrenomes brasileiros comuns sem acentos
sobrenomes = [
    "Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Almeida", "Souza", "Gomes", "Martins",
    "Barbosa", "Dias", "Lima", "Carvalho", "Castro", "Ferreira", "Mendes", "Ribeiro", "Teixeira",
    "Monteiro", "Vieira", "Moura", "Farias", "Moreira", "Correia", "Nascimento", "Campos", "Cardoso", "Coelho"
]

# Domínios de e-mail comuns
dominios = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com", "uol.com.br", "bol.com.br"]

# Gerador de senha aprimorada
def gerar_senha():
    dia = random.randint(1, 28)  # Limitado para evitar datas inválidas
    mes = random.randint(1, 12)
    ano = random.randint(1970, 2010)
    parte_data = f"{dia:02d}{mes:02d}{str(ano)[-2:]}"  # Exemplo: '081205'

    letra_mai = random.choice(string.ascii_uppercase)  # Letra maiúscula
    letra_min = random.choice(string.ascii_lowercase)  # Letra minúscula
    especial = random.choice("@#$%&*!")  # Caractere especial

    # Combina tudo aleatoriamente
    senha = list(parte_data + letra_mai + letra_min + especial)
    random.shuffle(senha)  # Embaralha os caracteres
    return ''.join(senha)

# Gerador de e-mail com senha
def gerar_email_com_senha():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    numero = random.randint(1, 99)  # Opcional para adicionar ao nome
    dominio = random.choice(dominios)
    email = f"{nome.lower()}.{sobrenome.lower()}{numero}@{dominio}"
    senha = gerar_senha()
    return f"{nome} {sobrenome}", email, senha

# Gerando 10 nomes, e-mails e senhas como exemplo
for _ in range(10):
    nome_completo, email, senha = gerar_email_com_senha()
    print(f"Nome: {nome_completo}")
    print(f"Email: {email}")
    print(f"Senha: {senha}")
    print()
