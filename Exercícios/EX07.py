# Leia 2 valores inteiros do terminal (teclado)
# E exiba a media desses valores.
# Ex.:
# Se os valores forem 10 e 5
# Exibir
# A média dos valores 10 e 5 é 7.5

print("Calculadora de média entre dois valores: ")
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
print(f"A média dos valores {valor1} e {valor2} é: {(valor1 + valor2)/2:.5f}")