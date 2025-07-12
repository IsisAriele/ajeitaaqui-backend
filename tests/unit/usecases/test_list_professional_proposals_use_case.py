import unittest
from unittest.mock import MagicMock

from apps.domain.entities.proposal import Proposal
from apps.domain.usecases.list_professional_proposals_use_case import ListProfessionalProposalsUseCase


class TestListProfessionalProposalsUseCase(unittest.TestCase):
    def test_list_professional_proposals_returns_all(self):
        mock_proposal_repository = MagicMock()
        mock_professional_repository = MagicMock()
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
                client=MagicMock(id=3),
                professional=MagicMock(id=2),
                services=[],
                value=200.0,
                scheduled_datetime="2025-07-13T10:00:00Z",
            ),
        ]
        mock_professional_repository.get_by_id.return_value = MagicMock(id=10)
        mock_proposal_repository.list_proposals_by_professional.return_value = proposals
        use_case = ListProfessionalProposalsUseCase(mock_proposal_repository, mock_professional_repository)
        result = use_case.list_all(2)
        self.assertEqual(result, proposals)
        mock_professional_repository.get_by_id.assert_called_once_with(2)
        mock_proposal_repository.list_proposals_by_professional.assert_called_once_with(10)
