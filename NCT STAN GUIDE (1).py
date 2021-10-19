"""
********
Luz Emilia Raygoza Murguía
A01635441
Programa de NCT: NCT STAN GUIDE
Es un menu que despliega la información a interes sobre NCT,
para poder comprender la dinamica del grupo.


Se usaron classes, las cuales sirven para darles cualidades/caracteristicas a un objeto; en este caso fueron personas.
https://www.w3schools.com/python/python_classes.asp

********
"""


"""
****
Funciones utiles (operaciones y arreglos)
****

"""    
def suma_1994_1995(Jy, Tl, Ty, Yt, K, Dy, T):
    
    """
    (uso de operaciones y funciones)
    
    Recibe: Jy, Tl, Ty, Yt, K, Dy, T (todos son representativos
    de los nombres de los miembros, para la clase que contiene su edad)
    
    Suma las edades de los miembros entre los años
    de 1994 y 1995
    
    Devuelve: La suma de los parametros
    """
    
    return Jy + Tl + Ty + Yt + K + Dy + T


def suma_1997_1999(Jh, W, Jw, L, M, Xj, Hd):
    
    """
    (uso de operaciones y funciones)
    
    Recibe: Jh, W, Jw, L, M, Xj, Hd (todos son representativos
    de los nombres de los miembros, para la clase que contiene su edad)
    
    Suma las edades de los miembros entre los años de 1997 y 1999
    
    Devuelve: La suma de los parametros
    """
    
    return Jh + W + Jw + L + M + Xj + Hd


def suma_2000_2002(Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js):
    
    """
    (uso de operaciones y funciones)
    
    Recibe: Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js (todos son representativos
    de los nombres de los miembros, para la clase que contiene su edad)
    
    Suma las edades de los miembros entre los años de 2000 y 2002
    
    Devuelve: La suma de los parametros
    """
    
    return Rj + J + Hc + Jm + Yy + St + Sc + Cl + Js


def promedio_edad(Jy, Tl, Ty, Yt, K, Dy, T, Jh, W, Jw, L, M, Xj, Hd, Rj,
                  J, Hc, Jm, Yy, St, Sc, Cl, Js):
    
    """
    (uso de operaciones y funciones)
    
    Recibe: Jy, Tl, Ty, Yt, K, Dy, T, Jh, W, Jw, L, M, Xj, Hd, Rj,
     J, Hc, Jm, Yy, St, Sc, Cl, Js (todos son representativos
    de los nombres de los miembros, para la clase que contiene su edad)
    
    Saca el promedio de edades de los 23 miembros
    
    Devuelve: El valor de la suma de los parametros entre
    el numero de miembros
    
    """
    
    suma_total = (suma_1994_1995(Jy, Tl, Ty, Yt, K, Dy, T)
                  + suma_1997_1999(Jh, W, Jw, L, M, Xj, Hd) +
                  suma_2000_2002(Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js))
    
    return (suma_total/23)


def promedio_nct_127(Jy, Tl, Ty, Yt, Dy, Jh, W, Jw, M, Hc):
    
    """
    (uso de funciones y operaciones)
    
    Recibe: Jy, Tl, Ty, Yt, Dy, Jh, W, Jw, M, Hc (todos son representativos
    de los nombres de los miembros, para la clase que contiene su edad)
    
    Saca el promedio de edad en NCT 127
    
    Devuelve: El valor de la suma de los parametros entre
    el numero de miembros
    """
    
    return (Jy + Tl + Ty + Yt + Dy + Jh + W + Jw + M + Hc)/10


def promedio_nct_dream(M, Rj, J, Hc, Jm, Cl, Js):
    
    """
    (uso de funciones y operaciones)
    
    Recibe: M, Rj, J, Hc, Jm, Cl, Js (todos son representativos
    de los nombres de los miembros, para la clase que contiene su edad)
    
    Saca el promedio de edad en NCT DREAM
    
    Devuelve:El valor de la suma de los parametros entre
    el numero de miembros
    """
    return (M + Rj + J + Hc + Jm + Cl + Js)/7


def promedio_wayv (K, T, W, L, Xj, Hd, Yy):
    
    """
    (uso de funciones y operaciones)
    
    Recibe: K, T, W, L, Xj, Hd, Yy (todos son representativos
    de los nombres de los miembros, para la clase que contiene su edad)
    
    Saca el promedio de edad en WAYV
    
    Devuelve: El valor de la suma de los parametros entre
    el numero de miembros
    """
    
    return (K + T + W + L + Xj + Hd + Yy)/7


