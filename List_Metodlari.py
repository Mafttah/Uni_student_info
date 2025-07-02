sayi = [1, 4, 6]
sehir = ["Berlin", "Dortmund", "Strazbourg"]

#sehir_index_no = sehir.index("Dortmund")
#sehir_index_no = sehir.index("Dortmund", 0,2)
# try except
# print("Ödev")
try:    
    sehir = input("Bir şehir ismi girin: ")
    sehir_index_no = sehir.index(sehir)
    print(f"sehir_index_no: {sehir_index_no}")
except ValueError as e:
    print(f"hata: {e}")
    if str(e) == "'{sehir}' is not in list":
        print(f"{sehir} listede bulunamadı.")

print(f"Şehir listesindeki kayıt sayısı: {len(sehir)}")

# print("Ödev")
# print("try expect ile hata kontrolü yap")
# print("Kullanıcıya toplam kayıt sayısı belirterek, silmek istediği kaydı input ile al")
# print("Şehir listesini uzat")
# silinen_deger = sehir.pop()
# print(f"Sondan silinen değer: {silinen_deger}")
# index_ile_silinen = sehir.pop(1)
# print(f"Silinen değer: {index_ile_silinen}")









