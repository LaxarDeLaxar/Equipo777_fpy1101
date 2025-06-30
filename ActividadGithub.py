
def luciano_diaz(estilo):
    import random
    sonidos = {
        "goregrind": ["*vómito*", "*sierras quirúrgicas*", "*guturales podridos*"],
        "mincecore": ["*blastbeat político*", "*feedback eterno*", "*crítica social*"],
        "powerviolence": ["*gritos rabiosos*", "*distorsión fea*", "*caos total*"]
    }
    if estilo in sonidos:
        print(f"Tocando {estilo.upper()}: {random.choice(sonidos[estilo])}")
    else:
        print("Estilo no válido. Usa goregrind, mincecore o powerviolence.")

luciano_diaz("mincecore")







while True:
  print("\n--- MENÚ PRINCIPAL ---")
  print("1. Función de integrante 1")
  print("2. Función de integrante 2")
  print("3. Función de integrante 3")
  print("0. Salir")
  op = input("Seleccione opción: ")
  if op == "0":
    print("Programa finalizado.")
    break
  elif op == "1":
    datos_LucianoR()
  elif op == "2":
    brandon_quiroz()
  elif op == "3":
    luciano_diaz("mincecore")
  else:
    print(" Opción inválida.")
