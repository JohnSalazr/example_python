accion1 = "Ya estoy en la entrada del evento"
accion2 = "Me estoy registrando"

#estructura de control (condicional if o si)
#nos permite realizar algo dependiendo de una condicion que se pida, es decir, si no cumple va a pasar algo, sino también pasa algo 
#esta sentencia (condicional if), va acompañado de lso operadores de comparación

"""
if estructora_datos1 < estructura_datos_dos
if estructora_datos1 <= estructura_datos_dos
if estructora_datos1 > estructura_datos_dos
if estructora_datos1 >= estructura_datos_dos
if estructora_datos1 == estructura_datos_dos
if estructora_datos1 != estructura_datos_dos
"""

#hay varias formas de utilizar la sentencia "if"
#if simple, if compuesto, if anidado



Dato_comparacion = 18
edad = 30
boleta = True
zona = 3
fecha_evento = "27-02-2023"
fecha_comparacion = "28-02-2023"

""""
#if simple
if edad >= Dato_comparación:
    print("ingresar,disfrutar del evento")
"""

#if compuesto
"""
if edad >= Dato_comparación:
    print("ingresar,disfrutar del evento")
else:
    print("vaya pa' la casa mijo")
"""

#if anidado


if edad >= Dato_comparacion and boleta:
    print("ingresar,disfrutar del evento")
else:
    print("vaya pa' la casa mijo")

zona 
if zona >= Dato_comparacion and boleta:
    print("Selecciona el tipo de boleta que deseas obtener")

if zona == 1 and edad >= Dato_comparacion and boleta:
    print('Su boleta esta situada en la zona vip')
if zona  == 2 and edad >= Dato_comparacion and boleta:
    print('Su boleta esta situada en la zona preferencial')
if zona  == 3 and edad >= Dato_comparacion and boleta:
    print('Su boleta esta situada en la zona general')
if zona  == 4 and edad >= Dato_comparacion and boleta:
    print('Su boleta esta situada en la zona baja')
if zona < 1 or zona > 4:
    print('Boleta no identificada, verifica de nuevo tu información')