import pytest

from pdc_ams.apps.blueprint.tests.factories import LearningObjectiveFactory

from .factories import ChoiceFactory
from .factories import ItemFactory
from .factories import QuestionFactory


@pytest.mark.django_db
def test_question_str():
    question = QuestionFactory(
        text="This is a test question that is quite long and should be truncated.",
    )
    assert str(question) == "This is a test question that is quite long"


@pytest.mark.django_db
def test_choice_str():
    question = QuestionFactory(text="Sample question")
    choice = ChoiceFactory(
        text="This is a test choice that is quite long and should be truncated.",
        question=question,
    )
    assert str(choice) == "This is a test choice"


@pytest.mark.django_db
def test_item_str(user):
    learning_objective = LearningObjectiveFactory()
    question = QuestionFactory(text="This is a test question for item")
    item = ItemFactory(
        stem=question,
        rationale="Sample rationale",
        learning_objective=learning_objective,
        author=user,
    )
    assert str(item) == "This is a test question for item"
