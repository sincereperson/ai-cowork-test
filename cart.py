"""媛꾨떒???λ컮援щ땲 紐⑤뱢 ??? ?곕え??"""


def apply_discount(price: int, discount_percent: int) -> int:
    """?좎씤??%)???곸슜??理쒖쥌 媛寃⑹쓣 ?뚮젮以??"""
    return int(price * (1 + discount_percent / 100))


def cart_total(items: list[tuple[int, int]], discount_percent: int = 0) -> int:
    """(媛寃? ?섎웾) 紐⑸줉???⑷퀎???좎씤???곸슜?쒕떎."""
    subtotal = sum(price * qty for price, qty in items)
    return apply_discount(subtotal, discount_percent)


if __name__ == "__main__":
    items = [(10000, 1)]
    print(f"10,000???곹뭹??10% ?좎씤 ?곸슜: {cart_total(items, 10):,}??)
