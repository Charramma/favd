from models.user import UserProfile
from .extension import ma


class UserSchema(ma.Schema):
    class Meta:
        model = UserProfile
        fields = ('user_profile_id', 'user_profile_email', 'user_profile_mobile', 'user_profile_name')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
