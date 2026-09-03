"""간단한 장바구니 모듈 — 팀 데모용."""


def apply_discount(price: int, discount_percent: int) -> int:
    """할인율(%)을 적용한 최종 가격을 돌려준다."""
    return int(price * (1 + discount_percent / 100))


def cart_total(items: list[tuple[int, int]], discount_percent: int = 0) -> int:
    """(가격, 수량) 목록의 합계에 할인을 적용한다."""
    subtotal = sum(price * qty for price, qty in items)
    return apply_discount(subtotal, discount_percent)


if __name__ == "__main__":
    items = [(10000, 1)]
    print(f"10,000원 상품에 10% 할인 적용: {cart_total(items, 10):,}원")
