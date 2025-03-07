import re

#Binarios Pares

pattern = r'^[01]*0$'

binarios = ['0', '1', '10', '101', '110', '1110', '1001']

pares = [binario for binario in binarios if re.match(pattern, binario)]

print("Números binários pares:", pares)


#Palavras (binárias) com 00 no final

pattern = r'^[01]*00$'

binarios = ['00', '100', '10100', '11100', '1100', '010', '011']

terminam_com_00 = [binario for binario in binarios if re.match(pattern, binario)]

print("Palavras binárias que terminam com '00':", terminam_com_00)


#String entre aspas

pattern = r'"(.*?)"'

texto = 'Ele disse "Olá, mundo!" e depois saiu.'

strings_entre_aspas = re.findall(pattern, texto)

print("Strings entre aspas duplas:", strings_entre_aspas)


#Telefones em SC

pattern = r'\(?(47|48|49)\)?[-.\s]?[2-9][0-9]{3,4}[-.\s]?[0-9]{4}'

texto = """
Contato 1: (47) 1234-5678
Contato 2: 48 98765-4321
Contato 3: 49-8765-4321
Contato 4: 47987654321
"""

telefones = re.findall(pattern, texto)

print("Números de telefone em Santa Catarina:", telefones)


#Placas de veiculos no Brasil

pattern = r'^[A-Z]{3}-[0-9][A-Z][0-9]{2}$|^[A-Z]{3}-[0-9]{4}$'

placas = [
    "ABC-1234",  # Sistema anterior
    "XYZ-9876",  # Sistema anterior
    "ABC1D23",   # Padrão Mercosul
    "XYZ9K87"    # Padrão Mercosul
]

placas_validas = [placa for placa in placas if re.match(pattern, placa)]

print("Placas de veículos válidas no Brasil:", placas_validas)


#Email .br ou .com.br

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(br|com\.br)$'

emails = [
    "usuario@dominio.com",
    "usuario@dominio.com.br",
    "usuario@dominio.br",
    "usuario@dominio.net.br",
    "usuario@dominio.com",
    "usuario@dominio.org"
    "usuario@dominio.br.br"
]

emails_validos = [email for email in emails if re.match(pattern, email)]

print("Emails válidos (terminados em .br ou .com.br):", emails_validos)



#Comentarios de linha

pattern = r'#.*'

texto = """
# Este é um comentário de linha em Python
int main() {
    # Outro comentário
    printf("Hello, World!"); # Comentário no final da linha
    return 0;
}
"""

comentarios = re.findall(pattern, texto)

print("Comentários de linha:", comentarios)




#comentários de múltiplas linhas '''   '''

pattern = r'\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\"'

texto = """Este é um exemplo de comentário de múltiplas linhas em Python.
Podemos usar três aspas simples ou três aspas duplas."""

def funcao_exemplo():
    """
    Este é um comentário de múltiplas linhas dentro de uma função.
    Podemos documentar a função com uma descrição detalhada.
    """
    pass

comentarios_multiplas_linhas = re.findall(pattern, texto, re.DOTALL)

comentarios_multiplas_linhas = [comentario[0] or comentario[1] for comentario in comentarios_multiplas_linhas]

print("Comentários de múltiplas linhas:", comentarios_multiplas_linhas)
