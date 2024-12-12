from PyQt6.QtGui import QColor

import cliente
import conexion
import var
from datetime import datetime
from PyQt6 import QtWidgets ,QtCore, QtGui

class Drivers():

    def limpiaPanel(self):
        """
              Módulo para limpiar los widgets del panel de los driver.
        """
        try:
            listawidgets = [var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtNombre, var.ui.txtMovil, var.ui.txtSalario,
                            var.ui.txtApel,
                            var.ui.txtDir, var.ui.lblValidarDni, var.ui.lblCodeBD_2]
            for i in listawidgets:
                i.setText(None)
            chk_licencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chk_licencia:
              i.setChecked(False)
            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')
        except Exception as error:
            print('error limpia panel driver', error)


    def cargaFecha(qDate):
        """
            Este módulo carga la fecha de hoy en el widgets txtFechaAlta
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAlta.setText(str(data))
        except Exception as error:
            print("Error en el calendario carga", error)
    def cargaFechaBaja(qDate):
        """
             Este módulo carga la fecha de hoy en el widgets txtFechaAlta
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.calendarBaja.txtFechaBaja.setText(str(data))
        except Exception as error:
            print("Error en el calendario carga", error)

    def validarSalario(self):
        """
            Comprueba que el salario es valido
        """
        try:
            salario = var.ui.txtSalario.text()
            try:
                float(salario)
            except Exception as error:
                print('Salario erroneo',error)
        except Exception as error:
            print('Salario Invalido')

    def validarDni(dni):
        """
            Este módulo valida si el dni que le pasamos por parametro es un dni valido
        :return:le pasamos el dni que queremos validar
        :rtype: boolean
        """
        try:

            dni = str(dni).upper()  # poner mayuscula
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:  # compruebo que son 9
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDni.setStyleSheet('color:green;')
                    var.ui.lblValidarDni.setText('V')
                    return True
                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.clear()
                    var.ui.txtDni.setFocus()
                    return False


            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.clear()
                var.ui.txtDni.setFocus()
                return False



        except Exception as error:
            print("Error al validar dni", error)

    def altaDriver(self):
        """
               Módulo que sirve para realizar el alta de un driver.
        """
        try:
            driver =[var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApel,  var.ui.txtNombre, var.ui.txtDir, var.ui.txtMovil, var.ui.txtSalario]
            newdriver = []
            for i in driver:
                newdriver.append(i.text().title())
            prov = var.ui.cmbProv.currentText()
            newdriver.insert(5, prov)
            muni = var.ui.cmbMuni.currentText()
            newdriver.insert(6, muni)
            licencias= []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())

            newdriver.append('-'.join(licencias))
            valor= conexion.Conexion.guardardri(newdriver)
            if valor == True:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Empleado dado de alta')
                mbox.exec()
            elif valor == False:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Asegurate que el conductor no existe')
                mbox.exec()


            #Aviso si tenemos campos vacios
            #if newdriver[0].strip()=="" or newdriver[1]=="" or newdriver[2].strip()=="" or newdriver[3].strip()=="" or newdriver[7].strip()=="":
            #        mbox = QtWidgets.QMessageBox()
            #        mbox.setWindowTitle('Aviso')
            #        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            #        mbox.setText('Falta campos por rellenar')
            #        mbox.exec()
            #else:
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
            print("Error en el Alta Driver",error)





    def cargartabladri(registros):
        """
                   Carga el contenido del parametro registro en la tabla
                   :param:parametro con los registros de los driver
        """
        try:
            var.ui.tabDrivers.clearContents()
            index = 0
            for registro in registros:
                 var.ui.tabDrivers.setRowCount(index + 1)  # crea una fila
                 var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                 var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                 var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                 var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                 var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                 var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                 var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                 var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                 var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                 var.ui.tabDrivers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                 index+=1
        except Exception as error:
            print("Cargar tabla",error)



    def cargadriver(self):
        """
                    Este módulo carga los datos de un cliente seleccionado en la tabla de drivers
                     en los widgets correspondientes.
        """
        try:

            Drivers.limpiaPanel(self)
            row = var.ui.tabDrivers.selectedItems()
            fila = [ dato.text() for dato in row]
            registro = conexion.Conexion.onedriver(fila[0])
            registro1 = conexion.Conexion.comprobarFechaBaja(fila[0])
            print('Cogiendo el registro',registro,registro1)
            datos = [var.ui.lblCodeBD_2, var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApel, var.ui.txtNombre,
                     var.ui.txtDir, var.ui.cmbProv, var.ui.cmbMuni, var.ui.txtMovil, var.ui.txtSalario]

            for i, dato in enumerate(datos):
               if i == 6 or i == 7:
                   dato.setCurrentText(str(registro[i]))
               else:
                   dato.setText(str(registro[i]))
            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)

        except Exception as error:
           print("Error al cargar datos en la tabla",error)



    def cargardatos(registro):
        """
                   Módulo para cargar los datos de un drivers en los widgets correspondientes.

                   :param registro: Lista que contiene los datos del drivers.
                   """
        try:
            datos = [var.ui.lblCodeBD_2, var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApel, var.ui.txtNombre,
                     var.ui.txtDir, var.ui.cmbProv, var.ui.cmbMuni, var.ui.txtMovil, var.ui.txtSalario]

            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)


        except Exception as error:
            print('error al cargar datos', error)






    def buscarDriverTabla(codigo):
        """
                  Módulo para buscar un driver en la tabla de driver según su código.

                  :param codigo: Código del driver a buscar en la tabla.
                  """
        try:
            for fila in range(var.ui.tabDrivers.rowCount()):
                if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                    var.ui.tabDrivers.selectRow(fila)
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
                 print('Error buscar Driver',error)




    def buscarDri(self):
        """
                   Este módulo se utiliza para buscar un driver por su DNI.
               """
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codDri(dni)
            if registro is None:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error en la busqueda de dni")
                mbox.exec()

            else:
                Drivers.cargardatos(registro)
                Drivers.buscarDriverTabla(registro[0])


                print("Entrou en buscar dri 2")
        except Exception as error:
            print("Error en la busqueda ",error)

    def modiDri(self):
        """
                     Módulo para modificar un driver.
                """
        try:
            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.comprobarFechaBaja(fila[0])
            if registro == ['']:
                driver = [var.ui.lblCodeBD_2, var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApel, var.ui.txtNombre, var.ui.txtDir,
                          var.ui.txtMovil, var.ui.txtSalario]
                modifdriver = []
                for i in driver:
                    modifdriver.append(i.text().title())
                prov = var.ui.cmbProv.currentText()
                modifdriver.insert(6, prov)
                muni = var.ui.cmbMuni.currentText()
                modifdriver.insert(7, muni)
                licencias = []
                chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
                for i in chklicencia:
                    if i.isChecked():
                        licencias.append(i.text())

                modifdriver.append('-'.join(licencias))
                conexion.Conexion.modifDriver(modifdriver)
            else:
                print('Entrada')
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Modificar o Alta')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Modificar o dar de Alta a un cliente')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Fecha')
                mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Modificar')
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Alta')
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)

                if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                    Drivers.ventanaModifFechaBaja(self)
                elif mbox.exec() == QtWidgets.QMessageBox.StandardButton.Ok:
                    Drivers.borrarFechaBaja(self)
                else:
                    driver = [var.ui.lblCodeBD_2, var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApel, var.ui.txtNombre,
                              var.ui.txtDir,
                              var.ui.txtMovil, var.ui.txtSalario]
                    modifdriver = []
                    for i in driver:
                        modifdriver.append(i.text().title())
                    prov = var.ui.cmbProv.currentText()
                    modifdriver.insert(6, prov)
                    muni = var.ui.cmbMuni.currentText()
                    modifdriver.insert(7, muni)
                    licencias = []
                    chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
                    for i in chklicencia:
                        if i.isChecked():
                            licencias.append(i.text())

                    modifdriver.append('-'.join(licencias))
                    conexion.Conexion.modifDriver(modifdriver)

        except Exception as error:
            print("Error en la modifDriv")




    def borraDriv(self):

        """
                   Módulo para borrar un driver.
         """
        try:

            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.comprobarFechaBaja(fila[0])
            print('Modificar fecha baja', registro)
            #Codigo para preguntar si quiere modificar o borrar la fecha de baja

            dni = var.ui.txtDni.text()
            conexion.Conexion.borraDriv(dni)
            Drivers.cargartabladri(conexion.Conexion.mostrarDrivers(self))

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error no se puede borrar")
            mbox.exec()



    def cambiarFechaBaja(self):
        """
            Módulo que permite cambiar la fecha al abrir un calendario y cambia
            la fecha en la base de datos
        """
        try:
            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registro1 = var.calendarBaja.txtFechaBaja.text()
            print('Registro1',registro1)
            print(fila[0])

            if var.calendarBaja.btnFechaBaja.clicked:
                print('se ha entrado aqui')
                var.dlgCalendarBaja.hide()
                conexion.Conexion.actualizarFechaBaja(registro1, fila[0])
                conexion.Conexion.mostrarDrivers(self)
        except Exception as error:
            print('Error en el cambio de fecha Baja',error)
    def borrarFechaBaja(self):
        """
            Modulo que elimina el contenido  del campo de fecha baja del campo que seleccionamos
        """
        row = var.ui.tabDrivers.selectedItems()
        fila = [dato.text() for dato in row]
        print('Entrastes en el borrado')
        conexion.Conexion.borrarFechaBaja(fila[0])
        conexion.Conexion.mostrarDrivers(self)
        registro = conexion.Conexion.onedriver(fila[0])
        print(registro)
    def ventanaModifFechaBaja(self):
        """
            Metódo para comprobar la entrada de la ventana modif fechabaja
        """
        try:
            print('Entrando den fecha baja')
            var.dlgCalendarBaja.show()
        except Exception as error:
            print('Error al modificar la fecha de baja',error)

