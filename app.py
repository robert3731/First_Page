from flask import Flask, request, redirect, render_template
app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def main():
    return render_template('me.html')


@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        print(request.form)
        return redirect('/mypage/contact')
