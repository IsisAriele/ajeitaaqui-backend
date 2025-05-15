# Ajeita Aqui - Backend

O **Ajeita Aqui** é uma plataforma digital para conectar clientes a prestadores de serviços autônomos (como pedreiros, faxineiros, eletricistas, instaladores, etc). Este repositório tem como objetivo principal a **refatoração e reestruturação** do backend original, aplicando os princípios da **Clean Architecture** para garantir maior modularidade, testabilidade e escalabilidade.

---

## Estrutura da Arquitetura (Clean Architecture)

```text
apps/
├── config/                 # Configuração do Django 
├── domain/                 # Regras de negócio
│   ├── entities/           # Entidades puras do sistema
│   └── usecases/           # Casos de uso da aplicação
├── infrastructure/         # Persistência e serviços externos
│   ├── db/
│   └── services/
├── interface_adapters/     # Camada de interface (Views, Serializers, Controllers)
│   └── api/
```

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ajeita-aqui-backend.git
cd ajeita-aqui-backend
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações e o servidor

```bash
python manage.py migrate
python manage.py runserver
```

---

## Rodando os testes

--- # WIP

---

## Documentação da API

--- # WIP

---

## Observações futuras

- Implantação em nuvem planejada com Docker e Docker Compose
- Integração de funcionalidades como chat em tempo real e pagamento de um serviço contratado

---