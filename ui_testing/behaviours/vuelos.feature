Feature: seleccionar vuelo en Mercury Tours

  Scenario: Buscar vuelos desde una ciudad a otra
    Given Estoy en la pagina de Mercury Tours para seleccionar vuelo
    When Hago Login con usuario "aortizu" y password "abc123"
    And selecciono un trayecto One way
    And selecciono "3" pasajeros
    And selecciono salida desde "London"
    And selecciono la fecha de partida en "April" "31"
    And selecciono el destino como "Portland"
    And selecciono el retorno en "May" "20"
    And selecciono la clase Business
    And selecciono la aerolinea "Unified Airlines"
    Then  envio el formulario de busqueda de vuelo

  Scenario: Seleccionar vuelos
    Given que he buscado un vuelo y estoy en la pagina de resultados
    And selecciono el vuelo de ida mas costoso
    And selecciono el vuelo de retorno mas costoso
    Then envio las seleccion de vuelos

  Scenario: Realiza reserva de vuelos
    Given que he seleccionado un vuelo de ida y vuelta
    And ingreso la informacion del pasajero "1" con nombre "Juan" apellido "Perez" y selecciono la opcion  de comida "Hindu"
    And ingreso la informacion del pasajero "2" con nombre "Maria" apellido "Gonzalez" y selecciono la opcion  de comida "Diabetic"
    And ingreso la informacion del pasajero "3" con nombre "Pedro" apellido "Marin" y selecciono la opcion  de comida "Vegetarian"
    And selecciono la opcion de tarjeta "Visa"
    And ingreso el numero de tarjeta "123456789"
    And ingreso la fecha de expiracion de la tarjeta mes "10" year "2009"
    And ingreso el nombre de la tarjeta "Juan" apellido "Perez"
    And ingreso la direccion de facturacion "Calle 123"
    And ingreso la ciudad de facturacion "New York"
    And ingreso el estado de facturacion "NY"
    And ingreso el codigo postal de facturacion "0011"
    And ingreso el pais de facturacion "UNITED STATES"
    And selecciono la opcion de entrega como la misma de facturacion
    And envio el formulario de compra
    Then El sistema me retorna la verificacion de la reserva