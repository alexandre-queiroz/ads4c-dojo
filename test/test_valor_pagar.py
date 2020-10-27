def test_valor_pagar():
    # Arrange
    salario = 0
    enquadramento = {'aliquota': 0.11}
    expectativa = 0

    # Act
    from domain.logic import valor_pagar
    resultado = valor_pagar(salario, enquadramento)

    # Assert
    assert resultado == expectativa
  