def promedio():
    
    """
    (uso de funciones)
    
    imprime el promedio de edad en cada subdivision
    """
    
    print("Promedio de todo NCT: ", promedio_edad(johnny.edad, taeil.edad,\
    taeyong.edad, yuta.edad, kun.edad, doyoung.edad, ten.edad, jaehyun.edad,\
    winwin.edad, jungwoo.edad, lucas.edad, mark.edad, xiaojun.edad,\
    hendery.edad,renjun.edad, jaemin.edad, haechan.edad, jaemin.edad,\
    yangyang.edad, shotaro.edad, sungchan.edad, chenle.edad,jisung.edad ))
    
    print("Promedio de NCT 127: ", promedio_nct_127(johnny.edad, taeil.edad,\
    taeyong.edad, yuta.edad, doyoung.edad, jaehyun.edad, winwin.edad,\
    jungwoo.edad, mark.edad, haechan.edad ))
    
    print("Promedio de NCT DREAM: ", promedio_nct_dream(mark.edad,\
    renjun.edad, jeno.edad, haechan.edad, jaemin.edad, chenle.edad,\
    jisung.edad))
    
    print("Promedio de WAYV", promedio_wayv(kun.edad, ten.edad,\
    winwin.edad, lucas.edad, xiaojun.edad, hendery.edad, yangyang.edad))


def nct_visual_estetico(i):
    
    """
    (uso de funciones, condicionales)
    
    Recibe:i (posicion de la subunidad en la lista principal)
    
    un titulo para tener una representacion
    visual más clara al imprimir la lista de
    nct_visual
    
    Devuelve: un titulo en base al valor de i,
    representativo de la posicion en la lista.
    
    """
    
    if i == 0:
        return "NCT U: "
    elif i == 1:
        return "NCT 127: "
    elif i == 2:
        return "NCT DREAM: "
    elif i == 3:
        return "WAYV: "
    
    
def nct_visual(grupo):
    
    """
    (uso de for, listas, listas anidadas y operadores)
    
    Recibe: grupo (lista anidada nct)
    
    fragmenta la lista para tener las subdivisiones con
    sus respectivos miembros.
    
    Devuelve: Lista con su titulo correspondiente a la subdivision
    """
    
    i = 0 
    for subdivision in grupo:
        print(nct_visual_estetico(i))
        print(subdivision)
        i= 1 + i
 
"""
****
Funciones menu (funcionamiento global de secciones)
****
"""
def inicio_bienvenida():
    
    """
    Imprime el menu principal con el que se van a explorar
    las secciones
    """
    print("Buenas tardes usuario")
    print("Para consultar nuestra información cheque el catalogo")
    print("Para terminar su busqueda escriba salir al selecionar su seccion")
    print("Responder si o no a menos que se indique lo contrario(minusculas)")
    print(
        """
        Subdivisiones:
        
        Miembros:
        
        Musica:
           
           """)
    
 
def seccion_subdivisiones(subdivisiones, sub1, sub2, sub3, sub4):
    
    """
    (uso de condicionales, ciclos while, ciclos while anidados y funciones)
    
    Recibe: subdivisiones (string con nombre de subdivisiones), sub1
    (conjunto nct_u), sub2 (conjuto nct_dream), sub3 (conjunto nct_127),
    sub4 (conjunto way)
    
    Seccion de subdivisiones, donde se va a explorar la seccion.
    """
    
    bandera = True
    while bandera:
        
        print(subdivisiones)
        
        print("Escribe nombre de subdivision o no para continuar")
        
        info_2 = input("¿Quieres saber quien esta en cierta subdivision? ")
        
    
        if info_2 == "nct u":
            print(nct_u)
        elif info_2 == "nct dream":
            print(nct_dream)
        elif info_2 == "nct 127":
            print(nct_127)
        elif info_2 == "wayv":
            print(wayv)
        
        else:
            while bandera:
       
                info_3 = input("¿Quieres saber en que subdivision esta alguien? ")
               
                
                if info_3 == "si":
                    print(miembros)
                    
                    info_5 = input("Escribe el nombre\
(Mayuscula al principio) ")
                    if info_5 in sub1:
                        print("Si esta en NCT U el miembro " + info_5)
                    if info_5 not in sub1:
                        print("No esta en NCT U el miembro " + info_5)
                    if info_5 in sub2:
                        print("Si esta en NCT DREAM el miembro " + info_5)
                    if info_5 not in sub2:
                        print("No esta en NCT DREAM el miembro " + info_5)
                    if info_5 in sub3:
                        print("Si esta en NCT 127 el miembro " + info_5)
                    if info_5 not in sub3:
                        print("No esta en NCT 127 el miembro " + info_5)
                    if info_5 in sub4:
                        print("Si esta en WAYV el miembro " + info_5)
                    if info_5 not in sub4: 
                        print("No esta en WAYV el miembro " + info_5) 
                else:
                    while bandera:
                        info_6 = input("¿Quieres una representación de NCT? ")
                        if info_6 == "si":
                            print(nct_visual(nct))
                        
                        else:
                            while info_6 == "no":
                                bandera = False
                                break
                            
                           
