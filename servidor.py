# Carlos Eduardo da Silva
# Mat: 172050112
from socket import *
import string, sys, struct
from threading import Thread


def cifra_de_cesar(texto, chave=13):
    # Certificando que está tudo minusculo, não ha tratamento para simbolos
    texto = texto.lower()
    decodificado = ''
    abcdario = string.ascii_lowercase
    for letra in texto:
        # Recupera o indice correspondete a letra 
        indice = abcdario.find(letra)
        # caso retorne -1, foi enviado numeros ou simbolos
        if indice != -1:
            # Tirando a criptografia
            indice -= chave
            # Tratamento para juntar o fim do alfabeto com o inicio x,y,z,a,b,c
            decodificado += abcdario[indice if indice >= 0 else indice+len(abcdario)]
        else:
            print('ERROR')
            exit()
    return decodificado

def executa_client(connection_socket):
    # Recebe o tamanho da string
    tam_str = struct.unpack('!I',connection_socket.recv(4))
    
    # A string criptografada com a quantidade certa de bytes
    encriptado = connection_socket.recv(tam_str[0]).decode()
    
    # A key da criptografia 
    chave_cifra = struct.unpack('!I',connection_socket.recv(4))

    # Roda o algoritmo
    desencriptado = cifra_de_cesar(encriptado,chave_cifra[0])
    print(desencriptado)

    connection_socket.send(desencriptado.encode())
    # Manda e encerra
    connection_socket.close()

__, serverPort = sys.argv
serverSocket = socket(AF_INET,SOCK_STREAM)
#                        IPV4 E TPC
serverSocket.settimeout(15)
# Settando timeout
serverSocket.bind(('',int(serverPort)))
#                 ip e a porta


serverSocket.listen(1)
#  Deixa em espera

while True:
    # Aloca um socket e anota endereço
    connectionSocket, addr = serverSocket.accept()
    # Cria a thread e ja deixa o servidor esperando novamente
    th = Thread(target=executa_client, args=(connectionSocket,))
    th.start()
    
    