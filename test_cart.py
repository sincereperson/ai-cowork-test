import pytest

from cart import apply_discount, cart_total, checkout_total, shipping_fee


def test_apply_discount_10_percent():
    assert apply_discount(10000, 10) == 9000


def test_apply_discount_zero():
    assert apply_discount(5000, 0) == 5000


def test_cart_total_with_discount():
    items = [(10000, 2), (5000, 1)]
    assert cart_total(items, 20) == 20000


# --- shipping_fee 단위 테스트 (설계서 S1~S9) ---


@pytest.mark.parametrize(
    "amount, expected",
    [
        (0, 0),  # S1 빈 장바구니
        (1, 3000),  # S2 최소 양수
        (49_999, 3000),  # S3 경계 바로 아래
        (50_000, 0),  # S4 "이상" 경계 포함
        (50_001, 0),  # S5 경계 바로 위
        (1_000_000, 0),  # S6 큰 금액
    ],
)
def test_shipping_fee(amount, expected):
    assert shipping_fee(amount) == expected


def test_shipping_fee_negative_raises():  # S7
    with pytest.raises(ValueError):
        shipping_fee(-1)


@pytest.mark.parametrize(
    "amount, expected",
    [
        (30_000, 0),  # S8
        (10_000, 2500),  # S9
    ],
)
def test_shipping_fee_custom_policy(amount, expected):
    assert shipping_fee(amount, threshold=20_000, fee=2500) == expected


# --- checkout_total 통합 테스트 (설계서 C1~C11) ---

@pytest.mark.parametrize(
    "items, discount_percent, expected",
    [
        ([], 0, 0),  # C1 빈 장바구니
        ([(10_000, 1)], 0, 13_000),  # C2 기본 유료
        ([(49_999, 1)], 0, 52_999),  # C3 경계 아래
        ([(50_000, 1)], 0, 50_000),  # C4 경계 정확히
        ([(25_000, 2)], 0, 50_000),  # C5 수량 곱 후 경계
        ([(20_000, 1), (30_000, 1)], 0, 50_000),  # C6 복수 품목 합산
        ([(55_000, 1)], 10, 52_500),  # C7 할인 후 기준 핵심 (할인 전 기준이면 무료가 됨)
        ([(60_000, 1)], 10, 54_000),  # C8 할인 후에도 무료
        ([(55_555, 1)], 10, 52_999),  # C10 int 절삭(49,999)이 경계 판정에 미치는 영향 고정
        ([(100_000, 1)], 50, 50_000),  # C11 할인으로 정확히 경계 도달
    ],
)
def test_checkout_total(items, discount_percent, expected):
    assert checkout_total(items, discount_percent) == expected


def test_checkout_total_default_discount():  # C9 discount_percent 기본값 경로에서 경계 유지
    assert checkout_total([(50_000, 1)]) == 50_000
