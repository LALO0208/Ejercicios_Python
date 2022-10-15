year = 2012

if year >= 1582:
    if year % 4 ==0:
        if year % 4 == 0 and (year % 100 or year % 400 == 0):
            print("el año {} es biciesto".format(year))
        else: 
            print("el año {} no es biciesto".format(year))
    else: 
        print("el año {} no es biciesto".format(year))
else:
    if year % 4 ==0     :
        print("el año {} es biciesto".format(year))
    else:
        print("el año {} no es biciesto".format(year))



