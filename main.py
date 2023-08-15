# TA FEITO (22:12, Aug 14, 2023)

idrev = int(
 input("Qual é a lição de revisão que você quer executar? Digite um número: "))

if idrev == 1:
	temp = float(input("Digite sua temperatura: "))
	if temp >= 37:
		print("A pessoa está com febre.")
	elif temp > 0 and temp < 37:
		print("A pessoa não está com febre.")
	else:
		print("Erro.")

elif idrev == 2:
	temp = int(input("Digite a temperatura: "))
	if temp >= 23 and temp <= 30:
		print("SIM")
	else:
		print("NÃO")

elif idrev == 3:
	num = int(input("Digite um inteiro: "))
	if (num % 2) == 0:
		print("Par")
	else:
		print("Ímpar")

elif idrev == 4:
	base1 = int(input("Digite o valor do lado do primeiro quadrado: "))
	base2 = int(input("Digite o valor do lado do segundo quadrado: "))
	if base1 != base2:
		print("Os dois quadrados não possuem a mesma área.")
	elif base1 == base2:
		print("Os dois quadrados possuem a mesma área.")

elif idrev == 5:
	base1 = int(input("Digite o valor da base do primeiro retângulo: "))
	altura1 = int(input("Digite o valor da altura do primeiro retângulo: "))
	base2 = int(input("Digite o valor da base do segundo retângulo: "))
	altura2 = int(input("Digite o valor da altura do segundo retângulo: "))
	if base1 * altura1 == base2 * altura2:
		print("Os dois retângulos possuem a mesma área.")
	else:
		print("Os dois retângulos não possuem a mesma área.")

elif idrev == 6:
	media = 6
	nota1 = float(input("Digite a primeira nota: "))
	nota2 = float(input("Digite a segunda nota: "))
	nota3 = float(input("Digite a terceira nota: "))
	nota4 = float(input("Digite a quarta nota: "))
	nota5 = float(input("Digite a quinta nota: "))
	notatotal = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
	if notatotal > 6 and notatotal <= 10:
		print(f"APROVADO com nota {notatotal}")
	elif notatotal < 6 and notatotal >= 0:
		print(f"REPROVADO com nota {notatotal}")
	else:
		print("ERRO.")

elif idrev == 7:
	print(
	 "PS. Professor, aqui eu coloquei um limite de nota pra cada semestre: 100 pontos são o máximo possível."
	)
	nota1 = float(input("Digite a nota do primeiro semestre: "))
	nota2 = float(input("Digite a nota do segundo semestre: "))
	notatotal = round(nota1 + nota2, 1)
	if notatotal > 60 and notatotal <= 200:
		print("NOTA FINAL: ", notatotal)
	elif notatotal < 60 and notatotal >= 0:
		print("NOTA FINAL:", notatotal)
		print("REPROVADO")
	else:
		print("ERRO.")

elif idrev == 8:
	val1 = int(input("Primeiro Número: "))
	val2 = int(input("Segundo Número: "))
	val3 = int(input("Terceiro Número: "))
	if val1 < val2 and val1 < val3:
		print(f"MENOR: {val1}")
	elif val2 < val1 and val2 < val3:
		print(f"MENOR: {val2}")
	elif val3 < val2 and val3 < val1:
		print(f"MENOR: {val3}")
	else:
		print("ERRO.")

elif idrev == 9:
	fixVal = 50
	fixTime = 100
	userTime = int(input("Digite a quantidade de minutos: "))
	userAddTime = (userTime % 50)
	userVal = userAddTime * 2
	if userTime > 0 and userTime > fixTime:
		print(f"Valor a Pagar: R${fixVal+userVal:.2f}")
	elif userTime > 0 and userTime <= fixTime:
		print(f"Valor a Pagar: R${fixVal:.2f}")
	else:
		print("ERRO.")

elif idrev == 10:
	gli = float(input("Digite a medida da glicose: "))
	if gli > 0 and gli <= 100:
		print("Classificação: normal")
	elif gli > 100 and gli <= 140:
		print("Classificação: elevada")
	elif gli > 140:
		print("Classificação: diabetes")
	else:
		print("ERRO. COMO QUE ALGUÉM PODE TER AÇÚCAR NEGATIVO?")

elif idrev == 0:
	print(
	 "Bazinga! Você achou o easter egg. Bem, você vai ver o código fonte disso mesmo, então não muda muita coisa eu ter feito isso, mas decidi brincar um pouco."
	)
