import PySimpleGUI as sg



class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkGrey1')
        # Layout
        layout = [
            [sg.Text('Name', size=(5,0)), sg.Input(size=(40,0), key ='name')],
            [sg.Text('Age', size=(5,0)), sg.Input(size=(2,0), key='age')],
            [sg.Text('Accepted email providers')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook') , sg.Checkbox('Yahoo', key='yahoo') ],
            [sg.Text('Credit Card?')],
            [sg.Radio('Yes', 'cards', key='acceptCard'), sg.Radio('No', 'cards', key='noAcceptCard')],
            [sg.Text ('Volume Fake', size=(15,0))],
            [sg.Slider(range=(0,10),default_value=0, orientation= 'h', size=(15,20), key='sliderVelocity')],
            [sg.Button("Send")],
            [sg.Output(size=(50,20))]
        ]
        #Janela
        self.janela = sg.Window('User Data').layout(layout)
            #   self.button, self.values = self.janela.Read() foi retirado daqui e colocado na line 25 p/ loop


    def Iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            name = self.values['name']
            age = self.values['age']
            accept_gmail = self.values['gmail']
            accept_outlook = self.values['outlook']
            accept_yahoo = self.values['yahoo']
            accept_card = self.values['acceptCard']
            no_accept_card = self.values['noAcceptCard']
            velocity_script = self.values['sliderVelocity']
            print(f'Name: {name}')
            print(f'Age : {age}')
            print(f'Accept Gmail: {accept_gmail}')
            print(f'Accept Outlook: {accept_outlook}')
            print(f'Accept Yahoo: {accept_yahoo}')
            print(f'Accept Card: {accept_card}')
            print(f'No Accept Card: {no_accept_card}')

tela = TelaPython()
tela.Iniciar()         
