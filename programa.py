while True:
    idade = int(input("Digite sua idade: "))
    
    if 0 <= idade <= 120:
        break  # Sai do loop se a idade estiver dentro do intervalo
    
    print("A idade deve estar no intervalo de 0 a 120 anos. Tente novamente.")

if idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

    