import pages.login as login
import pages.mainmenu as mainmenu
import pages.AddPrescription as AddPrescription
import pages.viewPrescription as ViewPrescription


class AppManager:
    def __init__(self, basecontainer):
        self.frames = {}
        for F in (login.LoginPage, mainmenu.MainmenuPage, AddPrescription.AddPrescriptionForm, ViewPrescription.ViewPrescriptionForm, ):
            page_name = F.__name__
            frame = F(parent=basecontainer, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
          
    def getFrame(self, framename):
        return self.frames[framename]

appmanager = None


def createAppManager(maincontroler):
    global appmanager
    appmanager = AppManager(maincontroler)


def getAppManager():
    return appmanager
