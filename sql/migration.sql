-- create the table Variador de Frecuencia
CREATE TABLE IF NOT EXISTS public.variador
(
    id serial,
    fecha timestamp,
    frecuencia_ref float,
    estado int,
    intensidad float,
    frecuencia float,
    tension float,
    dc_bus float,
    trip1 int,
    trip2 int,
    rpm float,
    PRIMARY KEY (id)
);