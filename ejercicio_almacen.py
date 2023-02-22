Articulos = {
    "Zapatos": 350000,
    "Tenis": 280000,
    "Camisetas": 175000,
    "Jeans": 200000
    }
    
print(Articulos)
#Precio total
resultado1 =Articulos["Zapatos"] + Articulos["Tenis"] + Articulos["Camisetas"] + Articulos["Jeans"]
print("precio total",resultado1)
#Promedio de ventas
Promedio = resultado1 / 4 
print ("El promedio de ventas es:",Promedio)
#Aumento Jeans
aumento = 6.2 
suma = Articulos ["Jeans"] * (aumento/100)
resultado2 = Articulos ["Jeans"] + suma
print("Aumento de 6.2%, Precio final Jeans es",resultado2)
#Descuento Zapatos
descuento = 0.8 
resta = Articulos ["Zapatos"] * (descuento/100)
resultado3 = Articulos ["Zapatos"]  - resta
print("descuento de 0.8%, Precio final de los zapatos es",resultado3)