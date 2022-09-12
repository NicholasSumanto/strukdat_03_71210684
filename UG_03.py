kalimat = str(input("masukkan sebuah klaimat ="))
kata = str(input("Masukkan kata yang ingin dicari ="))

list = 0
for i in kalimat.lower().split():
    if i == kata.lower():
        list += 1

print(list)