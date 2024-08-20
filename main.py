try:
  numero_de_participantes = int(input("coloque o numero de participantes:  "))
  if numero_de_participantes < 0:
    print("numero de participantes invalido")
    exit()

except ValueError:
  print("coloque apenas numeros")
  exit()
  
tipo_de_reuniao = input("coloque o tipo de reuniao: (Normal/Executiva) ").lower()

if tipo_de_reuniao != "normal" and tipo_de_reuniao != "executiva":
  print(f"tipo de reuniao invalido")
  exit()
  
if numero_de_participantes <= 5 and tipo_de_reuniao == "normal":
  print("O Ideal e a Sala Pequena")
  
elif numero_de_participantes >5 and numero_de_participantes <=15 and tipo_de_reuniao == "normal": 
  print("O Ideal e a Sala Media")
  
elif numero_de_participantes > 15 or tipo_de_reuniao == "executiva":
  print("O Ideal e a Sala Grande")