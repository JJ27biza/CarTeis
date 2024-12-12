from PyQt6 import QtWidgets
from PyQt6 import QtWidgets ,QtCore, QtGui

import cliente
import conexion
import var
from drivers import Drivers


class Facturas():

    def limpiarPanelfac(self):
        """
        Módulo que limpia los widgets donde podemos insertar texto en
        la parte de las Facturas
        """
        try:
            listawidgets = [var.ui.lblcdfact,var.ui.txtcifcli,var.ui.txtAltafac,var.ui.txtKm]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbdriver.setCurrentText('')
            var.ui.cmbOrigen_1.setCurrentText('')
            var.ui.cmbOrigen_2.setCurrentText('')
            var.ui.cmbDestino_1.setCurrentText('')
            var.ui.cmbDestino_2.setCurrentText('')

        except Exception as error:
            print('error limpia panel driver', error)
    def limpiarPanelviaje(self):
        """
            Este módulo solo limpia los widgets que están relacionado con los viajes
        """
        try:

            listawidgets = [var.ui.txtKm]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbOrigen_1.setCurrentText('')
            var.ui.cmbOrigen_2.setCurrentText('')
            var.ui.cmbDestino_1.setCurrentText('')
            var.ui.cmbDestino_2.setCurrentText('')
        except Exception as error:
            print('Error limpiar viaje',error)
    def buscaclifac(self):
        """
         Módulo que busca en la base de datos si el cliente existe a traves del dni
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
                var.ui.txtcifcli.setText('')

            else:
               cliente.cliente.cargarDatosCli(registro)
               cliente.cliente.buscarCliTabla(registro[0])
               print("Entrou en buscar dri 2")
        except Exception as error:
            print("Error en la busqueda ", error)

    def cargaFecha(qDate):
        """
        Este módulo carga en un widgets la fecha de hoy
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtAltafac.setText(str(data))
        except Exception as error:
            print("Error en el calendario carga", error)

    def altaFactura(self):
        """
            Módulo que comprueba que el los widgets son validos
            y llama al módulo  altafacturacion(registro) para
            almacenarlo en la base de datos
        """
        try:
            registro=[var.ui.txtcifcli.text(),var.ui.txtAltafac.text(),var.ui.cmbdriver.currentText().split(',')[0]]
            if len(var.ui.txtcifcli.text())<=0:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Campos vacios")
                mbox.exec()
            elif len(var.ui.txtAltafac.text()) <= 0:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Campos vacios")
                mbox.exec()
            elif len(var.ui.cmbdriver.currentText().split(',')[0]) <= 0:
              mbox = QtWidgets.QMessageBox()
              mbox.setWindowTitle('Aviso')
              mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
              mbox.setText("Campos vacios")
              mbox.exec()
            else:
                conexion.Conexion.altafacturacion(registro)
        except Exception as error:
            print("Error alta factura",error)

    def modifTarifa(self):
        """
            Módulo que comprueba que el los widgets son validos
            y llama al módulo  altafacturacion(registro) para
            almacenarlo en la base de datos
        """
        try:
            registro = [var.ui.txtModNaci.text(), var.ui.txtModLocal.text(), var.ui.txtModProv.text()]
            if len(var.ui.txtModNaci.text()) <= 0:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Campos vacios")
                mbox.exec()
            elif len(var.ui.txtModLocal.text()) <= 0:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Campos vacios")
                mbox.exec()
            elif len(var.ui.txtModProv.text()) <= 0:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Campos vacios")
                mbox.exec()
            else:
                conexion.Conexion.modifTarifa(registro)
        except Exception as error:
            print("Error alta factura", error)


    def cargartablafact(registros):
        """
            :param se le pasa el registro a añadir en la tabla
            Módulo que pinta en la tabla los registros que le pasamos por parametro
        """
        try:
            index = 0
            for registro in registros:
                var.ui.tablaFacturas.setRowCount(index + 1)
                var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("Cargar tabla", error)

    def cargartablaTarifa(registros):
        """
            :param se le pasa el registro a añadir en la tabla
            Módulo que pinta en la tabla los registros que le pasamos por parametro
        """
        try:
            index = 0
            for registro in registros:
                var.ui.tbTarifa.setRowCount(index + 1)
                var.ui.tbTarifa.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tbTarifa.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tbTarifa.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tbTarifa.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tbTarifa.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tbTarifa.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("Cargar tabla Tarifa", error)

    def cargarfact(self):
        """
            Módulo que carga la factura que seleccionamos en la tabla
            en los widgets correspondientes
        """
        try:

            Facturas.limpiarPanelfac(self)
            row = var.ui.tablaFacturas.selectedItems()
            fila = [dato.text() for dato in row]
            print('Entrando en cargarfac')
            registro = conexion.Conexion.onefac(fila[0])

            datos = [var.ui.lblcdfact, var.ui.txtcifcli, var.ui.txtAltafac, var.ui.cmbdriver]

            for i, dato in enumerate(datos):
                if i == 3:
                   conteniod=conexion.Conexion.codigoselDrivers(registro[i])
                   var.ui.cmbdriver.setCurrentText(str(conteniod))
                else:
                    dato.setText(str(registro[i]))


        except Exception as error:
            print("Error al cargar datos en la tabla de fac", error)


    def altaviaje(self):
        """
          Módulo que guarad un viaje en la base de datos
        """
        try:
            code=int(var.ui.lblcdfact.text())
            km= int(var.ui.txtKm.text())
            tarifa = conexion.Conexion.datosviaje(self)

            newdriver = []

            prov = var.ui.cmbOrigen_2.currentText()
            newdriver.insert(1, prov)
            muni = var.ui.cmbDestino_2.currentText()
            newdriver.insert(2, muni)
            newdriver.insert(0,code)
            newdriver.insert(4,km)
            newdriver.insert(3,float(tarifa))
            conexion.Conexion.cargarLineaViaje(newdriver)

        except Exception as error:
            print('Error alta viaje',error)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Faltan campos o es Erroneo')
            msg.exec()




    def cargarTablaViajes(registros):
        """
            :param son los registros que le pasamos para que pinte en la tabla
            Módulo que carga en la tabla los registros pasados por parametros
        """
        try:
            subtotal=0.0
            var.ui.tbviajes.clearContents()
            index =0
            for registro in registros:

                var.ui.tbviajes.setRowCount(index+1)
                var.ui.tbviajes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tbviajes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tbviajes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tbviajes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tbviajes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))

                totalviaje=round(float(registro[3])+float(registro[4]),2)
                var.ui.tbviajes.setItem(index, 5, QtWidgets.QTableWidgetItem(str(totalviaje)+' €'))
                var.ui.tbviajes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tbviajes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tbviajes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tbviajes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tbviajes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tbviajes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                #btn_borrar = QtWidgets.QPushButton()
                #btn_borrar.setFixedSize(1,1)
                #btn_borrar.setIcon(QtGui.QIcon('./IMG/Coche.png'))

                var.botonDel = QtWidgets.QPushButton()
                var.botonDel.setFixedSize(30, 28)
                var.botonDel.setIcon(QtGui.QIcon("./IMG/basura.png"))
                var.ui.tbviajes.horizontalHeader().setSectionResizeMode(6,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                var.ui.tbviajes.setColumnWidth(6, 50)
                var.ui.tbviajes.setCellWidget(index, 6, var.botonDel)
                var.botonDel.clicked.connect(Facturas.borrarViaje)


                 #Sumar el subtotal
                subtotal += totalviaje
                descuento = var.ui.txtDescuento.text()
                if descuento == '':
                    print('Hola')
                    descuentoTotal = 0
                else:
                    descuentoTotal = int(subtotal) - descuento

                index += 1

                iva_porc = 0.21
                iva = subtotal * iva_porc
                total_iva = subtotal + iva
                # Asignar el subtotal al QLabel después del bucle
                var.ui.lbl_subTotal.setText("{:.2f}".format(subtotal) + " \u20AC")
                var.ui.lbl_descuento.setText(str(descuentoTotal)+ " \u20AC")
                var.ui.lbl_iva.setText("{:.2f}".format(iva) + " \u20AC")
                var.ui.lbl_total.setText("{:.2f}".format(total_iva) + " \u20AC")


        except Exception as error:
            print('Tabla viajes error', error)

    def cargarFactura(self):
        """
            Módulo que carga las viajes en la tabla
        """
        try:
            code=var.ui.lblcdfact.text()
            print('codigo',code)
            conexion.Conexion.mostrarViaje(code)

        except Exception as error:
            print('cargarFACTURA', error)

    def cargarDatosViaje(self):
        """
            Módulo que carga los datos de un viaje en los widgets correspondientes
        """
        try:

            row = var.ui.tbviajes.selectedItems()
            fila = [dato.text() for dato in row]
            print('Fila',fila)

            registro = conexion.Conexion.oneViaje(fila[0])
            datos =[var.ui.cmbOrigen_1, var.ui.cmbOrigen_2,var.ui.cmbDestino_1,var.ui.cmbDestino_2,var.ui.txtKm]

            registro1=conexion.Conexion.getProvincia(fila[1])
            registro2=conexion.Conexion.getProvincia(fila[2])


            nombre1=conexion.Conexion.nombreProv(registro1[0])
            nombre2=conexion.Conexion.nombreProv(registro2[0])


            for i,dato in enumerate(datos):

                if i==0:
                  datos[0].setCurrentText(str(nombre1[0]))
                if i==1:
                   var.ui.cmbOrigen_2.setCurrentText(str(fila[1]))
                if i==2:
                    var.ui.cmbDestino_1.setCurrentText(str(nombre2[0]))
                if i==3:
                    var.ui.cmbDestino_2.setCurrentText(str(fila[2]))
                if i == 4:
                    var.ui.txtKm.setText(str(fila[4]))

        except Exception as error:
            print('error al cargar datos viaje', error)

    def borrarViaje(self):
        """
            Este módulo borra los datos que seleccionamos en la tabla de viajes
        """
        try:
            row = var.ui.tbviajes.selectedItems()
            fila = [dato.text() for dato in row]

            conexion.Conexion.borradoViaje(fila[0])


        except Exception as error:
            print('Error en el borrado de viaje ',error)
    def datosViaje(self=None):
        """
            Módulo que devuelve el contenido de los widgets
        :return: devuelve en contenido que le pasan los widgets
        :rtype: bytearray
        """
        try:
           tarifa=conexion.Conexion.datosviaje(self)
           registro=var.ui.cmbOrigen_1.currentText(),var.ui.cmbOrigen_2.currentText(),var.ui.cmbDestino_1.currentText(),var.ui.cmbDestino_2.currentText(),tarifa,var.ui.txtKm.text()

           return registro
        except Exception as error:
            print('Error datos viaje',error)

    def cargarClientesEspecifico(self):
        try:
            registro = var.ui.txtcifcli.text()
            if registro != '':
                print('Este es el registro: ', registro)
                conexion.Conexion.cargarFacturasEspecifica(registro)

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Campo vacio')
                msg.exec()

        except Exception as error:
            print('Error en el cliente especifico')


