"""
Suíte de testes unitários — Sistema de Reserva de Hotel

Técnicas aplicadas:
  - EP  : Particionamento de Equivalência
  - BVA : Análise do Valor Limite
  - EG  : Error Guessing
"""

import pytest

from app.reserva import Reserva, calcular_reserva


pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# RN01 — Adultos inválidos
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "adultos",
    [
        0,    # BVA - exatamente abaixo do mínimo
        -1,   # EG  - valor negativo
        -100, # EG  - valor muito negativo
    ],
)
def test_rejeita_adultos_invalidos(adultos: int) -> None:
    # Arrange
    reserva = Reserva(adultos=adultos, criancas=0, noites=1, tipo_quarto="standard")

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_reserva(reserva)


# ---------------------------------------------------------------------------
# RN01 — Adultos válidos
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "adultos",
    [
        1,  # BVA - limite inferior válido
        2,  # EP  - valor representativo
        10, # EP  - valor alto, ainda válido
    ],
)
def test_aceita_adultos_validos(adultos: int) -> None:
    # Arrange
    reserva = Reserva(adultos=adultos, criancas=0, noites=1, tipo_quarto="standard")

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(200.00)


# ---------------------------------------------------------------------------
# RN02 — Crianças inválidas
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "criancas",
    [
        -1,  # BVA - imediatamente abaixo do limite inferior
        -5,  # EG  - negativo representativo
        5,   # BVA - imediatamente acima do limite superior
        10,  # EP  - valor inválido alto
    ],
)
def test_rejeita_criancas_invalidas(criancas: int) -> None:
    # Arrange
    reserva = Reserva(adultos=1, criancas=criancas, noites=1, tipo_quarto="standard")

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_reserva(reserva)


# ---------------------------------------------------------------------------
# RN02 + RN05 — Crianças válidas e adicional de R$50 por criança
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "criancas, valor_esperado",
    [
        (0, 200.00),  # BVA - limite inferior, sem adicional
        (1, 250.00),  # EP  - uma criança, +R$50
        (4, 400.00),  # BVA - limite superior, +R$200
    ],
)
def test_aceita_criancas_validas_e_calcula_adicional(
    criancas: int, valor_esperado: float
) -> None:
    # Arrange
    reserva = Reserva(adultos=1, criancas=criancas, noites=1, tipo_quarto="standard")

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(valor_esperado)


# ---------------------------------------------------------------------------
# RN03 — Noites inválidas
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "noites",
    [
        0,   # BVA - exatamente abaixo do mínimo
        -1,  # EG  - valor negativo
        31,  # BVA - imediatamente acima do limite superior
        100, # EP  - valor inválido alto
    ],
)
def test_rejeita_noites_invalidas(noites: int) -> None:
    # Arrange
    reserva = Reserva(adultos=1, criancas=0, noites=noites, tipo_quarto="standard")

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_reserva(reserva)


# ---------------------------------------------------------------------------
# RN03 + RN05 — Noites válidas e cálculo do total
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "noites, valor_esperado",
    [
        (1,  200.00),  # BVA - limite inferior
        (15, 3000.00), # EP  - valor intermediário
        (30, 6000.00), # BVA - limite superior
    ],
)
def test_aceita_noites_validas_e_calcula_total(
    noites: int, valor_esperado: float
) -> None:
    # Arrange
    reserva = Reserva(adultos=1, criancas=0, noites=noites, tipo_quarto="standard")

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(valor_esperado)


# ---------------------------------------------------------------------------
# RN04 — Tipos de quarto válidos
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "tipo_quarto, valor_esperado",
    [
        ("standard", 200.00),
        ("luxo",     350.00),
        ("suite",    500.00),
    ],
)
def test_aceita_tipos_de_quarto_validos(
    tipo_quarto: str, valor_esperado: float
) -> None:
    # Arrange
    reserva = Reserva(adultos=1, criancas=0, noites=1, tipo_quarto=tipo_quarto)

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(valor_esperado)


