import pytest
from Checkout import Checkout


@pytest.fixture()
def checkoutcall():
    co = Checkout()
    co.addItemPrice("a", 1)
    co.addItemPrice("b", 2)
    return co


def test_CanCalculateTotal(checkoutcall):
    checkoutcall.addItem("a")
    assert checkoutcall.calculateTotal() == 1


def test_GetCorrectTotalWithMultipleItems(checkoutcall):

    checkoutcall.addItem("a")
    checkoutcall.addItem("b")
    assert checkoutcall.calculateTotal() == 3

def test_canAddDiscountRules(checkoutcall):
    checkoutcall.addDiscount("a", 3, 2)

#@pytest.mark.skip
def test_CanApplyDiscountRules(checkoutcall):
    checkoutcall.addDiscount("a", 3, 2)
    checkoutcall.addItem("a")
    checkoutcall.addItem("a")
    checkoutcall.addItem("a")
    assert checkoutcall.calculateTotal() == 2

def test_ExceptionWithBadItem(checkoutcall):
    with pytest.raises(Exception):
        checkoutcall.addItem("c")

