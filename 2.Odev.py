ulkeler = ["Almanya", "İngiltere",  "Galler", "İskoçya", "Fransa", "Sırbistan"]
print(ulkeler)
print("-------------")

ulkeler.append("İtalya, Polonya")
print(ulkeler)
print("---------------")

ulkeler.insert(0, "Macaristan")
ulkeler.insert(2, "Türkiye")
print(ulkeler)
print("-------------")

ulkeler.remove("Sırbistan")
print(ulkeler)
print("------------")

ulkeler.sort()
print(ulkeler)
print("------")

ulkeler.reverse()
print(ulkeler)
print("------")

sayilar =["1", "2", "20", "500", "250"]

ulkeler.extend(sayilar)
print(ulkeler)
print("--------")

sehirler =["Munich", "Dortmund",  "Istanbul", "London", "Paris", "Dortmund"]
ulkeler.copy()
print(sehirler)
print("------")


ulkeler.clear()
print(ulkeler)
print("----------")



telif = ({
    "Ülke": "İngiltere",
    "Sehir": "Londra",
    "Gezilecek yer": "London Eye",
    "Ücret": "15"
})

print(telif)
print("--------")
print(telif.get("Sehir"))
print("--------")
print(telif.keys())
print("---------")
print(telif.values())
print("-------")

print(telif["Ülke"])
print(telif["Ücret"])
print("-------")

print(telif.update({"Ücret": "10" }))
print(telif)
print("------")

print(len(telif))
print("------")

telif.clear()
print(telif)
print("-------")










