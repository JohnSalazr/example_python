text1 = "Bienvenido a la empresa WC, en este apartado vamos a determinar su salario"
print(text1)

text2 = "Para identificar tu estadía en la empresa te pediremos los siguientes datos"
print(text2)

text3 = "número de documento"
print(text3)

number = input()


proyecto = "Inserte el número de proyecto al que pertenece"
print(proyecto)

unicos = 1 
unicos1 = 3
numeros = 3

Proyectos = {
    'P_a': 20000,
    'P_b': 10000,
    'P_c': 5000,
    'H_e': 6/100
}

salario_a = 30 * (Proyectos ["P_a"] * 8)
salario_b = 30 * (Proyectos ["P_b"] * 8)
salario_c = (30 * (Proyectos ["P_c"] * 8)) + (((Proyectos ["P_c"] * (Proyectos ["H_e"])) + Proyectos ["P_c"]) * 4)

if numeros >= unicos and numeros <= unicos1:
    print("Bienvenido a DW.sas")
else:
    print("Papi, cojala larga que usted no es de aquí")

if numeros == 1:
    print("Usted hace parte del proyecto A y su salario excede el tope de 1'500.000, siendo de:", salario_a)

if numeros == 2:
    print("Usted hace parte del proyecto B y su salario excede el tope de 1'500.000, siendo de:", salario_b)

if numeros == 3:
    print("Usted hace parte del proyecto c, su salario es menor a 1'500.000, siendo de:", salario_c)

