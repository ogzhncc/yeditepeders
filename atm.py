konto=1000 #Bakiye
menu=int(input("Wahlen Sie 1 für Einzahlen, 2 für Auszahlen: "))
if menu==1:
   geld=int(input("Wieviel möchten Sie einzahlen: "))
   konto+=geld
   print("Neuer Kontostand: "+str(konto))
elif menu==2:
  geld=int(input("Wieviel möchten Sie auszahlen: "))
  if geld<=konto:
    konto=geld
    print("Neuer Kontostand "+str(konto))
    else:
    print("Konto nicht ausreichend")
  else:
    print("Ungültige Transaktion")