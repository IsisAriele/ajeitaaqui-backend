import unittest
from unittest.mock import MagicMock

from apps.domain.entities.proposal import Proposal
from apps.domain.exceptions.proposal_exceptions import ProposalException
from apps.domain.usecases.create_proposal_use_case import CreateProposalUseCase


class TestCreateProposalUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_proposal_repository = MagicMock()
        self.mock_client_repository = MagicMock()
        self.mock_professional_repository = MagicMock()
        self.mock_service_repository = MagicMock()
        self.use_case = CreateProposalUseCase(
            self.mock_proposal_repository,
            self.mock_client_repository,
            self.mock_professional_repository,
            self.mock_service_repository,
        )

    def test_create_proposal_success(self):
        proposal = Proposal(
            id=1,
            client=MagicMock(id=1),
            professional=MagicMock(id=2),
            services=[10, 20],
            value=100.0,
            scheduled_datetime="2025-07-12T10:00:00Z",
        )
        client_obj = MagicMock(id=1)
        professional_obj = MagicMock(id=2)
        service_obj_1 = MagicMock(id=10)
        service_obj_2 = MagicMock(id=20)
        self.mock_client_repository.get.return_value = client_obj
        self.mock_professional_repository.get_by_id.return_value = professional_obj
        self.mock_service_repository.get_by_id.side_effect = [service_obj_1, service_obj_2]
        self.mock_proposal_repository.create.return_value = proposal

        result = self.use_case.create_proposal(proposal)

        self.mock_client_repository.get.assert_called_once_with(1)
        self.mock_professional_repository.get_by_id.assert_called_once_with(2)
        self.assertEqual(self.mock_service_repository.get_by_id.call_count, 2)
        self.mock_service_repository.get_by_id.assert_any_call(10)
        self.mock_service_repository.get_by_id.assert_any_call(20)
        self.mock_proposal_repository.create.assert_called_once()
        self.assertEqual(result, proposal)
        self.assertEqual(proposal.client, client_obj)
        self.assertEqual(proposal.professional, professional_obj)
        self.assertEqual(proposal.services, [service_obj_1, service_obj_2])

    def test_create_proposal_repository_error(self):
        proposal = Proposal(
            id=1,
            client=MagicMock(id=1),
            professional=MagicMock(id=2),
            services=[10],
            value=100.0,
            scheduled_datetime="2025-07-12T10:00:00Z",
        )
        self.mock_client_repository.get.return_value = MagicMock(id=1)
        self.mock_professional_repository.get_by_id.return_value = MagicMock(id=2)
        self.mock_service_repository.get_by_id.return_value = MagicMock(id=10)
        self.mock_proposal_repository.create.side_effect = Exception("Erro ao criar proposta")
        with self.assertRaises(Exception) as exc:
            self.use_case.create_proposal(proposal)
        self.assertIn("Erro ao criar proposta", str(exc.exception))

    def test_create_proposal_client_not_found(self):
        proposal = Proposal(
            id=1,
            client=MagicMock(id=1),
            professional=MagicMock(id=2),
            services=[10],
            value=100.0,
            scheduled_datetime="2025-07-12T10:00:00Z",
        )
        self.mock_client_repository.get.side_effect = Exception("Cliente não encontrado")
        with self.assertRaises(ProposalException) as exc:
            self.use_case.create_proposal(proposal)
        self.assertIn("Cliente não encontrado", str(exc.exception))

    def test_create_proposal_professional_not_found(self):
        proposal = Proposal(
            id=1,
            client=MagicMock(id=1),
            professional=MagicMock(id=2),
            services=[10],
            value=100.0,
            scheduled_datetime="2025-07-12T10:00:00Z",
        )
        self.mock_client_repository.get.return_value = MagicMock(id=1)
        self.mock_professional_repository.get_by_id.side_effect = Exception("Profissional não encontrado")
        with self.assertRaises(ProposalException) as exc:
            self.use_case.create_proposal(proposal)
        self.assertIn("Profissional não encontrado", str(exc.exception))

    def test_create_proposal_service_not_found(self):
        proposal = Proposal(
            id=1,
            client=MagicMock(id=1),
            professional=MagicMock(id=2),
            services=[10, 20],
            value=100.0,
            scheduled_datetime="2025-07-12T10:00:00Z",
        )
        self.mock_client_repository.get.return_value = MagicMock(id=1)
        self.mock_professional_repository.get_by_id.return_value = MagicMock(id=2)
        self.mock_service_repository.get_by_id.side_effect = [MagicMock(id=10), Exception("Serviço não encontrado")]
        with self.assertRaises(ProposalException) as exc:
            self.use_case.create_proposal(proposal)
        self.assertIn("Serviço não encontrado", str(exc.exception))
