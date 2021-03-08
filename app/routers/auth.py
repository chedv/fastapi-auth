from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..dependencies import get_db_session
from ..schemas import UserRegistration, UserLogin
from ..database.users import create_user


auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/register', status_code=status.HTTP_201_CREATED)
def user_register(user: UserRegistration = Depends(UserRegistration.as_form),
                  db_session: Session = Depends(get_db_session)):
    try:
        user = create_user(db_session, user, user_role='client')
    except IntegrityError:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='User with specified parameters already exists')
    return {'user_uuid': user.id}


@auth_router.post('/login', status_code=status.HTTP_200_OK)
def user_login(user: UserLogin = Depends(UserLogin.as_form)):
    return {'access_token': '', 'token_type': 'bearer'}
