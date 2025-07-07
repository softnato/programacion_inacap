


def calcular_iva() :
    try:
        iva = 19/100
        precio = float(input('ingrese precio del producto'))
        if precio >= 0:
            valor_iva = precio*iva
            valor_total = precio  + valor_iva
            print(f'precio: {precio},   IVA: {valor_iva}, TOTAL: {valor_total}')
        else:
            print('no se permite ingresar valores negativos')
     
    except:
        print('valor ingresado no correspondea ubn numero')
    
calcular_iva()