from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Добро пожаловать на отбор астронавтов!"


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'POST':
        lastname = request.form.get('lastname')
        firstname = request.form.get('firstname')
        email = request.form.get('email')
        education = request.form.get('education')
        profession = request.form.getlist('profession')  
        gender = request.form.get('gender')
        motivation = request.form.get('motivation')
        stay_mars = request.form.get('stay_mars')

        print(lastname, firstname, email, education, profession, gender, motivation, stay_mars)

        return "Форма отправлена. Спасибо!"

    return render_template('astronaut_selection.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
