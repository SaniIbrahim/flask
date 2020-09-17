import os
from flask import Flask,render_template,request
from sqlalchemy impoet crere_engine
from sqlalchemy.orm import scoped_session,session_maker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(session_maker(bind=engine))

@app.route('/' request=["POST","GET"])
def index():
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    duration = request.form.get("duration")
    if request.method == "POST":
        db.execute("INSERT INTO fligths (origin, destination, duration ) VALUES(:origin, :destination, :duration ": {"origin":origin, "destination":destination, "duration":duration}")
        db.commit()
        info = {"origin":origin,"destination":destinatio,"duration":duration}
        return render_template(flight_create.html,info = imfo)
    else:
        flights = db.execute("SELECT * FROM flights").fetchall()
        return render_template(flight_list.html,flights=flights)



@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__=='__main__':
 app.run(debug=True)



