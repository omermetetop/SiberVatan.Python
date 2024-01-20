ad=" Ömer Mete"
soy_ad="Top"
yas=16
#
karsilama="Benim adım" + ad +" "+soy_ad+" "+"yaşım"+" "+ str(yas)+" "+"hoşgeldin"
print(karsilama)
#
uzunluk =len(karsilama)
print(uzunluk)
#
print(karsilama[-1]),
#
print(karsilama[4:10])
#
print(karsilama[12:25])
#
print(karsilama[:25])
#
print(karsilama[12:])
#
print(karsilama[2:25:3])
#
print(karsilama[:-3])
#
print(karsilama[::-1])
#
karsilama_upper=karsilama.upper()
print(karsilama_upper)

karsilama_lower=karsilama.lower()
print(karsilama_lower)

karsilama_strip=karsilama.strip()
print(karsilama_strip)

karsilama_split=karsilama.split()
print(karsilama_split)
print(karsilama_split[6])

karsilama_join="-".join(karsilama)
print(karsilama_join)

karsilama_find=karsilama.find("Ömer")
print(karsilama_find)

karsilama_startswith=karsilama.startswith("n")
print(karsilama_startswith)

karsilama_endwith=karsilama.endswith("b")
print(karsilama_endwith)

karsilama_replace=karsilama.replace("Ömer Mete","Arda")
print(karsilama_replace)

