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


#2- Criar algoritmo que faça a fatoração do número 1024. (Exemplo de fatoração: 6! = 6*5*4*3*2*1).
def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial indefinido para números negativos"
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Calcular o fatorial de 1024
numero_para_fatorial = 1024
resultado_fatorial = calcular_fatorial(numero_para_fatorial)

print(f"O fatorial de {numero_para_fatorial} é: {resultado_fatorial}")

# 3- Criar uma lista de frutas (bananas, maçãs, peras, uvas, laranjas) e fazer um algoritmo para consultar se uma fruta existe na lista. Caso não exista, adicionar a nova fruta. O programa só deve encerrar a brincadeira quando o usuário informar o número 999.
# Lista inicial de frutas
lista_de_frutas = ["bananas", "maçãs", "peras", "uvas", "laranjas"]

# Função para consultar e adicionar frutas à lista
def consultar_e_adicionar_fruta():
    while True:
        # Solicitar ao usuário uma fruta ou o número 999 para encerrar
        entrada_usuario = input("Digite o nome da fruta ou 999 para encerrar: ")

        # Verificar se o usuário deseja encerrar o programa
        if entrada_usuario == "999":
            print("Encerrando o programa.")
            break

        # Verificar se a fruta já está na lista
        if entrada_usuario in lista_de_frutas:
            print(f"{entrada_usuario} já está na lista.")
        else:
            # Adicionar a nova fruta à lista
            lista_de_frutas.append(entrada_usuario)
            print(f"{entrada_usuario} foi adicionada à lista.")

# Chamar a função para consultar e adicionar frutas
consultar_e_adicionar_fruta()

# Imprimir a lista final de frutas
print("Lista final de frutas:", lista_de_frutas)
