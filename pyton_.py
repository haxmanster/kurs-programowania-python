print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")
print("||                                                                                                ||")
print("||                            CCC    CC     CCC    CCC   CC   CC                                  ||")
print("||                           CC      CC    C   C  CC     CC CC                                    ||")
print("||                            CCC    CCCCC  CCC    CCC   CC   CC                                  ||")
print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")

print ("Witaj w moim programie do obliczania kata ktory tworza wskazowki zegara na tarczy ")

wybor = "t"
t = str(wybor)
while wybor == "t":
    godzina = float(input("Podaj godzine "))
    minuta = float(input("Podaj minute "))
    stala = float(5.5)
    a = stala * minuta
    b = (30 * godzina)
    c = b - a
    if godzina <= 12 and godzina != 13:
        if minuta <= 60 and minuta != 60:
#--Dla godziny 1:00 do 1:59
           if godzina == 1 and minuta >= 0  and  c >= 0:
               print((a - b) * -1)
           if godzina == 1 and minuta <= 39 and c <= 0:
               print(a - b)
           if godzina == 1 and minuta >= 40 and minuta <= 60 and  c <= 0:
               print(360 + c)
#--Dla godziny 2:00 do 2:59
           if godzina == 2 and minuta >= 0  and  c >= 0:
               print((a - b) * -1)
           if godzina == 2 and minuta <= 44 and c <= 0:
               print(a -b)
           if godzina == 2 and minuta >= 45 and minuta <= 60 and  c <= 0:
               print(c + 360)
# --Dla godziny 3:00 do 2:59
           if godzina == 3 and minuta >= 0 and c >= 0:
               print((a - b) * -1)
           if godzina == 3 and minuta <= 50 and c <= 0:
               print(a - b)
           if godzina == 3 and minuta >= 51 and minuta <= 60 and c <= 0:
               print(c + 360)
# --Dla godziny 4:00 do 4:59
           if godzina == 4 and minuta >= 0 and c >= 0:
               print((a - b) * -1)
           if godzina == 4 and minuta <= 55 and c <= 0:
               print(a - b)
           if godzina == 4 and minuta >= 56 and minuta <= 60 and c <= 0:
               print(c + 360)
# --Dla godziny 5:00 do 4:59
           if godzina == 5 and minuta >= 0 and c >= 0:
               print((a - b) * -1)
           if godzina == 5 and minuta <= 59 and c <= 0:
               print(a - b)
# --Dla godziny 6:00 do 6:59 --
           if godzina == 6 and minuta >= 0 and c >= 0:
               print((a - b) * -1)
           if godzina == 6 and minuta <= 59 and c <= 0:
               print(a - b)
# --Dla godziny 7:00 do 7:59 --
           if godzina == 7 and minuta <= 5  and c >= 0:
               print((c - 360)* -1)
           if godzina == 7 and minuta >= 6 and c >= 0:
               print((a - b) * -1)
           if godzina == 7 and minuta >= 39 and c <= 0:
               print(a - b)
# --Dla godziny 8:00 do 8:59 --
           if godzina == 8 and minuta <= 9 and c >= 0:
               print((c - 360) * -1)
           if godzina == 8 and minuta >= 10 and c >= 0:
               print(b - a)
           if godzina == 8 and minuta >= 44 and c <= 0:
               print(a -b)
# --Dla godziny 9:00 do 9:59 --
           if godzina == 9 and minuta <= 17 and c >= 0:
               print(360 - c)
           if godzina == 9 and minuta >= 18 and c >= 0:
               print(b - a)
           if godzina == 9 and minuta >= 49 and c <= 0:
               print(a - b)
# --Dla godziny 10:00 do 10:59 --
           if godzina == 10 and minuta <= 22 and c >= 0:
               print((a - b + 360))
           if godzina == 10 and minuta >= 23 and c >= 0:
               print(b - a)
           if godzina == 10 and minuta >= 55 and c <= 0:
               print(a - b)
# --Dla godziny 11:00 do 11:59 --
           if godzina == 11 and minuta <= 27 and c >= 0:
               print((a - b + 360))
           if godzina == 11 and minuta >= 28 and c >= 0:
               print(b - a)
# --Dla godziny 12:00 do 12:59 --
           if godzina == 12 and minuta <= 33 and c >= 0:
               print((a - b + 360))
           if godzina == 12 and minuta >= 34 and c >= 0:
               print(b - a)
        else:
            print ("Podales zly zakres Minut musisz podac minut od 0 do 59")
    else:
     print ("Podales zly zakres Godzinowy musisz podac godziny od 0 do 11")
    wybor = str(input("Jeszcze raz (t/n)? "))
print ("BYE BYE")