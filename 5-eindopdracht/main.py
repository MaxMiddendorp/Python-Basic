# Python klok met eigen gebintijd

# Selecteer de starttijd in Uren, Minuten en Seconden
uren = input("Op welk uur wilt u beginnen:"); uren = int(uren)
minuten = input("Op welk minuten wilt u beginnen:"); minuten = int(minuten)
seconden = input("Op welke seconden wilt u beginnen:"); seconden = int(seconden)

# Hier wordt de tijd library van python ingegoegd
import time
# Zolang de loop True is wordt de klok uitgevoerd
while True:
    # Hier wordt de tijd op het scherm weergeven door de print
     print(str(uren).zfill(2) + ":" + str(minuten).zfill(2) + ":" + str(seconden).zfill(2))
     seconden = seconden + 1
     time.sleep(1)
     # Als de 60 seconden wordt berijkt wordt er een minuut toegevoegd
     if seconden == 60:
         seconden = 0
         minuten = minuten + 1
     # Als de 60 minuten wordt berijkt wordt er een uur toegevoegd
     if minuten == 60:
        minuten = 0
        uren = uren + 1
     # Als er 24 uur wordt berijkt wordt de klok op 0 gezet
     if uren == 24:
          uren = 0 
          minuten = 0
          seconden = 0