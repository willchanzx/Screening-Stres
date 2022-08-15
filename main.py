import numpy as np
import skfuzzy as fuzzy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from database_con_exe import *
from flask import Flask, render_template, url_for, request, redirect, session, flash
from classes_def import *
from datetime import timedelta


gxtext = [] #list untuk menyimpan value 0 untuk diganti sbg text tampilan hasil akhir
g_test = [] #list untuk menyimpan value 0 untuk memastikan gejala ada dipilih dalam proses screening
gx = [] # list untuk menentukan jumlah gejala dan menyimpan value ada atau tidaknya gejala (1 ada, 0 tidak ada)
for i in pilihan:
    gx.append(0)
    g_test.append(0)
    gxtext.append(0)

max_sim=0
kasus_ke=0
kasus_terpilih=1
#kasus_terpilih="kv00001"
diagnosa="Tidak ada gejala yang terdeteksi dari jawaban anda"
app = Flask(__name__)
app.secret_key = "rahasia_ya"
app.permanent_session_lifetime = timedelta(days=2)
idpi = 0
idpbatch = 0
pertanyaan_induk = ['Apakah anda banyak memiliki beban pikiran?',
                    'Apakah merasa membebani orang lain?',
                    'Apakah anda punya riwayat penyakit asma?',
                    'Apakah anda merasa tidak enak badan?'
                    ]

#dbconn = create_engine("mysql+pymysql://root:@localhost/screening")

@app.route('/')
def root():
    global idpi, gx, g_test
    idpi = 0
    gx = g_test
    return redirect(url_for('index'))

@app.route('/homePage')
def index():
    global idpi, gx, g_test
    idpi = 0
    gx = g_test
    return render_template("index.html")

@app.route('/pertanyaan_I/', methods=["POST","GET"])
def pertanyaan_I():
    global idpi, idpbatch
    if request.method == "POST":
        print("post")
        if request.form['answer_button'] == "Ya":
            if idpi == 0:
                idpbatch = 0
                if idpi < 3:
                    idpi = idpi + 1
                return redirect(url_for('pertanyaan_batchInduk1'))
            if idpi == 1:
                idpbatch = 6
                if idpi < 3:
                    idpi = idpi + 1
                return redirect(url_for('pertanyaan_batchInduk2'))
            if idpi == 2:
                idpbatch = 11
                if idpi < 3:
                    idpi = idpi + 1
                return redirect(url_for('pertanyaan_batchInduk3'))
            if idpi == 3:
                idpbatch = 12
                if idpi < 3:
                    idpi = idpi + 1
                return redirect(url_for('pertanyaan_batchInduk4'))

        elif request.form['answer_button'] == "Tidak":
            if pertanyaan_induk[idpi] != pertanyaan_induk[-1]:
                if idpi < 3:
                    idpi = idpi + 1
                question = pertanyaan_induk[idpi]
                print(gx)
                return render_template("pertanyaan_induk.html", pertanyaan_induk=question)
            else:
                return redirect(url_for('result'))

    elif request.method == "GET":
        print("get")
        question = pertanyaan_induk[idpi]
        #return redirect(url_for('root'))
        return render_template("pertanyaan_induk.html", pertanyaan_induk=question)

@app.route('/pertanyaan_I/1', methods=["POST","GET"])
def pertanyaan_batchInduk1():
    global idpbatch, gx
    question = pertanyaan[idpbatch]
    if request.method == "POST":
        if request.form['answer_button'] == "Ya":
            gx[idpbatch] = 1
            if idpbatch < 15:
                idpbatch = idpbatch + 1
            print(gx)
            if idpbatch > 5:
                return redirect(url_for('pertanyaan_I'))
            else:
                return redirect(url_for('pertanyaan_batchInduk1'))
        elif request.form['answer_button'] == "Tidak":
            gx[idpbatch] = 0
            if idpbatch < 15:
                idpbatch = idpbatch + 1
            print(gx)
            if idpbatch > 5:
                return redirect(url_for('pertanyaan_I'))
            else:
                return redirect(url_for('pertanyaan_batchInduk1'))
    return render_template("hlm_pertanyaan.html", pertanyaang=question, angka=idpbatch)

