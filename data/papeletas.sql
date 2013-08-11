-- Base de datos Papeletas

-- Autor: Arturo Llaja Alarcón
-- Fecha: <2012-03-02 vie>

-- Tabla papeleta


CREATE TABLE personal(
       dni              TEXT NOT NULL PRIMARY KEY UNIQUE,
       nombre           TEXT NOT NULL,
       profesion        TEXT NOT NULL,
       oficina_servicio TEXT NOT NULL,
       CHECK ( dni LIKE '________' and dni != '00000000')
       -- con 8 caracteres y diferente de 0
      
 );

-- Poblar tabla personal
 INSERT INTO personal VALUES ('41614657','Sebastián', 'Médico', 'Emerg');
 INSERT INTO personal VALUES ('41614658','Rafael', 'Escritor', 'Emerg');
 INSERT INTO personal VALUES ('41614659','Leandro', 'Ingeniero', 'Emerg');

 -- tabla papeletas
CREATE TABLE papeletas (
       num_papeleta     INTEGER NOT NULL PRIMARY KEY,
       fecha            DATE NOT NULL,
       nombre           TEXT NOT NULL,
       autorizado_para  TEXT NOT NULL,
       hora_salida      TIME NOT NULL,
       hora_retorno     TIME NOT NULL,
       motivo           TEXT NOT NULL,
       fundamentacion   TEXT NOT NULL      
);

INSERT INTO papeletas ( num_papeleta, fecha, nombre, autorizado_para, hora_salida,
                       hora_retorno, motivo, fundamentacion )
              VALUES (  28, '05-03-2012', 'Sebastián', 'salir', '10:15', '10:45',
	               'Personales', 'ESSALUD' );

INSERT INTO papeletas ( num_papeleta, fecha, nombre, autorizado_para, hora_salida,
                       hora_retorno, motivo, fundamentacion )
              VALUES (  29 , '05-03-2012', 'Rafael' 'salir', '10:15', '10:45',
	               'Personales', 'ESSALUD' );
