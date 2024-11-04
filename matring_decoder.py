# Leitura das 4 linhas da Matring
matring = [input().strip() for _ in range(4)]

# Extraindo os valores das colunas necessárias
F = int(matring[0][0] + matring[1][0] + matring[2][0] + matring[3][0])
L = int(matring[0][-1] + matring[1][-1] + matring[2][-1] + matring[3][-1])

# Inicializando a string decodificada
decoded_message = ""

# Decodificação da Matring para uma string
for i in range(1, len(matring[0]) - 1):
    M_i = int(matring[0][i] + matring[1][i] + matring[2][i] + matring[3][i])
    C_i = (F * M_i + L) % 257
    decoded_message += chr(C_i)

# Saída da mensagem decodificada com nova linha
print(decoded_message)
