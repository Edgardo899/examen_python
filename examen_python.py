import csv

def nombreDelArchivo():
    nombre_archivo = input("Ingresar nombre del archivo: ")
    return nombre_archivo
#Fin del método nombreDelArchivo().

def verificacionExistenciaArchivo(nombre_ingresado):
    # Variables para determinar si se crea el archivo o no.
    archivo_existe = True

    #Variable con el nombre de archivo.
    nombre = nombre_ingresado
    nombre += ".cvs"

    try:
        with (open(nombre)) as archivo:
            print(archivo.read())
    except FileNotFoundError: #Se crea el archivo csv no existente. 
        with (open(nombre,"w")) as archivo:
            archivo_existe = False

    return archivo_existe
#Fin del método verificaciónArchivo().

def crearContenidoArchivo(nombre_del_archivo):
    #Creo un archivo .txt para después agregarle el contenido al .csv.
    nombre = nombre_del_archivo+".txt"
    with open(nombre,"w") as archivo_modelo:
        archivo_modelo.write("Legajo;Apellido;Nombre\n")
        archivo_modelo.write("1;Estevanez;Laura\n")
        archivo_modelo.write("2;Ricardo;Ruben\n")
        archivo_modelo.write("3;Paniagua;Laura\n")
        archivo_modelo.write("4;Gonzalez;Marco Antonio\n")
    with open(nombre) as archivo_modelo:
        print(archivo_modelo.read())
        
    #fin del método agregarContenidoAlArchivo()
    #Practica
def main():
    nombre = nombreDelArchivo()
    valor_devuelto = verificacionExistenciaArchivo(nombre)
    if valor_devuelto == False:
        crearContenidoArchivo(nombre)
    print("¡fin del programa!")
#Fin del método principal.

main()