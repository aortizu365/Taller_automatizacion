Feature: gestionar autores

  Background:
    Given  estoy en la url de la api de autores "https://fakerestapi.azurewebsites.net/api"

  Scenario: consultar todos los autores
    When consulto todos los autores
    Then trae todos los autores

  Scenario: consultar un autor
    When consulto un autor con codigo "2"
    Then trae la informacion de ese autor

  Scenario: consultar libro de un autor
    When consulto un libro de un autor con id "1"
    Then trae la informacion del libro de ese autor

  Scenario: crear un autor
    When ingreso el id de autor "20" y el nombre "juan perez"
    Then el autor es creado

  Scenario: actualizar un autor
    When ingreso el id de autor "20" y un nuevo nombre "juan perez perez"
    Then el autor se actualiza

  Scenario: eliminar un autor
    When ingreso el id de autor "20"
    Then el autor se elimina