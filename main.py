from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    title = 'halaman utama'
    return render_template('home.html', title= title)

@app.route("/about")
def about():
    title = 'halaman about'
    return render_template('about.html', title= title)
    
@app.route("/usia", methods=['GET','POST'])
def usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = 2024
        usia = tahun_sekarang - tahun_lahir
        return render_template('cek_usia.html', usia = usia, tahun_lahir = tahun_lahir)
    return render_template('cek_usia.html', usia = None)

if __name__ == "__main__":
    app.run(host='0.0.0.0')