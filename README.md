# Hash-Table
- *Tabela hash* é uma estrutura de dados desenvolvida para resolver de maneira eficiente o problema de busca e armazenamento de dados. O principal objetivo de uma tabela hash é permitir o acesso rápido aos elementos, independentemente do número de itens armazenados, diferentemente de outras estruturas como listas ou árvores, onde o tempo de busca pode crescer proporcionalmente à quantidade de dados.
- A ideia central por trás da *tabela hash* é o uso de uma **função hash** que mapeia chaves para posições específicas na tabela. Esta função, denotada como $h(k)$, recebe uma chave k como entrada e retorna um índice na tabela:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $índice=h(k)$  
onde $h(k)$ é um valor numérico, geralmente dentro do intervalo $[0, m-1]$, sendo m o número de slots da tabela.

- Uma *tabela hash* é dita bem projetada quando a função hash distribui as chaves de forma uniforme sobre as posições disponíveis, minimizando a ocorrência de colisões. **Colisões** ocorrem quando duas chaves diferentes são mapeadas para o mesmo índice. Existem várias estratégias para resolver colisões, como **encadeamento lógico**, onde os elementos que colidem são armazenados em uma lista encadeada no mesmo índice, ou **endereçamento aberto**, onde um novo índice é encontrado usando uma função de sondagem.

### Execução
- Esse foi um projeto para a disciplina de *Algoritmos e Estruturas de Dados II* que exigia os seguintes testes para validar seu funcionamento:

A) **Encadeamento lógico**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Inserir 500 chaves geradas aleatoriamente (valores inteiros de 1 a 2000) utilizando o método da divisão com h(k) = k mod m.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Imprimir os tamanhos de cada uma das listas encadeadas dos slots e calcular a média.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Buscar 3 chaves que pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves?  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Buscar 3 chaves que não pertençam a Hash Table. Quantos acessos foram necessários para finalizar a busca sem sucesso de cada uma das chaves?  

B) **Endereçamento aberto**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Testar para: **linear probing**, **quadratic probing** e **double hashing**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Inserir 500 chaves geradas aleatoriamente (valores inteiros de 1 a 2000).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Buscar 10 chaves que pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves? E na média?  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Buscar 10 chaves que não pertençam a Hash Table. Quantos acessos foram necessários para finalizar a busca sem sucesso de cada uma das chaves? E na média?  

##  Status: Finalizado
