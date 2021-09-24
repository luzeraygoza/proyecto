"""
********

Programa de NCT 

********
"""


"""
****
Funciones (AQUI ESTAN LAS OPERACIONES ;) )
****

"""    
def Suma1994_1995(Jy, Tl, Ty, Yt, K, Dy, T):
    return Jy + Tl + Ty + Yt + K + Dy + T

def Suma1997_1999(Jh, W, Jw, L, M, Xj, Hd):
    return Jh + W + Jw + L + M + Xj + Hd

def Suma2000_2002(Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js):
    return Rj + J + Hc + Jm + Yy + St + Sc + Cl + Js

def Promedio_Edad(Jy, Tl, Ty, Yt, K, Dy, T, Jh, W, Jw, L, M, Xj, Hd, Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js):
    SumaTotal = Suma1994_1995(Jy, Tl, Ty, Yt, K, Dy, T) + Suma1997_1999(Jh, W, Jw, L, M, Xj, Hd) + Suma2000_2002(Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js)
    return (SumaTotal/23)

def Promedio_NCT127(Jy, Tl, Ty, Yt, Dy, Jh, W, Jw, M, Hc):
    return (Jy + Tl + Ty + Yt + Dy + Jh + W + Jw + M + Hc)/10

def Promedio_NCTDREAM(M, Rj, J, Hc, Jm, Cl, Js):
    return (M + Rj + J + Hc + Jm + Cl + Js)/7

def Promedio_WAYV (K, T, W, L, Xj, Hd, Yy):
    return (K + T + W + L + Xj + Hd + Yy)/7

def Inicio_Bienvenida():
    

    print("Buenas tardes usuario, para consultar nuestra información cheque el catalogo")
    print(
        """
        Subdivisiones:
        
        Miembros:
        
        Musica:
           
           """)
          
         



"""
*****                     *****


VARIABLES PARA EL INICIO


*****                     *****
"""


Subdivisiones = """
NCT U, NCT DREAM, NCT 127 y WayV
"""
Miembros = """
Johnny, Taeil, Taeyong, Yuta, Kun, Doyoung, Ten, Jaehyun, WinWin, Jungwoo, Lucas,
Mark, Xiaojun, Hendery, Renjun, Jeno, Haechan, Jaemin, YangYang, Shotaro, Sungchan, Chenle & Jisung
        """
Musica = """
Albums, Mini Albums y Singles, Music Videos
"""

"""
****
CONJUNTOS: SUBDIVISIONES
****
"""

NCTU = {"Johnny", "Taeil", "Taeyong", "Yuta", "Kun", "Doyoung", "Ten", "Jaehyun", "Winwin", "Jungwoo", "Lucas", "Mark", "Xiaojun", "Hendery", "Renjun", "Jeno", "Haechan", "Jaemin", "Yangyang", "Shotaro", "Sungchan", "Chenle", "Jisung"}
NCTDREAM = {"Mark", "Renjun", "Jeno", "Haechan", "Jaemin", "Chenle", "Jisung"}
NCT127 = {"Johnny", "Taeil", "Taeyong", "Yuta", "Doyoung", "Jaehyun", "Winwin", "Jungwoo", "Mark", "Haechan"}
WAYV = {"Kun", "Ten", "Winwin", "Lucas", "Xiaojun", "Hendery", "Yangyang"}




"""
****
classes
****

"""
class Johnny:
    edad = 26
johnny = Johnny()
class Taeil:
    edad = 27
taeil = Taeil()
class Taeyong:
    edad = 26
taeyong = Taeyong()
class Yuta:
    edad = 26
yuta = Yuta()
class Kun:
    edad = 25
kun = Kun()
class Doyoung:
    edad = 25
doyoung = Doyoung()
class Ten:
    edad = 25
ten = Ten()
class Jaehyun:
    edad = 24
jaehyun = Jaehyun()
class Winwin:
    edad = 24
winwin = Winwin()
class Jungwoo:
    edad =23
jungwoo = Jungwoo()
class Lucas:
    edad = 22
lucas = Lucas()
class Mark:
    edad = 22
mark = Mark()
class Xiaojun:
    edad = 22
xiaojun = Xiaojun()
class Hendery:
    edad = 22
hendery = Hendery()
class Renjun:
    edad = 21
renjun = Renjun()
class Jeno:
    edad = 21
jeno = Jeno()
class Haechan:
    edad = 21
haechan = Haechan()
class Jaemin:
    edad = 21
jaemin = Jaemin()
class Yangyang:
    edad = 21
yangyang = Yangyang()
class Shotaro:
    edad = 21
shotaro = Shotaro()
class Sungchan:
    edad = 20
sungchan = Sungchan()
class Chenle:
    edad = 20
chenle = Chenle()
class Jisung:
    edad = 19
jisung = Jisung()


"""
****
Condiciones
****

"""

Inicio_Bienvenida()

info_1 = input("¿Que seccion quieres visitar? (en minusculas) ")

