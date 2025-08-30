from functools import reduce

# -------------------------------
# Funções estatísticas
# -------------------------------
sum_list = lambda numbers: reduce(lambda x, y: x + y, numbers)  # Lambda + alta ordem
avg_list = lambda numbers: sum_list(numbers) / len(numbers) if numbers else 0
max_list = lambda numbers: reduce(lambda x, y: x if x > y else y, numbers)
min_list = lambda numbers: reduce(lambda x, y: x if x < y else y, numbers)

# -------------------------------
# Função de alta ordem
# -------------------------------
def apply_filter(numbers, func):
    """Aplica um filtro funcional em uma lista"""
    return [x for x in numbers if func(x)]  # list comprehension

# -------------------------------
# Closure para histórico
# -------------------------------
def history_tracker():
    history = []
    def add_record(record):
        history.append(record)
        return history[-1]  # retorna o último registro
    return add_record

# Instanciando closure
save_history = history_tracker()

# -------------------------------
# Testes simples
# -------------------------------
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6]

    print("Soma:", sum_list(lista))
    print("Média:", avg_list(lista))
    print("Máximo:", max_list(lista))
    print("Mínimo:", min_list(lista))

    pares = apply_filter(lista, lambda x: x % 2 == 0)  # Uso de lambda
    print("Pares:", pares)

    print("Histórico:", save_history("Último cálculo foi a média = " + str(avg_list(lista))))