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


@when(u'envio el formulario de busqueda de vuelo')
def step_impl(context):
    vuelos.test_enviar_formulario()


@then(u'El sistema me retorna vuelos')
def step_impl(context):
    vuelos.test_validar_reserva()
    vuelos.close()


@step("selecciono el vuelo de ida mas costoso")
def step_impl(context):
    vuelos.test_ida_costoso()


@step("selecciono el vuelo de retorno mas costoso")
def step_impl(context):
    vuelos.test_retorno_costoso()


@step("envio las seleccion de vuelos")
def step_impl(context):
    vuelos.test_enviar_seleccion()


@step(
    'ingreso la informacion del pasajero "{numero}" con nombre "{nombre}" apellido "{apellido}" y selecciono la opcion  de comida "{comida}"')
def step_impl(context, numero, nombre, apellido, comida):
    vuelos.test_pasajero_numero(numero, nombre, apellido, comida)


@step('selecciono la opcion de tarjeta "{tipo}"')
def step_impl(context, tipo):
    vuelos.test_tarjeta_tipo(tipo)


@step('ingreso el numero de tarjeta "{numero}"')
def step_impl(context, numero):
    vuelos.test_tarjeta_numero(numero)


@step('ingreso la fecha de expiracion de la tarjeta mes "{mes}" year "{year}"')
def step_impl(context, mes, year):
    vuelos.test_tarjeta_fecha(mes, year)


@step('ingreso el nombre de la tarjeta "{nombre}" apellido "{apellido}"')
def step_impl(context, nombre, apellido):
    vuelos.test_tarjeta_nombre(nombre, apellido)


@step('ingreso la direccion de facturacion "{direccion}"')
def step_impl(context, direccion):
    vuelos.test_direccion_facturacion(direccion)


@step('ingreso la ciudad de facturacion "{ciudad}')
def step_impl(context, ciudad):
    vuelos.test_ciudad_facturacion(ciudad)

@step('ingreso el estado de facturacion "{estado}"')
def step_impl(context, estado):
    vuelos.test_estado_facturacion(estado)


@step('ingreso el codigo postal de facturacion "{numero}"')
def step_impl(context, numero):
    vuelos.test_codigo_postal_facturacion(numero)


@step('ingreso el pais de facturacion "{pais}"')
def step_impl(context, pais):
    vuelos.test_estado_facturacion(pais)


@step("selecciono la opcion de entrega como la misma de facturacion")
def step_impl(context):
    vuelos.test_entrega()


@step("envio el formulario de compra")
def step_impl(context):
    vuelos.test_enviar_datos()


@then("El sistema me retorna la verificacion de la reserva")
def step_impl(context):
    vuelos.test_validar_reserva()
