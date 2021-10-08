"""
********

Programa de NCT  (preguntar sobre mayusculas en NCT Y CARACTERES CUANDO SE IMPRIMEN LOS MIMBROS Y TODO ESO y de los estatutos (que son))

********
"""


"""
****
Funciones  
****

"""    
def suma_1994_1995(Jy, Tl, Ty, Yt, K, Dy, T):
    """ Suma las edades de los miembros entre los años de 1994 y 1995"""
    return Jy + Tl + Ty + Yt + K + Dy + T

def suma_1997_1999(Jh, W, Jw, L, M, Xj, Hd):
    """ Suma las edades de los miembros entre los años de 1997 y 1999"""
    return Jh + W + Jw + L + M + Xj + Hd

def suma_2000_2002(Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js):
    """ Suma las edades de los miembros entre los años de 2000 y 2002"""
    return Rj + J + Hc + Jm + Yy + St + Sc + Cl + Js

def promedio_edad(Jy, Tl, Ty, Yt, K, Dy, T, Jh, W, Jw, L, M, Xj, Hd, Rj,
                  J, Hc, Jm, Yy, St, Sc, Cl, Js):
    """Saca el promedio de edades de los 23 miembros"""
    suma_total = (suma_1994_1995(Jy, Tl, Ty, Yt, K, Dy, T)
                  + suma_1997_1999(Jh, W, Jw, L, M, Xj, Hd) +
                  suma_2000_2002(Rj, J, Hc, Jm, Yy, St, Sc, Cl, Js))
    
    return (suma_total/23)

def promedio_nct_127(Jy, Tl, Ty, Yt, Dy, Jh, W, Jw, M, Hc):
    return (Jy + Tl + Ty + Yt + Dy + Jh + W + Jw + M + Hc)/10

def promedio_nct_dream(M, Rj, J, Hc, Jm, Cl, Js):
    return (M + Rj + J + Hc + Jm + Cl + Js)/7

def promedio_wayv (K, T, W, L, Xj, Hd, Yy):
    return (K + T + W + L + Xj + Hd + Yy)/7

def inicio_bienvenida():
    

    print("Buenas tardes usuario")
    print("para consultar nuestra información cheque el catalogo")
    
    print(
        """
        Subdivisiones:
        
        Miembros:
        
        Musica:
           
           """)
def nct_visual_estetico(i):
    if i == 0:
        return "NCT U: "
    elif i == 1:
        return "NCT 127: "
    elif i == 2:
        return "NCT DREAM: "
    elif i == 3:
        return "WAYV: "
def nct_visual(grupo):
    i = 0 
    for subdivision in grupo:
        print(nct_visual_estetico(i))
        print(subdivision)
        i= 1 + i
         



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
        NCT 2018 EMPATHY, NCT#127 REGULAR-IRREGULAR, NCT#127 REGULATE (REPACKAGE), Awaken, NEO CITY: SEOUL, THE DREAM SHOW,
           NCT#127 Neo Zone, NCT#127 Neo Zone: The Final Round (REPACKAGE),Awaken The World, NCT RESONANCE Pt.2,
           Hot Sauce & Hello Future (REPACKAGE)
           """
mini_albums_singles = """
        The 7th sense, WITHOUT YOU, NCT#127, Chewing Gum, NCT#127 LIMITLESS, The First, NCT#127 CHERRY BOMB, Trigger the fever,
           JOY, Timeless,Radio Romance, Chain, Baby Don't Stop (Thai Version), We Go Up, Touch (Japanes Version), Up Next Session: NCT 127,
           DreamWorks Trolls X SM STATION, Candle Light, Let's Shut UP&DANCE, Don't need your love, So am I, Fireflies, The Vision,
           Take Off, NCT#127 WE ARE SUPERHUMAN, Highway to heaven (English version), We boom, When You're on the Blacklist of the Bullies,
           The tale of Nodku, Take Over the Moon, Love Talk (English Version), STATION X LOVEs for Winter, Reload,
           iScreaM Vol.1: Kick It (REMIX), iScreaM Vol.2: Ridin' (REMIXES), Turn Back Time, Bad Alive (English Version), RESONANCE,
           iScreaM Vol.6: Make a Wish/ 90's Love Remix, Kick Back, Save, iScreaM Vol9: Hot Sauce Remixes, Maniac
