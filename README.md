# cliente-servidorCriptografado

Introdução

Neste trabalho iremos desenvolver duas aplicações. Uma aplicação cliente que se conecta a um servidor e envia um string de texto criptografado, e uma aplicação servidora que recebe strings de clientes e retorna uma versão decodificada do mesmo. No texto abaixo, nomes de funções da biblioteca padrão relativas à tarefa sendo descrita estão referenciadas entre colchetes para facilitar o desenvolvimento do trabalho.
Objetivos

Introduzir a interface de programação de soquetes POSIX.

Introduzir os conceitos de aplicação cliente e aplicação servidor.

Introduzir os conceitos de codificação e transmissão de dados.

Cifra de César

Neste trabalho vamos usar um tipo de codificação simples para strings de texto denominado Cifra de César. O seu princípio de operação é escolher um certo inteiro X e trocar cada caractere do string pelo caractere X posições à frente no alfabeto. Considere que a letra [a] está à frente da letra [z]. Na prática, essa codificação é muito fácil de se quebrar, mas ilustra bem o princípio usado por algoritmos de criptografia. Na Internet, em grupos de discussão, uma versão muito popular usa X = 13 e é chamada de Rot13. Ela costuma ser usada para esconder spoilers ou a resposta de um quebra-cabeça, por exemplo.

Programa Cliente

O programa cliente receberá como parâmetros de linha de comando: o endereço IP da máquina onde o servidor estará executando, o número do porto em que ele estará esperando conexões, um string e um inteiro sem sinal. O string deve conter apenas os caracteres de [a] até [z], minúsculos e sem acento. (Note que o string não deve conter espaços, nem caracteres [\n] e [\r] de quebra de linha.) Ao executar, o cliente irá se conectar ao servidor [socket, bind, connect]. Após estabelecimento da conexão, o cliente irá enviar um inteiro de quatro bytes em network byte order [send, htonl/pack] indicando o tamanho do string. Em seguida, o cliente deve enviar o versão do string de entrada codificado usando a cifra de César (se você estiver usando C, note que o caractere de terminação [\0] não deve ser enviado). Imediatamente após o string, o cliente deve enviar o valor de X como um inteiro de quatro bytes, também em network byte order [send, htonl/pack]. 

Após o envio da requisição, o cliente irá esperar do servidor um string de caracteres ASCII [recv]. O string recebido contém o mesmo número de caracteres do string enviado, e também contém apenas caracteres entre [a] e [z], minúsculos e sem acento. Após recebimento do string do servidor, o cliente deve imprimi-lo na tela e fechar a conexão com o servidor [printf, close].

Programa Servidor

O programa servidor receberá como parâmetro de linha de comando o número do porto em que ele deve aguardar por conexões dos clientes [socket, bind, listen, accept]. Após o estabelecimento de uma conexão, o servidor deverá receber um inteiro de quatro bytes, network byte order [recv, ntohl/unpack] que indicará o tamanho do string que deverá ser lido em seguida [recv]. Após o recebimento do string, o servidor deverá receber outro inteiro de quatro bytes, network byte order [recv, ntohl/unpack],  com o valor de X.

O servidor deve então decodificar o string, escrevê-lo na saída [print/printf] e enviá-lo decodificado de volta para o cliente. Depois disso, o servidor deve fechar a conexão [close].

