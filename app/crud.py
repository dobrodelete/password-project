from app.models import db, User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def create_user(username, email, password):
    """
    Создает нового пользователя.

    :param username: Имя пользователя.
    :param email: Email пользователя.
    :param password: Пароль пользователя.
    :return: Объект пользователя.
    """
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id(user_id):
    """
    Возвращает пользователя по его ID.

    :param user_id: ID пользователя.
    :return: Объект пользователя или None, если пользователь не найден.
    """
    return User.query.get(user_id)


def get_user_by_username(username):
    """
    Возвращает пользователя по его имени пользователя.

    :param username: Имя пользователя.
    :return: Объект пользователя или None, если пользователь не найден.
    """
    return User.query.filter_by(username=username).first()


def get_user_by_email(email) -> User:
    """
    Возвращает пользователя по его email.

    :param email: Email пользователя.
    :return: Объект пользователя или None, если пользователь не найден.
    """
    return User.query.filter_by(email=email).first()


def update_user(user_id, username=None, email=None, password=None):
    """
    Обновляет информацию о пользователе.

    :param user_id: ID пользователя.
    :param username: Новое имя пользователя (необязательно).
    :param email: Новый email пользователя (необязательно).
    :param password: Новый пароль пользователя (необязательно).
    :return: Обновленный объект пользователя или None, если пользователь не найден.
    """
    user = User.query.get(user_id)
    if user:
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        db.session.commit()
    return user


def delete_user(user_id):
    """
    Удаляет пользователя по его ID.

    :param user_id: ID пользователя.
    :return: True, если пользователь был удален, False если пользователь не найден.
    """
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False
