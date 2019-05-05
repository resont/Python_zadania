from rectangle import Rectangle,Cuboid,InvalidData

if __name__ == "__main__":
    f = open("dane.txt","r")

    for line in f:
        fields = line.split(" ")
        try:
            a,b = fields[1],fields[2]
            if fields[0] == '1':
                rec = Rectangle(a,b)
                print(rec)
            if fields[0] == '2':
                c = fields[3]
                cub = Cuboid(a,b,c)
                print(cub)
        except InvalidData as e:
            print(e)
        except IndexError as e:
            print("Niepoprawna ilość boków!")

    f.close()