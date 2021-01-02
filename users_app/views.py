from jsonschema import validate
from jsonschema.exceptions import ValidationError
from users_app.schemas import user_schema
from flask import request
from users_app.models import User
from users_app import db
from operator import itemgetter
from users_app.helpers import CustomResponse, WebStatus, ErrorCode
from logging import getLogger
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import (jwt_required,
                                create_access_token,
                                get_jwt_identity)


log = getLogger(__name__)


def sign_in():
    request_data = request.get_json(silent=False)
    try:
        validate(request_data, user_schema)
        email, password = itemgetter('email', 'password')(request_data)
        user = User.query.filter_by(email=email).first()
        if user is not None and user.check_password(password):
            token = create_access_token(identity=user.to_json(),
                                        expires_delta=timedelta(hours=6))
            return CustomResponse(status=WebStatus.OK,
                                  data=dict(token=token),
                                  code=ErrorCode.SUCCESS)
        else:
            return CustomResponse(status=WebStatus.ERROR,
                                  code=ErrorCode.CREDENTIALS_ERROR)
    except ValidationError as error:
        log.error(error)
        return CustomResponse(status=WebStatus.ERROR,
                              code=ErrorCode.VALIDATION_ERROR)


def sign_up():
    request_data = request.get_json(silent=False)
    try:
        validate(request_data, user_schema)
        email, password = itemgetter('email', 'password')(request_data)
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return CustomResponse(status=WebStatus.OK,
                              code=ErrorCode.SUCCESS)
    except (ValidationError, IntegrityError) as error:
        log.error(error)
        return CustomResponse(status=WebStatus.ERROR,
                              code=ErrorCode.VALIDATION_ERROR)


@jwt_required
def profile():
    return CustomResponse(status=WebStatus.OK,
                          data=get_jwt_identity(),
                          code=ErrorCode.SUCCESS)

