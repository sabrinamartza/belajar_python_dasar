# Tanda pagar untuk menambah komentar
# bisa juga untuk pemisah
# kita sedang belajar variabel
# tipe data huruf itu string kalau angka itu integer ya!
message = ("rinn belajar python") 
print(message) #ini akan nge print sesuai dgn isi mssge mu
print(message)
print(message)
print(message)
print(message)
name = "Sabrina" 
friend = "Jev"
age = 18 #ini merupakan angka integer ga ada koma atau bentuk desimal (int)
height =159.9 #kalau ini adalah float (ada bentuk pecahannya)
print("halo my name "+ name) #bisa pake koma ataupun tanda + untuk bikin spasi
print ("and my friend name",friend)
print ("my age",str(age))
print("my height is",str(height))
print(type(name)) #ini menunjukkan tipe data nya jika kita ngetik type
print(type(friend))
print(type(age))
print(type(height))
#operasi matematika sederhana
line1 = 100
line2 = 50
print(line1 - line2 + line2)
print(line1 + line2)
print(line1 / line2)
print(line1 * line2)
print(line1 % line2) #sisa hasil
#boolean adalah tipe data True dan False
sedang_hujan = True
sedang_terik = True


#conditional
if sedang_hujan:
    print("jangan lupa bawa payung")
    print("jangan lupa pakai jas hujan")
    print("pasti dingin")
else:
    print("Tidak hujan")
    print("gerah")

uangSaya = 12000
SkinMl =12000

if uangSaya >= SkinMl: #soalnya kita pake syarat > uang kita harus lebih dri hrga atau sama dgn skinml
    print("boleh top up")
else:
    print("nabung dulu")

#ada juga yang tipe negasi yk right tipe kebalikannya
uangSaya = 11000
SkinMl =12000

if uangSaya != SkinMl: #karena di sini uang ku tidak sama dengan(lebih besar) harga skin ml makanya bisa kembalian
    print("ada kembalian")
else:
    print("uang pas")
   
#function (learn w jev)
def substraction(parameter1,parameter2):
    print(parameter1-parameter2)
def multiply(parameter1,parameter2):
    print(parameter1*parameter2)
def addition(parameter1,parameter2):
    print(parameter1+parameter2)

substraction(50 , 2)
multiply(1000 , 5)
addition(178 , 2)

#di 27 jun aku buka file ini, ini adalah file pertama bgt ku saat aku punya laptop dan belajar ngoding
age = 18#(ini adalah integer)
print(str(age)) #dan ini adalah perintah untuk meng string kan 18(int)tadi jadi string menggunakan perintah str
#oke jadi ini adalah perintah untuk memaksakan bentuk int jadi string namanya Casting(mengubah tipe data ke tipe data lainnya)


age = 18
print(age) #gini doang sebenernya bisa sih




   

    
 




