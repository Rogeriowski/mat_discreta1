# em c1_entrada e c2_entrada é a entrada para inserir os elementos do conjunto que você escolher
c1_entrada = input("\nDigite os elementos do conjunto 1 (separados por vírgula): ")
c2_entrada = input("\nDigite os elementos do conjunto 2 (separados por vírgula): ")
#em c1 e c2, coloquei a função "set()" para inserção de conjunto, ao mesmo tempo em que removi a "vírgula" como elemento desses conjuntos... Ou seja, na hora de inserir a entrada dos elementos, posso separá-los por vírgula, que o código não vai entender as vírgulas como elementos desse mesmo conjunto.
c1 = set(c1_entrada.split(','))
c2 = set(c2_entrada.split(','))
# variável básica para união, utilizando do moderador "|" para tal
uniao = c1 | c2
print(f"\nUnião dos conjuntos: {uniao}")
# variável básica para diferença, utilizando do moderador "-" para tal
dif = c1 - c2 
print(f"\nDiferença dos conjuntos é: {dif}")
print("\n")
