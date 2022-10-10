#PRISCILA CUBILLAS SOLANA
#cada elemento de la lista sera un diccionario del registro anterior.
listaArt=[]
def contieneCodigo(cod_art):
    for diccionario in listaArt:
        if (diccionario.get("codigo de articulo:") == cod_art):
            return listaArt.index(diccionario)
        return None
#ALTAS
def anadirProduc ():
    #añadidor de contenido cod de articulo
    cod_art = input("añade un codigo de articulo: ")
    while contieneCodigo(cod_art):
        cod_art = input("añade un codigo de articulo: ")
    # añadidor de contenido nombre
    nombArt = input("añade un nombre de articulo: ")
    # añadidor de contenido nombre
    descripArt = input("añade un descripcion de articulo: ")
    # añadidor de contenido precio
    precioArt = input("añade un precio de articulo: ")
    di_productos ={
            "codigo de articulo:":cod_art,
            "nombre de articulo:":nombArt,
            "descripcion de articulo:":descripArt,
            "precio de articulo:": precioArt

        }
    #añado tanto el nombre como la info
    listaArt.append(di_productos)
anadirProduc()
#print(listaArt)

#BAJAS
def eliminarProduc ():
    #añadidor de contenido cod de articulo
    cod_art = input("Seleccione  codigo de articulo que va a eliminar : " )
    articulo = contieneCodigo(cod_art)
    if articulo != None:
        listaArt.pop(articulo)
        print("Producto eliminado, codigo: "+ cod_art)
    else:
        print("El producto no se encuentra")
eliminarProduc()

    #una vez dentro preguntas que quieres modificae
#MODIFICAR
def modificarProduc ():
    cod_art = input("Introduce el codigo ")
    for i in listaArt:
        articulo_pro = contieneCodigo(cod_art)
        if articulo_pro != None:
            if i.get("codigo de articulo:") == cod_art:
                pregunta = input("Introduzca lo que quiere modificar ")
                if pregunta == 1:
                    nombre = input("Cambie el nombre del producto ")
                    articulo_pro.update({"Nombre articulo: ":nombre})
                elif pregunta == 2:
                    descripcion = input("Cambie el descripcion del producto ")
                    articulo_pro.update({"Descripcion articulo: ": descripcion})
                elif pregunta == 3:
                    precio = input("Cambie el precio del producto ")
                    articulo_pro.update({"Precio articulo: ":precio})
                else:
                    print("Introduzca un dato correcto")
            else:
                print("Introduzca un dato correcto")

modificarProduc()

#CONSULTA
def consultar():
    info = input("Introduce el codigo que quiere consultar")
    existente = False
    for i in listaArt:
        for clave, valor in i.items():
         if info != None  and valor == info:
            for clave, valor in i.items():
                existente = True
                print(clave,valor)
    if(existente == False):
        print("Producto no encontrado")

consultar()


def consultaDelProducto ():
    #si esta dentro lo modificas
    codigoArt = input("Introduce codigo articulo")
    for i in listaArt:
        i.get
        if (i.get("codigo artículo")== codigoArt):
            listaArt.__getitem__(i)

consultaDelProducto()