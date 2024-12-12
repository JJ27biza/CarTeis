import Factura
import drivers

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import eventos, var
import informes
from my_calendar import *
from datetime import datetime

from dlgFechaBaja import Ui_Dialog
from jdgSalir import *
from dlgAcercaDe import *


class Salir(QtWidgets.QDialog):
    def __init__(self):
        super(Salir, self).__init__()
        var.salir = Ui_jdgSalir()
        var.salir.setupUi(self)
        '''
        zona de botones
        '''
        var.salir.btnSalir.clicked.connect(eventos.Eventos.salir)
        var.salir.btnCancelar.clicked.connect(eventos.Eventos.cancelarSalir)



class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        super(AcercaDe, self).__init__()
        var.AcercaDe = Ui_dlgAcercaDe()
        var.AcercaDe.setupUi(self)
        '''
        zona de botones

        '''
        var.AcercaDe.btnSalir.clicked.connect(eventos.Eventos.salirAcercaDe)

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendar.calendarWidget.setSelectedDate(QtCore.QDate(ano,mes,dia))
        var.calendar.calendarWidget.clicked.connect(drivers.Drivers.cargaFecha)




class Calendarfac(QtWidgets.QDialog):
    def __init__(self):
        super(Calendarfac, self).__init__()
        var.calendarfac =Ui_dlgCalendarfac()
        var.calendarfac.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendarfac.calendarWidget.setSelectedDate(QtCore.QDate(ano,mes,dia))
        var.calendarfac.calendarWidget.clicked.connect(Factura.Facturas.cargaFecha)

class CalendarBaja(QtWidgets.QDialog):
    def __init__(self):
        super(CalendarBaja, self).__init__()
        var.calendarBaja = Ui_Dialog()
        var.calendarBaja.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendarBaja.calendarBaja.setSelectedDate(QtCore.QDate(ano,mes,dia))
        var.calendarBaja.calendarBaja.clicked.connect(drivers.Drivers.cargaFechaBaja)




class FileDialogAbrir(QtWidgets.QFileDialog):
      def __init__(self):
        super(FileDialogAbrir, self).__init__()