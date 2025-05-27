from django.core.management.base import BaseCommand

from apps.infrastructure.models import CategoryModel, PlanModel, ServiceModel


class Command(BaseCommand):
    help = "Popula o banco de dados com dados iniciais para categorias, serviços e planos"

    def handle(self, *args, **options):
        # Categorias e serviços correspondentes
        categories_services = {
            "Hidráulico": [
                "Conserto de vazamentos",
                "Instalação de torneiras",
                "Desentupimento de pias",
            ],
            "Elétrico": [
                "Instalação de tomadas",
                "Manutenção de fiação elétrica",
                "Troca de disjuntores",
            ],
            "Alvenaria": [
                "Reforma de paredes",
                "Assentamento de pisos",
                "Construção de muros",
            ],
            "Limpeza": [
                "Limpeza residencial",
                "Limpeza pós-obra",
                "Limpeza de vidros",
            ],
            "Ar-condicionado": [
                "Instalação de ar-condicionado",
                "Manutenção preventiva",
                "Recarga de gás",
            ],
            "Instalação": [
                "Instalação de chuveiros",
                "Montagem de móveis",
                "Instalação de suportes de TV",
            ],
            "Telecomunicação": [
                "Instalação de roteadores",
                "Configuração de redes Wi-Fi",
                "Passagem de cabos de rede",
            ],
            "Pintura": [
                "Pintura interna",
                "Pintura externa",
                "Texturização de paredes",
            ],
        }

        # Criar categorias e serviços
        for category_desc, services in categories_services.items():
            category = CategoryModel.objects.create(description=category_desc)
            for service_desc in services:
                ServiceModel.objects.create(description=service_desc, category=category)

        # Criar planos
        PlanModel.objects.create(name="Plano Ouro", description="Visibilidade padrão", value=89.90)
        PlanModel.objects.create(name="Plano Prata", description="Maior destaque nas buscas", value=59.90)
        PlanModel.objects.create(name="Plano Bronze", description="Impulsionamento máximo", value=29.90)

        self.stdout.write(self.style.SUCCESS("Dados populados com sucesso!"))
