import unittest
from unittest.mock import MagicMock

from apps.domain.usecases.accept_proposal_use_case import AcceptProposalUseCase


class TestAcceptProposalUseCase(unittest.TestCase):
    def setUp(self):
        self.client_user = MagicMock(id=1)
        self.proposal = MagicMock(id=99)
        self.mock_client_repository = MagicMock()
        self.mock_proposal_repository = MagicMock()
        self.mock_client_repository.get.return_value = self.client_user
        self.mock_proposal_repository.get.return_value = self.proposal
        self.mock_payment_repository = MagicMock()
        self.use_case = AcceptProposalUseCase(
            self.mock_proposal_repository, self.mock_payment_repository, self.mock_client_repository
        )

    def test_accept_proposal_success(self):
        self.use_case.accept(self.client_user.id, self.proposal.id)
        self.mock_client_repository.get.assert_called_once_with(self.client_user.id)
        self.mock_proposal_repository.accept_proposal.assert_called_once_with(self.client_user.id, self.proposal.id)
        self.mock_payment_repository.create_payment.assert_called_once()
