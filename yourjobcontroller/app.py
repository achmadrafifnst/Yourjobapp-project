from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import pickle

#get_jwt_identity,

app = Flask(__name__)
CORS(app)
app.secret_key = "project2"
jwt = JWTManager(app)

with open('static/model/model_fix.pkl', 'rb') as file:
    load_model = pickle.load(file)

decode = {
        'architectures':0,
        'attorney':1,
        'business analyst':2,
        'counselor':3,
        'criminal investigations':4,
        'editor':5,
        'flight instructor':6,
        'machine learning':7,
        'web designer':8,
        'writer':9,
        'architectural design':10,
        'arranger':11,
        'home offices':12,
        'lecturer':13,
        'mediator':14,
        'patrol':15,
        'photographer':16,
        'piloting':17,
        'producer':18,
        'programmer':19,
        'r':20,
        'big data':21,
        'composer':22,
        'construction disputes':23,
        'crime prevention':24,
        'design durable':25,
        'director':26,
        'flying':27,
        'java programmer':28,
        'teacher':29,
        'webfocus':30,
        'actor':31,
        'advocate':32,
        'data mining':33,
        'design urbain':34,
        'evidence':35,
        'graphic designer':36,
        'instrument rated pilot':37,
        'mis reporting':38,
        'reporter':39,
        'researcher':40,
        'aviation':41,
        'communication skill':42,
        'design architectural':43,
        'educator':44,
        'enforcement':45,
        'journalism':46,
        'legal advice':47,
        'python':48,
        'webmaster':49,
        'apache spark':50,
        'author':51,
        'copywriter':52,
        'criminal justice':53,
        'dancer':54,
        'interpersonal communications':55,
        'journalist':56,
        'litigation':57,
        'php':58,
        'plan darchitecture':59,
        'single engine land':60,
        'cameraman':61,
        'css':62,
        'field training officer':63,
        'freelancer':64,
        'law firm administration':65,
        'multiengine land':66,
        'predictive analytics':67,
        'speaker':68,
        'sustainable architecture':69,
        'administrator':70,
        'attorneys':71,
        'awardwinning writer':72,
        'community policing':73,
        'discrepancy resolution':74,
        'flight training':75,
        'hadoop':76,
        'public speaker':77,
        'sustainable design':78,
        'web development':79,
        'aircraft':80,
        'customer relation':81,
        'data visualization':82,
        'design research':83,
        'filmmaker':84,
        'interrogation':85,
        'javascript':86,
        'legal counseling':87,
        'novelist':88,
        'performer':89,
        'adaptive reuse':90,
        'big data analytics':91,
        'commercial piloting':92,
        'corporate law':93,
        'firearms':94,
        'social worker':95,
        'sviluppo web':96
    }

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="rafif",
    password="uncledrew",
    hostname="rafif.mysql.pythonanywhere-services.com",
    databasename="rafif$users",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'data_users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(50),nullable = False)
    sandi = db.Column(db.String(50),nullable = False)

@app.route("/api/rafif/yourjobapp/home",methods=['GET'])
@jwt_required()
def home():
    current_user = get_jwt_identity()
    data_user = Task.query.filter_by(username = current_user['username']).first()
    print(data_user)
    dataReturn = {
        'name':data_user.name,
        'status':'1',
        'msg':'success to home page'
    }
    return jsonify(dataReturn), 200

@app.route("/api/rafif/yourjobapp/main",methods=['GET'])
@jwt_required()
def main():
    dataReturn = {
        'status':'1',
        'msg':'success to main page'
    }
    return jsonify(dataReturn), 200

@app.route("/api/rafif/yourjobapp/register",methods=['POST'])
def register():
    dataReturn = {
        'status':'0',
        'msg':'Register gagal'
    }
    data_register = request.get_json()
    new_task = Task()
    existing_data = Task.query.filter((Task.username == data_register['username'])|(Task.email == data_register['email'])).first()

    if existing_data:
        dataReturn['msg'] = 'Username atau Email sudah pernah digunakan'
        return(dataReturn), 400
    else:
        for key, value in data_register.items():
            setattr(new_task, key, value)

        db.session.add(new_task)
        db.session.commit()
        dataReturn = {
            'status':'1',
            'msg':'Register berhasil'
        }
    return jsonify(dataReturn), 200

@app.route("/api/rafif/yourjobapp/login",methods=['POST'])
def login():
    dataReturn = {
        'status':'0',
        'msg':'Login gagal'
    }
    data_login = request.get_json()

    existing_data = Task.query.filter((Task.username == data_login['username'])&(Task.sandi == data_login['sandi'])).first()

    if existing_data:
        expires = timedelta(days=1)
        access_token = create_access_token(identity={'username':existing_data.username}, expires_delta=expires)
        dataReturn = {
            'access_token':access_token,
            'status':'1',
            'msg':'Login berhasil'
        }
    else:
        dataReturn = {
            'status':'0',
            'msg':'Username atau Password salah'
        }
        return jsonify(dataReturn), 400
    return jsonify(dataReturn), 200

@app.route("/api/rafif/yourjobapp/recommendation",methods=['POST'])
@jwt_required()
def predict():

    skill = request.get_json()

    skill_1 = skill['skill_1']
    skill_2 = skill['skill_2']
    skill_3 = skill['skill_3']
    skill_4 = skill['skill_4']
    skill_5 = skill['skill_5']
    skill_6 = skill['skill_6']
    skill_7 = skill['skill_7']
    skill_8 = skill['skill_8']
    skill_9 = skill['skill_9']
    skill_10 = skill['skill_10']

    inp_skill = [skill_1,skill_2,skill_3,skill_4,skill_5,skill_6,skill_7,skill_8,skill_9,skill_10]

    index = []
    inputan = [0 for i in range(97)]
    for k,v in decode.items():
        if k in inp_skill:
            index.append(v)
    for i in index:
        inputan[i] = 1
    inputan = np.array(inputan)
    inputan = inputan.reshape(1,-1)
    pred = load_model.predict_proba(inputan)

    sortir = sorted(range(len(pred[0])),reverse=True, key = lambda i:pred[0][i])
    pekerjaan = ['architecture','data analyst','data science','journalist','lawyer','pilot','police','researcher','teacher','web developer','writer']
    sortir = list(map(int,sortir))

    pek_1 = pekerjaan[sortir[0]]
    pek_2 = pekerjaan[sortir[1]]
    pek_3 = pekerjaan[sortir[2]]

    dataReturn = {
        'gambar_1':pek_1,
        'gambar_2':pek_2,
        'gambar_3':pek_3,
        'rekomen_1':pekerjaan[int(sortir[0])],
        'rekomen_2':pekerjaan[int(sortir[1])],
        'rekomen_3':pekerjaan[int(sortir[2])]
    }
    return jsonify(dataReturn), 200

if __name__=="__main__":
    app.run(debug = True,port=5002)


