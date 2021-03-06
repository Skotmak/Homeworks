from vpython import sphere, vector, color, rotate, canvas
import math

G = 6.667e-11 

MS = 1.9885e30 
ME = 5.97e24 
MM = 7.348e22 
MMercury = 3.33e23 
MVenus = 4.87e24 
MMars = 6.42e23 
MJupiter = 1.89e27 
MSaturn = 5.68e26 
MUran = 8.68e25 

REM = 384.4e6  
RSE = 1.496e11 
RMercury = 0.58e11
RVenus = 1.08e11
RMars = 2.28e11 
RJupiter = 7.78e11 
RSaturn = 14.30e11 
RUran = 19.19e11 

F_EM = G*ME*MM/(REM*REM)
F_SE = G*MS*ME/(RSE*RSE) 
F_MERCURY = G*MS*MMercury/(RMercury*RMercury)
F_VENUS = G*MS*MVenus/(RVenus*RVenus) 
F_MARS = G*MS*MMars/(RMars*RMars) 
F_JUPITER = G*MS*MJupiter/(RJupiter*RJupiter)
F_SATURN = G*MS*MSaturn/(RSaturn*RSaturn) 
F_URAN = G*MS*MUran/(RUran*RUran) 

wm = math.sqrt(F_EM/(MM*REM))
we = math.sqrt(F_SE/(ME*RSE))
wMercury = math.sqrt(F_MERCURY/(MMercury*RMercury))
wVenus = math.sqrt(F_VENUS/(MVenus*RVenus))
wMars = math.sqrt(F_MARS/(MMars*RMars))
wJupiter = math.sqrt(F_JUPITER/(MJupiter*RJupiter))
wSaturn = math.sqrt(F_SATURN/(MSaturn*RSaturn))
wUran = math.sqrt(F_URAN/(MUran*RUran))

c2 = canvas(title='Solar system model', width=1300, height=900,)

v = vector(0.5, 0, 0)
Sun = sphere(canvas=c2, pos=vector(0, 0, 0),  radius=5, color=color.yellow)
Mercury = sphere(canvas=c2, pos=vector(7.5, 0, 0),  radius=0.024, color=color.red)
Venus = sphere(canvas=c2, pos=vector(8, 0, 0),  radius=0.060, color=color.blue)
Earth = sphere(canvas=c2, pos=vector(9, 0, 0),  radius=0.063, color=color.green)
Moon = sphere(canvas=c2, pos=Earth.pos+v, radius=0.017, color=color.white)
Mars = sphere(canvas=c2, pos=vector(9.3, 0, 0),  radius=0.033,color=color.red)
Jupiter = sphere(canvas=c2, pos=vector(15.3, 0, 0), radius=0.699,color=color.yellow)
Saturn = sphere(canvas=c2, pos=vector(21.8, 0, 0), radius=0.582, color=color.gray)
Uran = sphere(canvas=c2, pos=vector(26.7, 0, 0),  radius=0.253,color=color.blue)

# Используем полярные координаты
# Шаг , от него зависит скорость полёта планет
dt = 100
# углы поворота за один шаг:
theta_earth = we*dt
theta_moon = wm*dt
theta_mercury = wMercury*dt
theta_venus = wVenus*dt
theta_mars = wMars*dt
theta_jupiter = wJupiter*dt
theta_saturn = wSaturn*dt
theta_uran = wUran*dt
while dt <= 86400*365:
    # Планеты поворачиваются вокруг оси z (0,0,1)
    Earth.pos = rotate(Earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
    Mercury.pos = rotate(Mercury.pos, angle=theta_mercury, axis=vector(0, 0, 1))
    Venus.pos = rotate(Venus.pos, angle=theta_venus, axis=vector(0, 0, 1))
    Mars.pos = rotate(Mars.pos, angle=theta_mars, axis=vector(0, 0, 1))
    Jupiter.pos = rotate(Jupiter.pos, angle=theta_jupiter, axis=vector(0, 0, 1))
    Saturn.pos = rotate(Saturn.pos, angle=theta_saturn, axis=vector(0, 0, 1))
    Uran.pos = rotate(Uran.pos, angle=theta_uran, axis=vector(0, 0, 1))
    v = rotate(v, angle=theta_moon, axis=vector(0, 0, 1))
    Moon.pos = Earth.pos + v
    dt += 10