"""

music_videos = """ YESTODAY, The 7th Sense, WITHOUT YOU, Fire Truck, Chewing Gum, Switch, Limitless, My First and Last, Dream in a Dream,
           Cherry Bomb, We Young, JOY, Timeless, BOSS, Baby Don't Stop, GO, TOUCH, New Heroes, Black on Black, We Go Up, 
           Regular (English Version), Regular (Korean Version), Simon Says, Hair in the Air, Candle Light, Regular, Dream Launch,
           Let's Shut Up & Dance, Wakey-Wakey, Take Off, Superhuman, Highway to Heaven (English Version), Boom,
           Moonwalk, Love Talk, Coming Home, Kick it, Ridin', Punch, Turn Back Time, Bad Alive (English Version), From Home,
           Make A Wish, 90s Love, Work it, RESONANCE, gimme gimme, Kick Back, Everytime, Hot Sauce, Hello Future, Save """

"""
****
CONJUNTOS: SUBDIVISIONES
****
"""

nct_u = ["Johnny", "Taeil", "Taeyong", "Yuta", "Kun", "Doyoung", "Ten",
         "Jaehyun", "Winwin", "Jungwoo", "Lucas", "Mark", "Xiaojun",
         "Hendery", "Renjun", "Jeno", "Haechan", "Jaemin",
         "Yangyang", "Shotaro", "Sungchan", "Chenle", "Jisung"]

nct_dream = ["Mark", "Renjun", "Jeno", "Haechan", "Jaemin", "Chenle", "Jisung"]

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

info_1 = input("¿Que seccion quieres visitar? (en minusculas) ")

if info_1 == "subdivisiones":
    bandera = True
    while bandera:
        print(subdivisiones)
        info_2 = input("¿Quieres saber que miembros estan en que subdivision? si no quieres saber pon no ")
    
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
       
                info_3 = input("¿Quieres saber que miembro esta en que subdivision? (escribe si o no) ")
                
                
                if info_3 == "si":
                    print(miembros)
                    info_5 = input("Escribe el nombre del miembro a saber (Mayuscula al principio) ")
                    if info_5 in nct_u:
                        print("Si esta en NCT U el miembro " + info_5)
                    if info_5 not in nct_u:
                        print("No esta en NCT U el miembro " + info_5)
                    if info_5 in nct_dream:
                        print("Si esta en NCT DREAM el miembro " + info_5)
                    if info_5 not in nct_dream:
                        print("No esta en NCT DREAM el miembro " + info_5)
                    if info_5 in nct_127:
                        print("Si esta en NCT 127 el miembro " + info_5)
                    if info_5 not in nct_127:
                        print("No esta en NCT 127 el miembro " + info_5)
                    if info_5 in wayv:
                        print("Si esta en WAYV el miembro " + info_5)
                    if info_5 not in wayv: 
                        print("No esta en WAYV el miembro " + info_5) 
                else:
                    info_6 = input("¿Quieres una representación de NCT? (escribe si o no) ")
                    if info_6 == "si":
                        print(nct_visual(nct))
                        bandera= False
                    else:
                        while info_6 == "no":
                            bandera = False
                            break
                        print("¡Gracias por su busqueda! ^_^") 
                    
elif info_1 == "miembros": 
    
    print(miembros)
   
    promedio_pregunta = input("¿Quieres saber el promedio de edad de NCT? (si o no) ")
    if promedio_pregunta == "si":
        print("Promedio de todo NCT: ", promedio_edad(johnny.edad, taeil.edad, taeyong.edad, yuta.edad, kun.edad, doyoung.edad, ten.edad, jaehyun.edad, winwin.edad, jungwoo.edad, lucas.edad, mark.edad, xiaojun.edad, hendery.edad,renjun.edad, jaemin.edad, haechan.edad, jaemin.edad, yangyang.edad, shotaro.edad, sungchan.edad, chenle.edad,jisung.edad ))
        print("Promedio de NCT 127: ", promedio_nct_127(johnny.edad, taeil.edad, taeyong.edad, yuta.edad, doyoung.edad, jaehyun.edad, winwin.edad, jungwoo.edad, mark.edad, haechan.edad ))
        print("Promedio de NCT DREAM: ", promedio_nct_dream(mark.edad, renjun.edad, jeno.edad, haechan.edad, jaemin.edad, chenle.edad, jisung.edad))
        print("Promedio de WAYV", promedio_wayv(kun.edad, ten.edad, winwin.edad, lucas.edad, xiaojun.edad, hendery.edad, yangyang.edad))
        print("¡Gracias por su busqueda! ^_^")
    else:
        print("¡Gracias por su busqueda! ^_^")
else:
    print(musica)
    
    while True:
        info_4 = input("¿Que sub-categoria quieres desplegar? albums, mini albums & singles, music videos (para terminar escribir no) ")
        if info_4 == "albums":
            print(albums)
        elif info_4 == "mini albums & singles":
            print(mini_albums_singles)
 
        elif info_4 == "music videos":
            print(music_videos)
       
        else:
            while info_4 == "no":
                pregunta = str(input("¿Quieres volver a explorar esta sección? "))
                if pregunta in ("si", "no"):
                    break
                print("invalido intenta otra vez con si y no")
            if pregunta == "si":
                continue     
            else:
                print("¡Gracias por su busqueda! ^_^")
                break


