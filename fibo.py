# 1- Criar algoritmo que liste a sequencia de Fibonacci até o numero 100

# Função para gerar a sequência de Fibonacci até um determinado limite
def fibonacci_sequence(limit):
    sequence = [0, 1]
    
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

# Definindo o limite como 100
limite = 100

# Chamando a função e imprimindo a sequência
sequencia_fibonacci = fibonacci_sequence(limite)
print("Sequência de Fibonacci até", limite, ":", sequencia_fibonacci)

fibonacci_sequence(100)