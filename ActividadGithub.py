

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


def datos_LucianoR ():
  print("Mi nombre es Luciano Roca y tengo 23 años")
  print("Calculadora de area de un triangulo")
  a=int(input("Ingrese la base del triangulo: "))
  b=int(input("Ingrese la altura del triangulo: "))
  c=(a*b)/2
  print(c)


def brandon_quiroz():
  import time
  from datetime import datetime
  horas = ["10:00", "13:00", "16:00", "19:00", "21:30"]
  print("⏳ Recordatorio de fumar iniciado. Ctrl+C para salir.")
  try:
    while True:
      ahora = datetime.now().strftime("%H:%M")
      if ahora in horas:
        print(f"🚬 ¡Hora de fumar! ({ahora})")
        time.sleep(60)  # Espera 1 minuto para no repetir
      time.sleep(30)  # Verifica cada 30 segundos
  except KeyboardInterrupt:
    print("\n👋 Recordatorio finalizado.")

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
