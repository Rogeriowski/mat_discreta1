# em c1_entrada e c2_entrada é a entrada para inserir os elementos do conjunto que você escolher
c1_entrada = input("\nDigite os elementos do conjunto 1 (separados por vírgula): ")
c2_entrada = input("\nDigite os elementos do conjunto 2 (separados por vírgula): ")
#em c1 e c2, coloquei a função "set()" para inserção de conjunto, ao mesmo tempo em que removi a "vírgula" como elemento desses conjuntos... Ou seja, na hora de inserir a entrada dos elementos, posso separá-los por vírgula, que o código não vai entender as vírgulas como elementos desse mesmo conjunto.
c1 = set(c1_entrada.split(','))
c2 = set(c2_entrada.split(','))
# Aqui, inseri um comando básico de if e else, para identificar se um conjunto está contido no outro, utilizando do moderador "<="
if c1 <= c2:
    print("O conjunto 1 está contido no conjunto 2.")
else:
    print("O conjunto 1 não está contido no conjunto 2.")
print("\n")

