def areaTriangulo(base, altura):
  area = (base*altura)/2
  return area
print("Calculadora de area de un triangulo")
a=int(input("Ingrese la base del triangulo: "))
b=int(input("Ingrese la altura del triangulo: "))
print(areaTriangulo(a,b))
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
    pass # Aquí se llamará a la función del integrante 2
  elif op == "3":
    pass # Aquí se llamará a la función del integrante 3
  else:
    print(" Opción inválida.")
