import unittest
from unittest.mock import MagicMock

from apps.domain.entities.proposal import Proposal
from apps.domain.usecases.reject_proposal_use_case import RejectProposalUseCase


class TestRejectProposalUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_proposal_repository = MagicMock()
        self.client = MagicMock(id=123)
        self.mock_client_repository = MagicMock()
        self.mock_client_repository.get.return_value = self.client
        self.proposal = Proposal(
            id=1,
            client=123,
            professional=MagicMock(id=2),
            services=[],
            value=100.0,
            scheduled_datetime="2025-07-12T10:00:00Z",
        )

        self.use_case = RejectProposalUseCase(self.mock_proposal_repository, self.mock_client_repository)

    def test_reject_proposal_success(self):
        self.use_case.reject(self.client.id, self.proposal.id)
        self.mock_client_repository.get(self.proposal.id)
        self.mock_proposal_repository.reject_proposal.assert_called_once_with(self.client.id, self.proposal.id)
