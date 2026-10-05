from dataclasses import dataclass


PRECOS_QUARTOS: dict[str, float] = {
    "standard": 200.00,
    "luxo": 350.00,
    "suite": 500.00,
}

DESCONTOS_CUPONS: dict[str, float] = {
    "HOTEL10": 0.10,
    "HOTEL20": 0.20,
}


@dataclass(frozen=True)
class Reserva:
    adultos: int
    criancas: int
    noites: int
    tipo_quarto: str
    cupom: str | None = None


def _validar_tipos(reserva: Reserva) -> None:
    if type(reserva.adultos) is not int:
        raise TypeError("A quantidade de adultos deve ser um número inteiro.")

    if type(reserva.criancas) is not int:
        raise TypeError("A quantidade de crianças deve ser um número inteiro.")

    if type(reserva.noites) is not int:
        raise TypeError("A quantidade de noites deve ser um número inteiro.")

    if not isinstance(reserva.tipo_quarto, str):
        raise TypeError("O tipo de quarto deve ser uma string.")

    if reserva.cupom is not None:
        if not isinstance(reserva.cupom, str):
            raise TypeError("O cupom deve ser uma string ou None.")


def calcular_reserva(reserva: Reserva) -> float:
    """Valida uma reserva e calcula o valor total da hospedagem."""

    if not isinstance(reserva, Reserva):
        raise TypeError("O objeto informado deve ser uma Reserva.")

    _validar_tipos(reserva)

    if reserva.adultos < 1:
        raise ValueError("A reserva deve possuir pelo menos 1 adulto.")

    if reserva.criancas < 0:
        raise ValueError("A quantidade de crianças não pode ser negativa.")

    if reserva.criancas > 4:
        raise ValueError("A reserva pode possuir no máximo 4 crianças.")

    if reserva.noites < 1:
        raise ValueError("A reserva deve possuir pelo menos 1 noite.")

    if reserva.noites > 30:
        raise ValueError("A reserva pode possuir no máximo 30 noites.")

    if reserva.tipo_quarto not in PRECOS_QUARTOS:
        raise ValueError("Tipo de quarto inválido.")

    if reserva.cupom is not None:
        if reserva.cupom not in DESCONTOS_CUPONS:
            raise ValueError("Cupom inválido.")

    valor_diaria = PRECOS_QUARTOS[reserva.tipo_quarto]
    valor_diaria += reserva.criancas * 50.00

    valor_total = valor_diaria * reserva.noites

    if reserva.cupom is not None:
        desconto = DESCONTOS_CUPONS[reserva.cupom]
        valor_total *= 1 - desconto

    return round(valor_total, 2)