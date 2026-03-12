from flask import Flask, render_template


from data import db_session
from data.jobs import Jobs

app = Flask(__name__)


db_session.global_init("db/mars_explorer.db")
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


@app.route("/image_mars")
def image_mars():
    return render_template("image_mars.html")



@app.route("/promotion_image")
def promotion_image():
    return render_template("promotion_image.html")


if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")

    session = db_session.create_session()
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    session.add(job)

    app.run("127.0.0.1", 8080)
