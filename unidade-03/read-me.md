## Unidade III

#### Manipulação de funções, strings e arquivos

- Funções: 
Por definição, "função" é todo bloco de código que só poderá ser executado ser for explicitamente chamado. Uma função pode receber ou não dados que são chamados de parâmetros ou argumentos. Ela pode também, devolver ou não alguma informação ou dado, fica a critério do programador para qual finalidade a função criada. Veja exemplo01.py

1.1. Parâmetros: Os parâmetros, como já foi citado, são informações passadas para uma função. Os parâmetros ficam dentros do parênteses logo após o nome. Veja exemplo02.py

Podemos colocar qualquer quantidade de parâmetros quanto necessário, devendo ser separados por vírgulas. Além disso, uma função deve ser chamada com a quantidade de parâmetros ou argumentos com as quais foi definida. Veja exemplo03

Uma função também pode retornar valores com a instrução "return". Veja exemplo04.py

1.2. Variáveis locais e globais: Uma variável só está disponível ser for chamada na região em que foi chamada. Isso é chamado de "escopo" da função. Dessa forma, uma variável criada dentro de uma função só pode ser chamada dentro do escopo local dessa mesma função. Veja exemplo05.py
Uma variável criada dentro do escopo principal do Python é chamada de variável global e portanto pertence ao escopo global. Assim, uma variável global pode ser chamada em qualquer parte do programa Python, sendo local ou global. Veja exemplo06.py
Outro ponto a ser observado é que uma função pode ser definida dentro de outra função. Dessa forma, variáveis declaradas na função "externa" podem ser utilizadas na função "interna". 
É possível criar uma variável com escopo global dentro de uma função, utilizando a instrução global na criação da variável. Veja exemplo07.py
Outra observação é que é possível utilizar um valor de argumento padrão, caso a função seja chamada sem o argumento, e nesse caso a função usará o valor default (padrão). Veja exemplo09.py

1.3. Argumento default: Outra forma de enviar os argumentos para as funções é através da sintaxe chave = valor. Veja exemplo08.py

-----


