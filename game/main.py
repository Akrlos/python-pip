import random # Se importa una opción aleatoria
Options=("Papel","Piedra","Tijera")
Computer_Wins=0
User_Wins=0
Rounds=1
while True:
  print("*"*10)
  print("ROUND",Rounds)
  print("*"*10)
  print("Computer_Wins",Computer_Wins)
  print("User_Wins", User_Wins)
  User_option=input("Elija entre Piedra, Papel o Tijera => ").capitalize()
  if not User_option in Options: # Si el dato no esta en las opciones arroja el mensaje a continuación
    print("Esa opción no es válida")
    continue
  Computer_option=random.choice(Options) # Permite seleccionar aleatoriamente un elemento de la lista señalada
  print("User option => ",User_option)
  print("Computer option => ",Computer_option)
  if User_option==Computer_option:
    print("Es un empate!")
  elif User_option=="Piedra":
    if Computer_option=="Tijera":
      print("Piedra gana a Tijera")
      print("User Wins")
      User_Wins+=1
    else:
      print("Papel gana a Piedra")
      print("Computer Wins")
      Computer_Wins+=1
  elif User_option=="Tijera":
    if Computer_option=="Papel":
      print("Tijera gana a Papel")
      print("User Wins")
      User_Wins+=1
    else:
      print("Piedra gana a Tijera")
      print("Computer Wins")
      Computer_Wins+=1
  elif User_option=="Papel":
    if Computer_option=="Piedra":
      print("Papel gana a Piedra")
      print("User Wins")
      User_Wins+=1
    else:
      print("Tijera gana a Papel")
      print("Computer Wins")
      Computer_Wins+=1
  if Computer_Wins==2:
    print("*"*10)
    print("Computer_Wins",Computer_Wins)
    print("User_Wins", User_Wins)
    print("El ganador definitivo es la computadora")
    break
  else:
    if User_Wins==2:
      print("*"*10)
      print("Computer_Wins",Computer_Wins)
      print("User_Wins", User_Wins)
      print("El ganador definitivo es el usuario")
      break
  Rounds+=1