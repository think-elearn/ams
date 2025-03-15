import pytest

from .factories import BlueprintFactory
from .factories import CategoryFactory
from .factories import LearningObjectiveFactory
from .factories import SubcategoryFactory


@pytest.mark.django_db
class TestBlueprintModel:
    def test_str_method(self):
        blueprint = BlueprintFactory(version="1.0")
        assert str(blueprint) == "1.0"


@pytest.mark.django_db
class TestCategoryModel:
    def test_str_method(self):
        category = CategoryFactory(short_name="Cat1")
        assert str(category) == "Cat1"


@pytest.mark.django_db
class TestSubcategoryModel:
    def test_str_method(self):
        subcategory = SubcategoryFactory(name="Subcategory 1")
        assert str(subcategory) == "Subcategory 1"


@pytest.mark.django_db
class TestLearningObjectiveModel:
    def test_str_method(self):
        learning_objective = LearningObjectiveFactory(
            text="Understand the basics of testing",
        )
        assert str(learning_objective) == "Understand the basics of testing"
