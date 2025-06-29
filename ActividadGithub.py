
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
    pass # Aquí se llamará a la función del integrante 1
  elif op == "2":
    brandon_quiroz()
  elif op == "3":
    pass # Aquí se llamará a la función del integrante 3
  else:
    print(" Opción inválida.")

