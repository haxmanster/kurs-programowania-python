print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")
print("||                                                                                                ||")
print("||                            CCC    CC     CCC    CCC   CC   CC                                  ||")
print("||                           CC      CC    C   C  CC     CC CC                                    ||")
print("||                            CCC    CCCCC  CCC    CCC   CC   CC                                  ||")
print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")

print ("Witaj w moim programie do obliczania kata ktory tworza wskazowki zegara na tarczy ")

wybor = "t"
exit = "n"
t = str('t')
n = str('n')
while wybor == 't':
  godzina = input("Podaj godzine ")
  minuta = input("Podaj minute ")
  godzina = float(godzina)
  minuta = float(minuta)
  stala = float(5.5)
  a = stala * minuta
  b = (30 * godzina)
  c = a - b
  if godzina <= 12 and godzina != 13:
    if minuta <= 60 and minuta != 60:
     if a <= 165 and a >=0 and b <= 180 and b >= 0 and c > 0:
        print(a -b )
     if a <= 180 and a >= 0 and b <= 180 and b >= 0 and c < 0:
        print(c * -1)
     if a >= 170 and a <= 209 and b <= 180 and b >= 0 and c > 0:
         print(b - a)
     #if a >= 210 and a <= 360 and b <= 180 and b >= 0:
      #   print(b - a + 360)
     if a <= 240 and a >= 269 and  b <= 90 and b >= 0:
         print(b - a)
    else:
     print ("Podales zly zakres Minut musisz podac minut od 0 do 59")
  else:
     print ("Podales zly zakres Godzinowy musisz podac godziny od 0 do 11")

wybor = input("Jeszcze raz (t/n)? ")
print ("BYE BYE")