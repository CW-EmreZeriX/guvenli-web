print("  ____    __        __   _____   ______   ")
print(" / ___|   \ \      / /  / _ \ \ / / ___|  ")
print("| |  _ ____\ \ /\ / /  | | | \ V /\___ \  ")
print("| |_| |_____\ V  V /   | |_| || |  ___) | ")
print(" \____|      \_/\_/     \___/ |_| |____/  ")
print("--------------------------------")
print("Güvenli Web Oys Giriş Hazır Text")
print("--------------------------------")
while (True):
   a=str(input("Grup Adı Giriniz(Sosyal Medya,Bahis Kumar):"))
   if(a=="Sosyal Medya"):
      f=str(input("1.Grup Üyesi:"))
      g=str(input("2.Grup Üyesi:"))
      h=str(input("3.Grup Üyesi:"))
      print("--------------------------------")
      ihbar=int(input("{0} kişisinin ihbar sayısı:".format(f)))
      ihbar2=int(input("{0} kişisinin ihbar sayısı:".format(g)))
      ihbar3=int(input("{0} kişisinin ihbar sayısı:".format(h)))
      break
   elif(a=="sosyal medya"):
      f=str(input("1.Grup Üyesi:"))
      g=str(input("2.Grup Üyesi:"))
      h=str(input("3.Grup Üyesi:"))
      print("--------------------------------")
      ihbar=int(input("{0} kişisinin ihbar sayısı:".format(f)))
      ihbar2=int(input("{0} kişisinin ihbar sayısı:".format(g)))
      ihbar3=int(input("{0} kişisinin ihbar sayısı:".format(h)))
      break
   elif(a=="Bahis Kumar"):
      f=str(input("1.Grup Üyesi:"))
      g=str(input("2.Grup Üyesi:"))
      h=str(input("3.Grup Üyesi:"))
      print("--------------------------------")
      ihbar=int(input("{0} kişisinin ihbar sayısı:".format(f)))
      ihbar2=int(input("{0} kişisinin ihbar sayısı:".format(g)))
      ihbar3=int(input("{0} kişisinin ihbar sayısı:".format(h)))
      break
   elif(a=="bahis kumar"):
      f=str(input("1.Grup Üyesi:"))
      g=str(input("2.Grup Üyesi:"))
      h=str(input("3.Grup Üyesi:"))
      print("--------------------------------")
      ihbar=int(input("{0} kişisinin ihbar sayısı:".format(f)))
      ihbar2=int(input("{0} kişisinin ihbar sayısı:".format(g)))
      ihbar3=int(input("{0} kişisinin ihbar sayısı:".format(h)))
      break
   else:
      print("Mr.Armador Lütfen geçerli bir grup adı giriniz.")
x=ihbar+ihbar2+ihbar3 
print("--------------------------------")
e=str(input("Grup İstek ve öneri varsa giriniz:"))
print("--------------------------------")
z=input("İhbar Tarihi:")
print("--------------------------------")
if(e=="yok"):
    print("Grup Adı: {0}".format(a))
    print("Grup Sorumlusu: Mr.Armador")
    print("Grup Üyeleri: {0} , {1} , {2}".format(f,g,h))
    print("Grup Haftalık İhbar Adedi: {0}".format(x))
    print("Grup Üye Açıklamaları: {0} = {1} , {2} = {3} , {4} = {5} Adet Link Toplamıştır.".format(f,ihbar,g,ihbar2,h,ihbar3))
    print("Grup İstek ve Önerisi: Grup istek ve önerisi bulunmamaktadır.")
    print("Tarih : {0}".format(z))
elif(e==""):
    print("Grup Adı: {0}".format(a))
    print("Grup Sorumlusu: Mr.Armador")
    print("Grup Üyeleri: {0} , {1} , {2}".format(f,g,h))
    print("Grup Haftalık İhbar Adedi: {0}".format(x))
    print("Grup Üye Açıklamaları: {0} = {1} , {2} = {3} , {4} = {5} Adet Link Toplamıştır.".format(f,ihbar,g,ihbar2,h,ihbar3))
    print("Grup İstek ve Önerisi: Grup istek ve önerisi bulunmamaktadır.")
    print("Tarih : {0}".format(z))
else:
    print("Grup Adı: {0}".format(a))
    print("Grup Sorumlusu: Mr.Armador")
    print("Grup Üyeleri: {0} , {1} , {2}".format(f,g,h))
    print("Grup Haftalık İhbar Adedi: {0}".format(x))
    print("Grup Üye Açıklamaları: {0} = {1} , {2} = {3} , {4} = {5} Adet Link Toplamıştır.".format(f,ihbar,g,ihbar2,h,ihbar3))
    print("Grup İstek ve Önerisi: {0}".format(e))
    print("Tarih : {0}".format(z))