@app.route('/pertanyaan_I/2', methods=["POST","GET"])
def pertanyaan_batchInduk2():
    global idpbatch, gx
    question = pertanyaan[idpbatch]
    if request.method == "POST":
        if request.form['answer_button'] == "Ya":
            gx[idpbatch] = 1
            if idpbatch < 15:
                idpbatch = idpbatch + 1
            print(gx)
            if idpbatch > 10:
                return redirect(url_for('pertanyaan_I'))
            else:
                return redirect(url_for('pertanyaan_batchInduk2'))
        elif request.form['answer_button'] == "Tidak":
            gx[idpbatch] = 0
            if idpbatch < 15:
                idpbatch = idpbatch + 1
            print(gx)
            if idpbatch > 10:
                return redirect(url_for('pertanyaan_I'))
            else:
                return redirect(url_for('pertanyaan_batchInduk2'))
    return render_template("hlm_pertanyaan.html", pertanyaang=question, angka=idpbatch)

@app.route('/pertanyaan_I/3', methods=["POST","GET"])
def pertanyaan_batchInduk3():
    global idpbatch, gx
    question = pertanyaan[idpbatch]
    if request.method == "POST":
        if request.form['answer_button'] == "Ya":
            gx[idpbatch] = 1
            if idpbatch < 15:
                idpbatch = idpbatch + 1
            print(gx)
            if idpbatch > 11:
                return redirect(url_for('pertanyaan_I'))
            else:
                return redirect(url_for('pertanyaan_batchInduk3'))
        elif request.form['answer_button'] == "Tidak":
            gx[idpbatch] = 0
            if idpbatch < 15:
                idpbatch = idpbatch + 1
            print(gx)
            if idpbatch > 11:
                return redirect(url_for('pertanyaan_I'))
            else:
                return redirect(url_for('pertanyaan_batchInduk3'))

    return render_template("hlm_pertanyaan.html", pertanyaang=question, angka=idpbatch)

@app.route('/pertanyaan_I/4', methods=["POST","GET"])
def pertanyaan_batchInduk4():
    global idpbatch, gx
    question = pertanyaan[idpbatch]
    if request.method == "POST":
        if request.form['answer_button'] == "Ya":
            gx[idpbatch] = 1
            if idpbatch < 15:
                idpbatch = idpbatch + 1
                return redirect(url_for('pertanyaan_batchInduk4'))
            else:
                return redirect(url_for('result'))
        elif request.form['answer_button'] == "Tidak":
            gx[idpbatch] = 0
            if idpbatch < 15:
                idpbatch = idpbatch + 1
                return redirect(url_for('pertanyaan_batchInduk4'))
            else:
                return redirect(url_for('result'))
    return render_template("hlm_pertanyaan.html", pertanyaang=question, angka=idpbatch)

#load halaman hasil
@app.route('/result')
def result():
    gej_pil = list()
    global idpi, idpbatch, gx, g_test, gxtext, pilihan, max_sim, kasus_ke, kasus_terpilih, diagnosa

    for i in range(len(pilihan)):
        if gx[i] == 1:
            gxtext[i]="Ya"
        else:
            gxtext[i]="Tidak"
        gej_pil.append([pilihan[i],gxtext[i]])
        print(gej_pil)

