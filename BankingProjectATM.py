from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def logininfo():

    txtusername = request.form.get("txtusername", "")
    txtpass = request.form.get("txtpass", "")

    for user in user_info:

        if user["username"] == txtusername:
            if check_password_hash(user["password"], txtpass):
                return render_template('user.html',username=txtusername)

    print("Username or password incorrect!")
    return render_template('login.html')


@app.route('/createaccount', methods=['GET'])
def useraccount():
    return render_template('createaccount.html')

user_info = []
@app.route('/createaccount', methods=['POST'])
def userinfo():

    txtfname = request.form.get("txtfname", "")
    txtlname = request.form.get("txtlname", "")
    txtmidin = request.form.get("txtmidin", "")
    txtbirth = request.form.get("birth", "")
    txtssn = request.form.get("txtssn", "")
    txtpass = request.form.get("txtpass", "")
    txtconfpass = request.form.get("txtconfpass", "")

    username = f"{txtfname} {txtlname}"

    if txtpass != txtconfpass:

        print("Passwords do not match!")
        return render_template('createaccount.html')

    hashed_password = generate_password_hash(txtpass)

    user_info.append({"username": username, "birthdate": txtbirth, "ssn": txtssn, "password": hashed_password})

    print("Successfully created an account.")

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
