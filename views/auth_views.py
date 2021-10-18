from flask import Blueprint,make_response
from flask_apispec import use_kwargs
from service import auth_service
from serializers.auth import SignupRequestSchema

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=['POST'])
@use_kwargs(SignupRequestSchema)
def signup(username, password):
    auth_service.signup(username, password)
    return make_response('{} signup success'.format(username),201)



# @bp.route('/login/', methods=('GET', 'POST'))
# def login():
#
#     return render_template('auth/login.html', form=form)




