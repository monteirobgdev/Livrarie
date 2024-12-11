# Livrarie

import flet as ft
import sqlite3

# Função para obter os dados da tabela Disciplina
def get_disciplinas(professorId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    '''cursor.execute("SELECT IdDisciplina, Nome, Descricao, ProfessorId FROM Disciplina WHERE ProfessorId = ?", (professorId,))  # Consulta os dados'''
    cursor.execute("SELECT IdDisciplina, Nome, Descricao, ProfessorId FROM Disciplina")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_unique_disciplina_nome(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_disciplina_descricao(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Descricao FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_disciplina_professorid(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT ProfessorId FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_professor_nome(professorId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Professor WHERE IdProfessor = ?", (professorId,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def faz_engenharia_de_software(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT EG FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_metodologia_de_desenvolvimento_de_sistemas(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT MDS FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_redes_de_computadores(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT RC FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_informatica(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT IF FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_probabilidade_e_estatistica(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT PE FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_economia(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT EC FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_banco_de_dados(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT BD FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False

materiaAtual = -1
professorAtual = -1
alunoAtual = 5

def main(page: ft.Page):
    navigation_stack = [] #Pilha de navegação

    def show_view(view):
        navigation_stack.append(view)
        page.views.clear()
        page.views.extend(navigation_stack)
        page.update()

    def go_back(e):
        if len(navigation_stack) > 1:
            navigation_stack.pop()
            page.views.clear()
            page.views.extend(navigation_stack)
            page.update()

    # Função para atualizar a lista de disciplinas na interface
    def refresh_disciplinas():
        def abrir_pagina_materia(e):
            global materiaAtual
            materiaAtual = e.control.data
            show_view(materia_professor_view())

        disciplina_list.controls.clear()  # Limpa a lista
        for disciplina in get_disciplinas(1):
            disciplina_list.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        title=ft.Text(disciplina[1], size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                        #subtitle=ft.Text(f'Professor(a): {get_unique_professor_nome(disciplina[3])}', size=20, color=ft.colors.BLUE_200),
                        data=disciplina[0],
                        on_click=lambda e: abrir_pagina_materia(e)
                    ),
                    border_radius=ft.border_radius.all(12),
                    bgcolor=ft.colors.WHITE10
                )
            )
        page.update()

    # Lista de disciplinas
    disciplina_list = ft.Column()

    def home_view(): #Página de escolher login
        return ft.View(
            '/',
            [
                ft.Column(
                    controls=[
                        ft.Container(
                            ft.Text('Login', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                'Aluno', 
                                on_click=lambda _: show_view(login_aluno_view()), 
                                width=300, 
                                color=ft.colors.BLUE_200
                            ), 
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                'Professor', 
                                on_click=lambda _: show_view(login_professor_view()), 
                                width=300, 
                                color=ft.colors.BLUE_200
                            ), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
                
            ]
        )
    
    def login_aluno_view(): #Página de login do aluno
        return ft.View(
            '/loginAluno',
            [
                ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back),
                                            ft.Text('Login Aluno', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200)
                                        ]
                                    ),
                                    width=300
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaMatricula],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaSenha],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(
                            ft.ElevatedButton('Entrar', on_click=loginAluno, width=150, color=ft.colors.BLUE_200), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

    def login_professor_view(): #Página de login do professor
        return ft.View(
            '/loginProfessor',
            [
                ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back),
                                            ft.Text('Login Professor', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200)
                                        ]
                                    ),
                                    width=300
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaMatricula],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaSenha],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(
                            ft.ElevatedButton('Entrar', on_click=loginProfessor, width=150, color=ft.colors.BLUE_200), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

    def area_aluno_view(): #Área do aluno
        def abrir_tela_materia(disciplinaId):
            global materiaAtual
            materiaAtual = disciplinaId
            show_view(materia_aluno_view())

        def abrir_dialogo(e):
            page.overlay.append(caixaDialogo)
            caixaDialogo.open = True
            page.update()

        def fechar_dialogo(e):
            caixaDialogo.open = False
            page.update()

        caixaDialogo = ft.AlertDialog(
            title=ft.Text('Deseja sair da área do aluno?', color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
            actions=[
                ft.TextButton('Sim', on_click=go_back),
                ft.TextButton('Não', on_click=fechar_dialogo)
            ]
        )

        areaView = ft.View(
            '/areaAluno',
            [
                # Página inicial do aluno
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Text(
                                                'Livrarie Aluno', 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            ),
                                            ft.TextButton(
                                                text='Sair',
                                                style=ft.ButtonStyle( 
                                                    color=ft.colors.BLACK87
                                                ),
                                                on_click=abrir_dialogo
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        
                        # Seção principal com as disciplinas e atividades pendentes
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Disciplinas matriculadas', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),

                                        # Coluna de Disciplinas Matriculadas
                                        ft.Column(
                                            [
                                                ft.Row( # Engenharia de Software
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(1), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(1)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_materia(1),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_engenharia_de_software(alunoAtual),
                                                    expand=True
                                                ),

                                                ft.Row( # Metodologia de Desenvolvimento de Sistemas
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(2), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(2)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_materia(2),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_metodologia_de_desenvolvimento_de_sistemas(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Redes de Computadores
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(3), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(3)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_materia(3),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_redes_de_computadores(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Informática
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(4), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(4)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_materia(4),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_informatica(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Probabilidade e Estatística
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(5), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(5)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_materia(5),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_probabilidade_e_estatistica(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Economia
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(6), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(6)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_materia(6),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_economia(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Banco de Dados
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(7), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(7)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_materia(7),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_banco_de_dados(alunoAtual),
                                                    expand=True
                                                ),
                                            ],
                                            scroll='auto',
                                            alignment=ft.alignment.top_center,
                                            expand=True
                                        )
                                    ],
                                    expand=True
                                ),
                                
                                # Coluna de Atividades Pendentes
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Atividades pendentes', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),
                                        ft.ElevatedButton(
                                            content=ft.Column(
                                                [
                                                    ft.Row(
                                                        [
                                                            ft.Column(
                                                                [
                                                                    ft.Text('Projeto - Segunda etapa', size=24, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Metodologia de Desenvolvimento de Sistemas 2', size=18, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            ft.Text('Prazo de entrega:\n13/11/2024, 08:00', color=ft.colors.RED_500)
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.Column(
                                                                [
                                                                    ft.Text('Lista 1', size=24, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Economia', size=18, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            ft.Text('Prazo de entrega:\n15/11/2024, 23:59', color=ft.colors.BLUE_200)
                                                        ]
                                                    )
                                                ],
                                                spacing=20
                                            ),
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.colors.WHITE10,
                                                padding=ft.padding.all(20),
                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                alignment=ft.alignment.center_left
                                            ),
                                            width=1080,
                                            expand=True
                                        )
                                    ],
                                    expand=True  # Expande a coluna para ocupar o espaço verticalmente
                                )
                            ],
                            expand=True  # Expande a Row para ocupar o espaço horizontalmente
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )
        refresh_disciplinas()
        return areaView

    def area_professor_view(): #Área do professor
        def abrir_dialogo(e):
            page.overlay.append(caixaDialogo)
            caixaDialogo.open = True
            page.update()

        def fechar_dialogo(e):
            caixaDialogo.open = False
            page.update()
            
        caixaDialogo = ft.AlertDialog(
            title=ft.Text('Deseja sair da área do professor?', color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
            actions=[
                ft.TextButton('Sim', on_click=go_back),
                ft.TextButton('Não', on_click=fechar_dialogo)
            ]
        )

        areaView = ft.View(
            '/areaProfessor',
            [
                # Página inicial do aluno
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Text(
                                                'Livrarie Professor', 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            ),
                                            ft.TextButton(
                                                text='Sair',
                                                style=ft.ButtonStyle( 
                                                    color=ft.colors.BLACK87
                                                ),
                                                on_click=abrir_dialogo
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        # Seção principal com as disciplinas e atividades pendentes
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Disciplinas atribuídas', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),

                                        # Coluna de Disciplinas Matriculadas
                                        ft.Column(
                                            [disciplina_list],
                                            scroll='auto',
                                            alignment=ft.alignment.top_center,
                                            expand=True
                                        )
                                    ],
                                    expand=True
                                )
                            ],
                            expand=True  # Expande a Row para ocupar o espaço horizontalmente
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )
        refresh_disciplinas()
        return areaView

    def materia_aluno_view(): #Página de detalhes da matéria do aluno
        return ft.View(
            '/materiaAluno',
            [
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back, icon_color=ft.colors.BLACK87),
                                            ft.Text(
                                                value=get_unique_disciplina_nome(materiaAtual), 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            )
                                        ]
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        ft.Container(ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(materiaAtual)), size=20, color=ft.colors.BLUE_200), padding=ft.padding.only(left=20, top=12)),
                        ft.Container(
                            content=ft.Text(value=get_unique_disciplina_descricao(materiaAtual), size=30, color=ft.colors.BLUE_200),
                            border_radius=ft.border_radius.all(12),
                            bgcolor=ft.colors.WHITE10,
                            padding=ft.padding.all(20)
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )

    def materia_professor_view(): #Página de detalhes da matéria do professor
        return ft.View(
            '/materiaProfessor',
            [
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back, icon_color=ft.colors.BLACK87),
                                            ft.Text(
                                                value=get_unique_disciplina_nome(materiaAtual), 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            )
                                        ]
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        ft.Container(
                            content=ft.Text(value=get_unique_disciplina_descricao(materiaAtual), size=30, color=ft.colors.BLUE_200),
                            border_radius=ft.border_radius.all(12),
                            bgcolor=ft.colors.WHITE10,
                            padding=ft.padding.all(20)
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )

    page.title = "Livrarie"
    page.padding = 20
    show_view(home_view())

    def loginAluno(e):
        if not entradaMatricula.value:
            entradaMatricula.error_text = 'Preencha a matrícula'
            page.update()
        elif not entradaSenha.value:
            entradaSenha.error_text = 'Preencha a senha'
            page.update()
        else:
            show_view(area_aluno_view())

    def loginProfessor(e):
        if not entradaMatricula.value:
            entradaMatricula.error_text = 'Preencha a matrícula'
            page.update()
        elif not entradaSenha.value:
            entradaSenha.error_text = 'Preencha a senha'
            page.update()
        else:
            show_view(area_professor_view())

    entradaMatricula = ft.TextField(label='Matrícula', border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)
    entradaSenha = ft.TextField(label='Senha', password=True, border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)

    page.update()

ft.app(target=main)