def seccion_miembros(miembros):
    
    """
    (uso de funciones, condicionales y ciclos while)
    
    Recibe: miembros (string con nombre de miembros)
    
    Seccion miembros, donde se va a explorr esta seccion.
    """
    
    print(miembros)
   
    promedio_pregunta = input("¿Quieres saber el promedio de edad de NCT? ")
    if promedio_pregunta == "si":
        promedio()
    elif promedio_pregunta == "no":
        while promedio_pregunta == "no":
            bandera = False
            break
                           
    
def seccion_musica(musica, albums, mini_albums_singles, music_videos ):
    """
    (uso de funciones, ciclos while, condicionales)
    
    Recibe: musica (string con opciones de la seccion de musica),
    albums (string con nombre de albums), mini_albums_singles
    (string con nombre de mini albums & singles), music_videos
    (string con nombre de videos musicales)
    
    Seccion de musica, donde se explora la seccion.
    """
    
    print(musica)
    
    while True:
        info_4 = input("¿Que sub-categoria quieres desplegar? \
albums, mini albums & singles, music videos (para terminar escribir no) ")
        if info_4 == "albums":
            print(albums)
        elif info_4 == "mini albums & singles":
            print(mini_albums_singles)
 
        elif info_4 == "music videos":
            print(music_videos)
       
        elif info_4 == "no":
            break    
                    


"""
*****                     *****


VARIABLES PARA EL INICIO


*****                     *****
"""


subdivisiones = """
NCT U, NCT DREAM, NCT 127 y WayV
"""
miembros = """
Johnny, Taeil, Taeyong, Yuta, Kun, Doyoung, Ten, Jaehyun, WinWin, Jungwoo,
Lucas, Mark, Xiaojun, Hendery, Renjun, Jeno, Haechan, Jaemin, YangYang,
Shotaro, Sungchan, Chenle & Jisung
        """

musica = """
Albums, Mini Albums y Singles, Music Videos
"""
albums = """
        NCT 2018 EMPATHY, NCT#127 REGULAR-IRREGULAR,
        NCT#127 REGULATE (REPACKAGE), Awaken, NEO CITY: SEOUL,
        THE DREAM SHOW, NCT#127 Neo Zone,
        NCT#127 Neo Zone: The Final Round (REPACKAGE),Awaken The World,
        NCT RESONANCE Pt.2, Hot Sauce & Hello Future (REPACKAGE)
           """
mini_albums_singles = """
           The 7th sense, WITHOUT YOU, NCT#127, Chewing Gum,
           NCT#127 LIMITLESS, The First, NCT#127 CHERRY BOMB,
           Trigger the fever, JOY, Timeless,Radio Romance, Chain,
           Baby Don't Stop (Thai Version), We Go Up, Touch (Japanes Version),
           Up Next Session: NCT 127, DreamWorks Trolls X SM STATION,
           Candle Light, Let's Shut UP&DANCE, Don't need your love,
           So am I, Fireflies, The Vision, Take Off,
           NCT#127 WE ARE SUPERHUMAN, Highway to heaven (English version),
           We boom, When You're on the Blacklist of the Bullies,
           The tale of Nodku, Take Over the Moon, Love Talk (English Version),
           STATION X LOVEs for Winter, Reload, iScreaM Vol.1: Kick It (REMIX),
           iScreaM Vol.2: Ridin' (REMIXES), Turn Back Time,
           Bad Alive (English Version), RESONANCE,
           iScreaM Vol.6: Make a Wish/ 90's Love Remix, Kick Back, Save,
           iScreaM Vol9: Hot Sauce Remixes, Maniac
"""

