print("Inicio do programa")

while True:
  print("realizando nheco nheco")
  # meu pai receberá a noticia de gravidez, .strip() e .lower() são métodos de string
  # que tiram espaços em branco e transformam tudo em minúsculo
  noticia_gravidez = input("tá grávida? (sim/não)").strip().lower()
  # se meu pai receber noticia de gravidez, ele vai comprar cigarro
  if noticia_gravidez == "sim":
    print("comprar cigarro")
    # este comando para o loop
    break
  # Note que não precisa colocar o else aqui, por que caso 
  # noticia_gravidez for igual a sim, ele já para o loop
  # antes de chegar aqui.
  print("ta safe")
print("fim do programa")
