# Carlos Eduardo da Silva
# Mat: 172050112
from socket import *
import sys, string, struct

def cifra_de_cesar(texto, chave=13):
    texto = texto.lower()
    criptografado = ''
    abcdario = string.ascii_lowercase
    for letra in texto:
        indice = abcdario.find(letra)
        if indice != -1:
            indice += chave
            criptografado += abcdario[indice if indice < len(abcdario) else indice-len(abcdario)]
        else:
            print('ERROR')
            exit()
    return criptografado

__, serverName, serverPort, texto, num = sys.argv

msg = cifra_de_cesar(texto, int(num))

#                        IPV4 E TPC
clientSocket = socket(AF_INET,SOCK_STREAM)
# Timeout settado para 15segundos
clientSocket.settimeout(15)
# Tentativa de conexão com o server
clientSocket.connect((serverName,int(serverPort)))

# Envia para o servidor 
clientSocket.send(struct.pack('!I',len(msg)))
clientSocket.send(msg.encode())
clientSocket.send(struct.pack('!I', int(num)))

# Recebe o texto alterado
desencriptado = clientSocket.recv(len(msg))

print(desencriptado.decode())
# Printa e encerra a conexão
clientSocket.close()
