filename= "notepad_python.txt"
my_file = open(filename)
my_file_membaca = my_file.read()
print("Content of " + filename + ":\n" + my_file_membaca)
my_file.close()

#kode alternatif lain kalau ga ganti/ nambahin kata lain di baris ketiga setelah my_file_bla bla bla
filename = "notepad_python.txt"

# Pakai kata "with" di depan, dan diberi titik dua (:) di ujung
with open(filename) as my_file:
    my_file = my_file.read() # <--- BEBAS pakai nama sama (ditimpa)
    print(my_file)
    
# Di sini file sudah otomatis ditutup sendiri sama Python!