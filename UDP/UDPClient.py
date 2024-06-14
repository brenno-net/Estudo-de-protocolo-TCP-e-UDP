from socket import *

serverName = 'hostname' # Define o nome do servidor (ou endereço IP) e a porta na qual o servidor está escutando
serverPort = 12000

# Cria um socket cliente do tipo UDP (SOCK_DGRAM) utilizando o protocolo de endereço IPv4 (AF_INET)
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')# Solicita ao usuário que insira uma frase em minúsculas

# Envia a mensagem digitada pelo usuário ao servidor.`encode()` converte a string em bytes
# A função `sendto` envia a mensagem ao endereço e porta especificados
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Recebe a resposta do servidor. `recvfrom` lê até 2048 bytes de dados
# Também retorna o endereço do servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Imprime a resposta recebida do servidor. O método `decode()` converte os bytes recebidos de volta para uma string
print(modifiedMessage.decode())

clientSocket.close()# Fecha o socket do cliente

