temperatura= int(input("temperatura del agua"))



if (temperatura<0):
    print("hielo")
elif(temperatura>100):
    print("vapor")
else:
    print("liquido")