music_videos = """ YESTODAY, The 7th Sense, WITHOUT YOU, Fire Truck,
           Chewing Gum, Switch, Limitless, My First and Last,
           Dream in a Dream, Cherry Bomb, We Young, JOY, Timeless, BOSS, Baby
           Don't Stop, GO, TOUCH, New Heroes, Black on Black, We Go Up,
           Regular (English Version), Regular (Korean Version), Simon Says,
           Hair in the Air, Candle Light, Regular, Dream Launch,
           Let's Shut Up & Dance, Wakey-Wakey, Take Off, Superhuman,
           Highway to Heaven (English Version), Boom,Moonwalk, Love Talk,
           Coming Home, Kick it, Ridin', Punch, Turn Back Time,
           Bad Alive (English Version), From Home, Make A Wish, 90s Love,
           Work it, RESONANCE, gimme gimme, Kick Back, Everytime, Hot Sauce,
           Hello Future, Save """




"""
****
CONJUNTOS: SUBDIVISIONES
****
"""

nct_u = ["Johnny", "Taeil", "Taeyong", "Yuta", "Kun", "Doyoung", "Ten",
         "Jaehyun", "Winwin", "Jungwoo", "Lucas", "Mark", "Xiaojun",
         "Hendery", "Renjun", "Jeno", "Haechan", "Jaemin",
         "Yangyang", "Shotaro", "Sungchan", "Chenle", "Jisung"]

nct_dream = ["Mark", "Renjun", "Jeno", "Haechan", "Jaemin", "Chenle",
             "Jisung"]

nct_127 = ["Johnny", "Taeil", "Taeyong", "Yuta", "Doyoung", "Jaehyun",
          "Winwin", "Jungwoo", "Mark", "Haechan"]

wayv = ["Kun", "Ten", "Winwin", "Lucas", "Xiaojun", "Hendery", "Yangyang"]

nct =[nct_u, nct_127, nct_dream, wayv]



"""
****
classes
****

"""
class johnny:
    edad = 26
johnny = johnny()
class taeil:
    edad = 27
taeil = taeil()
class taeyong:
    edad = 26
taeyong = taeyong()
class yuta:
    edad = 26
yuta = yuta()
class kun:
    edad = 25
kun = kun()
class doyoung:
    edad = 25
doyoung = doyoung()
class ten:
    edad = 25
ten = ten()
class jaehyun:
    edad = 24
jaehyun = jaehyun()
class winwin:
    edad = 24
winwin = winwin()
class jungwoo:
    edad =23
jungwoo = jungwoo()
class lucas:
    edad = 22
lucas = lucas()
class mark:
    edad = 22
mark = mark()
class xiaojun:
    edad = 22
xiaojun = xiaojun()
class hendery:
    edad = 22
hendery = hendery()
class renjun:
    edad = 21
renjun = renjun()
class jeno:
    edad = 21
jeno = jeno()
class haechan:
    edad = 21
haechan = haechan()
class jaemin:
    edad = 21
jaemin = jaemin()
class yangyang:
    edad = 21
yangyang = yangyang()
class shotaro:
    edad = 21
shotaro = shotaro()
class sungchan:
    edad = 20
sungchan = sungchan()
class chenle:
    edad = 20
chenle = chenle()
class jisung:
    edad = 19
jisung = jisung()


"""
****
Condiciones
****

"""

inicio_bienvenida()
info_1= ""
while info_1 != "salir":
    info_1 = input("¿Que seccion quieres visitar? (en minusculas) ")

    if info_1 == "subdivisiones":
        seccion_subdivisiones(subdivisiones, nct_u, nct_dream, nct_127, wayv)
                    
    elif info_1 == "miembros":
        seccion_miembros(miembros)
    
    
    elif info_1 == "musica":
       seccion_musica(musica, albums, mini_albums_singles, music_videos)
print("¡Gracias por su busqueda! ^_^")
    


