#imc = peso / (altura * altura)
print("academia mc valinhos")
print("....................")
print("Seja bem vindo(a)!")
nome = input("Por favor, me diga, o seu nome:")
idade = int(input("Agora precisa que você me informe a sua idade:"))
altura = float(input("Informe a sua altura:"))
nascimento = 2024 - idade
peso = float(input("informe o seu peso:"))
IMC = peso / (altura * altura)
print("olá senhor(A)", nome)
print("sua idade é:", idade, "anos.")
print("Você nasceu em :", nascimento)
print("sua altura é de:", altura, "mentros.")
print("seu peso é:", peso)
print("seu IMC é: {:.2f} kg/m²".format(IMC))