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

