from datetime import datetime

from PyQt6 import QtWidgets,QtSql,QtCore

import Factura
import cliente
import drivers
import var

class Conexion():

    def conexion(self= None):
        """
            Este módulo permite la conexion con nuestra base de datos indicandole su nombre
        """
        var.bbdd='bbdd2.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print('error de conexión')

        else:
            print('base datos conectada')

    def conexionCli(self=None):
        """
            Este módulo permite la conexion con nuestra base de datos de clientes indicandole su nombre
        """
        var.bbdd = 'clientes.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print('error de conexión')

        else:
            print('base datos conectada')


    def cargaprov(self = None):
        """
            Este módulo selecciona en la base de dotos todas las provincias y las carga en un comboBox
        """
        try:

            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProv.addItem('')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))

        except Exception as error:
            print("Error en la carga de la provincia",error)

    def cargaprovCli(self=None):
        """
                Este módulo selecciona en la base de dotos todas las provincias para los clientes y las carga en un comboBox
        """
        try:

            var.ui.cmbProvCli.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProvCli.addItem('')
                while query.next():
                    var.ui.cmbProvCli.addItem(query.value(0))

        except Exception as error:
            print("Error en la carga de la provincia", error)

    def selMuni(self = None):
        """
            Este módulo se conecta a la base de datos y carga los municipios dependiendo
            de la provincia que esté añadida en el comboBox de provincias y carga
            los municipios de esa provincia
        """
        try:
            id=0
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMuni.addItem('')
                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))

        except Exception as  error:
            print("Error en los municipios", error)


    def selMuniCli(self=None):
        """
            Este módulo se conecta a la base de datos  de clientes y carga los municipios dependiendo
            de la provincia que esté añadida en el comboBox de provincias y carga
            los municipios de esa provincia

        """
        try:
            id = 0
            var.ui.cmbMuniCli.clear()
            prov = var.ui.cmbProvCli.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMuniCli.addItem('')
                while query1.next():
                    var.ui.cmbMuniCli.addItem(query1.value(0))

        except Exception as error:
            print("Error en los municipios", error)

    def cargaprovFactOrigen(self=None):
        """
             Este módulo selecciona en la base de dotos todas las provincias
             y las carga en un comboBox en el apartado de las Facturas en
             este caso sirve para seleccionar el Origen
        """
        try:

            var.ui.cmbOrigen_1.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbOrigen_1.addItem('')
                while query.next():
                    var.ui.cmbOrigen_1.addItem(query.value(0))

        except Exception as error:
            print("Error en la carga de la provincia Origen", error)
    def cargaprovFactDestino(self=None):
        """
              Este módulo selecciona en la base de dotos todas las provincias
             y las carga en un comboBox en el apartado de las Facturas en
             este caso sirve para seleccionar el Destino

        """
        try:

            var.ui.cmbDestino_1.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbDestino_1.addItem('')
                while query.next():
                    var.ui.cmbDestino_1.addItem(query.value(0))

        except Exception as error:
            print("Error en la carga de la provincia Destino", error)

    def selMuniOrigen(self=None):
        """
             Este módulo se conecta a la base de datos  de provincia y de municipios
            y carga los municipios dependiendode la provincia que esté añadida en el
            comboBox de provincias y carga los municipios de esa provincia que será el
            municipio de origen
        """
        try:
            id = 0
            var.ui.cmbOrigen_2.clear()
            prov = var.ui.cmbOrigen_1.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbOrigen_2.addItem('')
                while query1.next():
                    var.ui.cmbOrigen_2.addItem(query1.value(0))

        except Exception as error:
            print("Error en los municipios", error)

    def selMuniDestino(self=None):
        """
            Este módulo se conecta a la base de datos  de provincia y de municipios
            y carga los municipios dependiendode la provincia que esté añadida en el
            comboBox de provincias y carga los municipios de esa provincia que será el
            municipio de destino

        """
        try:
            id = 0
            var.ui.cmbDestino_2.clear()
            prov = var.ui.cmbDestino_1.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbDestino_2.addItem('')
                while query1.next():
                    var.ui.cmbDestino_2.addItem(query1.value(0))

        except Exception as error:
            print("Error en los municipios", error)


    def guardardri(newdriver):
        """

        :return:modulo que devuelve la inserccion de un driver
        :rtype: bytearray

        Este modulo inserta en la base de datos un driver y
        llama al método de mostrarDriver()
        """
        try:

            query =QtSql.QSqlQuery()
            query.prepare('insert into drivers (dnidri, altadri, apeldri, nombredri, direcciondri, provdri, ' 
                          ' munidri, movildri, salario, carnet) VALUES (:dni, :alta, :apel, :nombre, :direccion, '
                          ' :provincia, :municipio, :movil, :salario, :carnet)')
            query.bindValue(':dni', str(newdriver[0]))
            query.bindValue(':alta', str(newdriver[1]))
            query.bindValue(':apel', str(newdriver[2]))
            query.bindValue(':nombre', str(newdriver[3]))
            query.bindValue(':direccion', str(newdriver[4]))
            query.bindValue(':provincia', str(newdriver[5]))
            query.bindValue(':municipio', str(newdriver[6]))
            query.bindValue(':movil', str(newdriver[7]))
            query.bindValue(':salario', str(newdriver[8]))
            query.bindValue(':carnet', str(newdriver[9]))

            if query.exec():

                   return True
            else:
                  return False

            Conexion.mostrarDrivers(self)

        except Exception as error:
            print("error en alta conductor",error)

    def guardarCli(newcli):
        """

        :return:Modulo que guarda los Clientes
        :rtype: bytearray
        Este módulo inserta en la base de datos los Clientes y
        llama al método de mostrarCli
        """
        try:

            query = QtSql.QSqlQuery()
            query.prepare('insert into Clientes (DNI, Razon_Social, Direccion, Telefono, Provincia, Municipio, Correo) VALUES (:dni, :social, :direc, :tel, :prov, '
                          ' :municipio, :correo) ')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':social', str(newcli[1]))
            query.bindValue(':direc', str(newcli[2]))
            query.bindValue(':tel', str(newcli[3]))
            query.bindValue(':prov', str(newcli[4]))
            query.bindValue(':municipio', str(newcli[5]))
            query.bindValue(':correo', str(newcli[6]))

            if query.exec():

                return True
            else:
                return False

            Conexion.mostrarClis(self)

        except Exception as error:
            print("error en alta cliente", error)



    def mostrarDrivers(self):
        """

        :return:Devuelve el registro de un driver
        :rtype: bytearray
        Modulo que devuelve el registro de un driver y los carga en el método cargartabladri()
        """
        try:
            registro = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select codigo, apeldri, nombredri, movildri, '
                           ' carnet, bajadri from drivers')
            if query1.exec():
                while query1.next():
                    row =[query1.value(i) for i in range(query1.record().count())]
                    registro.append(row)
            drivers.Drivers.cargartabladri(registro)
            return registro
        except Exception as error:
            print('Error mostrar driver',error)

    def mostrarClis(self):
        """

        :return: :Devuelve el registro de un cliente
        :rtype:bytearray
        Modulo que devuelve el registro de un cliente y los carga en el método cargartablaCli()
        """
        try:
            registro = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select Codigo, DNI, Razon_Social, Direccion, '
                           ' Telefono, Provincia, Municipio, Fecha_Baja from Clientes')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registro.append(row)
            cliente.cliente.cargartabCli(registro)
            return registro
        except Exception as error:
            print('Error mostrar driver', error)


    def mostrarBajaDriver(self):
        """

        :return: devuelve el registro de los drivers de baja en donde el registro baja tiene contenido
        :rtype: bytearray
        Modulo que devuelve el registro de un cliente y los carga en el método cargartablaCli()

        """
        try:
            registro = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select codigo, apeldri, nombredri, movildri, '
                           ' carnet, bajadri from drivers where bajadri is not null')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registro.append(row)
            drivers.Drivers.cargartabladri(registro)
            return registro

        except Exception as error:
            print('Error mostrarbaja driver', error)

    def mostrarBajaCli(self):
        """

        :return: devuelve el registro de los clientes de baja en donde el registro baja tiene contenido
        :rtype: bytearray
         Módulo que devuelve el registro de un cliente y los carga en el método cargartablaCli()
        """
        try:
            registro = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select Codigo, DNI, Razon_Social, Direccion, '
                           ' Telefono, Provincia, Municipio,Fecha_Baja from Clientes where Fecha_Baja is not null')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registro.append(row)
            cliente.cliente.cargartabCli(registro)
            return registro


        except Exception as error:
            print('Error mostrarbaja driver', error)

    def mostrarAltaDriver(self):
        """

        :return: devuelve el registro de los drivers de alta en donde el registro baja no tiene contenido
        :rtype: bytearray
        Módulo que devuelve el contenido de la base de datos y llama  al método cargartabladri(registro)
        """
        try:
            registro = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select codigo, apeldri, nombredri, movildri, '
                           ' carnet, bajadri from drivers where bajadri is null')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registro.append(row)
            drivers.Drivers.cargartabladri(registro)
            return registro


        except Exception as error:
            print('Error mostrarbaja driver', error)
    def mostrarAltaCli(self):
        """

        :return:  devuelve el registro de los clientes de alta en donde el registro baja no tiene contenido
        :rtype: bytearray
        Módulo que devuelve el contenido de la base de datos y llama  al método cargartabladri(registro)
        """
        try:
            registro = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select Codigo, DNI, Razon_Social, Direccion, '
                           ' Telefono, Provincia, Municipio,Fecha_Baja from Clientes where Fecha_Baja is null')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registro.append(row)
            cliente.cliente.cargartabCli(registro)
            return registro


        except Exception as error:
            print('Error mostrarbaja driver', error)

    def onedriver(codigo):
        """

        :return: devuelve la consulta de la base de datos que le hacemos
        :rtype: bytearray
        Módulo que pide un "codigo" y devuelve todos los drivers con ese código
        """
        try:
            print(codigo)
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select *  from drivers where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print ("Error en onedriver", error)

    def oneCli(codigo):
        """

        :return:  devuelve la consulta que le hacemos a la base de datos
        :rtype: bytearray
        Módulo que pide un "codigo" y devuelve todos los clientes con ese código
        """
        try:
            print(codigo)
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select *  from Clientes where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en onedriver", error)

    def comprobarFechaBaja(codigo):
        """

        :return:devuelve la fecha de baja de ese codigo que le pasamos
        :rtype: bytearray
        Módulo que devuelve la fecha de baja que le pasamos por el parametro "codigo"
        """
        try:
            print(codigo)
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select bajadri from drivers where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(1):
                        registro.append(str(query.value(i)))
            return registro


        except Exception as error:
            print('Error al comprobar la fecha de baja',error)





    def actualizarFechaBaja(fechabaja, id):
        """

        :param id:En los parametros le pasamos la fecha de baja y su "id"
        :type id: int
        Módulo que actualiza la fecha de baja del driver del "id o codigo " que le pasamos
        """
        try:

            query = QtSql.QSqlQuery()
            query.prepare('update drivers set bajadri = :bajadri where codigo= :codigo')
            query.bindValue(':codigo', int(id))
            query.bindValue(':bajadri', str(fechabaja))
            query.exec()
            print('fecha actualizada')
        except Exception as error:
            print('Error actualizar Fecha',error)

    def borrarFechaBaja(codigo):
        """
            Módulo que le pasamos por parametro el "codigo" y borra su fecha_baja en la base de datos
        """
        try:

            query = QtSql.QSqlQuery()
            query.prepare('update drivers set bajadri = null where codigo= :codigo')
            query.bindValue(':codigo', int(codigo))
            query.exec()
            print('fecha borrada')
        except Exception as error:
            print('Error borrar Fecha',error)


    def codDri(dni):
        """

        :return: devuelve desde la base de datos el codigo  donde su dni sea igual al que
        le pasamos por parametro
        :rtype: bytearray
        Módulo que devuelve el codigo de un driver dependiendo del dni que tiene
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dnidri = :dnidri')
            query.bindValue(':dnidri', str(dni))
            if query.exec():
              while query.next():
                codigo = query.value(0)
                registro = Conexion.onedriver(codigo)
                return registro

        except Exception as error:

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Avisa')
            mbox.setWindowIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("No existe")
            mbox.exec()

            print("Error en codDri",error)

    def codCli(dni):
        """

        :return:  devuelve desde la base de datos el codigo  donde su dni sea igual al que
        le pasamos por parametro
        :rtype: bytearray
        Módulo que devuelve el codigo de un cliente dependiendo del dni que tiene
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select Codigo from Clientes where DNI = :dnidri')
            query.bindValue(':dnidri', str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                    registro = Conexion.oneCli(codigo)
                    return registro

        except Exception as error:

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Avisa')
            mbox.setWindowIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("No existe")
            mbox.exec()

    def modifDriver(modifdriver):
        """
            Actualizamos en la base de datos al driver pasandole un registro "modifdriver"
            por parametro
        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select * from drivers where dnidri=:dnidri')
            query1.bindValue(':dnidri',str(modifdriver[1]))
            registro=[]
            if query1.exec():
                while query1.next():
                    for i in range(11):
                        registro.append(str(query1.value(i)))
            query = QtSql.QSqlQuery()
            query.prepare('update drivers set  dnidri = :dni, altadri = :alta, apeldri = :apel, nombredri = :nombre, '
                          ' direcciondri = :direccion, provdri = :provincia,' 
                          ' munidri = :municipio, movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')
            query.bindValue(':codigo', int(modifdriver[0]))
            query.bindValue(':dni',str(modifdriver[1]))
            query.bindValue(':alta', str(modifdriver[2]))
            query.bindValue(':apel', str(modifdriver[3]))
            query.bindValue(':nombre', str(modifdriver[4]))
            query.bindValue(':direccion', str(modifdriver[5]))
            query.bindValue(':provincia', str(modifdriver[6]))
            query.bindValue(':municipio', str(modifdriver[7]))
            query.bindValue(':movil', str(modifdriver[8]))
            query.bindValue(':salario', str(modifdriver[9]))
            query.bindValue(':carnet', str(modifdriver[10]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Datos Conductor Modificados')
                mbox.exec()
                Conexion.mostrarDrivers(self=None)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()





        except Exception as error:
            print("Error modificarDriver",error)

    def modifCli(modifCli):
        """
             Actualizamos en la base de datos al cliente pasandole un registro "modifdriver"
            por parametro
        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select * from Clientes where DNI=:dnidri')
            query1.bindValue(':dnidri',str(modifCli[1]))

            registro=[]
            if query1.exec():
                while query1.next():
                    for i in range(7):

                        registro.append(str(query1.value(i)))
                        print(registro ,'aqui tambien')
            query = QtSql.QSqlQuery()
            query.prepare('update Clientes set  DNI = :dni, Razon_Social = :social, Direccion = :direc, Telefono = :tel, '
                          ' Provincia = :prov, Municipio = :muni where Codigo = :codigo')
            query.bindValue(':codigo', int(modifCli[0]))
            query.bindValue(':dni', str(modifCli[1]))
            query.bindValue(':social', str(modifCli[2]))
            query.bindValue(':direc', str(modifCli[3]))
            query.bindValue(':tel', str(modifCli[4]))
            query.bindValue(':prov', str(modifCli[5]))
            query.bindValue(':muni', str(modifCli[6]))


            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Datos Conductor Modificados')
                mbox.exec()
                Conexion.mostrarClis(self=None)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Error: '+query.lastError().text())
                mbox.exec()





        except Exception as error:
            print("Error modificarDriver",error)

    def borraDriv(dni):
        """
            Módulo que coge la fecha de hoy y comprueba si el driver con el dni
            que le pasamos por parametros tiene fecha de baja o no si no tiene
            se la añdimos con un update dependiendo de su dni

        """
        try:
            fecha = datetime.today()
            fecha = ('{:02d}/{:02d}/{:4d}'.format(fecha.day,fecha.month,fecha.year))
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadri from drivers where'
                           ' dnidri = :dni ')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
            if str(valor) == '':
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadri = :fechabaja where '
                              ' dnidri = :dni')
                query.bindValue(':fechabaja',str(fecha))
                query.bindValue(':dni', str(dni))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Conductor dado de baja')
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText(query.lastError().text() + ' Error baja conductor')
                    mbox.exec()

        except Exception as error:
            print("error en la baja driver en conexion",error)

    def borrarCli(dni):
        """
             Módulo que coge la fecha de hoy y comprueba si el cliente con el dni
            que le pasamos por parametros tiene fecha de baja o no si no tiene
            se la añdimos con un update dependiendo de su dni
        """
        try:
            fecha = datetime.today()
            fecha = ('{:02d}/{:02d}/{:4d}'.format(fecha.day, fecha.month, fecha.year))
            query1 = QtSql.QSqlQuery()
            query1.prepare('select Fecha_Baja from Clientes where'
                           ' DNI = :dni ')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
            if str(valor) == '':
                query = QtSql.QSqlQuery()
                query.prepare('update Clientes set Fecha_Baja = :fechabaja where '
                              ' DNI = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Conductor dado de baja')
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText(query.lastError().text() + ' Error baja conductor')
                    mbox.exec()

        except Exception as error:
            print("error en la baja driver en conexion", error)

    @staticmethod
    def selectDriverTodos():
        """

        :return: devuelve todos los registros de drivers en orden por su apellido
        :rtype: bytearray
        Módulo que devuelve todos los registros de los drivers en orden por su apellido
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers order by apeldri')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]#funcion lambda
                    registro.append(row)

            return registro

        except Exception as error:
            print('error devolver todos los drivers', error)
    def selDrivers(self=None):
        """
            Módulo que selecciona el codigo, nombre y apellido de un driver si no esta de baja
            y los añade en el comboBox cmbdriver

        """
        try:

            var.ui.cmbdriver.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombredri, apeldri from drivers where bajadri is null ')
            if query.exec():
                print("ejecuta")
                var.ui.cmbdriver.addItem('')
                while query.next():
                    contenido = str(query.value(0))+',' + str(query.value(1))+' '+ str(query.value(2))
                    var.ui.cmbdriver.addItem(str(contenido))

        except Exception as error:
            print("Error en la carga de conductores ", error)
    def codigoselDrivers(codigo):
        """

        :return: devuelve el contenido de los drivers en la base de datos
        :rtype:bytearray
        Módulo que devuelve el nombre el codigo y el apellido de un driver dependiendo del codigo
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombredri, apeldri from drivers where codigo= :codigo ')
            query.bindValue(':codigo', str(codigo))
            if query.exec():
                while query.next():
                    contenido = str(query.value(0))+',' + str(query.value(1))+' '+ str(query.value(2))
            return contenido



        except Exception as error:
            print("Error en la carga de conductores ", error)

    def modifTarifa(registro):
        try:
            print(str(registro))
            if Conexion.comprobarcliente(registro[0]):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Cliente dado de baja')
                mbox.exec()
            else:
                query= QtSql.QSqlQuery()
                query.prepare('update tarifas set '
                                  'Nacional = :nacional, Local = :local, Provincial = :provincial'
                                  ' where id = 1 ')
                query.bindValue(':nacional',str(registro[0]))
                query.bindValue(':local', str(registro[1]))
                query.bindValue(':provincial', str(registro[2]))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Tarifa Modificad')
                    mbox.exec()
                    Conexion.cargarTarifas()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText(query.lastError().text() + ' Error tarifa')
                    mbox.exec()

        except Exception as error:
            print("Error alta facturacion",error)

    def altafacturacion(registro):
        """
            Este módulo sirve para registrar una nueva factura en la base de datos.

            :param registro: Una lista que contiene información de la factura (DNI del cliente, fecha y conductor).

        """
        try:
            print(str(registro))
            if Conexion.comprobarcliente(registro[0]):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Cliente dado de baja')
                mbox.exec()
            else:
                query= QtSql.QSqlQuery()
                query.prepare('insert into facturas(dnicli, fecha, driver)'
                          ' VALUES(:dni, :fecha, :driver) ')
                query.bindValue(':dni',str(registro[0]))
                query.bindValue(':fecha', str(registro[1]))
                query.bindValue(':driver', str(registro[2]))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Factura grabada')
                    mbox.exec()
                    Conexion.cargarFacturas()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText(query.lastError().text() + ' Error facturacion')
                    mbox.exec()

        except Exception as error:
            print("Error alta facturacion",error)
    def cargarFacturas(self=None):
        """
             Módulo para cargar las facturas desde la base de datos y mostrarlas en una tabla desde el metdodo cargartablafact(registro).
        """
        try:
           registros=[]
           query = QtSql.QSqlQuery()
           query.prepare('select numfac,dnicli from facturas')
           if query.exec():
             while query.next():

               row= [query.value(i) for i in range(query.record().count())]
               registros.append(row)
           print(registros)
           Factura.Facturas.cargartablafact(registros)

        except Exception as error:
            print('Error al cargarFactura',error)
    def cargarTarifas(self=None):
        """
             Módulo para cargar las facturas desde la base de datos y mostrarlas en una tabla desde el metdodo cargartablafact(registro).
        """
        try:
           registros=[]
           query = QtSql.QSqlQuery()
           query.prepare('select Nacional,Local,Provincial from tarifas')
           if query.exec():
             while query.next():
               row= [query.value(i) for i in range(query.record().count())]
               registros.append(row)
           print('Tarifa',registros)
           Factura.Facturas.cargartablaTarifa(registros)

        except Exception as error:
            print('Error al cargarFactura',error)
    def cargarTarifasUtilizar(self=None):
        """
             Módulo para cargar las facturas desde la base de datos y mostrarlas en una tabla desde el metdodo cargartablafact(registro).
        """
        try:
           registros=[]
           query = QtSql.QSqlQuery()
           query.prepare('select Nacional,Local,Provincial from tarifas')
           if query.exec():
             while query.next():
               row= [query.value(i) for i in range(query.record().count())]
               registros.append(row)
           print('TarifaUtilizar',registros)
           return registros


        except Exception as error:
            print('Error al cargarFactura',error)
    def comprobarcliente(dato):
        """
        Módulo para verificar si un cliente está dado de baja en la base de datos.
        :return:  True si el cliente está dado de baja, False en caso contrario.
        :rtype: bytearray
        """
        try:
            query= QtSql.QSqlQuery()
            query.prepare('SELECT * FROM Clientes WHERE DNI =:dni AND Fecha_Baja IS NOT NULL')
            query.bindValue(':dni',str(dato))
            if query.exec():
                while query.next():
                    return True

        except Exception as error:
            print('Error al comprobar cliente',error)

    def onefac(numfac):
        """
         Este módulo se utiliza para obtener los detalles de una factura dado su número.
        :return: Una lista con los detalles de la factura si se encuentra, o una lista vacía si no se encuentra.
        :rtype: bytearray
        """
        try:
            print(numfac)
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select *  from facturas where numfac = :codigo')
            query.bindValue(':codigo', int(numfac))
            if query.exec():
                while query.next():
                    for i in range(4):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print ("Error en onefac", error)

    def cargarLineaViaje(registro):
        """
        Módulo para registrar un nuevo viaje en la base de datos.

        """
        try:
            #if any(not elemento.strip()for elemento in registro):
            #    msg=QtWidgets.QMessageBox()
            #    msg.setWindowTitle('Aviso')
            #    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            #    msg.setText('Faltan datos del viaje o número Factura')
            #    msg.exec()
            #else:
                query= QtSql.QSqlQuery()
                query.prepare('insert into viaje(factura, origen, destino, tarifa, km)'
                              ' VALUES(:factura, :origen, :destino, :tarifa, :km)')
                query.bindValue(':factura',int(registro[0]))
                query.bindValue(':origen', str(registro[1]))
                query.bindValue(':destino', str(registro[2]))
                query.bindValue(':tarifa', float(registro[3]))
                query.bindValue(':km', int(registro[4]))
                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Viaje grabado en base de datos')
                    msg.exec()
                    #Factura.Facturas.cargartablaviajes(self=None)
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('Faltan campos o es Erroneo')
                    msg.exec()


        except Exception as error:
            print('CARGARLINEAVIAJE',error)

    def datosviaje(self):
        """
            Módulo para obtener los datos del viaje desde la interfaz gráfica.
        :return: Una lista que contiene los datos del viaje.
        :rtype:bytearray
        """
        try:
            try:
                registros = []
                query = QtSql.QSqlQuery()
                query.prepare('select Nacional,Local,Provincial from tarifas')
                if query.exec():
                    while query.next():
                        registroNacion=float(query.value(0))
                        registroLocal=float(query.value(1))
                        registroProvincial=float(query.value(2))
                print('TarifaUtilizar', str(float(registros)))
                return str(registros)
            except Exception as error:
                print('Error',error)


            datosviaje = [var.ui.cmbOrigen_1.currentText(), var.ui.cmbOrigen_2.currentText(),
                          var.ui.cmbDestino_1.currentText(), var.ui.cmbDestino_2.currentText()]


            if str(datosviaje[0])==str(datosviaje[2]):
                if str(datosviaje[1])==str(datosviaje[3]):
                    var.ui.rblocal.setChecked(True)
                    datosviaje.append(str(registroLocal))
                    return registroLocal
                else:
                    var.ui.rbprovi.setChecked(True)
                    datosviaje.append(str(registroProvincial))
                    return registroProvincial

            elif str(datosviaje[0])!=str(datosviaje[2]):
                var.ui.rbnacional.setChecked(True)
                datosviaje.append(str(registroNacion))
                return registroNacion

            return datosviaje
        except Exception as error:
            print(error)
    def viajesFactura(codigo):
        """
        Función para obtener los viajes asociados a una factura dada su código.
        :param codigo: Código de la factura.
        :return: Una lista que contiene los viajes asociados a la factura.

        """
        try:
            registro=[]
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM viaje WHERE factura = :codigo')
            query.bindValue(':codigo', int(codigo))

            if query.exec():
                #registro=[query.value(0),query.value(1),query.value(2),query.value(3),query.value(4),query.value(5)]
                while query.next():
                    for i in range(6):
                        registro.append(str(query.value(i)))
                        print('viajesfactura', registro)




        except Exception as error:
            print('Error en viajes Factura',error)


    def mostrarViaje(numeroFactura):
        """
            Este módulo nos muestra los viajes asociados a una factura dada su número.

            :param numeroFactura: Número de la factura.
             :return: Una lista que contiene los detalles de los viajes asociados a la factura.
        """
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare("select idviaje, origen, destino, tarifa, km from viaje where factura= :factura")
            query1.bindValue(":factura", int(numeroFactura))
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            print('Este es el registro',registros)
            Factura.Facturas.cargarTablaViajes(registros)
            return registros

        except Exception as error:
            print('error mostrar resultados de viajes', error)

    def oneViaje(codigo):
        """
            Función para obtener los detalles de un viaje dado su código.

            :param codigo: Código del viaje.
            :return: Una lista que contiene los detalles del viaje.
        """
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare("select idviaje, origen, destino, tarifa, km  from viaje where idviaje= :factura")
            query1.bindValue(":factura", int(codigo))
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            print('Este es el registro',registros)
            return registros

        except Exception as error:
            print('error carga oneviajes', error)

    def borradoViaje(codigo):
        """
          Módulo para borrar un viaje de la base de datos dado su código.

           :param codigo: Código del viaje a borrar.
           """
        try:

            query1 = QtSql.QSqlQuery()
            query1.prepare("delete from viaje where idviaje = :factura")
            query1.bindValue(":factura", int(codigo))
            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Viaje borrado en base de datos')
                msg.exec()




        except Exception as error:
            print('No se a podido borrar el viaje', error)

    def getProvincia(comunidad):
        """
            Módulo para obtener el identificador de la provincia de un municipio dado su nombre.

            :param comunidad: Nombre del municipio.
            :return: Una lista que contiene el identificador de la provincia del municipio.
            """
        try:
            registros=[]
            query1 = QtSql.QSqlQuery()
            query1.prepare("select idprov from municipios where municipio= :comunidad")
            query1.bindValue(":comunidad", str(comunidad))
            if query1.exec():
                while query1.next():
                    registros.append(query1.value(0))
            return registros


        except Exception as error:
            print('Error al devolver la provincia',error)

    def nombreProv(provincia):
        """
            Función para obtener el nombre de la provincia dado su identificador.

            :param provincia: Identificador de la provincia.
            :return: Una lista que contiene el nombre de la provincia.
            """
        try:
            registros =[]

            query1 = QtSql.QSqlQuery()
            query1.prepare("select provincia from provincias where idprov = :comunidad")
            query1.bindValue(":comunidad", int(provincia))
            if query1.exec():
                while query1.next():
                    registros.append(query1.value(0))

                    print('ee',registros)
            return registros


        except Exception as error:
            print('error en el nombre de la provincia',error)

    def modifViaje(self=None):
        """
        Método para modificar un viaje.
        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Confirmar Modificado')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText('¿Desea modificar el viaje con los datos actuales?')
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                row = var.ui.tbviajes.selectedItems()
                fila = [dato.text() for dato in row]
                idViaje = fila[0]
                datosModificados = Factura.Facturas.datosViaje()
                print('Foña',fila)
                print('Moid',datosModificados)
                if (str(fila[1]) == str(datosModificados[1]) and str(fila[2]) == str(datosModificados[3])
                and str(fila[4]) == str(datosModificados[5])):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("No hay datos que modificar.")
                    mbox.exec()
                else:
                    query = QtSql.QSqlQuery()
                    query.prepare("update viaje set "
                                  "origen = :origen, destino = :destino, km = :km, tarifa = :tarifa "
                                  "where idViaje = :idViaje")
                    query.bindValue(":origen", str(datosModificados[1]))
                    query.bindValue(":destino", str(datosModificados[3]))
                    query.bindValue(":km", str(datosModificados[5]))
                    query.bindValue(":tarifa", str(datosModificados[4]))
                    query.bindValue(':idViaje', int(idViaje))

                    if query.exec():
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle("Aviso")
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText("Viaje modificado correctamente.")
                        mbox.exec()

                    else:
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle("Aviso")
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText("El viaje no se pudo modificar.")
                        mbox.exec()
                        print(query.lastError().text())
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("El viaje no se modificó.")
                mbox.exec()

        except Exception as error:
            print('Error al modif viaje ', error)

    def cargarFacturasEspecifica(registro):

        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare('select numfac,dnicli from facturas where dnicli =:registro')
            query.bindValue(":registro", str(registro))
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
                    registro1 = Conexion.onefac(str(query.value(0)))

            print('Registro :', registros)

            datos = [var.ui.lblcdfact, var.ui.txtcifcli, var.ui.txtAltafac, var.ui.cmbdriver]

            for i, dato in enumerate(datos):
                if i == 3:
                    conteniod = Conexion.codigoselDrivers(registro1[i])
                    var.ui.cmbdriver.setCurrentText(str(conteniod))
                else:
                    dato.setText(str(registro1[i]))

            Factura.Facturas.cargartablafact(registros)
            code = var.ui.lblcdfact.text()
            print('codigo', code)
            Conexion.mostrarViaje(code)

        except Exception as error:
            print('Error al cargarFactura', error)









