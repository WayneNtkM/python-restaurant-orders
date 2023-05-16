from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    stroganoff = Dish("stroganoff", 22.00)

    stroganoff.add_ingredient_dependency(Ingredient("frango"), 1)

    assert stroganoff.name == "stroganoff"
    assert stroganoff.recipe == {Ingredient('frango'): 1}
    assert stroganoff.__eq__(Dish("feijoada", 25.00)) is False
    assert stroganoff.__eq__(Dish("stroganoff", 22.00))
    assert stroganoff.get_ingredients() == {Ingredient('frango')}
    assert stroganoff.get_restrictions() == Ingredient('frango').restrictions
    assert hash(stroganoff) == hash(Dish("stroganoff", 22.00))
    assert hash(stroganoff) != hash(Dish("stroganoff", 23.00))
    assert stroganoff.__repr__() == "Dish('stroganoff', R$22.00)"

    with pytest.raises(
        ValueError,
        match="Dish price must be greater then zero."
    ):
        Dish("stroganoff", -22)
