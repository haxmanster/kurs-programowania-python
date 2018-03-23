print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")
print("||                                                                                                ||")
print("||                            CCC    CC     CCC    CCC   CC   CC                                  ||")
print("||                           CC      CC    C   C  CC     CC CC                                    ||")
print("||                            CCC    CCCCC  CCC    CCC   CC   CC                                  ||")
print("|//////////////////////////////////////////////////////////////////////////////////////////////////|")

print ("Witaj w moim programie do obliczania kata ktory tworza wskazowki zegara na tarczy ")

<<<<<<< HEAD
<<<<<<< HEAD
def limit(godzina,minuta):
  if godzina < 25 and minuta < 60:
      return normalizacja_kata()
  return "Podałes nie własciwy zakres ninut i godzin ! Minuta może mieć maks 60 a godziny mak 24"

=======
>>>>>>> 7248da98491fb78349e26e4cc0ef973d1a614cf5
=======
>>>>>>> 7248da98491fb78349e26e4cc0ef973d1a614cf5

def normalizacja_kata():
  if suma_katow > 0:
    if suma_katow < 0:
      return suma_katow
    return suma_katow
  if suma_katow < -180:
    return suma_katow + 360
  if suma_katow >= 180:
    return suma_katow
  return -suma_katow

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7248da98491fb78349e26e4cc0ef973d1a614cf5
def limit(godzina,minuta):
  if godzina < 25:
    if minuta < 60:
      return normalizacja_kata()
  return "Podałes nie własciwy zakres ninut i godzin ! Minuta może mieć maks 60 a godziny mak 24"


<<<<<<< HEAD
>>>>>>> 7248da98491fb78349e26e4cc0ef973d1a614cf5
=======
>>>>>>> 7248da98491fb78349e26e4cc0ef973d1a614cf5
wybor = "t"
t = str(wybor)
while wybor == "t":
  godzina = float(input("Podaj godzine "))
  minuta = float(input("Podaj minute "))
  stala = float(5.5)
  kat_minuty = stala * minuta
  kat_godziny = (30 * godzina)
  suma_katow = kat_minuty - kat_godziny
  print("Kąt pomiedzy wskazówkami zegara wynosi : ",limit(godzina,minuta))
  wybor = str(input("Jeszcze raz (t/n)? "))
print ("bye")
