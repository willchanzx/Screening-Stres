list1 = ['makan','tidur','main']
list2 = [0,0,0]
list_gabung = list()
indeks = 0
for i in range(len(list1)):
    list_gabung.append([list1[indeks],list2[indeks]])
    indeks =+ 1

print(list_gabung)
list1 = list2
print(list1)

#run sblm mulai koding lagi
#start tailwind update = npx tailwindcss -i input.css -o static/src/output.css --watch
#dependency library : numpy, scikit-fuzzy, flask, flask-sqlalchemy, mysql-connector