my=require("myapps")

--joystick,x,520  joystick,y,522  joystick,bp,1  temperature,0  ultrason,52  son,219  lumiere,745

val = my.capteurs()
print("joystick,x : "..val[1])
print("joystick,y : "..val[2])
print("joystick,bp :"..val[3])
print("temperature : "..val[4])
print("ultrason : "..val[5])
print("son : "..val[6])
print("lumiere : "..val[7])


