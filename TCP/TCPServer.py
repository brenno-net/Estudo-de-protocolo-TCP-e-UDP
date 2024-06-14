from socket import *

serverPort = 12000 # Define a porta na qual o servidor irá escutar

# Cria um socket do servidor do tipo TCP (SOCK_STREAM) utilizando o protocolo de endereço IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))# Associa o socket do servidor a um endereço IP e porta específicos
                                   # '' significa que o servidor aceita conexões em qualquer interface de rede

serverSocket.listen(1)# Configura o socket do servidor para ouvir conexões de entrada
                      # O argumento 1 especifica o número máximo de conexões pendentes

print('The server is ready to receive')# Exibe uma mensagem indicando que o servidor está pronto para receber conexões

# Loop infinito para manter o servidor rodando e aceitando conexões
while True:
    connectionSocket, addr = serverSocket.accept() # Aceita uma nova conexão de um cliente
    sentence = connectionSocket.recv(1024).decode() # Recebe a mensagem do cliente, até 1024 bytes 
    capitalizedSentence = sentence.upper() # Converte a mensagem recebida para letras maiúsculas
    connectionSocket.send(capitalizedSentence.encode()) # Envia a mensagem convertida de volta ao cliente
 
    connectionSocket.close()    # Fecha a conexão com o cliente atual

