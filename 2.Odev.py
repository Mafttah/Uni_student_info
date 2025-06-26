ulkeler = ["Zambia", "Almanya", "İngiltere",  "Galler", "İskoçya", "Fransa", "Sırbistan"]
# ulkeler adında bir değişken tanımladım ve bu değişkenin tipini list [] olarak belirledim.
print(ulkeler)
print("-------------")

ulkeler.append("İtalya, Polonya, Arjantin")
# list metodlarından append ile metod parametresinde belirtilen değer sona atanabilir. 
# metodun parametresi: parantez içindeki değerlerdir. Metodun üzerine mouse ile gelinince metod parametreleri ide tarafından gösterilir. (metodun parametresi o metodun imzası olarak da yorumlanır.)
print(ulkeler)
print("---------------")

ulkeler.insert(0, "Macaristan")
ulkeler.insert(2, "Türkiye")
# list metodlarından insert ile metot parametresinde belirtilen index numarasına ilgili değer atanabilir.
print(ulkeler)
print("-------------")

ulkeler.remove("Sırbistan")
# list metodlarından remove ile metod parametresinde belirtilen değer aranarak bulunan ilk değer silinir. 
print(ulkeler)
print("------------")

ulkeler.sort()
print(f"Sıranamış bir şekilde ülkeler: {ulkeler}")
print("------")

ulkeler.reverse()
print(ulkeler)
print("------")

sayilar =["1", "2", "20", "500", "250"]

ulkeler.extend(sayilar)
print(f"Extend ile eklenenler: {ulkeler}")
print("--------")

ulkeler_copies = ulkeler.copy()
print(f"Copyalama ile ülkeler: {ulkeler_copies}")
print("------")


ulkeler.clear()
print(ulkeler)
print("----------")



telif = [
    {
    "ulke": "İngiltere",
    "sehir": "Londra",
    "gezilecek_yer": "London Eye",
    "ucret": "15"
}
]

# list ve dictionary kalıbı örneği:
list_dicitonary_ornegi = [
    {
        "key1": "deger1",
        "key2": "deger2"
    },
    {
        "key1": "deger3",
        "key2": "deger4"
    }
]


print(telif)
print("--------")

sehir = telif[0].get("sehir")
print(f"Get ile sehir değişkenindeki değeri yazdırma: {sehir}")
print("--------")
print(telif[0].keys())
print("---------")
print(telif[0].values())
print("-------")

print(telif[0]["ulke"])
print(telif[0]["ucret"])
print("-------")

telif[0].update({"ucret": "10" })
guncellenen_ucret = telif[0]["ucret"]
print(f"Güncellenen ücret: {guncellenen_ucret}")
print("------")

print(len(telif))
print("------")

telif.clear()
print(telif)
print("-------")










