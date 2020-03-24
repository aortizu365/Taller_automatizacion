Feature: gestionar libros

  Background:
    Given  estoy en la url de la api de libros "https://fakerestapi.azurewebsites.net/api"

  Scenario: consultar todos los libros
    When consulto todos los libros
    Then trae todos los libros

  Scenario: consultar un libro
    When consulto un libro con codigo "1"
    Then trae la informacion de ese libro

  Scenario: crear un libro
    When ingreso el id del libro "20" y el nombre "el quijote"
    Then el libro es creado

  Scenario: actualizar un autor
    When ingreso el id del libro "20" y un nuevo nombre "el quijote de la mancha"
    Then el libro se actualiza

  Scenario: eliminar un libro
    When ingreso el id de libro "20"
    Then el libro se elimina