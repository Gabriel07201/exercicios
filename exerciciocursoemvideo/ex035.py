# ler 3 retas e dizer se elas podem formar um triângulo
print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro segmento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos abaixo NÃO PODEM FORMAR um triÂngulo!')
