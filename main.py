# This is a sample Python script.
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

import Factura
import cliente
import conexion
import dlgAcercaDe
import drivers
import eventos
import time
import sys

import informes
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from mainWindow import *
import eventos, sys, var
from windowsaux import *
from dlgAcercaDe import *
import locale
import var
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')
#para la modificacion de la FechaBaja es en el botón de borrar

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, True)
        var.ui.setupUi(self)  # encargado de generar la interfaz
        var.calendar = Calendar()
        var.calendarfac = Calendarfac()
        var.salir = Salir()
        var.dlgCalendarBaja = CalendarBaja()
        var.AcercaDe = AcercaDe()
        var.dlgAbrir = FileDialogAbrir()
        var.version = "Version 0.0.1"
        conexion.Conexion.conexion()
        conexion.Conexion.selDrivers()
        conexion.Conexion.cargaprov()
        conexion.Conexion.mostrarDrivers(self)
        conexion.Conexion.cargaprovCli()
        conexion.Conexion.mostrarClis(self)
        conexion.Conexion.cargarFacturas(self)
        conexion.Conexion.cargaprovFactOrigen()
        conexion.Conexion.cargaprovFactDestino()
        conexion.Conexion.cargarTarifas(self)





        #screen = QApplication.primaryScreen().geometry()
        #var.ui.frame.setMaximumSize(screen.width(), screen.height())
        '''
        eventos de tablas
        
        '''
        eventos.Eventos.resizeTabdrivers(self)
        eventos.Eventos.resizeTabCli(self)
        eventos.Eventos.resizeTabviajes(self)
        eventos.Eventos.resizeTabFacturas(self)
        eventos.Eventos.resizeTabvTarifa(self)



        '''    
        zona de eventos de botones
        '''



        # var.ui.actionSalir.connect(eventos.Eventos.salir)
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altaDriver)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modiDri)
        var.ui.btnBuscar.clicked.connect(drivers.Drivers.buscarDri)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borraDriv)
        var.ui.rbtBaja.clicked.connect(conexion.Conexion.mostrarBajaDriver)
        var.ui.rbtTodos.clicked.connect(conexion.Conexion.mostrarDrivers)
        var.ui.rbtAlta.clicked.connect(conexion.Conexion.mostrarAltaDriver)
        var.calendarBaja.btnFechaBaja.clicked.connect(drivers.Drivers.cambiarFechaBaja)
        var.ui.btnBuscaclifac.clicked.connect(Factura.Facturas.buscaclifac)
        var.ui.btnBuscarcli.clicked.connect(cliente.cliente.buscarCli)
        var.ui.btnCalendarfac.clicked.connect(eventos.Eventos.abrirCalendarfac)
        var.ui.btnFacturar.clicked.connect(Factura.Facturas.altaFactura)
        var.ui.btn_limpiar.clicked.connect(Factura.Facturas.limpiarPanelviaje)
        var.ui.btn_modif.clicked.connect(conexion.Conexion.modifViaje)
        var.ui.btnBuscaclifac.clicked.connect(Factura.Facturas.cargarClientesEspecifico)
        var.ui.btnTarifa.clicked.connect(Factura.Facturas.modifTarifa)

        var.ui.btnAltaCli.clicked.connect(cliente.cliente.AltaCli)
        var.ui.btnBajaCli.clicked.connect(cliente.cliente.borrarCli)
        var.ui.btnModCli.clicked.connect(cliente.cliente.ModifCli)
        var.ui.rbtTodosCli.clicked.connect(conexion.Conexion.mostrarClis)
        var.ui.rbtAltaCli.clicked.connect(conexion.Conexion.mostrarAltaCli)
        var.ui.rbtBajaCli.clicked.connect(conexion.Conexion.mostrarBajaCli)

        var.ui.btnGrabar.clicked.connect(Factura.Facturas.altaviaje)




        '''
        xona de eventos de menubar

        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercaDe)
        var.ui.actionExportar_Datos_Excel.triggered.connect(eventos.Eventos.exportarDatosxl)
        var.ui.actionImportar_Datos.triggered.connect(eventos.Eventos.importarDatosxls)
        var.ui.actionListar_Clientes.triggered.connect(informes.Informes.reportclientes)
        var.ui.actionListarConductores.triggered.connect(informes.Informes.reportdrivers)
        var.ui.actionListar_Facturas.triggered.connect(informes.Informes.reportFacturas)

        '''
        zona eventos cajas de texto
        '''
        var.ui.txtDni.editingFinished.connect(lambda: drivers.Drivers.validarDni(var.ui.txtDni.displayText()))
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        '''
        eventos de la menubar
        '''
        var.ui.actionRestaurar_Copia_de_Seguridad.triggered.connect(eventos.Eventos.restaurarbackup)
        var.ui.actionCrear_Copia_Seguridad.triggered.connect(eventos.Eventos.crearbackup)
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiaPanel)
        var.ui.actionlimpiarPanel.triggered.connect(cliente.cliente.limpiaPanel2)
        var.ui.actionlimpiarPanel.triggered.connect(Factura.Facturas.limpiarPanelfac)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargadriver)
        var.ui.tablaFacturas.clicked.connect(Factura.Facturas.cargarfact)
        var.ui.actionactionCrearInformes.triggered.connect(informes.Informes.checkboxinforme)
        var.ui.actionListado.triggered.connect(informes.Informes.checkboxinforme)
        var.ui.actionlistadoviajes.triggered.connect(informes.Informes.reportviajes)


        var.ui.tabCli.clicked.connect(cliente.cliente.cargarCli)
        var.ui.tablaFacturas.clicked.connect(conexion.Conexion.cargarFacturas)
        var.ui.tablaFacturas.clicked.connect(Factura.Facturas.cargarFactura)
        var.ui.tbviajes.clicked.connect(Factura.Facturas.cargarDatosViaje)
        var.ui.tbTarifa.clicked.connect(conexion.Conexion.cargarTarifas)







        '''
        eventos de distintas cosas
        
        '''
        eventos.Eventos.cargarStatusBar(self)
        var.ui.txtMovil.editingFinished.connect(eventos.Eventos.numeroCorrecto)
        var.ui.txtTel.editingFinished.connect(eventos.Eventos.NumeroCorrecto2)
        '''
        eventos combobox
        '''

        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.cmbProvCli.currentIndexChanged.connect(conexion.Conexion.selMuniCli)
        var.ui.cmbOrigen_1.currentIndexChanged.connect(conexion.Conexion.selMuniOrigen)
        var.ui.cmbDestino_1.currentIndexChanged.connect(conexion.Conexion.selMuniDestino)
        var.ui.cmbOrigen_2.currentIndexChanged.connect(conexion.Conexion.datosviaje)
        var.ui.cmbDestino_2.currentIndexChanged.connect(conexion.Conexion.datosviaje)











        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.selEstado)

    def closeEvent(self, event):
        # event.ignore()
        # eventos.Eventos.abrirSalir()

        msbox = QtWidgets.QMessageBox.warning(self, 'Salir', "¿Estas seguro que quieres salir?",
                                              QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if msbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/'''
