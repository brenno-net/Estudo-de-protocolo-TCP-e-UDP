# Descrição geral: TCPClient.py

Este é um exemplo de um cliente TCP simples que se conecta a um servidor, envia uma mensagem e recebe uma resposta. O fluxo do programa é o seguinte:

- Importa as funções necessárias do módulo socket.
- Define o nome do servidor e a porta à qual deseja se conectar.
- Cria um socket do cliente e conecta ao servidor especificado.
- Solicita ao usuário uma entrada de texto.
- Envia a entrada para o servidor.
- Recebe a resposta do servidor.
- Exibe a resposta do servidor.
- Fecha a conexão do socket.

# Descrição geral: TCPServer.py

Este é um exemplo de um servidor TCP simples que escuta conexões em uma porta específica, recebe mensagens dos clientes, converte as mensagens para letras maiúsculas e as envia de volta aos clientes. O fluxo do programa é o seguinte:

- Importa as funções necessárias do módulo socket.
- Define a porta na qual o servidor irá escutar.
- Cria e configura um socket do servidor.
- Coloca o socket do servidor em modo de escuta para aceitar conexões.
- Mantém um loop infinito para aceitar e processar conexões dos clientes.
- Para cada conexão, recebe uma mensagem, a processa (convertendo para maiúsculas) e envia a resposta de volta ao cliente.
- Fecha a conexão com o cliente após o processamento.
