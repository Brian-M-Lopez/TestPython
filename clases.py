                                    # Ejercicio Clases
# ------------------------------------------------------------------------------------------------------------------------

# creo la clase
class Circulo:
    # defino los atributos iniciadores
    def __init__(self, rad):
        # creo una excepcion para que no permia que la instanciacion del circulo sea menor a 0
        if rad <= 0: 
            raise Exception('😭 No se puede crear un circulo con valor menor o igual a 0')
        self.rad = rad
        self.circle_area = 3.14 * self.rad  ** 2
        self.circle_perimetro = self.rad * 3.14 * 2

    # modifico el Dunder/magic Method de multiplicacion para permitir que al multiplicar la clase 
    # me devuelva la misma clase ya con el radio modificado por el multiplo
    def __mul__(self, other):
        if  other <= 0:
            raise Exception('El número debe ser mayor a cero 😤')
        new_circulo = Circulo(self.rad * other )
        return new_circulo
    
    # defino el metodo para devolver el area del circulo
    def area(self):
        return self.circle_area

    # defino el metodo para devolver el perimetro
    def perimetro(self):
        return self.circle_perimetro

    # defino el metodo para modificar el radio del circulo y evitando que sea igual o menor a 0
    def set_rad(self, new_rad):
        if new_rad <= 0:
            raise Exception('😭 No se puede crear un circulo con valor menor o igual a 0')
        self.rad = new_rad
        self.circle_area = 3.14 * new_rad ** 2
        self.circle_perimetro = new_rad * 3.14 * 2

    # metodo para mostrar por consola un print mas amigable del circulo
    def __str__(self):
            return f'Tu circulo tiene un radio de:📏 {int(self.rad)}cm \n un area de 📏 {int(self.circle_area)}cm \n un perimetro de 📏 {int(self.circle_perimetro)}cm '
    
# FUNCIONES PARA CREAR CIRCULOS:

# 1) FUNCION QUE MODIFICARÁ EL RADIO DEL CIRCULO
def rad_uppdate(x_cricle):
    uppdate = ''
    
    uppdate = input('¿Desea modificar el radio? Y/N: ')
    if uppdate == 'n' or uppdate == 'N':
        print('Okey su circulo quedo del siguiente modo:')
        print(x_cricle)
        return
    elif uppdate == 'y' or uppdate == 'Y':
        setting_rad = int(input('Ingrese el nuevo radio del criculo '))
        x_cricle.set_rad(setting_rad)
        print(x_cricle)
    else:
        raise Exception('debe ingresar Y or N...')

# 2) FUNCION QUE MULTIPLICARA EL RADIO DEL CIRCULO
def multiplicar():
    rad = int(input('Escriba el radio de su circulo '))
    mult = int(input('Por cuanto desea multiplicarlo? '))

    mi_circulo = Circulo(rad) * mult

    print(mi_circulo) 

    uppdate = ''

    uppdate = input('¿Desea modificar el radio? Y/N: ')
    if uppdate == 'n' or uppdate == 'N':
        print('Okey, no habra modificaciones')
        return
    elif uppdate == 'y' or uppdate == 'Y':
        setting_rad = int(input('Ingrese el nuevo radio del criculo '))
        mi_circulo.set_rad(setting_rad)
        print(mi_circulo)
    else:
        raise Exception('debe ingresar Y or N...')

# 3) CREACION DEL CRICULO INCLUYENDO LAS MODIFICACIONES
def new_circle ():
    rad = int(input('Escriba el radio de su circulo '))
    
    circle = Circulo(rad)

    print(circle)

    rad_uppdate(circle)

    mult_update = input('¿Desea multiplicar el radio? Y/N: ')
    if mult_update == 'N' or mult_update == 'n':
        print('Okey, no habra modificaciones')
    elif mult_update== 'y' or mult_update == 'Y':
        multiplicar()
    else:
        raise Exception('debe ingresar Y or N...')

# EJECUCION DE CREACION DEL CIRCULO MEDIANTE LA CONSOLA 
new_circle()
