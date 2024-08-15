class Chained_Hash():
    def __init__(self, m):
        self.m = m      # número de slots
        self.table = [[] for _ in range(m)]     # cada slot aponta para uma lista encadeada
    
    def hash_function(self, key):       # função para mapear as chave na tabela
        return (key % self.m)   # k mod m
        
    def insert(self, key):
        index = self.hash_function(key)     # calcular o slot h(key)
        
        if key in self.table[index]:        # não é permitido inserir 2 chaves iguais
            return False
        
        self.table[index].append(key)       # inserir key na cabeça da lista
        
    def search(self, key):
        index = self.hash_function(key)     # calcular o slot h(key)
        count = 0       # contador de acessos
        
        for i in range(len(self.table[index])):     # buscar chave na lista h(key)
            count+=1
            if self.table[index][i] == key:
                print(f"Chave {key} encontrada! O número de acessos nessa busca foi {count}")
                return True
        
        print(f"Chave {key} não encontrada! O número de acessos nessa busca foi {count}")
        return False
    
    def delete(self, key):
        index = self.hash_function(key)     # calcular o slot h(key)
        
        if key not in self.table[index]:    # checar se key está na lista encadeada
            return
            
        self.table[index].remove(key)       # remover a chave da lista
        
    def display(self):      # função para imprimir as chaves da tabela
        for i in range(self.m):
            print(f"[{i}]", end='')
            for k in self.table[i]:
                print(f" -> {k}", end='')
            print()
        print()