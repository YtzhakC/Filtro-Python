def menu():
    sw = True

    print('''
                |────────────────────────────────|
                |              *MENÚ*            |
                | 1. Generar informe de factura. |
                | 2. Generar resumen facturas.   |
                | 3. Salir                       |
                |────────────────────────────────|
                        ''')
    print('')
    try:
        opc = input('Digite una opción: ')
        match opc:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
    except ValueError:
        print('Por favor, digite una opción')
    
#                                                                                            :(