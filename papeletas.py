#! /usr/bin/env python
# -*- coding: utf-8 -*-


from gi.repository import Gtk



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


         # Obtener botones de barra de tareas
        self.btn_papeleta = b.get_object("btn_papeleta")
        self.btn_reporte = b.get_object("btn_reporte")
        self.btn_personal = b.get_object("btn_personal")
        
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

if __name__ == "__main__":
    gui = VentanaPrincipal()
    Gtk.main()



