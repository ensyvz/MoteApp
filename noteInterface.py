from appJar import gui
import noteCore as core

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        if core.userLogin(usr,pwd) != False:
            app.clear()
            app.addLabel("Welcome")
        else:
            app.addLabel("Wrong") 

app = gui("Note","300x100")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.addButtons(["Submit","Cancel"],press)
app.go()