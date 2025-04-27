import os
import pandas as pd

os.system("cls")

caminho_arquivo = "pacientes.xlsx"



def gerar_relatorio():
    documento = []
    with open("relatorio.txt", "w+", encoding="utf-8") as arq:
        print("Relatório do Paciente(Pressione enter em branco para finalizar): \n")
        while True:
            relatorio = input("")
            if relatorio == "":
                break
            documento.append(relatorio + "\n")
        arq.writelines(documento)




def exibir_relatorio():
        nome_arquivo = input("\nDigite o nome do arquivo (sem extensão) ou 'sair' para cancelar: ").strip()

        caminho_relatorio = nome_arquivo + ".txt"
        if os.path.exists(caminho_relatorio):
            with open(caminho_relatorio, "r", encoding="utf-8") as arq:
               print("\nRelatorio:\n")
               linhas = arq.readlines()
               for i, linha in enumerate(linhas, 1):
                    print(f"{i}. {linha.strip()}")
        else:
            print("O arquivo não foi encontrado, tente novamente!")



def modificar_relatorio():
    nome_arquivo = input("O arquivo tem que estar em txt. Digite o nome do relatório que deseja modificar sem a extensão: ").strip()
    caminho_relatorio = nome_arquivo + ".txt"
    
    if os.path.exists(caminho_relatorio):

        with open(caminho_relatorio, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()
        

        print("\n--- Conteúdo atual do relatório ---")
        for i, linha in enumerate(linhas, 1):
            print(f"{i}. {linha.strip()}")
        

        print("\nOpções:")
        print("1 - Adicionar novas linhas")
        print("2 - Editar linha existente")
        print("3 - Remover linha")
        print("4 - Cancelar")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":

            print("\nDigite as novas linhas (linha vazia para terminar):")
            while True:
                nova_linha = input()
                if nova_linha == "":
                    break
                linhas.append(nova_linha + "\n")


        elif opcao == "2":
                
            num_linha = int(input("Número da linha a editar: ")) - 1
            if 0 <= num_linha < len(linhas):
                novo_texto = input(f"Editar linha {num_linha+1}: ")
                linhas[num_linha] = novo_texto + "\n"
            else:
                print("Número de linha inválido!")


        elif opcao == "3":

            num_linha = int(input("Número da linha a remover: ")) - 1
            if 0 <= num_linha < len(linhas):
                del linhas[num_linha]
            else:
                    print("Número de linha inválido!")
        

        elif opcao == "4":
            print("Operação cancelada. Nenhuma alteração foi salva.")
            return  # Sai da função sem salvar
        
        elif opcao == "": return
        
        
        # Salva as alterações se não foi cancelado
        if opcao in ("1", "2", "3"):
            with open(caminho_relatorio, "w", encoding="utf-8") as arq:
                arq.writelines(linhas)
            print("Relatório atualizado com sucesso!")

    else:
        print("O arquivo não foi encontrado, tente novamente!")




def planilha():

    print("""Você deseja Registrar ou Consultar um paciente?
          
          1 - Consultar
          2 - Registrar\n""")
    
    escolha = input("Escolha: ")

    if escolha == "1":
        importar_planilha()
    elif escolha == "2":
        exportar_para_planilha()
    else:
        print("Opção inválida.")





def exportar_para_planilha():
    novos_dados = {
        "Nome do paciente": [],
        "Responsável": [],
        "Idade": [],
        "Número de Celular": [],
        "Endereço": [],
        "Número da casa ou apartamento": [],
        "CEP": [],
    }

    print("\n--- Cadastro de Pacientes ---")
    while True:
        nome = input("Nome do paciente (ou pressione Enter para sair e salvar): ").strip()
        if nome == "":
            break

        responsavel = input("Responsável: ").strip()

        while True:
            idade_input = input("Idade: ").strip()
            if idade_input.isdigit() and int(idade_input) > 0:
                idade = int(idade_input)
                break
            print("Idade inválida. Digite um número positivo.")

        celular = input("Número de Celular: ").strip()
        endereco = input("Endereço: ").strip()
        numero_casa_apt = input("Número da casa ou apartamento: ").strip()
        CEP = input("CEP: ").strip()

        novos_dados["Nome do paciente"].append(nome)
        novos_dados["Responsável"].append(responsavel)
        novos_dados["Idade"].append(idade)
        novos_dados["Número de Celular"].append(celular)
        novos_dados["Endereço"].append(endereco)
        novos_dados["Número da casa ou apartamento"].append(numero_casa_apt)
        novos_dados["CEP"].append(CEP)

        print("Paciente cadastrado com sucesso!\n")

    if novos_dados["Nome do paciente"]:
        if os.path.exists(caminho_arquivo):
            df_existente = pd.read_excel(caminho_arquivo)
        else:
            df_existente = pd.DataFrame(columns=novos_dados.keys())

        df_novos = pd.DataFrame(novos_dados)
        df_final = pd.concat([df_existente, df_novos], ignore_index=True)
        df_final.to_excel(caminho_arquivo, index=False)

        print(f"\nDados adicionados com sucesso em {caminho_arquivo}")
    else:
        print("Nenhum dado foi cadastrado.")




def importar_planilha():
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return

    df = pd.read_excel(caminho_arquivo)
    print("\n--- Dados da Planilha ---\n")
    print(df.to_string(index=False))






def menu():
    while True:
        print("""
            1 - Gerar Relatório de um paciente
            2 - Exibir Relatório de um paciente
            3 - Modificar Relatório de um paciente
            4 - Registar ou Consultar paciente
            0 - Sair\n""")
        
        escolha = input("Escolha uma das opções: ")

        if escolha == "0": break
        elif escolha == "1": gerar_relatorio()
        elif escolha == "2": exibir_relatorio()
        elif escolha == "3": modificar_relatorio()
        elif escolha == "4": planilha()
        else: print("Essa opção não existe")

menu()
