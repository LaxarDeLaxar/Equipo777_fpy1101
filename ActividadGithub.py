def areaTriangulo(base, altura):
  area = (base*altura)/2
  return area
print("Calculadora de area de un triangulo")
a=int(input("Ingrese la base del triangulo: "))
b=int(input("Ingrese la altura del triangulo: "))
print(areaTriangulo(a,b))
