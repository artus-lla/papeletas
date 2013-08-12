#!/usr/bin/env python3
from gi.repository import Gtk
import re

def mensaje_dialogo(mensaje):
    # Reemplazar OK_CANCEL para botones Aceptar y Cancelar
    msg = Gtk.MessageDialog(None,
                            Gtk.DialogFlags.MODAL |Gtk.DialogFlags.DESTROY_WITH_PARENT,
                            Gtk.MessageType.INFO,
                            Gtk.ButtonsType.OK,
                            mensaje)
    msg.run()
    msg.destroy()


def solo_numeros(entry, Text):
    if re.match("[0-9]", Text):
        pass
    else:
        entry.stop_emission("insert_text")


def fecha(entry, Text):
    if re.match("[0-9-]", Text):
        pass
    else:
        entry.stop_emission("insert_text")

def hora(entry, Text):
    if re.match("[0-9:]", Text):
        pass
    else:
        entry.stop_emission("insert_text")

def valor_combobox(combobox):
    modelo = combobox.get_model()
    activo = combobox.get_active_iter()
    if activo is None:
        return None 
    return modelo[activo][0]

def llenar_combo_anio(combo):
    anios = [2013, 2014, 2015, 2015]
    listaComboAnio = Gtk.ListStore(int)
    for i in anios:
        listaComboAnio.append([i])

    combo.set_model(listaComboAnio)
    render = Gtk.CellRendererText()
    combo.pack_start(render, True)
    combo.add_attribute(render, 'text', 0)

def llenar_combo_mes(combo):
    """ Llenar combo Mes """

    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
             'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    listaComboMes = Gtk.ListStore(str)
    for i in meses:
        listaComboMes.append([i])
    
    combo.set_model(listaComboMes)
    render = Gtk.CellRendererText()
    combo.pack_start(render, True)
    combo.add_attribute(render, 'text', 0)    

def arreglar_fecha(fecha):
    """Transforma una fecha en formato 10-12-2013 a 2013-12-10"""
    
    fecha_div = fecha.split('-')
    #print(fecha_div)
    for i in fecha_div:
        nueva_fecha = fecha_div[2] + '-' + fecha_div[1] + '-' + fecha_div[0]
    #print(nueva_fecha)

    return nueva_fecha
