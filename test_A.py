from chained_hash import Chained_Hash
import random

print("A)")

ch_hash = Chained_Hash(43)

keys = [random.randint(1, 2000) for _ in range(550)]

print("1) Inserir 500 chaves geradas aleatoriamente:")
for i in range(500):
    ch_hash.insert(keys[i])
    
ch_hash.display()

print("2) Imprimir os tamanhos de cada uma das listas encadeadas dos slots e calcular a média:")
length = []

for i in range(ch_hash.m):
    length.append(len(ch_hash.table[i]))
    print(f"[{i}] = {length[i]}")

average = sum(length)/ch_hash.m

print(f"Média do tamanho de cada lista encadeada da tabela = {average:.2f}")
print()

print("3) Busque 3 chaves que pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves?")

ch_hash.search(keys[0])
ch_hash.search(keys[200])
ch_hash.search(keys[400])

print()
print("4) Busque 3 chaves que não pertençam a Hash Table. Quantos acessos foram necessários para finalizar a busca sem sucesso de cada uma das chaves?")

ch_hash.search(2542)
ch_hash.search(3212)
ch_hash.search(2423)