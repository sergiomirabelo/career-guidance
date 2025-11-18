# src/cli.py
import sys
from .models import Perfil
from .recommender import Recommender
from .storage import carregar_carreiras, salvar_perfil

MENU = '''\n=== Orientação de Carreiras ===
1) Cadastrar perfil
2) Avaliar perfil
3) Sair
Escolha: '''

def criar_perfil() -> Perfil:
    nome = input('Nome do candidato: ').strip()
    perfil = Perfil(nome=nome)
    print('Insira níveis de 0 a 10 para as competências. Deixe em branco para terminar.')
    while True:
        comp = input('Competência (ex: Lógica): ').strip()
        if not comp:
            break
        nivel = input(f'Nível em {comp} (0-10): ').strip()
        try:
            nivel_int = int(nivel)
        except ValueError:
            print('Valor inválido. Use inteiro 0-10.')
            continue
        perfil.adicionar_competencia(comp, nivel_int)
    return perfil

def avaliar_perfil(perfil: Perfil, recommender: Recommender):
    resultados = recommender.avaliar(perfil)
    print(f'\nResultados para {perfil.nome} (média de competências: {perfil.obter_media():.2f})')
    for carreira, score in resultados:
        print(f'- {carreira.nome}: {score} %')
    print('\nTrilhas sugeridas:')
    trilhas = recommender.gerar_trilhas(perfil)
    for t in trilhas:
        print(f"\nCarreira: {t['carreira']} (score {t['score']})")
        if not t['gaps']:
            print('  Perfil alinhado. Considere aprofundar projetos práticos.')
        else:
            for g in t['gaps']:
                print(f"  - Melhorar {g['competencia']}: atual {g['atual']} -> desejado {g['desejado']}")
            for s in t['sugestoes']:
                print('   *', s)

def main():
    careers = carregar_carreiras()
    recommender = Recommender(careers)
    while True:
        escolha = input(MENU).strip()
        if escolha == '1':
            perfil = criar_perfil()
            salvar = input('Salvar perfil? (s/n): ').strip().lower()
            if salvar == 's':
                salvar_perfil(perfil)
                print('Perfil salvo.')
        elif escolha == '2':
            perfil = criar_perfil()
            avaliar_perfil(perfil, recommender)
        elif escolha == '3':
            print('Tchau!')
            sys.exit(0)
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()
