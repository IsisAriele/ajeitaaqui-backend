import unittest
from unittest.mock import MagicMock

from apps.domain.entities.proposal import Proposal
from apps.domain.usecases.list_client_proposals_use_case import ListClientProposalsUseCase


class TestListClientProposalsUseCase(unittest.TestCase):
    def test_list_client_proposals_returns_all(self):
        mock_proposal_repository = MagicMock()
        mock_client_repository = MagicMock()
        proposals = [
            Proposal(
                id=1,
                client=MagicMock(id=1),
                professional=MagicMock(id=2),
                services=[],
                value=100.0,
                scheduled_datetime="2025-07-12T10:00:00Z",
            ),
            Proposal(
                id=2,
                client=MagicMock(id=1),
                professional=MagicMock(id=3),
                services=[],
                value=200.0,
                scheduled_datetime="2025-07-13T10:00:00Z",
            ),
        ]
        mock_proposal_repository.list_proposals_by_client.return_value = proposals
        mock_client_repository.get.return_value = MagicMock(id=1)
        use_case = ListClientProposalsUseCase(mock_proposal_repository, mock_client_repository)
        result = use_case.list_all(client_id=1)
        self.assertEqual(result, proposals)
        mock_proposal_repository.list_proposals_by_client.assert_called_once_with(1)
        mock_client_repository.get.assert_called_once_with(1)
