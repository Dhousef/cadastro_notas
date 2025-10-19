# ==========================================================
# APLICAÇÃO: CADASTRO DE ALUNOS E CÁLCULO DE MÉDIAS
# Estruturas utilizadas: Listas e Matrizes (Lista de Listas)
# ==========================================================

# 1. Variáveis Globais (Listas e Matrizes)
# Lista para armazenar os nomes dos alunos
alunos = [] 
# Matriz (Lista de Listas) para armazenar as notas. 
# notas[i] será uma lista contendo as notas do aluno na posição i da lista 'alunos'.
notas = [] 
NUM_AVALIACOES = 3 # Número fixo de avaliações (P1, P2, P3)

def exibir_menu():
    """Exibe o menu de opções ao usuário."""
    print("\n==============================================")
    print("        SISTEMA DE GESTÃO DE NOTAS          ")
    print("==============================================")
    print("1. Cadastrar Novo Aluno e Notas")
    print("2. Exibir Boletim Completo")
    print("3. Calcular Média de um Aluno Específico")
    print("4. Sair")
    print("----------------------------------------------")

def adicionar_aluno_e_notas():
    """Adiciona um novo aluno à lista e suas notas à matriz."""
    nome = input("Digite o nome do aluno: ").strip()
    
    # Verifica se o aluno já está cadastrado
    if nome in alunos:
        print(f"ERRO: O aluno '{nome}' já está cadastrado.")
        return

    # Adiciona o aluno à lista
    alunos.append(nome)
    
    # Cria uma lista temporária para as notas do aluno atual
    notas_do_aluno = []
    
    print(f"--- Inserir notas para {nome} ({NUM_AVALIACOES} avaliações) ---")
    
    # Laço de Repetição para coletar as notas
    for i in range(NUM_AVALIACOES):
        while True:
            try:
                # Condicional para validar a entrada da nota
                nota = float(input(f"Nota da Avaliação {i + 1} (0-10): "))
                if 0 <= nota <= 10:
                    notas_do_aluno.append(nota)
                    break
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    
    # Adiciona a lista de notas do aluno à matriz principal
    notas.append(notas_do_aluno)
    print(f"\n[SUCESSO] Aluno '{nome}' cadastrado com notas.")


def calcular_media(lista_notas):
    """Calcula a média de uma lista de notas (Função auxiliar)."""
    if not lista_notas:
        return 0
    # Uso de list comprehension implícito (sum() funciona em listas)
    return sum(lista_notas) / len(lista_notas)


def exibir_boletim():
    """Exibe todos os alunos, suas notas e médias (uso da Matriz)."""
    if not alunos:
        print("\n[INFO] Nenhum aluno cadastrado ainda.")
        return

    print("\n==============================================")
    print("               BOLETIM GERAL                  ")
    print("==============================================")
    print(f"{'Aluno':<20}{'P1':<5}{'P2':<5}{'P3':<5}{'Média':<8}{'Situação':<10}")
    print("-" * 55)

    # Laço de Repetição para iterar sobre a lista de alunos e a matriz de notas
    for i in range(len(alunos)):
        nome = alunos[i]
        notas_aluno = notas[i] # Acessa a linha 'i' da matriz (lista de notas)
        media = calcular_media(notas_aluno)
        
        # Condicional para determinar a situação do aluno
        situacao = "APROVADO" if media >= 7.0 else "REPROVADO"
        
        # Uso de formatação de string (f-string)
        print(f"{nome:<20}{notas_aluno[0]:<5.1f}{notas_aluno[1]:<5.1f}{notas_aluno[2]:<5.1f}{media:<8.2f}{situacao:<10}")
    
    print("==============================================")

def consultar_media_especifica():
    """Permite ao usuário consultar a média de um aluno pelo nome."""
    if not alunos:
        print("\n[INFO] Nenhum aluno cadastrado para consulta.")
        return
        
    nome_consulta = input("Digite o nome do aluno para consultar a média: ").strip()
    
    # Laço e condicional para buscar o aluno
    if nome_consulta in alunos:
        indice = alunos.index(nome_consulta)
        notas_aluno = notas[indice]
        media = calcular_media(notas_aluno)
        
        print("-" * 40)
        print(f"Aluno: {nome_consulta}")
        print(f"Notas: {', '.join(map(str, notas_aluno))}")
        print(f"Média Final: {media:.2f}")
        print("-" * 40)
    else:
        print(f"\n[ERRO] Aluno '{nome_consulta}' não encontrado no cadastro.")


# 2. Função Principal do Programa
def main():
    """Função principal que executa o menu interativo."""
    while True:
        exibir_menu()
        try:
            opcao = input("Escolha uma opção: ")
            
            # Estrutura Condicional (if/elif/else) para navegar no menu
            if opcao == '1':
                adicionar_aluno_e_notas()
            elif opcao == '2':
                exibir_boletim()
            elif opcao == '3':
                consultar_media_especifica()
            elif opcao == '4':
                print("\nEncerrando o Sistema. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 4.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

# Inicia a execução do programa
if __name__ == "__main__":
    main()