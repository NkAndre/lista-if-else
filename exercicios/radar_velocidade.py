# 1. O Radar de Velocidade (Básico) Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80 km/h, exiba uma mensagem dizendo que ele foi multado. A multa custa R$ 7,00 por cada km acima do limite. Se estiver abaixo, exiba "Boa viagem!".

v = int (input("Insira a velocidade do Carro : "))

if v > 80:
   excesso = v - 80
   multa = excesso * 7
   print(f"MULTADO! Você excedeu o limite de 80km/h em {excesso}km/h.")
   print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Boa Viagem ")