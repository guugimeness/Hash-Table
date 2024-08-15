class Open_Addressing_Hash():
    def __init__(self, m, hf, M, c1, c2):
        self.m = m      # número de slots
        self.hf = hf    # 1: linear probing; 2: quadratic probing; 3: double hashing
        self.table = [[None] for _ in range(m)]    # chaves armazenadas direto na tabela
        self.c1, self.c2 = c1, c2       # constantes auxiliares (quadratic); se não for quadratic: None
        self.M = M      # m auxiliar (double hashing); se não for double: None
        
    def hash_function(self, hf, key, i):
        if hf == 1:     # linear probing
            return (key+i) % self.m
        elif hf == 2:       # quadratic probing
            return (key + self.c1*i + self.c2*(i**2)) % self.m
        elif hf == 3:       # double hashing
            h1 = key % self.m
            h2 = 1 + (key % self.M)
            return ((h1) + i*(h2)) % self.m
        else:
            return

        
    def insert(self, key):
        i = 0
    
        while i!=self.m:
            index = self.hash_function(self.hf, key, i)
            if self.table[index][0] == None:
                self.table[index][0] = key
                break
            i+=1
        return True
            
    def search(self, key):
        i = 0
        index = self.hash_function(self.hf, key, i)
    
        while (i<self.m) and (self.table[index][0] is not None):
            if self.table[index][0] == key:
                print(f"Chave {key} encontrada! O número de acessos nessa busca foi {i+1}")
                return i+1
            
            i+=1
            index = self.hash_function(self.hf, key, i)
        
        print(f"Chave {key} não encontrada! O número de acessos nessa busca foi {i+1}")
        return i+1
        
    def delete(self, key):
        i = 0
        index = self.hash_function(self.hf, key, i)
        
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None
                return True
            i+=1

        return False
        