
greeting=input("Selamlama ifadesi giriniz:")
name=input("İsim giriniz:")
surname=input("Soyisim giriniz:")
age=int(input("Yas giriniz:"))  
#Burada input dan aldıgımız degeri integer'a cevirdik.Cunku input bize string deger verir.
#Yas hesaplamasi yapacagımız zaman sıkıntılar olusabilir.Bu yuzden int almak daha dogru olacaktır.
university=input("Universiteniz:")
department=input("Bolumunuz:")

#Bunları bir kac sekilde yazdırabiliriz.
print("*****************************************")
print(f"{greeting}\nİsminiz:{name}\nSoyisminiz:{surname}\nYasiniz:{age}\nOkulunuz:{university}\nBolumunuz:{department}")
print("*****************************************")


print(greeting,"İsminiz:%s\nSoyisminiz:%s\nYasiniz:%d\nOkulunuz:%s\nBolumunuz:%s" % (name,surname,age,university,department))

print(greeting,"İsminiz:",name,"Soyisminiz:",surname,"Yasiniz:",age,"Okulunuz:",university,"Bolumunuz:",department,sep="\n")
#Burada sep her kelime arasına oraya ne yazarsak onu koyar.
