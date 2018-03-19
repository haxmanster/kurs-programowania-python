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
  c = a - b
  def WartoscBezwgledna(godzina,minuta):
    if a - b < 0:
      return -c
    if a - b >= 180:
      return 360 -c
    else:
      return c
  print("Kąt pomiedzy wskazówkami zegara wynosi : ", WartoscBezwgledna(godzina,minuta))
  wybor = str(input("Jeszcze raz (t/n)? "))
print ("bye")


