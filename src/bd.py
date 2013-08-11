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

reporte = """\
select num_papeleta, strftime('%Y', fecha) as Año, strftime('%m', fecha) as Mes,
       nombre, autorizado_para, hora_salida, hora_retorno, motivo, fundamentacion
from papeletas
where strftime('%Y', fecha) = ?
GROUP BY nombre, motivo
"""


def bd_conectar():
    bd = sqlite3.connect("../data/pepeletas.db")
    cursor = bd.cursor()
 
