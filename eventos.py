import locale
import os.path
import shutil
import sys
import xlwt
import xlrd
from PyQt6.uic.properties import QtGui

import conexion
import drivers
import var,sys,locale
import time
import zipfile
import datetime
import shutil
from PyQt6 import QtWidgets, QtCore
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Eventos():
    def salir(self):
        """
        Este módulo es un evento que cierra el programa
        """
        try:
            sys.exit(0)
        except Exception as error:
            print(error, "en modulo eventos")

    def abrirCalendar(self):
        """
        Módulo que abre el calendario
        """
        try:
            var.calendar.show()
        except Exception as error:
            print("error en abrir calendar", error)
    def abrirCalendarfac(self):
        """
            Módulo que abre el calendario del apartado de facturas
        """
        try:
            var.calendarfac.show()
        except Exception as error:
            print("error en abrir calendarfac", error)

    def acercaDe(self):
        """
            Módulo que muestra el acerca de de la aplicacion
        """
        try:
            var.AcercaDe.show()
        except Exception as error:
            print("error en acercaDe", error)

    def abrirSalir(self):
        """
            Módulo que muestra la ventana de salida
        """
        try:
            var.salir.show()
        except Exception as error:
            print("error en abrir calendar", error)

    def cancelarSalir(self):
        """
            Módulo que oculta la ventana de salida
        """
        try:
            var.salir.hide()
        except Exception as error:
            print("error al cancelar salida", error)

    def salirAcercaDe(self):
        """
        Módulo que oculta el acercade
        """
        try:
            var.AcercaDe.hide()
        except Exception as error:
            print("error al cancelar salida", error)

    def cargarStatusBar(self):
        """
        Módulo que carga nuestra barra de estado con la fecha
        """
        try:
            fecha = time.strftime("%A") + " - " + time.strftime("%x") + "  " + var.version
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)

        except Exception as error:
            print("Error al cargar en el statusBar", error)


    def selEstado(self):
        """
        Módulo para indicar el cambio de estado
        """
        if var.ui.rbtTodos.isChecked():
            print('Pulsaste todos')
        elif var.ui.rbtAlta.isChecked():
            print('Pulsaste altas')
        elif var.ui.rbtBaja.isChecked():
            print('Pulsaste baja')

    def resizeTabdrivers(self):#redimension de las filas en la tabla
        """
            Este módulo redimensiona la tabla de drivers
        """
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i == 0  or i == 3 or  i == 4:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2 :
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("Error en las dimentsiones de tabla",error)
    def resizeTabFacturas(self):
        """
         Este módulo redimensiona la tabla de facturas
         """
        try:
            header = var.ui.tablaFacturas.horizontalHeader()
            for i in range(2):
                if i == 0 :
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 :
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("Error en las dimentsiones de tabla Factura",error)
    def resizeTabviajes(self):
        """
                   Este módulo redimensiona la tabla de viajes
        """
        try:
            header = var.ui.tbviajes.horizontalHeader()
            for i in range(5):
                if i == 0  or i == 3 :
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2 or i==5:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("Error en las dimentsiones de tabla Factura",error)
    def resizeTabvTarifa(self):
        """
                   Este módulo redimensiona la tabla de viajes
        """
        try:
            header = var.ui.tbTarifa.horizontalHeader()
            for i in range(3):
                if i == 0  or i == 3 :
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i==2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("Error en las dimentsiones de tabla Factura",error)
    def resizeTabCli(self):
        """
                   Este módulo redimensiona la tabla de clientes
         """
        try:
            header = var.ui.tabCli.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 2 or i == 4:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("Error en las dimentsiones de tabla", error)

    def formatCajaTexto(self = None):
        """
            Módulo que da forma a la cajas de texto de txtApel ,txtNombre y txtSalario
        """
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))
        except Exception as error:
            print("Error letra capital",error)


    def numeroCorrecto(self = None):
        """
        Módulo que comprueba si un numero de telefono tiene el formato correcto
        """
        try:
            numeroMovil = var.ui.txtMovil.text()

            var.ui.txtMovil.setText(numeroMovil)
            valor ='123456789'

            for n in numeroMovil:
                 if n in valor and len(numeroMovil) == 9:
                        pass

                 else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Valor de Movil Incorrecto (00000000.00)')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtMovil.setText("")
                    break

        except Exception as error:
            print("Error de numero movil",error)

    def NumeroCorrecto2(self =None):
        """
        Módulo que comprueba si un numero de telefono tiene el formato correcto
        """
        try:
            numeroMovil = var.ui.txtTel.text()

            var.ui.txtTel.setText(numeroMovil)
            valor = '123456789'

            for n in numeroMovil:
                if n in valor and len(numeroMovil) == 9:
                    pass

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Valor de Movil Incorrecto (00000000.00)')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtTel.setText("")
                    break

        except Exception as error:
            print("Error de numero movil", error)



    def mostrarsalir(self=None):
        """
            Módulo de la ventana de salida
        """
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle('Confirmar Salida')
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setText('¿Está seguro de que desea salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()


    def crearbackup(self):
        """
            Móduloa para crea una copia de la base de datos y la guarda en un .zip
            donde podemos indicar donde queremos guardarlo
        """
        try:

            fecha = datetime.datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%M_%S')
            copia = (str(fecha+'_backup.zip'))
            directorio, filename = var.dlgAbrir.getSaveFileName(None,'Guardar Copia Seguridad', copia, '.zip')
            if var.dlgAbrir.accept and filename !='':
                fichzip = zipfile.ZipFile(copia,'w')
                fichzip.write(var.bbdd,os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia),str(directorio))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Informacion')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de seguridad creada')
                msg.exec()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en copia de seguridad', error)
            msg.exec()
    def restaurarbackup(self):
        """
            Módulo en que seleccionamos el .zip con la base de datos para añadirla como la nueva
            base de datos que queremos utilizar
        """
        try:
            filename= var.dlgAbrir.getOpenFileName(None,'Restaurar copia de seguridad',
                                                 '','*.zip;;All Files(*)')
            file = filename[0]
            if var.dlgAbrir.accept and file:
                with zipfile.ZipFile(str(file),'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            #conexion.Conexion.conexion()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Informacion')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Copia de seguridad resturada')
            msg.exec()
            conexion.Conexion.mostrarDrivers(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error restauración en copia de seguridad', error)
            msg.exec()

    def exportarDatosxl(self):
        """
            Este módulo crea un excel que guarda los datos que le llegan desde
            el módulo selectDriverTodos() con la informacion de los drivers
        """
        try:
            fecha = datetime.datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%M_%S')
            file = (str(fecha)+'_Datos.xls')
            directorio, filename = var.dlgAbrir.getSaveFileName(None, 'Guardar Datos XLS', file, '.xls')
            if var.dlgAbrir.accept and filename:

                wd=xlwt.Workbook()#crear hoja de calculo
                sheet1= wd.add_sheet('Conductores')

                sheet1.write(0, 0,'ID')#escribe en la fila 0 y en la columna 0 ID
                sheet1.write(0, 1,'DNI')
                sheet1.write(0, 2, 'FechaAlta')
                sheet1.write(0, 3, 'Apellidos')
                sheet1.write(0, 4, 'Nombre')
                sheet1.write(0, 5, 'Direccion')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Municipio')
                sheet1.write(0, 8, 'Movil')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'Carnet')
                sheet1.write(0, 11, 'Fecha_Baja')
                registros = conexion.Conexion.selectDriverTodos()


                for fila,registro in enumerate(registros,1):

                    for i,valor in enumerate(registro):

                        sheet1.write(fila, i, str(valor))

                wd.save(directorio)
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Exportación de Datos Realizada')
            msg.exec()
            var.dlgAbrir.hide()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Exportar Datos en Hoja de calculo', error)
            msg.exec()

    def importarDatosxls(self): #importar datos de un xls
        """
            Módulo que importa datos de los drivers de un excel a nuestra base de datos
        """
        try:
            estado = 0
            drivers.Drivers.limpiaPanel(self)
            filename, _ = var.dlgAbrir.getOpenFileName(None, 'Importar datos',
                                                       '', '*.xls;;All Files (*)')
            if filename:
                file = filename
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j == 1:
                                dato = xlrd.xldate_as_datetime(datos.cell_value(i, j), documento.datemode)
                                dato = dato.strftime('%d/%m/%Y')
                                new.append(str(dato))
                            else:
                                new.append(str(datos.cell_value(i, j)))

                        if drivers.Drivers.validarDni(str(new[0])):
                            conexion.Conexion.guardardri(new,1)
                        elif estado == 0:
                            estado = 1
                            msg = QtWidgets.QMessageBox()
                            msg.setModal(True)
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                            msg.setText('Hay DNI incorrectos')
                            msg.exec()

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importación de Datos Realizada')
                msg.exec()
            conexion.Conexion.mostrarDrivers(self)
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Importar Datos de la  Hoja de calculo', error)
            msg.exec()

