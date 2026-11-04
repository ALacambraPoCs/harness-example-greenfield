def total(lines: list[tuple[int, float]], descuento: float = 0, iva: float = 0) -> float:
    """Suma cantidad × precio de cada línea, aplica el descuento porcentual (0–100) y,
    después, el IVA porcentual (≥ 0). Redondea a 2 decimales.
    Rechaza cantidades y precios negativos, descuentos fuera de 0–100 e IVA negativo."""
    for n, (q, p) in enumerate(lines, start=1):
        if q < 0:
            raise ValueError(f"Cantidad negativa en la línea {n}: {q}")
        if p < 0:
            raise ValueError(f"Precio negativo en la línea {n}: {p}")
    if not 0 <= descuento <= 100:
        raise ValueError(f"Descuento fuera de rango (0–100): {descuento}")
    if iva < 0:
        raise ValueError(f"IVA negativo: {iva}")
    subtotal = sum(q * p for q, p in lines)
    con_descuento = subtotal * (1 - descuento / 100)
    return round(con_descuento * (1 + iva / 100), 2)
