from behave import *

from taller_test.core import api_books as act
from taller_test.tests.tests_books import ApiRequestsBooks

test = ApiRequestsBooks()


@given('estoy en la url de la api de libros "{url}"')
def step_impl(context, url):
    act.url = url


@when("consulto todos los libros")
def step_impl(context):
    test.test_get_all_books()


@then("trae todos los libros")
def step_impl(context):
    test.test_validate_status_code(200)


@when('consulto un libro con codigo "{id}"')
def step_impl(context, id):
    test.test_get_book(id)


@then("trae la informacion de ese libro")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id del libro "{id}" y el nombre "{nombre}"')
def step_impl(context, id, nombre):
    test.test_create_book(id, nombre)


@then("el libro es creado")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id del libro "{id}" y un nuevo nombre "{nombre}"')
def step_impl(context, id, nombre):
    test.test_update_book(id, nombre)


@then("el libro se actualiza")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id de libro "{id}"')
def step_impl(context, id):
    test.test_delete_book(id)


@then("el libro se elimina")
def step_impl(context):
    test.test_validate_status_code(200)
