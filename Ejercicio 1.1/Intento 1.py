print("Cuenta bancaria \n")

saldoinicial = 3480
print(f"Saldo incial:{saldoinicial}$ \n")

saldorestante = saldoinicial - 96
print(f"Se han retirado 96 \nSaldo del 11 de abril del 2021:{saldorestante}$ \n")

saldorestante += 1200
print(f"Se han agregado 1200 \nSaldo del 17 de abril de 2021:{saldorestante}$ \n")

saldorestante += int(saldorestante * 0.03)
print(f"Se ha agregado el 3% \nSaldo del 30 de abril de 2021:{saldorestante}$ \n")

saldorestante -= 51
print(f"Se han retidao 51 \nSaldo del 02 de mayo de 2021:{saldorestante}$ \n")

