Feature: login en Mercury Tours

  Scenario: realizar login
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "aortizu" y un password "abc123"
    Then El sistema me autentica como usuario legitimo