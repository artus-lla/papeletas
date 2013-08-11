#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from gi.repository import Gtk
import sqlite3

import src.misutils as misutils
import src.bd as bd

#global autorizado_para
#global motivo
#autorizado_para = 'Salir'

class VentanaPrincipal:
    """ Renderiza la ventana principal de la aplicación """
   
    def __init__ (self):
        """ Inicialización de la interface  """

        b = Gtk.Builder()
        b.add_from_file("./ui/main.ui")

         # Obtener ventana
        self.window1 = b.get_object("window1")
        self.notebook = b.get_object("notebook")

        #self.window1.set_activate_default(True)

        self.aboutdialog1 = b.get_object("aboutdialog1")

         # Obtener botones de barra de tareas
        self.btn_papeleta = b.get_object("btn_papeleta")
        self.btn_reporte = b.get_object("btn_reporte")
        self.btn_personal = b.get_object("btn_personal")
        self.tbtn_salir = b.get_object("tbtn_salir")

        # Obtener objetos ingreso personal
        self.ent_dni = b.get_object("ent_dni")
        self.ent_ape_nom = b.get_object("ent_ape_nom")
        self.ent_profesion = b.get_object("ent_profesion")
        self.ent_oficina = b.get_object("ent_oficina")
        self.btn_guardar_personal = b.get_object("btn_guardar_personal")
        self.vista_personal = b.get_object("vista_personal")

        # Obtener objetos ingreso papeleta
        self.ent_ing_num_papel = b.get_object("ent_ing_num_papel")
        self.ent_ing_fecha = b.get_object("ent_ing_fecha")
        self.ent_ing_nombres = b.get_object("ent_ing_nombres")
       
        self.radio_contituar = b.get_object("radio_contituar")
        self.radio_ingresar = b.get_object("radio_ingresar")
        self.radio_salir = b.get_object("radio_salir")

        self.ent_ing_hsalida = b.get_object("ent_ing_hsalida")
        self.ent_ing_hretorno = b.get_object("ent_ing_hretorno")

        self.radio2_particulares = b.get_object("radio2_particulares")
        self.radio2_enfermedad = b.get_object("radio2_enfermedad")
        self.radio2_personales = b.get_object("radio2_personales")
        self.radio2_comision = b.get_object("radio2_comision")

        self.text_fundamento = b.get_object("text_fundamento")

        self.btn_ing_guardar = b.get_object("btn_ing_guardar")
        self.btn_ing_nuevo = b.get_object("btn_ing_nuevo")

        self.acerca_de = b.get_object("acerca_de")
                
        
         # Auto conectar con las señales
        b.connect_signals(self)
        self.window1.show()
        self.notebook.hide()
         # Destruir ventana
        self.window1.connect('destroy', lambda w: Gtk.main_quit())

  

    def on_btn_papeleta_toggled(self, widget, data=None):
        if widget.get_active():
            self.notebook.set_current_page(0)
            #self.btn_papeleta.set_active(True)
            self.notebook.show()

            self.btn_reporte.set_active(False)
            self.btn_personal.set_active(False)

    def on_btn_reporte_toggled(self, widget, data=None):
        if widget.get_active():
            self.notebook.set_current_page(1)
            #self.btn_reporte.set_active(True)
            self.notebook.show()
       
            self.btn_papeleta.set_active(False)
            self.btn_personal.set_active(False)

    def on_btn_personal_toggled(self, widget, data=None):
        if widget.get_active():
            self.notebook.set_current_page(2)
            self.notebook.show()

            self.btn_papeleta.set_active(False)
            self.btn_reporte.set_active(False)
            self.ent_dni.grab_focus()

    def on_tbtn_salir_clicked(self, widget, data=None):
        print("Good bye")
        Gtk.main_quit()

    # ========= Ingresar papeleta ===================

    def on_acerca_de_clicked(self, widget, data=None):
        self.aboutdialog1.run()
        self.aboutdialog1.hide()

    def on_ent_ing_num_papel_insert_text(self, widget, Text, position, data=None):
        misutils.solo_numeros(self.ent_ing_num_papel, Text)

    def on_ent_ing_fecha_insert_text(self, widget, Text, position, data=None):
        misutils.fecha(self.ent_ing_fecha, Text)

    def on_ent_ing_hsalida_insert_text(self, widget, Text, position, data=None):
        misutils.hora(self.ent_ing_hsalida, Text)

    def on_ent_ing_hretorno_insert_text(self, widget, Text, position, data=None):
        misutils.hora(self.ent_ing_hretorno, Text)

    def on_btn_ing_guardar_clicked(self, widget, data=None):
        """Grabar datos de papeleta"""
        autorizado_para = ""
        motivo = ""
        # * Obtener datos
        num_papeleta = self.ent_ing_num_papel.get_text()
        fecha        = self.ent_ing_fecha.get_text()
        nombres      = self.ent_ing_nombres.get_text()

        # **  Determinar el valor de la variable autorizado para
        if self.radio_contituar.get_active() is True:
            autorizado_para = "Continuar"
        elif self.radio_ingresar.get_active() is True:
            autorizado_para = "Ingresar"
        else:
            autorizado_para = "Salir"
        #print(autorizado_para)

        hora_salida  = self.ent_ing_hsalida.get_text()
        hora_retorno = self.ent_ing_hretorno.get_text()

        # ** Determinar el valor de la variable motivo
        if self.radio2_enfermedad.get_active() is True:
            motivo =  "Enfermedad"
        elif self.radio2_personales.get_active() is True:
            motivo = "Personales"
        elif self.radio2_comision.get_active() is True:
            motivo = "Comisión de servicios"
        else:
            motivo = "Particulares"
        #print(motivo)

        fundamento = self.text_fundamento.get_text()

        campos = ( num_papeleta, fecha, nombres, autorizado_para,
                   hora_salida, hora_retorno, motivo, fundamento )
        #for campo in campos:
        #    print(campo)

        try:
            bd_papeletas = sqlite3.connect("./data/papeletas.db")
            cursor = bd_papeletas.cursor()
        
            cursor.execute(bd.insertar_papeleta, campos)
            bd_papeletas.commit()
            bd_papeletas.close()
        except sqlite3.IntegrityError:
            misutils.mensaje_dialogo("Debe llenar todos los campos")

        # Limpiar campos
        self.ent_ing_num_papel.set_text("")
        self.ent_ing_fecha.set_text("")
        self.ent_ing_nombres.set_text("")
        self.ent_ing_hsalida.set_text("")
        self.ent_ing_hretorno.set_text("")
        self.text_fundamento.set_text("")                

        self.ent_ing_num_papel.grab_focus()

    # ========== Ingreso de Personal ===================
    def on_ent_dni_insert_text(self, widget, Text, position, data=None):
        """Permitir sólo números dni personal"""
        misutils.solo_numeros(self.ent_dni, Text)

    def on_btn_guardar_personal_clicked(self, widget, data=None):
        """Graba datos de personal en la tabla personal"""

        # Obtener datos
        dni = self.ent_dni.get_text()
        nombre = self.ent_ape_nom.get_text()
        profesion = self.ent_profesion.get_text()
        oficina = self.ent_oficina.get_text()
        # Tupla con los campos
        campos = (dni, nombre, profesion, oficina)

        falta_campo = False # si falta algún campo

        for campo in campos:
            if campo is None or campo == "": # comprobar que ningún campo esté vacío
                falta_campo = True

        if falta_campo is True:
            misutils.mensaje_dialogo("Debe llenar todos los campos")
        else:
            try:
                bd_papeletas = sqlite3.connect("./data/papeletas.db")
                cursor = bd_papeletas.cursor()
            
                cursor.execute(bd.insertar_datos, campos)
                cursor.execute(bd.select_personal)

                personal = cursor.fetchall()
               
                
                bd_papeletas.commit()
                bd_papeletas.close()

                # Limpar campos
                self.ent_dni.set_text("")
                self.ent_ape_nom.set_text("")
                self.ent_profesion.set_text("")
                self.ent_oficina.set_text("")
                self.ent_dni.grab_focus()

                # Poblar tree view vista_personal

                lista = Gtk.ListStore(str, str, str, str)
               
                for tupla in personal:
                    lista.append([tupla[0], tupla[1], tupla[2], tupla[3]])
                    #print(tupla)
                #lista.append(["Negro", 12])

                render = Gtk.CellRendererText()
                columna1 = Gtk.TreeViewColumn("DNI", render, text=0)
                columna2 = Gtk.TreeViewColumn("Apellidos y Nombres",render,text=1)
                columna3 = Gtk.TreeViewColumn("Profesión",render,text=2)
                columna4 = Gtk.TreeViewColumn("Oficina o servicio",render,text=3)

                self.vista_personal.set_model(lista)
                self.vista_personal.append_column(columna1)
                self.vista_personal.append_column(columna2)
                self.vista_personal.append_column(columna3)
                self.vista_personal.append_column(columna4)
               
                self.vista_personal.show()
                

            except sqlite3.IntegrityError:
                misutils.mensaje_dialogo("El campo DNI debe tener 8 dígitos o el DNI ya existe")
                self.ent_dni.grab_focus()

    
if __name__ == "__main__":
    gui = VentanaPrincipal()
    Gtk.main()