####======== Bagian Perhitungan ========#####
    max_sim = 0
    # indeks [a] ke 0 adalah text gejala, ke 1 hasil, ke 2 id_gejala
    for a in range(jumlah_kasus):
        print("===============================")
        print("tes kasus ke-", a + 1)
        nx = 0
        n = 0
        simpan_nilai_gejala = []
        for i in kasus[a][0]:  # masukkan digit kasus ke-a
            simpan_nilai_gejala.append(int(i))
        print("digit input:", gx)
        print("digit kasus:", simpan_nilai_gejala)
        for b in range(len(gx)):
            if simpan_nilai_gejala[b] == 0 and gx[b] == 1:
                nx = nx
                n = n + 1
            elif simpan_nilai_gejala[b] == 1 and simpan_nilai_gejala[b] != gx[b]:
                nx = nx
                n = n + 1
            elif simpan_nilai_gejala[b] == 1 and simpan_nilai_gejala[b] == gx[b]:
                nx = nx + 1
                n = n + 1
            else:
                nx = nx
                n = n
        print("yang sama:", nx)
        print("total var:", n)
        sim_a = nx / n
        if sim_a > max_sim:
            max_sim = sim_a
            kasus_ke = a
            kasus_terpilih = kasus[a][2]
            diagnosa = kasus[a][1]
    print("===============================")
    print("Kasus yang terpilih adalah kasus ke-", kasus_ke + 1, "di database")
    print("Tingkat stres adalah:", diagnosa)
    print("Similaritas adalah:", max_sim)
    if max_sim == 1 or gx == g_test:  # Jika kasus gejalanya sama persis, tidak disimpan ke kasus baru
        pass
    elif max_sim > 0.85:
        text_gejala = ""  # untuk menyimpan gejala yang diisi dalam record
        for i in gx:
            text_gejala += str(i)
        print("text gejala adalah:", text_gejala)
        mycursor.execute("insert into kasus_new (text_gejala,tingkat_stres,id_v,max_sim)"
                         "values(%s,%s,%s,%s)",
                         (text_gejala, diagnosa, kasus_terpilih, max_sim),
                         )
        dbase.commit()
    # =============================================================================
    # Proses fuzzy, dilakukan apabila similarity waktu membandingkan kasus di bawah 0.85
    # =============================================================================
    # 2 variabel fuzzy, gejala psikis, gejala fisik(psikosomatik)
    # gejala psikis ada 11 gejala 3 himpunan, rendah, sedang, tinggi,
    # gejala fisik(psikosomatik) ada 5 gejala, 3 himpunan, rendah, sedang, tinggi
    # Variabel akhir adalah tingkat stress, terdiri atas rendah, sedang, tinggi
    # =============================================================================
    elif max_sim < 0.85:
        print("Similaritas terlalu kecil")
        # x mewakili variabel gejala psikis
        # y mewakili variabel gejala fisik
        x_rendah = 0
        x_sedang = 0
        x_tinggi = 0
        y_rendah = 0
        y_sedang = 0
        y_tinggi = 0
        index_psi = 0
        index_fis = 0
        print("===============")
        print(gx)
        print(bobot)
        print(x_rendah_mult,y_rendah_mult)
        print(x_sedang_mult,y_sedang_mult)
        print(x_tinggi_mult,y_tinggi_mult)
        print("===============")

        for input_gej in range(len(gx)):
            if input_gej < len(gcp):
                x_rendah = x_rendah + (gx[input_gej] * bobot[input_gej] * x_rendah_mult[index_psi])
                x_sedang = x_sedang + (gx[input_gej] * bobot[input_gej] * x_sedang_mult[index_psi])
                x_tinggi = x_tinggi + (gx[input_gej] * bobot[input_gej] * x_tinggi_mult[index_psi])
                index_psi = index_psi + 1
            else:
                y_rendah = y_rendah + (gx[input_gej] * bobot[input_gej] * y_rendah_mult[index_fis])
                y_sedang = y_sedang + (gx[input_gej] * bobot[input_gej] * y_sedang_mult[index_fis])
                y_tinggi = y_tinggi + (gx[input_gej] * bobot[input_gej] * y_tinggi_mult[index_fis])
                index_fis = index_fis + 1
        print("===============")
        print("psi rendah:",x_rendah)
        print("psi sedang:",x_sedang)
        print("psi tinggi:",x_tinggi)
        print("psi rendah:",y_rendah)
        print("psi sedang:",y_sedang)
        print("psi tinggi:",y_tinggi)
        print("===============")
        # variabel kasus dan jarak (min,max,step)
        gejala_psikis = np.arange(0, 45, 0.1)
        gejala_fisik = np.arange(0, 22, 0.1)
        hasil_diagnosa = np.arange(0, 100, 0.1)

        # penentuan range himpunan masing-masing variabel, trap grafik trapesium, tri grafik segitiga
        gejala_psi_ringan = fuzzy.trapmf(gejala_psikis, [0, 0, 5, 15])
        gejala_psi_sedang = fuzzy.trapmf(gejala_psikis, [10, 14, 18, 26])
        gejala_psi_tinggi = fuzzy.trapmf(gejala_psikis, [15, 30, 45, 45])

        gejala_fis_ringan = fuzzy.trapmf(gejala_fisik, [0, 0, 3, 6])
        gejala_fis_sedang = fuzzy.trimf(gejala_fisik, [4, 6, 12])
        gejala_fis_tinggi = fuzzy.trapmf(gejala_fisik, [8, 12, 22, 22])

        hasil_diagnosa_r = fuzzy.trapmf(hasil_diagnosa, [0, 0, 25, 40])
        hasil_diagnosa_s = fuzzy.trimf(hasil_diagnosa, [25, 60, 75])
        hasil_diagnosa_t = fuzzy.trapmf(hasil_diagnosa, [50, 75, 100, 100])

        psi = [fuzzy.interp_membership(gejala_psikis, gejala_psi_ringan, x_rendah),
               fuzzy.interp_membership(gejala_psikis, gejala_psi_sedang, x_sedang),
               fuzzy.interp_membership(gejala_psikis, gejala_psi_tinggi, x_tinggi)]

        fis = [fuzzy.interp_membership(gejala_fisik, gejala_fis_ringan, y_rendah),
               fuzzy.interp_membership(gejala_fisik, gejala_fis_sedang, y_sedang),
               fuzzy.interp_membership(gejala_fisik, gejala_fis_tinggi, y_tinggi)]

        print("nilai fuzzy grafik gejala_psikis:")
        print("psikis R:", psi[0])
        print("psikis S:", psi[1])
        print("psikis T:", psi[2])
        print("\nnilai fuzzy grafik gejala_fisik:")
        print("fisik R:", fis[0])
        print("fisik S:", fis[1])
        print("fisik T:", fis[2])

        # cari a-predikat | Rule yang sudah ditentukan ||indeks list 0=rendah,1=sedang,2=tinggi
        r1 = min(psi[2], fis[2])  # jika gejala psikis tinggi dan gejala fisik tinggi, stres tinggi
        r2 = min(psi[2], fis[1])  # jika gejala psikis tinggi dan gejala fisik sedang, stres tinggi
        r3 = min(psi[1], fis[2])  # Jika gejala psikis sedang dan gejala fisik tinggi, stres tinggi
        r4 = min(psi[1], fis[1])  # jika gejala psikis sedang dan gejala fisik sedang, stres sedang
        r5 = min(psi[1], fis[0])  # Jika gejala psikis sedang dan gejala fisik rendah, stres sedang
        r6 = min(psi[0], fis[1])  # Jika gejala psikis rendah dan gejala fisik sedang, stres rendah
        r7 = min(psi[0], fis[0])  # Jika gejala psikis rendah dan gejala fisik rendah, stres rendah
        r8 = min(psi[1], fis[0])  # Jika gejala psikis sedang dan gejala fisik rendah, stres rendah
        r9 = min(psi[2], fis[0])  # Jika gejala psikis tinggi dan gejala fisik rendah, stres tinggi

        # tinggi | rx = z-50 / 75-50
        # sedang | rx = z-25 / 60-25 | rx = 75-z / 75-60
        # rendah | rx = 40-z / 40-25

        # cari nilai z
        z1 = 50 + (25 * r1)
        z2 = 50 + (25 * r2)
        z3 = 50 + (25 * r3)

        z4alt = [0, 0]
        z4alt[0] = (35 * r4) + 25
        z4alt[1] = 75 - (15 * r4)
        z4 = min(z4alt)

        z5alt = [0, 0]
        z5alt[0] = (35 * r5) + 25
        z5alt[1] = 75 - (15 * r5)
        z5 = min(z5alt)

        z6 = 40 - (15 * r6)
        z7 = 40 - (15 * r7)
        z8 = 40 - (15 * r8)
        z9 = 50 + (25 * r9)

        # Hasil Defuzzifikasi Average
        z_final = ((r1 * z1) + (r2 * z2) + (r3 * z3) + (r4 * z4) + (r5 * z5) + (r6 * z6) + (r7 * z7) + (
                r8 * z8) + (
                           r9 * z9)) / \
                  (r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9)

        print("\nAverage:", z_final)

        hsl = [fuzzy.interp_membership(hasil_diagnosa, hasil_diagnosa_r, z_final),
               fuzzy.interp_membership(hasil_diagnosa, hasil_diagnosa_s, z_final),
               fuzzy.interp_membership(hasil_diagnosa, hasil_diagnosa_t, z_final)]

        print('\nrendah:', hsl[0],
              '\nsedang:', hsl[1],
              '\ntinggi:', hsl[2])

        if max(hsl) == hsl[0]:
            print('Hasil diagnosa : tingkat stres rendah')
            diagnosa = "rendah"
        elif max(hsl) == hsl[1]:
            print('Hasil diagnosa : tingkat stres sedang')
            diagnosa = "sedang"
        else:
            print('Hasil diagnosa : tingkat stres tinggi')
            diagnosa = "tinggi"
        text_gejala = ""  # untuk menyimpan gejala yang diisi dalam record
        for i in gx:
            text_gejala += str(i)
        print("text gejala adalah:", text_gejala)
        mycursor.execute("insert into kasus_new (text_gejala,tingkat_stres,id_v,max_sim)"
                         "values(%s,%s,%s,%s)",
                         (text_gejala, diagnosa, kasus_terpilih, max_sim),
                         )
        dbase.commit()


    idpi = 0
    idpbatch = 0
    g_test = []
    for i in pilihan:
        g_test.append(0)
    gx = g_test
    return render_template("result.html", gej_pil=gej_pil, hasil_screen=diagnosa)


if __name__ == "__main__":
    app.run(debug=True)