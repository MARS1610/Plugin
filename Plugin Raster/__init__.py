def name ():
    return "Raster"

def author():
    return "Miguel Angel Ruiz Sanchez"

def authorNAme():
    return author()

def email():
    return "miguelangelruizsanchez2@gmail.com"

def description():
    return "raster"

def about():
    return "Raster"

def version():
    return "0.0.1"

def qgisMiniumVersion():
    return "3.0"

def icon():
    return "icon.png"

def category():
    return "Raster"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)