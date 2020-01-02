from vpython import sphere, vector, color, rotate
import math

# Константы
G = 6.667e-11  # гравитационная постоянная, м^3 кг^-1 с^-2

MS = 1.9885e30  # масса Солнца, кг
ME = 5.97e24  # масса Земли, кг
MM = 7.348e22  # масса Луны, кг
MMercury = 3.33e23 # масса Меркурия, кг
MVenus = 4.87e24 # масса Венеры, кг
MMars = 6.42e23 # масса Марса, кг
MJupiter = 1.89e27 # масса Юпитера, кг
MSaturn = 5.68e26 # масса Сатурна, кг
MUran = 8.68e25 # масса Урана, кг

REM = 384.4e6  # расстояние от Земли до Луны
RSE = 1.496e11 # среднее расстояние от Солнца до Земли, метры
RSMercury = 0.58e11 # среднее расстояние от Солнца до Меркурия, метры
RSVenus = 1.08e11 # среднее расстояние от Солнца до Венеры, метры
RSMars = 2.28e11 # среднее расстояние от Солнца до Марса, метры
RSJupiter = 7.78e11 # среднее расстояние от Солнца до Юпитера, метры
RSSaturn = 14.30e11 # среднее расстояние от Солнца до Сатурна, метры
RSUran = 19.19e11 # среднее расстояние от Солнца до Урана, метры

F_SE = G*MS*ME/(RSE*RSE) # Гравитационная сила между Солнцем и Землей. Н
F_EM = G*ME*MM/(REM*REM) # Гравитационная сила между Землей и Луной, Н

wm = math.sqrt(F_EM/(MM*REM))# Угловая скорость Луны
we = math.sqrt(F_SE/(ME*RSE))# Угловая скорость Земли

v = vector(0.5, 0, 0)
Sun = sphere(pos=vector(0, 0, 0), texture='texture_sun.jpg', radius=1)
Mercury = sphere(pos=vector(1.5, 0, 0), texture='texture_sun.jpg', radius=1)
Venus = sphere(pos=vector(2.5, 0, 0), texture='texture_sun.jpg', radius=1)
Earth = sphere(pos=vector(3.5, 0, 0), radius=.25, make_trail=True, texture='earth_texture.jpg')
Moon = sphere(pos=Earth.pos+v, texture='texture_moon.jpg', radius=0.08, make_trail=False)
Mars = sphere(pos=vector(4.5, 0, 0), texture='texture_sun.jpg', radius=1)
Jupiter = sphere(pos=vector(5.5, 0, 0), texture='texture_sun.jpg', radius=1)
Saturn = sphere(pos=vector(6.5, 0, 0), texture='texture_sun.jpg', radius=1)
Uran = sphere(pos=vector(7.5, 0, 0), texture='texture_sun.jpg', radius=1)
 
# Будем использовать полярные координаты
# Шаг
dt = 100
# углы поворота за один шаг:
theta_earth = we*dt
theta_moon = wm*dt
theta_mercury = wm*dt
theta_venus = wm*dt
theta_mars = wm*dt
theta_jupiter = wm*dt
theta_saturn = wm*dt
theta_uran = wm*dt
while dt <= 86400*365:
    # Земля и Луна поворачиваются вокруг оси z (0,0,1)
    Earth.pos = rotate(Earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
    v = rotate(v, angle=theta_moon, axis=vector(0, 0, 1))
    Moon.pos = Earth.pos + v
    dt += 10