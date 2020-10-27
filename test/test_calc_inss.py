def test_calculo_inss():
  # Arrange
  salario = 3000
  expectativa = 3000 * 0.11 #aliquota inss 11%

  # Act
  from domain.logic import calculo_inss
  resultado = calculo_inss(salario)

  # Assert
  assert resultado == expectativa

def test_valor_pagar(salario, enquadramento):
  # Arrange
  salario = 0
  expectativa = 0

  # Act
  from domain.logic import calculo_inss
  resultado = calculo_inss(salario)

  # Assert
  assert resultado == expectativa
  