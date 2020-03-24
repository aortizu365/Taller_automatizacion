from behave import *

from ui_testing.tests.vuelos import VuelosTest

vuelos = VuelosTest()


@given(u'Estoy en la pagina de Mercury Tours para seleccionar vuelo')
def step_impl(context):
    vuelos.init_driver()
    vuelos.test_go_url("http://newtours.demoaut.com/mercuryreservation.php")


@when(u'Hago Login con usuario "{user}" y password "{password}"')
def step_impl(context, user, password):
    context.user = user
    context.password = password
    vuelos.test_login(context.user, context.password)


@when(u'selecciono un trayecto One way')
def step_impl(context):
    vuelos.test_seleccionar_one_way()


@when(u'selecciono "{numero}" pasajeros')
def step_impl(context, numero):
    vuelos.test_numero_pasajeros(numero)


@when(u'selecciono salida desde "{partida}"')
def step_impl(context, partida):
    vuelos.test_seleccionar_partida(partida)


@when(u'selecciono la fecha de partida en "{mes}" "{dia}"')
def step_impl(context, mes, dia):
    vuelos.test_seleccionar_fecha_partida(mes, dia)


@when(u'selecciono el destino como "{llegada}"')
def step_impl(context, llegada):
    vuelos.test_seleccionar_llegada(llegada)


@when(u'selecciono el retorno en "{mes}" "{dia}"')
def step_impl(context, mes, dia):
    vuelos.test_seleccionar_fecha_retorno(mes, dia)


@when(u'selecciono la clase Business')
def step_impl(context):
    vuelos.test_seleccionar_clase()


@when(u'selecciono la aerolinea "{aerolinea}"')
def step_impl(context, aerolinea):
    vuelos.test_seleccionar_aerolinea(aerolinea)


@when(u'envio el formulario')
def step_impl(context):
    vuelos.test_enviar_formulario()


@then(u'El sistema me retorna vuelos')
def step_impl(context):
    vuelos.test_validar_respuesta()
    vuelos.close()