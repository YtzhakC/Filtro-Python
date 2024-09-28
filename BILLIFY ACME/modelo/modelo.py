import io

# Funciones productos.dat
datos = {}
productos = {}
clientes = {}
ventas = {}
def lectorProductos():
    f = open('BILLIFY ACME/datos/productos.dat', 'r')
    for i in f:
        data = f.readline().split(';')
        datos[i] = data
        producto = {
            'CODPROD':(datos[i]),
            'DESCPROD':datos[i],
            'VALORUNIT':(datos[i])
        }
        productos['CODPROD'] = producto
        print(datos[i])
    f.close()


def lectorClientes():
    f = open('BILLIFY ACME/datos/clientes.dat', 'r')
    for i in f:
        data = f.readline().split(';')
        datos[i] = data
        cliente = {
            'CODCLI':(datos[i]),
            'NOMBRE':datos[i],
            'TELEFONO':(datos[i])
        }
        clientes['CODCLI'] = cliente
        print(datos[i])
    f.close()
    return clientes

def lectorVentas():
    f = open('BILLIFY ACME/datos/ventas.dat', 'r')
    for i in f:
        data = f.readline().split(';')
        datos[i] = data
        venta = {
            'CODFACT':(datos[i]),
            'AÑO':datos[i],
            'MES':(datos[i]),
            'DIA':(datos[i]),
            'CODCLI':(datos[i]),
            'CODPROD':(datos[i]),
            'UNIDADESPROD':(datos[i]),
            'VALOR':(datos[i]),
            'VALORFACT':(datos[i]),
            
        }
        ventas['CODFACT'] = venta
        print(datos[i])
    f.close()
    return ventas
