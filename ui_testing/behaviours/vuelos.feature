Feature: seleccionar vuelo en Mercury Tours

  Scenario: consultar vuelos
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
    And envio el formulario
    Then El sistema me retorna vuelos