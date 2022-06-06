from flask import Blueprint,render_template
auth = Blueprint('auth', __name__)
def array():
    return list(range(5))


@auth.route('/login')
def login():
    return render_template("login.html", kami=array())

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

#pohui
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
