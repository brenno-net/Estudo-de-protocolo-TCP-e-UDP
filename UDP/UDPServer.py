from socket import *

serverPort = 12000# Define a porta na qual o servidor irá escutar


# Cria um socket do servidor do tipo UDP (SOCK_DGRAM) utilizando o protocolo de endereço IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Associa o socket do servidor a um endereço IP e porta específicos
# '' significa que o servidor aceita conexões em qualquer interface de rede
serverSocket.bind(('', serverPort))

# Exibe uma mensagem indicando que o servidor está pronto para receber mensagens
print('The server is ready to receive')

# Loop infinito para manter o servidor rodando e aceitando mensagens
while True:
    print('loop em andamento...')  # Indica que o loop está ativo
    
    message, clientAddress = serverSocket.recvfrom(2048) # Recebe mensagem.`recvfrom` lê até 2048 bytes e retorna o endereço
    modifiedMessage = message.decode().upper() # Converte a mensagem recebida para letras maiúsculas
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) # Envia a mensagem convertida de volta ao cliente

