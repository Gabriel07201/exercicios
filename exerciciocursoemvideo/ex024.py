# um programa que leia o nome de uma cidade e diga se contém o nome santo ou não
#cid = str.lower(input('Digite o nome de uma cidade:')).strip()
#print('santo' in cid)

#outro modo
c = str(input('Digite o nome de uma cidade:')).strip()
print('santo' in c.lower())
# esse segundo ficou melhor porque não modifica a frase da pessoa, mas claro que poderia colocar .title e isso iria ficar correto tbm
