# essa porra aí em baixo é uma lista de dicionários
# provavelmente vc não sabe oq é pq vc é burro
# mas imagine que cada {} contém valores de uma pessoa que assistiu

assistiu = [
    {
        'nome': 'jailson',
        'deu_like': True,
        'comentou': True
    },
    {
        'nome': 'mano deyvin',
        'deu_like': True,
        'comentou': True
    },
    {
        'nome': 'alexandre de moraes',
        'deu_like': False,
        'comentou': False
    }
]

# Então, para cada pessoa que assistiu, ele vai fazer algo
for pessoa in assistiu:
  # aqui nós pegamos os valores de deu_like e de comentou de cada
  # pessoa e verificamos se os dois valores são verdadeiros
  # se sim, o cria agradece, se não....
  if pessoa['deu_like'] and pessoa['comentou']:
    print("Cria agradece")
  else:
    print("vai pra casa do c4r@l#0")