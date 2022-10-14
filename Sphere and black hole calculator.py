from math import *

object = input("Object: ")
omass = float(input(object + "'s mass in kg: "))
onumber = float(input(object + "/s number: "))
oheight = float(input(object + "'s max height in meters: "))
olenght = float(input(object + "'s max length in meters: "))
owidth = float(input(object + "'s max width in meters: "))

allmass = float(omass * onumber)
cside = float((oheight + olenght + owidth) / 3)

volume = float(pow(cside, 3) * onumber)

radius = float((3 * volume / 4 * pi) ** (1 / 3))
area_surface = float(4 * pi * pow(radius, 2))
blackhole = float(((2 * 6.67e-11) * allmass) / pow(3e8, 2))


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


tvolume = truncate(volume, 4)
tarea_surface = truncate(area_surface, 4)
tradius = truncate(radius, 4)

if onumber >= 2:
    print("Sphere made of " + str(onumber) + " " + object + "s would have volume of " + str(tvolume) +
          "m^3, surface area of " + str(tarea_surface) + "m^2 and radius of " + str(tradius) + "m.")

elif onumber <= 2:
    print("Sphere made of " + str(onumber) + " " + object + " would have volume of " + str(tvolume) +
          "m^3, surface area of " + str(tarea_surface) + "m^2 and radius of " + str(tradius) + "m.")

print("It'd weight " + str(allmass) + " kg.")
print("Black hole made from that sphere would have a radius of " + str(blackhole) + "m.")

# there is a possibility it's all wrong but oh well
