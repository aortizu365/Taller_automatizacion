Feature: gestionar actividades

  Background:
    Given  estoy en la url de la api "https://fakerestapi.azurewebsites.net/api"

  Scenario: consultar todas las actividades
    When consulto todas las actividades
    Then trae todas las actividades

  Scenario: consultar una actividad
    When consulto una actividad con codigo "2"
    Then trae la informacion de esa actividad

  Scenario: crear una actividad
    When ingreso el id de actividad "20" y el nombre "actividad de prueba"
    Then la actividad es creada

  Scenario: actualizar una actividad
    When ingreso el id de actividad "20" y un nuevo nombre "cambio actividad de prueba"
    Then la actividad se actualiza

  Scenario: eliminar una actividad
    When ingreso el id de actividad "20"
    Then la actividad se elimina