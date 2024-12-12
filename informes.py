import os, var, shutil
from PIL import Image
from PyQt6 import QtSql, QtWidgets
from PyQt6.uic.properties import QtGui
from reportlab.pdfgen import canvas
from datetime import datetime
from svglib.svglib import svg2rlg
import conexion
import informes


class Informes:

    def reportclientes(self):
        """
            Módulo que saca un informe en pdf con los clientes y sus campos
        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre =  fecha + '_listadoclientes.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CLIENTES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items=['Codigo', 'DNI', 'RAZON SOCIAL', 'MUNICIPIO', 'TELEFONO', 'FECHA_BAJA']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(58, 675, str(items[0]))
            var.report.drawString(110, 675, str(items[1]))
            var.report.drawString(165, 675, str(items[2]))
            var.report.drawString(305, 675, str(items[3]))
            var.report.drawString(390, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50,670,525,670)
            #obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select Codigo ,DNI , Razon_Social ,Municipio ,Telefono, Fecha_Baja '
                          ' from Clientes order by Razon_Social')
            var.report.setFont('Helvetica',size=9)
            if query.exec():
                i=55
                j=655
                while query.next():
                    if j<=80:
                        var.report.drawString(450,90,'Pagina siguiente...')
                        var.report.showPage()#crea una nueva pagina
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica-Bold',size=10)
                        var.report.drawString(58,675,str(items[0]))
                        var.report.drawString(110, 675, str(items[1]))#130
                        var.report.drawString(165, 675, str(items[2]))#205
                        var.report.drawString(305, 675, str(items[3]))#335
                        var.report.drawString(390, 675, str(items[4]))#450
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50,670,525,670)
                        i=55
                        j=655
                    texto = '*****'+str(query.value(1)[5:7])+'**'
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i + 15,j,str(query.value(0)))
                    var.report.drawString(i + 50, j, str(texto))#60
                    var.report.drawString(i + 120, j, str(query.value(2)))#150
                    var.report.drawString(i + 250, j, str(query.value(3)))#280
                    var.report.drawString(i + 340, j, str(query.value(4)))
                    var.report.drawString(i + 410, j, str(query.value(5)))
                    j=j-25
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('listadoclientes.pdf'):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO CLIENTES :', error)

    def topInforme(titulo):
        """
        Este módulo personaliza la parte superior del informe
        """
        try:
            ruta_logo = ('.\\IMG\\logo.ico')
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Transportes Teis')
                var.report.drawString(240, 695, titulo)
                var.report.line(50, 690, 525, 690)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)

    def footInforme(titulo):
        """
        Módulo para personalizar la parte inferior del informe
        """
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    def reportdrivers(self):
        """
             Módulo que saca un informe en pdf con los drivers y sus campos
        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadodrivers.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO DRIVERS'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = ['CODIGO', 'APELLIDOS', 'NOMBRE', 'TELEFONO', 'LICENCIAS', 'FECHA_BAJA']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(58, 675, str(items[0]))
            var.report.drawString(120, 675, str(items[1]))
            var.report.drawString(205, 675, str(items[2]))
            var.report.drawString(275, 675, str(items[3]))
            var.report.drawString(360, 675, str(items[4]))
            var.report.drawString(440, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)
            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select codigo ,apeldri , nombredri ,movildri ,carnet, bajadri '
                          ' from drivers order by apeldri')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 90, 'Pagina siguiente...')
                        var.report.showPage()  # crea una nueva pagina
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(58, 675, str(items[0]))
                        var.report.drawString(120, 675, str(items[1]))
                        var.report.drawString(205, 675, str(items[2]))
                        var.report.drawString(275, 675, str(items[3]))
                        var.report.drawString(360, 675, str(items[4]))
                        var.report.drawString(440, 675, str(items[5]))
                        var.report.line(50, 670, 525, 670)
                        i = 55
                        j = 655

                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 65, j, str(query.value(1)))
                    var.report.drawString(i + 155, j, str(query.value(2)))
                    var.report.drawString(i + 225, j, str(query.value(3)))
                    var.report.drawString(i + 320, j, str(query.value(4)))
                    var.report.drawString(i + 390, j, str(query.value(5)))
                    j = j - 25

            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('listadodrivers.pdf'):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO Drivers :', error)
    def reportviajes(self):
        """
             Módulo que saca un informe en pdf con los drivers y sus campos
        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoviajes.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO VIAJES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = ['NºVIAJES', 'ORIGEN', 'DESTINO', 'KM']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(58, 675, str(items[0]))
            var.report.drawString(200, 675, str(items[1]))
            var.report.drawString(350, 675, str(items[2]))
            var.report.drawString(500, 675, str(items[3]))
            var.report.line(50, 670, 525, 670)
            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select idviaje ,origen , destino ,km  '
                          ' from viaje where factura = 8')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 90, 'Pagina siguiente...')
                        var.report.showPage()  # crea una nueva pagina
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(58, 675, str(items[0]))
                        var.report.drawString(200, 675, str(items[1]))
                        var.report.drawString(350, 675, str(items[2]))
                        var.report.drawString(500, 675, str(items[3]))

                        var.report.line(50, 670, 525, 670)
                        i = 55
                        j = 655

                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 145, j, str(query.value(1)))
                    var.report.drawString(i + 300, j, str(query.value(2)))
                    var.report.drawString(i + 450, j, str(query.value(3)))

                    j = j - 25

            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('listadoviajes.pdf'):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO Viajes :', error)



    @staticmethod
    def checkboxinforme():
        """
            Módulo que realiza los informes al pulsar en un determinado botón
        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Realizar Informe")
            #mbox.setWindowIcon(QtGui.QIcon("IMG/Coche.png"))
            mbox.setText("Seleccione informe/es")

            conductorcheck = QtWidgets.QCheckBox("Informe de conductores")
            clientecheck = QtWidgets.QCheckBox("Informe de clientes")
            facturacheck = QtWidgets.QCheckBox("Informe de facturas")

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(conductorcheck)
            layout.addWidget(clientecheck)
            layout.addWidget(facturacheck)


            container = QtWidgets.QWidget()
            container.setLayout(layout)

            mbox.layout().addWidget(container, 1, 1, 1, mbox.layout().columnCount())

            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Aceptar')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Cancelar')

            resultado = mbox.exec()

            if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
                if conductorcheck.isChecked():

                    Informes.reportdrivers(self=None)
                if clientecheck.isChecked():

                    Informes.reportclientes(self=None)
                if facturacheck.isChecked():
                    Informes.reportFacturas(self=None)

                if not (conductorcheck.isChecked() or clientecheck.isChecked()):
                   print('No esta checkeado')

        except Exception as error:
            print("Error en checkbox_informe", error)

    def reportFacturas(self):
        """
         Módulo que saca un informe en pdf con las facturas y sus campos
        """
        try:
            print('Has entrado en facturas')
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadofacturas.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO FACTURAS'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = ['ID VIAJE', 'ORIGEN', 'DESTINO', 'TARIFA', 'KM', 'TOTAL']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 650, str(items[0]))
            var.report.drawString(130, 650, str(items[1]))
            var.report.drawString(250, 650, str(items[2]))
            var.report.drawString(390, 650, str(items[3]))
            var.report.drawString(430, 650, str(items[4]))
            var.report.drawString(480, 650, str(items[5]))
            var.report.line(50, 670, 525, 670)
            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select idviaje ,origen , destino ,tarifa ,km '
                          ' from viaje order by km')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 140, 'Pagina siguiente...')
                        var.report.showPage()  # crea una nueva pagina
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(50, 650, str(items[0]))
                        var.report.drawString(130, 650, str(items[1]))  # 130
                        var.report.drawString(250, 650, str(items[2]))  # 205
                        var.report.drawString(390, 650, str(items[3]))  # 335
                        var.report.drawString(430, 650, str(items[4]))  # 450
                        var.report.drawString(480, 650, str(items[5]))
                        var.report.line(50, 645, 525, 645)
                        i = 55
                        j = 630
                    totalviaje = round(float(query.value(3)) * float(query.value(4)), 2)
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 70, j, Informes.ajustarTamanho(str(query.value(1)), 25))
                    var.report.drawString(i + 190, j, Informes.ajustarTamanho(str(query.value(2)), 25))
                    var.report.drawString(i + 335, j, str(query.value(3)))
                    var.report.drawString(i + 385, j, str(query.value(4)))
                    var.report.drawString(i + 410, j, str(totalviaje))
                    var.report.drawString(i + 430, j, str('{:.2f}'.format(totalviaje)) + " €")
                    j = j - 25
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('listadofacturas.pdf'):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error en el reportFacturas',error)





    def ajustarTamanho(texto, maximo):
        """

        :param maximo: numero indicado para el maximo de tamaño
        :type maximo: integer
        :return: devuelve el mensaje personalizado
        :rtype: bytearray
        Módulo que ajusta el tamaño del texto
        """
        try:
            mensaje = str(texto)
            if len(mensaje) > maximo:
                mensaje = mensaje[:(maximo - 1)] + "..."
            return mensaje
        except Exception as error:
            print('Error al ajustar el tamaño del texto: ', error)
