from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def new():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def promotion():
    promo_text = (
        "Человечество вырастает из детства.<br>"
        "Человечеству мала одна планета.<br>"
        "Мы сделаем обитаемыми безжизненные пока планеты.<br>"
        "И начнем с Марса!<br>"
        "Присоединяйся!<br>"
    )
    return promo_text

if __name__ == "__main__":
    app.run("127.0.0.1", 8080)