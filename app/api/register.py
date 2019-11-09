from flask import Blueprint, jsonify
from app.models import User, UserProfile
from app import db
from app.api.user import schema_required
from app.helper.send_confirmation_email import send_confirmation_email, confirm_serializer


bp = Blueprint('register', __name__)


@bp.route('/api/register', methods=['POST'])
@schema_required
def register_user(name, email, password):
    added_user = User(name, email, password)
    profile_added = UserProfile()
    added_user.profile.append(profile_added)
    db.session.add(added_user)
    db.session.commit()
    send_confirmation_email(added_user.email)

    return jsonify(message='Thanks for registering! Please check your email to confirm your email address.',
                   added_user=added_user.serialize)


@bp.route('/api/register/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
    except:
        return jsonify(message='The confirmation link is invalid or has expired.')

    user = User.query.filter_by(email=email).first()

    if user.activated:
        return jsonify(message='Account already confirmed. Please login.')
    else:
        user.activated = True
        db.session.add(user)
        db.session.commit()
        return jsonify(message='Thank you for confirming your email address.', your_email=email)
