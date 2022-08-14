class ColaDePacientes:
    def __init__(self):
        self.cola_de_pacientes = [] 
        
    #Anade elementos a la cola
    def nuevo_paciente(self,pacientes):
        self.cola_de_pacientes.append(pacientes)
        
    #Devuelve elemento de la cola 
    def proximo_paciente(self):
        print("EL SIGUIENTE PACIENTE ES: ", self.cola_de_pacientes.pop(0))
            
    def ver_cola(self):
        print(self.cola_de_pacientes)
      
       
cola_pacientes = ColaDePacientes()    
while True:
    print("1 ---> AGREGAR NUEVO PACIENTE:") 
    print("2 ---> LLAMAR PROXIMO PACIENTE:")
    print("3 ---> MOSTRAR LISTA DE PACIENTES:")
    print("4 ---> FIN DE PROGRAMA....")
    opciones = int(input("ELIJA UNA DE LAS OPCIONES ANTERIORES:"))
    if opciones == 1:
        name = str(input("NOMBRE DEL NUEVO PACIENTE:")) 
        cola_pacientes.nuevo_paciente(name)

    elif opciones == 2:
        print(cola_pacientes.proximo_paciente())

    elif opciones == 3:
        print(cola_pacientes.ver_cola())

    elif opciones == 4:
        break
    else:
        print("OPCION FUERA DE LOS LIMITES DE SELECCION, ELEGIR UN NUMERO DEL RANGO PERMITIDO..")