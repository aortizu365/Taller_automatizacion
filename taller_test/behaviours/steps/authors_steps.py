from behave import *

from taller_test.core import api_authors as act
from taller_test.tests.tests_authors import ApiRequestsAuthors

test = ApiRequestsAuthors()


@given('estoy en la url de la api de autores "{url}"')
def step_impl(context, url):
    act.url = url


@when("consulto todos los autores")
def step_impl(context):
    test.test_get_all_authors()


@then("trae todos los autores")
def step_impl(context):
    test.test_validate_status_code(200)


@when('consulto un autor con codigo "{id}"')
def step_impl(context, id):
    test.test_get_author(id)


@then("trae la informacion de ese autor")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id de autor "{id}" y el nombre "{nombre}"')
def step_impl(context, id, nombre):
    test.test_create_author(id, nombre)


@then("el autor es creado")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id de autor "{id}" y un nuevo nombre "{nombre}"')
def step_impl(context, id, nombre):
    test.test_update_author(id, nombre)


@then("el autor se actualiza")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id de autor "{id}"')
def step_impl(context, id):
    test.test_delete_author(id)


@then("el autor se elimina")
def step_impl(context):
    test.test_validate_status_code(200)


@when('consulto un libro de un autor con id "{id}"')
def step_impl(context, id):
    test.test_get_libro_author(id)


@then("trae la informacion del libro de ese autor")
def step_impl(context):
    test.test_validate_status_code(200)