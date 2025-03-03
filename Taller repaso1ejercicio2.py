class Empleado():
     def __init__(self,nombre,edad,cargo,salario):
         self.nombre=nombre
         self.edad=edad
         self.cargo=cargo
         self.salario=salario
         
         def getNombre(self):
          return self.nombre
         
         def getEdad(self):
             return self.edad
         
         def getCargo(self):
             return self.cargo
         
         def getSalario(self):
             return self.salario
         
         def setNombre(self,nombre):
             self.nombre=nombre
         
         def setEdad(self,edad):
            self.edad=edad
         
         def setCargo(self,cargo):
             self.cargo=cargo
            
         def setSalario(self,salario):
            self.salario=salario   
            
def cantidadSalarioMayor4000000Millones(empleado):
      cantidad = 0
      for empleado in empleado: 
        if empleado.getSalario() >4000000  and empleado. getCargo() == 'ingeniero':
         cantidad += 1
         print('la cantidad de empleados  con un salario mayo a 4000000 millones y con el cargo de ingenieroes de: ',cantidad)
         
def  calcularAcumuladoSalariosMenor2500000Millones(empleado):
         acumulado = 0
         for empleado in empleado:
            if empleado.getSalario() <=2500000  and empleado.getEdad()<=30 >=18:
                  acumulado += empleado.getSalario()
            print('el precio total de los vehiculos de combustible electrico es de: ',acumulado)
            
            
def calcularPromedioSalarioCargo(empleado):
        acumulado = 0
        cantidad = 0
        for empleado in empleado:
            if empleado.getSalario() == 'analista':
             acumulado += empleado.getSalario()
            cantidad += 1
        if cantidad == 0:
            print('No hay empleados con el cargo de analista')
        else:
            promedio = acumulado / cantidad
            print('El promedio del salario de los empleados con cargo de analista es de : ', promedio)
            
def calcularCuantosEmpleadosSpmMayores50Años(empleado):
         acumulado=0
         cantidad=0
         for empleado in empleado():
             if empleado.getEdad()>=50 and empleado.getCargo()== 'gerencia o direccion':
                cantidad +=1
                
                  
class Main():
          def main():    
            Empleados=[]
            for i in range(10): 
                  nombre= input('por favor ingrese el nombre del empleado:')
                  edad= int(input('por favor ingrese la edad del empleado: '))
                  cargo= input('por favor ingrese el cargo del empleado ')
                  salario=int(input('por favor ingrese el salario del empleado: '))
                  print ('Se guardo de manera exitosa la informacion del empleado')
                  empleado = Empleado(nombre,edad,cargo,salario)
                  Empleados.append(empleado)
        
            cantidadSalarioMayor4000000Millones(Empleados)
            calcularAcumuladoSalariosMenor2500000Millones(Empleados)
            calcularPromedioSalarioCargo(Empleados)  
            calcularCuantosEmpleadosSpmMayores50Años(Empleados)

if __name__ == "__main__":
    Main.main()                 