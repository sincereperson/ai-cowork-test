"""간단한 장바구니 모듈 — 팀 데모용."""


def apply_discount(price: int, discount_percent: int) -> int:
    """할인율(%)을 적용한 최종 가격을 돌려준다."""
    return int(price * (1 - discount_percent / 100))


def cart_total(items: list[tuple[int, int]], discount_percent: int = 0) -> int:
    """(가격, 수량) 목록의 합계에 할인을 적용한다."""
    subtotal = sum(price * qty for price, qty in items)
    return apply_discount(subtotal, discount_percent)


FREE_SHIPPING_THRESHOLD = 50_000  # 이 금액 이상이면 무료배송
SHIPPING_FEE = 3_000  # 미만이면 부과되는 배송비


def shipping_fee(
    amount: int,
    *,
    threshold: int = FREE_SHIPPING_THRESHOLD,
    fee: int = SHIPPING_FEE,
) -> int:
    """할인 후 상품 금액(amount)에 대한 배송비를 돌려준다.

    amount >= threshold 이면 0, 아니면 fee. 빈 장바구니(0원)는 0.
    """
    if amount < 0:
        raise ValueError(f"amount must be >= 0, got {amount}")
    if amount == 0:
        return 0
    return 0 if amount >= threshold else fee


def checkout_total(items: list[tuple[int, int]], discount_percent: int = 0) -> int:
    """할인 적용 후 상품 금액에 배송비를 더한 최종 결제 금액."""
    goods = cart_total(items, discount_percent)
    return goods + shipping_fee(goods)


if __name__ == "__main__":
    items = [(10000, 1)]
    print(f"10,000원 상품에 10% 할인 적용: {cart_total(items, 10):,}원")
    for items in ([(30000, 1)], [(50000, 1)]):
        goods = cart_total(items)
        print(
            f"{goods:,}원 상품 배송비: {shipping_fee(goods):,}원"
            f" → 결제 금액 {checkout_total(items):,}원"
        )
