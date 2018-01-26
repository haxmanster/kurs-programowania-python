def wprowadzaj():
    email = raw_input("Podaj adres: ")
    if "@" in email:
        print "Twoj e-mail to: " + email
    else:
        print "Zly adres!"
        wprowadzaj()

