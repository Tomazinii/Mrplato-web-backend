

from unittest.mock import Mock


def test_get_invite_usecase():

    repository = Mock()
    usecase = GetInviteUsecase(repository=repository)

    result = usecase.execute()