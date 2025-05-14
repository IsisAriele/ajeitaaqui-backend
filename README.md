# ajeitaaqui-backend
API do sistema Ajeita Aqui

Passo-a-passo para a criação da estrutura do projeto:
```bash
mkdir apps
django-admin startproject config apps
python manage.py startapp core
mv core apps
python manage.py startapp infrastructure
mv infrastructure apps 
python manage.py startapp api
mv api apps 
```

```
+---------------------------+
| 1. Enterprise Business Rules       -->  core/domain/ 
+---------------------------+
| 2. Application Business Rules      -->  core/usecases/
+---------------------------+
| 3. Interface Adapters             -->  api/ + infrastructure/repositories/ + serializers/
+---------------------------+
| 4. Frameworks & Drivers           -->  infrastructure/models/ + config/ + Django + DRF + DB
+---------------------------+
```

```
/seu_projeto/
├── manage.py
├── requirements.txt
├── apps/
│   ├── core/                     # Núcleo de regras de negócio (entidades, casos de uso)
│   │   ├── __init__.py
│   │   ├── domain/               # Entidades (models do domínio, sem dependência de Django)
│   │   │   └── user.py
│   │   └── usecases/            # Casos de uso (serviços da aplicação)
│   │       └── create_user.py
│   ├── infrastructure/          # Infraestrutura (ORM, cache, serviços externos)
│   │   ├── __init__.py
│   │   ├── models/              # Models do Django (para persistência)
│   │   │   └── user_model.py
│   │   ├── repositories/        # Implementações concretas dos repositórios
│   │   │   └── user_repository.py
│   │   └── services/            # Integrações externas (email, APIs de terceiros)
│   │       └── email_service.py
│   ├── api/                     # Camada de apresentação (entrada de dados)
│   │   ├── __init__.py
│   │   ├── views/               # DRF views (controladores)
│   │   │   └── user_view.py
│   │   ├── serializers/         # DRF serializers
│   │   │   └── user_serializer.py
│   │   └── urls.py              # Rotas da API
│   └── config/                  # Configuração do Django
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── tests/
│   ├── unit/                    # Testes unitários (core e usecases)
│   ├── integration/             # Testes com dependências reais (DB, etc)
│   └── api/                     # Testes de ponta-a-ponta da API
└── README.md
```