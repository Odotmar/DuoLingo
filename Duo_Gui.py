import duolingo

import DuoLanguageTrans
import PySimpleGUI as sg


def login_screen():
    welcome_banner = [
        [
            sg.Text("Welcome!")
        ]
    ]

    login_details = [
        [
            sg.Text("Username"),
            sg.In(size=(25, 1), enable_events=True, key="-L-USERNAME-")
        ],
        [
            sg.Text("Password"),
            sg.In(size=(25, 1), enable_events=True, key="-L-PASSWORD-"),
        ],
        [
            sg.Button("Submit", key="-SUBMIT-"),
        ]
    ]

    layout = [
        [
            sg.Column(welcome_banner),
        ],
        [
            sg.Frame("Please Enter Username and Password", login_details)
        ],
        [
            sg.Button("Exit")
        ]

    ]

    main_window = sg.Window("DuoLingo Word Practice", layout, margins=(350, 350))

    while True:
        event, values = main_window.read()
        # End program if user closes window or
        # presses the exit button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Submits duolingo credentials if user
        # presses the submit button
        if event == "-SUBMIT-":
            uname = values["-L-USERNAME-"]
            pw = values["-L-PASSWORD-"]

            if uname == "" or pw == "":
                sg.Popup("Please enter a Username and Password", no_titlebar=True,background_color="grey")
            else:
                try:
                    DuoLanguageTrans.get_words(uname, pw)
                except duolingo.DuolingoException:
                    sg.Popup("Incorrect Username/Password", no_titlebar=True,background_color="grey")


login_screen()
