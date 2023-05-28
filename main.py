import eel

eel.init('Vex')

@eel.expose
def App():
    print("Application is Running")

App()

eel.start('index.html')