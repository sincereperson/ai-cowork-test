from cart import apply_discount, cart_total


def test_apply_discount_10_percent():
    assert apply_discount(10000, 10) == 9000


def test_apply_discount_zero():
    assert apply_discount(5000, 0) == 5000


def test_cart_total_with_discount():
    items = [(10000, 2), (5000, 1)]
    assert cart_total(items, 20) == 20000
