from PyQt6.QtGui import QColor

import conexion
import drivers
import var
from datetime import datetime
from PyQt6 import QtWidgets ,QtCore, QtGui
class cliente():

    def limpiaPanel2(self):
        """
            Módulo para limpiar los widgets del panel 2.
        """
        try:
            listawidgets = [var.ui.txtDniCliente, var.ui.txtDirCli, var.ui.txtRazon, var.ui.txtTel,
                            var.ui.lblcode]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbProvCli.setCurrentText('')
            var.ui.cmbMuniCli.setCurrentText('')
        except Exception as error:
            print('error limpia panel driver', error)

    def AltaCli(self):
        """
        Módulo que sirve para realizar el alta de un cliente.
        """
        try:
            driver = [var.ui.txtDniCliente, var.ui.txtRazon, var.ui.txtDirCli, var.ui.txtTel]
            newdriver = []
            for i in driver:
                newdriver.append(i.text().title())
            prov = var.ui.cmbProvCli.currentText()
            newdriver.insert(5, prov)
            muni = var.ui.cmbMuniCli.currentText()
            newdriver.insert(6, muni)
            if '@' in var.ui.txtCorreo.text():
                newdriver.insert(7,var.ui.txtCorreo.text())
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Asegurate del correo')
                mbox.exec()
            print(newdriver)



            valor = conexion.Conexion.guardarCli(newdriver)
            if valor == True:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Cliente dado de alta')
                mbox.exec()
                conexion.Conexion.mostrarClis(self)
            elif valor == False:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Asegurate que el Cliente no existe')
                mbox.exec()

            # Aviso si tenemos campos vacios
            # if newdriver[0].strip()=="" or newdriver[1]=="" or newdriver[2].strip()=="" or newdriver[3].strip()=="" or newdriver[7].strip()=="":
            #        mbox = QtWidgets.QMessageBox()
            #        mbox.setWindowTitle('Aviso')
            #        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            #        mbox.setText('Falta campos por rellenar')
            #        mbox.exec()
            # else:
            #        conexion.Conexion.guardardri(newdriver)
            #        conexion.Conexion.mostrarDrivers(self)

            '''
             index=0
            var.ui.tabDrivers.setRowCount(index+1)#crea una fila
            var.ui.tabDrivers.setItem(index, 0,QtWidgets.QTableWidgetItem(str(newdriver[0])))
            var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newdriver[1])))
            var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newdriver[2])))
            var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newdriver[3])))
            var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newdriver[4])))
            var.ui.tabDrivers.item(index,0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            print(newdriver)
            '''

        except Exception as error:
            print("Error en el Alta cliente", error)

    def correoElectronico(self):
        try:
            registro=var.ui.txtCorreo.text()
            if '@'in registro:
                print()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error no es un correo")
                mbox.exec()

        except Exception as error:
            print('Error')
    def cargartabCli(registros):
        """
            Carga el contenido del parametro registro en la tabla
            :param:parametro con los registros de los clientes
        """
        try:
            var.ui.tabCli.clearContents()
            index = 0
            for registro in registros:
                var.ui.tabCli.setRowCount(index + 1)  # crea una fila
                var.ui.tabCli.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabCli.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabCli.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabCli.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabCli.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabCli.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabCli.setItem(index, 6, QtWidgets.QTableWidgetItem(str(registro[6])))
                var.ui.tabCli.setItem(index, 7, QtWidgets.QTableWidgetItem(str(registro[7])))
                var.ui.tabCli.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCli.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCli.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCli.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                index += 1
        except Exception as error:
            print("Cargar tabla", error)

    def borrarCli(self):
        """
            Módulo para borrar un cliente.
        """
        try:

            # Codigo para preguntar si quiere modificar o borrar la fecha de baja

            dni = var.ui.txtDniCliente.text()
            conexion.Conexion.borrarCli(dni)
            cliente.cargartabCli(conexion.Conexion.mostrarClis(self))

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error no se puede borrar")
            mbox.exec()

    def cargarCli(self):
        """
            Este módulo carga los datos de un cliente seleccionado en la tabla de clientes
             en los widgets correspondientes.
        """
        try:

            drivers.Drivers.limpiaPanel(self)
            row = var.ui.tabCli.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneCli(fila[0])
            # registro1 = conexion.Conexion.comprobarFechaBaja(fila[0])
            datos = [var.ui.lblcode, var.ui.txtDniCliente, var.ui.txtRazon, var.ui.txtDirCli, var.ui.txtTel,
                     var.ui.cmbProvCli, var.ui.cmbMuniCli]

            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            var.ui.txtcifcli.setText(var.ui.txtDniCliente.text())


        except Exception as error:
            print("Error al cargar datos en la tabla", error)

    def cargarDatosCli(registro):
        """
           Módulo para cargar los datos de un cliente en los widgets correspondientes.

           :param registro: Lista que contiene los datos del cliente.
           """
        try:
            datos = [var.ui.lblcode, var.ui.txtDniCliente, var.ui.txtRazon, var.ui.txtDirCli, var.ui.txtTel,
                     var.ui.cmbProvCli, var.ui.cmbMuniCli]

            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))


        except Exception as error:
            print('error al cargar datos', error)
    def buscarCliTabla(codigo):
        """
           Módulo para buscar un cliente en la tabla de clientes según su código.

           :param codigo: Código del cliente a buscar en la tabla.
           """
        try:
            for fila in range(var.ui.tabCli.rowCount()):
                if var.ui.tabCli.item(fila, 0).text() == str(codigo):
                    var.ui.tabCli.selectRow(fila)
                    '''
                    var.ui.panDrivers.scrollToItem(var.ui.panDrivers.item(fila,0))
                    var.ui.panDrivers.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    var.ui.panDrivers.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(registro[3])))
                    var.ui.panDrivers.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(registro[4])))
                    var.ui.panDrivers.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(registro[8])))
                    var.ui.panDrivers.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[10])))
                    var.ui.panDrivers.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(registro[11])))
                    var.ui.panDrivers.item(fila, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.panDrivers.item(fila, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.panDrivers.item(fila, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.panDrivers.item(fila, 0).setBackground(QColor(255, 241, 150))
                    var.ui.panDrivers.item(fila, 1).setBackground(QColor(255, 241, 150))
                    var.ui.panDrivers.item(fila, 2).setBackground(QColor(255, 241, 150))
                    var.ui.panDrivers.item(fila, 3).setBackground(QColor(255, 241, 150))
                    var.ui.panDrivers.item(fila, 4).setBackground(QColor(255, 241, 150))
                    var.ui.panDrivers.item(fila, 5).setBackground(QColor(255, 241, 150)) '''
        except Exception as error:
            print('Error buscar Driver', error)

    def buscarCli(self):
        """
            Este módulo se utiliza para buscar un cliente por su DNI.
        """
        try:
            dni = var.ui.txtDniCliente.text()
            registro = conexion.Conexion.codCli(dni)
            if registro is None:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error en la busqueda de dni")
                mbox.exec()

            else:
                cliente.cargarDatosCli(registro)
                cliente.buscarCliTabla(registro[0])

                print("Entrou en buscar dri 2")
        except Exception as error:
            print("Error en la busqueda ", error)

    def ModifCli(self):
        """
             Módulo para modificar un cliente.
        """
        try:

            driver = [var.ui.lblcode, var.ui.txtDniCliente, var.ui.txtRazon, var.ui.txtDirCli, var.ui.txtTel]
            modifdriver = []
            for i in driver:
                modifdriver.append(i.text().title())
            prov = var.ui.cmbProvCli.currentText()
            modifdriver.insert(5, prov)
            muni = var.ui.cmbMuniCli.currentText()
            modifdriver.insert(6, muni)

            conexion.Conexion.modifCli(modifdriver)
        except Exception as error:
            print('Error')

    def buscaclifac(self):
        """
             Módulo para buscar un cliente por su DNI en la ventana de facturación.
        """
        try:
            dni = var.ui.txtcifcli.text()
            registro = conexion.Conexion.codCli(dni)
            if registro is None:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error en la busqueda de dni")
                mbox.exec()

            else:
                cliente.cargarDatosCli(registro)
                cliente.buscarCliTabla(registro[0])

                print("Entrou en buscar dri 2")
        except Exception as error:
            print("Error en la busqueda ", error)