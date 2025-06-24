# Análise dos Requisitos Levantados

## 1. Lista de Verificação Aplicada aos Requisitos

| Requisito                          | Verificação               | Observação                                                                 |
|-----------------------------------|---------------------------|----------------------------------------------------------------------------|
| RF01 - Gerenciar categorias e serviços | Requisito único e necessário | Sem problemas identificados                                                 |
| RF02 - Gerenciar profissionais        | Requisito único e necessário | Sem problemas identificados                                                 |
| RF03 - Gerenciar usuários (moderador) | Requisito único e necessário | Sem problemas identificados                                                 |
| RF04 - Pesquisar profissionais por categoria | Claro e testável          | Sem ambiguidade                                                             |
| RF05 - Planos de impulsionamento     | Potencial ambiguidade     | Pode gerar dúvida: o que define o plano? quais funcionalidades ele ativa?  |
| RF06 - Apresentar melhor avaliados   | Requisito combinado       | Poderia ser dividido em: "calcular melhores avaliados" e "exibir resultados" |
| RF07 - Favoritar profissional        | Simples, claro e necessário | Independente e testável                                                     |
| RF08 - Avaliar serviço               | Claro e testável          | Depende da existência de um modelo de avaliação                             |
| RF09 - Gerenciar portfólio          | Ambiguidade leve          | "Gerenciar" pode ser dividido: criar, editar, excluir, visualizar           |
| RF10 - Chat interno                 | Projeto prematuro         | Pode conter decisão técnica embutida: que tipo de chat? assíncrono? tempo real? |

## 2. Identificação de Problemas e Observações

### Projeto Prematuro:
- RF10 pode conter definição técnica não discutida ainda (tipo de chat e tecnologia envolvida).

### Requisitos Combinados:
- RF06 deveria ser dividido em dois: cálculo de nota e exibição no sistema.

### Requisitos Desnecessários:
- Nenhum identificado até o momento. Todos possuem valor funcional claro.

### Ambiguidade:
- RF05 e RF09 têm termos genéricos ("plano", "gerenciar") que podem ser interpretados de formas diferentes pelos stakeholders.

### Realismo:
- Todos os requisitos parecem tecnicamente viáveis.

### Teste:
- Com exceção de RF05 e RF06, os requisitos são testáveis.

---

## 3. Matriz de Interação dos Requisitos

|        | RF01 | RF02 | RF03 | RF04 | RF05 | RF06 | RF07 | RF08 | RF09 | RF10 |
|--------|------|------|------|------|------|------|------|------|------|------|
| RF01   | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |
| RF02   | 0    | 0    | 1000 | 1000 | 0    | 0    | 0    | 0    | 0    | 0    |
| RF03   | 0    | 1000 | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |
| RF04   | 0    | 1000 | 0    | 0    | 0    | 1000 | 0    | 0    | 0    | 0    |
| RF05   | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 1000 | 0    |
| RF06   | 0    | 0    | 0    | 1000 | 0    | 0    | 0    | 1000 | 0    | 0    |
| RF07   | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |
| RF08   | 0    | 0    | 0    | 0    | 0    | 1000 | 0    | 0    | 0    | 0    |
| RF09   | 0    | 0    | 0    | 0    | 1000 | 0    | 0    | 0    | 0    | 0    |
| RF10   | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

---

## 4. Requisitos Conflitantes

- Nenhum requisitos conflitantes entre si identificados até o momento.
