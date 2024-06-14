# Descrição geral: UDPClient.py

Este é um exemplo de um cliente UDP simples que se conecta a um servidor, envia uma mensagem e recebe uma resposta. O fluxo do programa é o seguinte:

- Importa as funções necessárias do módulo socket.
- Define o nome do servidor e a porta à qual deseja se conectar.
- Cria um socket do cliente do tipo UDP.
- Solicita ao usuário uma entrada de texto.
- Envia a entrada para o servidor, convertendo-a em bytes.
- Recebe a resposta do servidor, lendo até 2048 bytes.
- Exibe a resposta do servidor, convertendo-a de bytes para string.
- Fecha o socket do cliente.

# Descrição geral: UDPServer.py

Este é um exemplo de um servidor UDP simples que escuta mensagens em uma porta específica, recebe mensagens dos clientes, converte as mensagens para letras maiúsculas e as envia de volta aos clientes. O fluxo do programa é o seguinte:

- Importa as funções necessárias do módulo socket.
- Define a porta na qual o servidor irá escutar.
- Cria e configura um socket do servidor do tipo UDP.
- Associa o socket do servidor a um endereço IP e porta.
- Exibe uma mensagem indicando que o servidor está pronto para receber mensagens.
- Mantém um loop infinito para processar mensagens dos clientes.
- Para cada mensagem recebida, converte a mensagem para maiúsculas e envia a resposta de volta ao cliente.
