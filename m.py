boleta = 5
if boleta >= dato_comparacion and boleta:
    print("Selecciona el tipo de boleta que deseas obtener")

if boleta == 1:
    print('Su boleta esta situada en la zona vip')
if boleta  == 2:
    print('Su boleta esta situada en la zona preferencial')
if boleta  == 3:
    print('Su boleta esta situada en la zona general')
if boleta  == 4:
    print('Su boleta esta situada en la zona baja')
if boleta < 1 or boleta > 4:
    print('Boleta no identificada, verifica de nuevo tu información')