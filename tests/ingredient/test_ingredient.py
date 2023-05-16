from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    flour = Ingredient("farinha")

    assert isinstance(flour, Ingredient)
    assert flour.name == "farinha"
    assert flour.__eq__(Ingredient("carne")) is False
    assert flour.__eq__(Ingredient("farinha"))
    assert flour.__repr__() == "Ingredient('farinha')"
    assert hash(flour) == hash(Ingredient("farinha"))
    assert hash(flour) != hash(Ingredient("carne"))
    assert flour.restrictions == {Restriction.GLUTEN}