# ---------------------------------------------------------------------------
# RN04 — Tipos de quarto inválidos
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "tipo_quarto",
    [
        "economico",  # EP  - valor inexistente
        "",           # EG  - string vazia
        "STANDARD",   # EG  - maiúsculas
        "Luxo",       # EG  - capitalização parcial
        "suite ",     # EG  - espaço extra no final
    ],
)
def test_rejeita_tipo_de_quarto_invalido(tipo_quarto: str) -> None:
    # Arrange
    reserva = Reserva(adultos=1, criancas=0, noites=1, tipo_quarto=tipo_quarto)

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_reserva(reserva)


# ---------------------------------------------------------------------------
# RN05 — Cálculo do valor total (cenários combinados)
# ---------------------------------------------------------------------------


def test_calcula_valor_total_luxo_sem_criancas() -> None:
    # Arrange
    reserva = Reserva(adultos=2, criancas=0, noites=5, tipo_quarto="luxo")

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(1750.00)


def test_calcula_valor_total_standard_com_duas_criancas() -> None:
    # Arrange
    reserva = Reserva(adultos=2, criancas=2, noites=3, tipo_quarto="standard")

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(900.00)


def test_calcula_valor_total_suite_com_quatro_criancas() -> None:
    # Arrange
    reserva = Reserva(adultos=2, criancas=4, noites=2, tipo_quarto="suite")

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(1400.00)


# ---------------------------------------------------------------------------
# RN06 — Cupons válidos
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "cupom, valor_esperado",
    [
        (None,      1000.00), # EP  - sem cupom, valor cheio
        ("HOTEL10",  900.00), # EP  - 10% de desconto
        ("HOTEL20",  800.00), # EP  - 20% de desconto
    ],
)
def test_aplica_cupom_corretamente(
    cupom: str | None, valor_esperado: float
) -> None:
    # Arrange
    reserva = Reserva(
        adultos=2, criancas=0, noites=5, tipo_quarto="standard", cupom=cupom
    )

    # Act
    resultado = calcular_reserva(reserva)

    # Assert
    assert resultado == pytest.approx(valor_esperado)


# ---------------------------------------------------------------------------
# RN06 — Cupons inválidos
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "cupom",
    [
        "",          # EG  - string vazia
        "HOTEL30",   # EG  - desconto inexistente
        "hotel10",   # EG  - case diferente
        "INVALIDO",  # EP  - valor aleatório inválido
    ],
)
def test_rejeita_cupom_invalido(cupom: str) -> None:
    # Arrange
    reserva = Reserva(
        adultos=1, criancas=0, noites=1, tipo_quarto="standard", cupom=cupom
    )

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_reserva(reserva)


# ---------------------------------------------------------------------------
# Validação de tipos — Error Guessing
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "campo, valor",
    [
        ("adultos",     "2"),   # EG - string no lugar de int
        ("adultos",     2.0),   # EG - float no lugar de int
        ("criancas",    "1"),   # EG - string no lugar de int
        ("noites",      True),  # EG - bool (rejeitado por type() is not int)
        ("tipo_quarto", 123),   # EG - int no lugar de str
        ("cupom",       99),    # EG - int no lugar de str/None
    ],
)
def test_rejeita_tipos_de_dados_invalidos(campo: str, valor: object) -> None:
    # Arrange
    dados: dict[str, object] = {
        "adultos": 1,
        "criancas": 0,
        "noites": 1,
        "tipo_quarto": "standard",
        "cupom": None,
    }
    dados[campo] = valor
    reserva = Reserva(**dados)  # type: ignore[arg-type]

    # Act / Assert
    with pytest.raises(TypeError):
        calcular_reserva(reserva)


@pytest.mark.parametrize(
    "objeto",
    [
        "string qualquer",
        None,
        42,
        {"adultos": 1},
    ],
)
def test_rejeita_objeto_que_nao_e_reserva(objeto: object) -> None:
    # Arrange / Act / Assert
    with pytest.raises(TypeError):
        calcular_reserva(objeto)  # type: ignore[arg-type]
