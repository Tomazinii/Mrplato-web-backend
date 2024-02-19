import datetime
import uuid

from ..value_object import ListProblem
from unittest.mock import Mock
from .problem import Problem
from .problem import PropsProblemType

def test_create_problem_entity():
    props = PropsProblemType()

    props.id = str(uuid.uuid4())
    props.list_name = "list 01"
    props.comentary = "training list"
    lista = Mock()

    props.list_problem_input = ListProblem(list=lista)
    props.created_at = datetime.datetime.now()
    props.updated_at = datetime.datetime.now()
    entity = Problem(props)

    assert entity.get_list_name() == props.list_name
    # assert entity.get_list_problem() == props.list_problem_input
    assert entity.get_id() == props.id
    assert entity.get_comentary() == props.comentary
    assert entity.get_created_at() == props.created_at
    assert entity.get_updated_at() == props.updated_at
