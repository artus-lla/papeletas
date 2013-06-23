-- Base de datos Papeletas

-- Autor: Arturo Llaja Alarcón
-- Fecha: <2012-03-02 vie>

-- Tabla papeleta

CREATE TABLE personal(
       dni              TEXT NOT NULL UNIQUE,
       nombre           TEXT NOT NULL,
       profesion        TEXT NOT NULL,
       oficina_servicio TEXT NOT NULL,
       CHECK ( dni LIKE '________' and dni != '00000000')
       -- con 8 caracteres y diferente de 0
      
 );

-- Poblar tabla personal
 INSERT INTO personal VALUES ('41614657','Sebastían', 'Medico', 'Emerg');
 INSERT INTO personal VALUES ('41614658','Rafael', 'Escritor', 'Emerg');
 INSERT INTO personal VALUES ('41614659','Leandro', 'Ingeniero', 'Emerg');

 
CREATE TABLE papeleta (
       rowid            INTEGER NOT NULL REFERENCES personal( rowid ),
       num_papeleta     INTEGER NOT NULL PRIMARY KEY,
       fecha            DATE NOT NULL,
       autorizado_para  TEXTO NOT NULL,
       hora_salida      TIME,
       hora_retorno     TIME,
       motivo           TEXT,
       fundamentacion   TEXT       
);

INSERT INTO papeleta ( rowid, num_papeleta, fecha, autorizado_para, hora_salida,
                       hora_retorno, motivo, fundamentacion )
              VALUES ( 1, 28, '05-03-2012', 'salir', '10:15', '10:45',
	               'Personales', 'ESSALUD' );

INSERT INTO papeleta ( rowid, num_papeleta, fecha, autorizado_para, hora_salida,
                       hora_retorno, motivo, fundamentacion )
              VALUES ( 1, 29 , '05-03-2012', 'salir', '10:15', '10:45',
	               'Personales', 'ESSALUD' );
