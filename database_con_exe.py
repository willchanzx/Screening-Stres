import mysql.connector

'''
pw db amazon aws 
Screenpw123

dbase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="screening"
)    

dbase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="screening2"
)

dbase = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6511291",
    password="pYaS1NTRL5",
    database="sql6511291"
)

Host: sql6.freesqldatabase.com
Database name: sql6511291
Database user: sql6511291
Database password: pYaS1NTRL5
Port number: 3306
'''
dbase = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6511291",
    password="pYaS1NTRL5",
    database="sql6511291"
)

print(dbase)
mycursor = dbase.cursor()
# =======================================================
# Setup list yang dibutuhkan
mycursor.execute("SELECT id_n, text_gejala, tingkat_stres, max_sim, id_v FROM kasus_new")
all_kasus_baru = mycursor.fetchall()

pilihan_p = []
pertanyaan_p = []
bobot_p = []
pilihan_f = []
pertanyaan_f = []
bobot_f = []
answer = []
x_rendah_mult = []
x_sedang_mult = []
x_tinggi_mult = []
y_rendah_mult = []
y_sedang_mult = []
y_tinggi_mult = []
# =======================================================
mycursor.execute("SELECT gejala,bobot,rendah,sedang,tinggi,deskripsi FROM list_gejala WHERE jenis ='psikis'")
for i in mycursor:
    pilihan_p.append(i[0])
    bobot_p.append(i[1])
    x_rendah_mult.append(i[2])
    x_sedang_mult.append(i[3])
    x_tinggi_mult.append(i[4])
    pertanyaan_p.append(i[5])
    answer.append(0)

mycursor.execute("SELECT gejala,bobot,rendah,sedang,tinggi,deskripsi FROM list_gejala WHERE jenis ='fisik'")
for i in mycursor:
    pilihan_f.append(i[0])
    bobot_f.append(i[1])
    y_rendah_mult.append(i[2])
    y_sedang_mult.append(i[3])
    y_tinggi_mult.append(i[4])
    pertanyaan_f.append(i[5])
    answer.append(0)

pilihan = pilihan_p + pilihan_f
pertanyaan = pertanyaan_p + pertanyaan_f
bobot = bobot_p + bobot_f


# =======================================================
# ambil data kasus dari database
mycursor.execute("SELECT text_gejala, tingkat_stres, id_v FROM kasus_verified")
kasus = []
for i in mycursor:
    kasus.append(i)


jumlah_kasus = len(kasus)
diagnosa = str
max_sim = 0
# a adalah pengulangan untuk masing-masing kasus, b adalah pengulangan komparasi masing-masing gejala(elemen list)


gcp = list() # list untuk menentukan jumlah index gejala sifat psikis
for i in pilihan_p:
    gcp.append(0)

gcf = list() # list untuk menentukan jumlah index gejala sifat psikis
for i in pilihan_f:
    gcf.append(0)

gejala = pilihan # variabel untuk mempermudah pengertian saja

mycursor.execute("SELECT id_n, text_gejala, tingkat_stres, max_sim, id_v FROM kasus_new")
record_gej_baru = mycursor.fetchall()
def load_data():
    global list_all_kasus_baru
    mycursor.execute("SELECT id_n, text_gejala, tingkat_stres, max_sim, id_v FROM kasus_new")
    records = mycursor.fetchall()
    list_all_kasus_baru=[]
    kk = 0
    for setiap_kasus_baru in records:
        DAFTAR_GEJALA_KASUS = ""
        y = 0
        for i in records[kk][1]:  # records[kode kasus ke-][list digit gejala]
            if int(i) != 1:
                pass
            else:
                nama_gejala = pilihan[y]
                DAFTAR_GEJALA_KASUS = DAFTAR_GEJALA_KASUS + nama_gejala + ", "
            y = y + 1
        DAFTAR_GEJALA_KASUS_all = DAFTAR_GEJALA_KASUS[:-2]
        for setiap_kasus_baru in records:
            list_all_kasus_baru.append([setiap_kasus_baru[0], DAFTAR_GEJALA_KASUS_all, setiap_kasus_baru[2], setiap_kasus_baru[3], setiap_kasus_baru[4]])
        kk = kk + 1

