from behave import *

from taller_test.core import api_activities as act
from taller_test.tests.tests_activities import ApiRequestsActivities

test = ApiRequestsActivities()


@given(u'estoy en la url de la api "{url}"')
def step_impl(context, url):
    act.url = url


@when(u'consulto todas las actividades')
def step_impl(context):
    test.test_get_all_activities()


@then(u'trae todas las actividades')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una actividad con codigo "{id}"')
def step_impl(context, id):
    test.test_get_activity(id)


@then(u'trae la informacion de esa actividad')
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id de actividad "{id}" y el nombre "{nombre}"')
def step_impl(context, id, nombre):
    test.test_create_activity(id, nombre)


@then("la actividad es creada")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id de actividad "{id}" y un nuevo nombre "{nombre}"')
def step_impl(context, id, nombre):
    test.test_update_activity(id, nombre)


@then("la actividad se actualiza")
def step_impl(context):
    test.test_validate_status_code(200)


@when('ingreso el id de actividad "{id}"')
def step_impl(context, id):
    test.test_delete_activity(id)


@then("la actividad se elimina")
def step_impl(context):
    test.test_validate_status_code(200)