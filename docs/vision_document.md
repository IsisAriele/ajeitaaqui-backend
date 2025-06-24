# Documento de Visão - Projeto Ajeita Aqui

### Histórico da Revisão

| Data       | Versão | Descrição             | Autor                       |
|------------|--------|-----------------------|-----------------------------|
| 27/06/2024 | 1.0    | Versão inicial        | Adna, Isis, Ramon e Vinícius |
| 12/05/2025 | 1.1    | Revisão do documento  | Isis                        |
| 12/06/2025 | 1.2    | Atualização do requisitos não funcionais | Isis                        |

---


## 1. Descrição do Problema

O problema de **encontrar prestadores de serviços autônomos qualificados**, como pedreiros, faxineiros, eletricistas, instaladores etc., afeta tanto os **clientes** que precisam desses serviços quanto os **profissionais** que os oferecem.

O impacto inclui:

- Dificuldade de contratação
- Atrasos e serviços de baixa qualidade
- Baixa visibilidade dos profissionais

Uma boa solução seria desenvolver **uma plataforma de classificados de serviços** que:

- Facilite a conexão entre clientes e prestadores
- Permita a avaliação dos profissionais
- Promova maior confiança na contratação
- Fortaleça a visibilidade dos prestadores

---

## 2. Descrição dos Usuários

| Nome       | Descrição               | Responsabilidade                                      |
|------------|-------------------------|--------------------------------------------------------|
| Visitante  | Indivíduo não cadastrado | Visualizar postagens; cadastrar-se na plataforma      |
| Usuário    | Contrata e pode ofertar serviços | Pesquisar, contatar, contratar e avaliar profissionais; ofertar serviços |
| Profissional | Oferece serviços       | Criar ofertas; contatar clientes                      |
| Moderador  | Administra o sistema     | Gerenciar contas; remover postagens; oferecer suporte |

---

## 3. Descrição do Ambiente dos Usuários

- Acesso 24 horas por dia via desktops ou smartphones
- Requer conexão com a internet
- Disponibilidade de chat interno para comunicação entre usuários e profissionais

---

## 4. Principais Necessidades dos Usuários

| Problema                        | Causa                          | Como é resolvido hoje    | Solução desejada                        |
|---------------------------------|--------------------------------|---------------------------|------------------------------------------|
| Dificuldade em encontrar profissionais | Falta de centralização        | Busca manual ou por indicação | Plataforma com catálogo organizado       |
| Qualidade dos serviços incerta | Ausência de avaliações públicas e confiáveis | Indicações pessoais       | Sistema de avaliações públicas de usuários |
| Contato difícil com prestadores | Falta de canal interno         | Mensagens externas         | Chat interno integrado                   |

---

## 5. Alternativas Concorrentes

### 5.1. GetNinjas
- **Pontos fortes:** Ampla variedade de serviços, app móvel
- **Pontos fracos:** Prestador paga por oportunidade, qualidade variável

### 5.2. Triider
- **Pontos fortes:** Avaliações, categorias bem definidas
- **Pontos fracos:** Poucas categorias, presença geográfica limitada

### 5.3. OLX
- **Pontos fortes:** Grande base de usuários, gratuito
- **Pontos fracos:** Não é focado em serviços, sem avaliações

### 5.4. Higitec
- **Pontos fortes:** Avaliação técnica, foco técnico
- **Pontos fracos:** Atuação limitada à região de SP

### 5.5. "Boca a Boca"
- **Pontos fortes:** Confiança e gratuidade
- **Pontos fracos:** Rede limitada, sem avaliações públicas

---

## 6. Visão Geral do Produto

- Acesso via desktop
- Interface simples e intuitiva
- Funcionalidades:
  - Publicação de ofertas
  - Sistema de avaliação
  - Chat interno
  - Integração com sistema de pagamento para planos de impulsionamento e contratação de serviços

---

## 7. Requisitos Funcionais

| Código | Nome                             | Descrição                                                                 |
|--------|----------------------------------|---------------------------------------------------------------------------|
| RF01   | Gerenciar categorias e serviços | Listar, cadastrar, excluir e editar serviços                              |
| RF02   | Gerenciar profissionais         | Listar, cadastrar, pesquisar, editar e excluir profissionais              |
| RF03   | Gerenciar usuários              | Listar, cadastrar, pesquisar, editar e excluir usuários (moderador)       |
| RF04   | Pesquisar profissionais         | Listar profissionais por categoria                                        |
| RF05   | Gerenciar planos de profissionais | Visualizar e assinar planos de impulsionamento                           |
| RF06   | Apresentar profissionais melhor avaliados | Apresentar profissionais melhor avaliados mensalmente             |
| RF07   | Favoritar profissional          | Salvar profissionais de interesse                                         |
| RF08   | Avaliar serviço                 | Avaliar serviço prestado                                                  |
| RF09   | Gerenciar portfólio               | Criar, editar e excluir portfólio                                           |
| RF10   | Sistema de mensagens (Chat)     | Comunicação entre usuário e profissional na plataforma                    |

---

## 8. Requisitos Não-Funcionais

### RNF01 - Arquitetura Modular

- **Objetivo:** Seguir princípios da Arquitetura Limpa
- **Categoria ISO 25010:** Manutenibilidade e Implementação
- **Classificação:** Obrigatório

### RNF02 - Logging e Tratamento de Erros

- **Objetivo:** Registro de logs de erro para manutenção e depuração
- **Categoria ISO 25010:** Observabilidade
- **Classificação:** Obrigatório

### RNF03 - Documentação da API com Swagger

- **Objetivo:** Documentar rotas do backend com Swagger
- **Categoria ISO 25010:** Documentação
- **Classificação:** Obrigatório

### RNF04 - Facilidade de Deploy

- **Objetivo:** Automação do deploy com scripts ou arquivos como Dockerfile
- **Categoria ISO 25010:** Implantação
- **Classificação:** Obrigatório

---

### Observações

As categorias de serviços definidas foram: **hidráulicos, elétricos, obras (alvenaria), limpeza, ar-condicionado, instalações, telecomunicações e pintura**.