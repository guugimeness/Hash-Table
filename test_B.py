from open_addr_hash import Open_Addressing_Hash
import random

print("B) i) - Linear Probing")

linear_hash = Open_Addressing_Hash(1019, 1, None, None, None)

keys = [random.randint(1, 2000) for _ in range(500)]

print("1) Inserir 500 chaves geradas aleatoriamente...")
for i in range(500):
    linear_hash.insert(keys[i])

print()
print("2) Busque 10 chaves que pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves? E na média?")

count = 0   # contador de acessos
count += linear_hash.search(keys[0])
count += linear_hash.search(keys[50])
count += linear_hash.search(keys[100])
count += linear_hash.search(keys[150])
count += linear_hash.search(keys[200])
count += linear_hash.search(keys[250])
count += linear_hash.search(keys[300])
count += linear_hash.search(keys[350])
count += linear_hash.search(keys[400])
count += linear_hash.search(keys[450])
print(f"Média da quantidade de acessos = {count/10:.2f}")

print()
print("3) Busque 10 chaves que não pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves? E na média?")

count = 0   # contador de acessos
count += linear_hash.search(2354)
count += linear_hash.search(2105)
count += linear_hash.search(2486)
count += linear_hash.search(2657)
count += linear_hash.search(2871)
count += linear_hash.search(2989)
count += linear_hash.search(3210)
count += linear_hash.search(3320)
count += linear_hash.search(3489)
count += linear_hash.search(3654)
print(f"Média da quantidade de acessos = {count/10:.2f}")
print()

print("B) ii) - Quadratic Probing")

quadratic_hash = Open_Addressing_Hash(1019, 2, None, 3, 5)

print("1) Inserir 500 chaves geradas aleatoriamente...")
for i in range(500):
    quadratic_hash.insert(keys[i])

print()
print("2) Busque 10 chaves que pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves? E na média?")

count = 0   # contador de acessos
count += quadratic_hash.search(keys[0])
count += quadratic_hash.search(keys[50])
count += quadratic_hash.search(keys[100])
count += quadratic_hash.search(keys[150])
count += quadratic_hash.search(keys[200])
count += quadratic_hash.search(keys[250])
count += quadratic_hash.search(keys[300])
count += quadratic_hash.search(keys[350])
count += quadratic_hash.search(keys[400])
count += quadratic_hash.search(keys[450])
print(f"Média da quantidade de acessos = {count/10:.2f}")

print()
print("3) Busque 10 chaves que não pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves? E na média?")

count = 0   # contador de acessos
count += quadratic_hash.search(2354)
count += quadratic_hash.search(2105)
count += quadratic_hash.search(2486)
count += quadratic_hash.search(2657)
count += quadratic_hash.search(2871)
count += quadratic_hash.search(2989)
count += quadratic_hash.search(3210)
count += quadratic_hash.search(3320)
count += quadratic_hash.search(3489)
count += quadratic_hash.search(3654)
print(f"Média da quantidade de acessos = {count/10:.2f}")
print()

print("B) iii) - Double Hashing")

double_hash = Open_Addressing_Hash(1019, 3, 1013, None, None)

print("1) Inserir 500 chaves geradas aleatoriamente...")
for i in range(500):
    double_hash.insert(keys[i])

print()
print("2) Busque 10 chaves que pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves? E na média?")

count = 0   # contador de acessos
count += double_hash.search(keys[0])
count += double_hash.search(keys[50])
count += double_hash.search(keys[100])
count += double_hash.search(keys[150])
count += double_hash.search(keys[200])
count += double_hash.search(keys[250])
count += double_hash.search(keys[300])
count += double_hash.search(keys[350])
count += double_hash.search(keys[400])
count += double_hash.search(keys[450])
print(f"Média da quantidade de acessos = {count/10:.2f}")

print()
print("3) Busque 10 chaves que não pertençam a Hash Table. Quantos acessos foram necessários para encontrar cada uma das chaves? E na média?")

count = 0   # contador de acessos
count += double_hash.search(2354)
count += double_hash.search(2105)
count += double_hash.search(2486)
count += double_hash.search(2657)
count += double_hash.search(2871)
count += double_hash.search(2989)
count += double_hash.search(3210)
count += double_hash.search(3320)
count += double_hash.search(3489)
count += double_hash.search(3654)
print(f"Média da quantidade de acessos = {count/10:.2f}")
