#!/usr/bin/env python3
import sqlite3
select_personal = "select * from personal"

insertar_datos = """\
INSERT INTO personal VALUES (?, ?, ?, ?)
"""
insertar_papeleta = """\
INSERT INTO papeletas ( num_papeleta, fecha, nombre, autorizado_para, hora_salida,
                       hora_retorno, motivo, fundamentacion )
              VALUES (  ?, ?, ?, ?, ?, ?, ?, ? );
"""


def bd_conectar():
    bd = sqlite3.connect("../data/pepeletas.db")
    cursor = bd.cursor()
 