if info_1 == "subdivisiones":
    bandera = True
    while bandera:
        print(Subdivisiones)
        info_2 = input("¿Quieres saber que miembros estan en cierta subdivision? (escribe el nombre de la subdivision en mayusculas) si no quieres saber pon NO ")
    
        if info_2 == "NCT U":
            print(NCTU)
        elif info_2 == "NCT DREAM":
            print(NCTDREAM)
        elif info_2 == "NCT 127":
            print(NCT127)
        elif info_2 == "WAYV":
            print(WAYV)
        
        else:
            while bandera:
       
                info_3 = input("¿Quieres saber que miembro esta en que subdivision? (escribe SI o NO) ")
                
                
                if info_3 == "SI":
                    print(Miembros)
                    info_5 = input("Escribe el nombre del miembro a saber (Mayuscula al principio) ")
                    if info_3 in NCTU:
                        print("Si esta en NCT U el miembro " + info_3)
                    if info_3 not in NCTU:
                        print("No esta en NCT U el miembro " + info_3)
                    if info_3 in NCTDREAM:
                        print("Si esta en NCT DREAM el miembro " + info_3)
                    if info_3 not in NCTDREAM:
                        print("No esta en NCT DREAM el miembro " + info_3)
                    if info_3 in NCT127:
                        print("Si esta en NCT 127 el miembro " + info_3)
                    if info_3 not in NCT127:
                        print("No esta en NCT 127 el miembro " + info_3)
                    if info_3 in WAYV:
                        print("Si esta en WAYV el miembro " + info_3)
                    if info_3 not in WAYV: 
                        print("No esta en WAYV el miembro " + info_3) 
                else:
                    while info_3 == "NO":
                        bandera = False
                        break
                    print("¡Gracias por su busqueda! ^_^") 
                    
elif info_1 == "miembros": 
    
    print(Miembros)
   
    Promedio_Pregunta = input("¿Quieres saber el promedio de edad de NCT? (SI o NO) ")
    if Promedio_Pregunta == "SI":
        print("Promedio de todo NCT: ", Promedio_Edad(johnny.edad, taeil.edad, taeyong.edad, yuta.edad, kun.edad, doyoung.edad, ten.edad, jaehyun.edad, winwin.edad, jungwoo.edad, lucas.edad, mark.edad, xiaojun.edad, hendery.edad,renjun.edad, jaemin.edad, haechan.edad, jaemin.edad, yangyang.edad, shotaro.edad, sungchan.edad, chenle.edad,jisung.edad ))
        print("Promedio de NCT 127: ", Promedio_NCT127(johnny.edad, taeil.edad, taeyong.edad, yuta.edad, doyoung.edad, jaehyun.edad, winwin.edad, jungwoo.edad, mark.edad, haechan.edad ))
        print("Promedio de NCT DREAM: ", Promedio_NCTDREAM(mark.edad, renjun.edad, jeno.edad, haechan.edad, jaemin.edad, chenle.edad, jisung.edad))
        print("Promedio de WAYV", Promedio_WAYV(kun.edad, ten.edad, winwin.edad, lucas.edad, xiaojun.edad, hendery.edad, yangyang.edad))
        print("¡Gracias por su busqueda! ^_^")
    else:
        print("¡Gracias por su busqueda! ^_^")
else:
    print(Musica)
    
    while True:
        info_4 = input("¿Que sub-categoria quieres desplegar? albums, mini albums & singles, music videos (escribir todo en minuscula, para terminar escribir NO) ")
        if info_4 == "albums":
            print( """
        NCT 2018 EMPATHY, NCT#127 REGULAR-IRREGULAR, NCT#127 REGULATE (REPACKAGE), Awaken, NEO CITY: SEOUL, THE DREAM SHOW,
           NCT#127 Neo Zone, NCT#127 Neo Zone: The Final Round (REPACKAGE),Awaken The World, NCT RESONANCE Pt.2,
           Hot Sauce & Hello Future (REPACKAGE)
           """)
        elif info_4 == "mini albums & singles":
            print("""
        The 7th sense, WITHOUT YOU, NCT#127, Chewing Gum, NCT#127 LIMITLESS, The First, NCT#127 CHERRY BOMB, Trigger the fever,
           JOY, Timeless,Radio Romance, Chain, Baby Don't Stop (Thai Version), We Go Up, Touch (Japanes Version), Up Next Session: NCT 127,
           DreamWorks Trolls X SM STATION, Candle Light, Let's Shut UP&DANCE, Don't need your love, So am I, Fireflies, The Vision,
           Take Off, NCT#127 WE ARE SUPERHUMAN, Highway to heaven (English version), We boom, When You're on the Blacklist of the Bullies,
           The tale of Nodku, Take Over the Moon, Love Talk (English Version), STATION X LOVEs for Winter, Reload,
           iScreaM Vol.1: Kick It (REMIX), iScreaM Vol.2: Ridin' (REMIXES), Turn Back Time, Bad Alive (English Version), RESONANCE,
           iScreaM Vol.6: Make a Wish/ 90's Love Remix, Kick Back, Save, iScreaM Vol9: Hot Sauce Remixes, Maniac
""")
 
        elif info_4 == "music videos":
            print(""" YESTODAY, The 7th Sense, WITHOUT YOU, Fire Truck, Chewing Gum, Switch, Limitless, My First and Last, Dream in a Dream,
           Cherry Bomb, We Young, JOY, Timeless, BOSS, Baby Don't Stop, GO, TOUCH, New Heroes, Black on Black, We Go Up, 
           Regular (English Version), Regular (Korean Version), Simon Says, Hair in the Air, Candle Light, Regular, Dream Launch,
           Let's Shut Up & Dance, Wakey-Wakey, Take Off, Superhuman, Highway to Heaven (English Version), Boom,
           Moonwalk, Love Talk, Coming Home, Kick it, Ridin', Punch, Turn Back Time, Bad Alive (English Version), From Home,
           Make A Wish, 90s Love, Work it, RESONANCE, gimme gimme, Kick Back, Everytime, Hot Sauce, Hello Future, Save """)
       
        else:
            while info_4 == "NO":
                pregunta = str(input("¿Quieres volver a explorar esta sección? (MAYUSCULAS) "))
                if pregunta in ("SI", "NO"):
                    break
                print("invalido intenta otra vez con SI y NO")
            if pregunta == "SI":
                continue     
            else:
                print("¡Gracias por su busqueda! ^_^")
                break


