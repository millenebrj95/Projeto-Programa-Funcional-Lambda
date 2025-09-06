<img width="782" height="99" alt="image" src="https://github.com/user-attachments/assets/d36c0bf4-3727-48d8-889a-f45f3bf4970d" /># 🐍 Atividade Parcial - Programação Funcional

Este repositório contém a implementação da **Atividade Parcial N704.25.2 - Programação Funcional**.

## 📌 Objetivo
Aplicar os conceitos de **Programação Funcional** em Python, desenvolvendo um software que utiliza:
- Funções **lambda**  
- **List comprehensions**  
- **Closures**  
- **Funções de alta ordem**

## 👥 Membros da Equipe:
- Millene de Souza Júnior – 2326165 
- Herison Daniel Wanderley – 2315221
- Talles de Lima Pereira – 2326201
- João Eduardo Lúcio Araújo – 291356

## 👩‍💻 Atribuição de funções:
Millene Júnior – Responsável pela documentação de requisitos, execução da primeira fase de implementação, realização dos primeiros testes e elaboração do relatório final.

Herison Daniel – Responsável pela segunda fase de implementação, garantindo a integração das funcionalidades desenvolvidas.

Talles de Lima – Responsável pela terceira fase de implementação, focando na codificação e ajustes finais das funcionalidades.

João Eduardo – Responsável pela segunda fase de testes, verificando a qualidade e o funcionamento das implementações. 

## ⚙️ Requisitos Funcionais
1. O sistema deve calcular estatísticas de uma lista de números (soma, média, máximo e mínimo).  
2. O sistema deve permitir o uso de filtros personalizados em listas.  
3. O sistema deve utilizar funções anônimas (lambda).  
4. O sistema deve manter um histórico de cálculos (closure).  

## 🚫 Requisitos Não Funcionais
- O sistema deve ser desenvolvido em **Python 3.8+**.  
- O código deve ser publicado em um **repositório GitHub**.  
- O sistema não deve apresentar erros em tempo de execução.  

## 🧩 Estrutura do Código
- `sum_list` → Soma de números (**lambda + reduce**)  
- `avg_list` → Média dos números (**lambda**)  
- `max_list` → Maior valor (**lambda + reduce**)  
- `min_list` → Menor valor (**lambda + reduce**)  
- `apply_filter` → Função de alta ordem para filtros  
- `history_tracker` → Closure que guarda histórico  

## 🧪 Casos de Teste
| Caso | Entrada | Saída Esperada |
|------|---------|----------------|
| Soma | [1, 2, 3] | 6 |
| Média | [2, 4, 6] | 4 |
| Máximo | [2, 5, 1] | 5 |
| Mínimo | [2, 5, 1] | 1 |
| Filtrar pares | [1, 2, 3, 4] | [2, 4] |
| Histórico | Último cálculo: média = 4 | Retornar string |

## ▶️ Execução
```bash
python main.py
```

Saída esperada:
```
Soma: 21
Média: 3.5
Máximo: 6
Mínimo: 1
Pares: [2, 4, 6]
Histórico: Último cálculo foi a média = 3.5
```

## 🤖 Observação
Parte do desenvolvimento contou com apoio do **ChatGPT**, usado para estruturar o documento de requisitos, gerar exemplos de código e elaborar este relatório. Todas as respostas foram adaptadas pela equipe.

## 🚀 Como executar o projeto
1. Pré-requisitos
Python 3.8+ instalado (download aqui)
Git instalado (opcional)

2. Clonar ou baixar o projeto
git clone https://github.com/millenebrj95/Projeto-Programa-Funcional-Lambda.git

3. Acessar a pasta do projeto
cd Projeto-Programa-Funcional-Lambda-main

4. Criar ambiente virtual (opcional)
python -m venv venv

Ativar:
Windows: venv\Scripts\activate
Linux/Mac: source venv/bin/activate

5. Instalar dependências
pip install -r requirements.txt

6. Executar o programa
python main.py

7. Testar manualmente no Python
from main import sum_list, avg_list, max_list, min_list, apply_filter, history_tracker

print(sum_list([1, 2, 3, 4]))                  # 10
print(avg_list([1, 2, 3, 4]))                  # 2.5
print(max_list([1, 2, 3, 4]))                  # 4
print(min_list([1, 2, 3, 4]))                  # 1
print(apply_filter([1, 2, 3, 4], lambda x: x % 2 == 0))  # [2, 4]

history = history_tracker()
print(history("Primeira execução"))            # Primeira execução
print(history("Segunda execução"))             # Segunda execução




