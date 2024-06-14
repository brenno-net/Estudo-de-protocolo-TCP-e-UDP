from socket import *

# Define o nome do servidor (ou endereço IP) e a porta na qual o servidor está escutando
serverName = 'hostname'
serverPort = 12000

# Cria um socket cliente do tipo TCP (SOCK_STREAM) utilizando o protocolo de endereço IPv4 (AF_INET)
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))# Estabelece uma conexão com o servidor especificado pelo endereço e porta
sentence = input('Input lowercase sentence: ')# Solicita ao usuário que insira uma frase em minúsculas


# Envia a frase digitada pelo usuário ao servidor.'encode()' converte a string em bytes
clientSocket.send(sentence.encode())

# Recebe a resposta do servidor. Especifica que até 1024 bytes serão lidos de uma vez
modifiedSentence = clientSocket.recv(1024)

# Imprime a resposta recebida do servidor.`decode()` converte os bytes recebidos de volta para uma string
print('From Server:', modifiedSentence.decode())

clientSocket.close()# Fecha a conexão do socket com o servidor