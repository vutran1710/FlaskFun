from flask import Blueprint, jsonify
from app.models import User, UserProfile
from app import db
from app.api.user import schema_required

bp = Blueprint('register', __name__)


@bp.route('/api/register', methods=['POST'])
@schema_required
def register_user(name, email, password):
    added_user = User(name, email, password)
    profile_added = UserProfile()
    added_user.profile.append(profile_added)
    db.session.add(added_user)
    db.session.commit()

    return jsonify(message='Thanks for registering! Please check your email to confirm your email address.',
                   added_user=added_user.serialize)
