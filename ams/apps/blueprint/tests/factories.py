import factory
from factory.django import DjangoModelFactory

from ams.apps.blueprint.models import Blueprint
from ams.apps.blueprint.models import Category
from ams.apps.blueprint.models import LearningObjective
from ams.apps.blueprint.models import Subcategory


class BlueprintFactory(DjangoModelFactory):
    class Meta:
        model = Blueprint

    version = factory.Faker("word")


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")
    short_name = factory.Faker("word")
    blueprint = factory.SubFactory(BlueprintFactory)


class SubcategoryFactory(DjangoModelFactory):
    class Meta:
        model = Subcategory

    name = factory.Faker("word")
    category = factory.SubFactory(CategoryFactory)
    items_per_form = factory.Faker("random_int", min=1, max=100)


class LearningObjectiveFactory(DjangoModelFactory):
    class Meta:
        model = LearningObjective

    reference = factory.Faker("bothify", text="?.?.?")
    text = factory.Faker("sentence", nb_words=10)
    subcategory = factory.SubFactory(SubcategoryFactory)
    bloom_level = factory.Faker(
        "random_element",
        elements=[level[0] for level in LearningObjective.BloomLevel.choices],
    )
