import factory
from factory.django import DjangoModelFactory

from ams.apps.blueprint.tests.factories import LearningObjectiveFactory
from ams.apps.items.models import Choice
from ams.apps.items.models import Item
from ams.apps.items.models import Question
from ams.apps.users.tests.factories import UserFactory


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    text = factory.Faker("sentence", nb_words=10)
    type = Question.Type.STANDARD


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    text = factory.Faker("sentence", nb_words=5)
    question = factory.SubFactory(QuestionFactory)
    is_correct = False


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    stem = factory.SubFactory(QuestionFactory)
    status = Item.Status.DRAFT
    rationale = factory.Faker("paragraph")
    learning_objective = factory.SubFactory(LearningObjectiveFactory)
    author = factory.SubFactory(UserFactory)
    estimated_p_value = 0.85
    p_value = None
    legacy_id = None
