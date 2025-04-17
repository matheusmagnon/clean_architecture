import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    mocked_first_name = "John"
    mocked_last_name = "Doe"
    mokcked_age = 30

    users_reposotory = UsersRepository()
    users_reposotory.insert_user(
        mocked_first_name, mocked_last_name, mokcked_age)

    sql = '''
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = '{}'
    '''.format(mocked_first_name, mocked_last_name, mokcked_age)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mokcked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    '''))

    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    mocked_first_name = "John_2"
    mocked_last_name = "Doe_2"
    mokcked_age = 30

    sql = '''
        INSERT INTO users (first_name, last_name, age)
        VALUES ('{}', '{}', '{}')
    '''.format(mocked_first_name, mocked_last_name, mokcked_age)

    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_first_name)

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mokcked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
    '''))

    connection.commit()
