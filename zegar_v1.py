print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")
print("||                                                                                                ||")
print("||                            CCC    CC     CCC    CCC   CC   CC                                  ||")
print("||                           CC      CC    C   C  CC     CC CC                                    ||")
print("||                            CCC    CCCCC  CCC    CCC   CC   CC                                  ||")
print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")

print ("Witaj w moim programie do obliczania kata ktory tworza wskazowki zegara na tarczy ")


def normalizacja_kata(godzina, minuta):
  if suma_katow > 0:
    if suma_katow:
      return suma_katow
    return suma_katow
  if suma_katow < -180:
    return suma_katow + 360
  if suma_katow >= 180:
    return suma_katow
  return -suma_katow

wybor = "t"
t = str(wybor)
while wybor == "t":
  godzina = float(input("Podaj godzine "))
  minuta = float(input("Podaj minute "))
  stala = float(5.5)
  kat_minuty = stala * minuta
  kat_godziny = (30 * godzina)
  suma_katow = kat_minuty - kat_godziny


  print("Kąt pomiedzy wskazówkami zegara wynosi : ", normalizacja_kata(godzina,minuta))
  wybor = str(input("Jeszcze raz (t/n)? "))
print ("bye")
