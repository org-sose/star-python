volume_dicket = 1.44 * 1024 * 1024
page = 100
line = 50
symbol = 25
inf_symbol = 4
volume_book = page * line * symbol * inf_symbol
num_book = volume_dicket // volume_book
print(num_book)

#Задача 2
storona = 5
radius = 5
pi = 3.1415
s_krug = pi * radius ** 2
dlina_okr = 2 * pi * radius
P_kvadrat = 4 * storona
S_kvadrat = storona ** 2
print(round(S_kvadrat, 2))
print(S_kvadrat, )
print(round(dlina_okr, 2))
print(P_kvadrat)

#Задача 3
a = '0'
b = '1'
c = '2'
str_number = (a * 20) + (b * 50) + (c * 30)
print(str_number)

#Задача 4
speed = 4096
time = 120
coast = 0.125
free = 500
speed_in_kd_sec = speed / 1024
time_in_sec = time * 60
file = spee_in_kd_sec * time_in_sec
money = (file-free) * coast
print(file)
print(money)

#Задача 5
length = 90
width = 50
perimeter = (length + width) * 2
print(perimeter)
