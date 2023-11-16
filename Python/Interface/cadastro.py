from PySimpleGUI import PySimpleGUI as sg
#Layout
sg.theme('Reddit')
Layout = [
    [sg.Text('Usuàrio'), sg.Input(key='usuario')],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char = '*', size= (20,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Login',Layout)
#Ler Eventos 
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuario'] == 'Diogomachadocmb@gmail.com' and valores['senha'] =='123456':
            print('Bem-vindo')