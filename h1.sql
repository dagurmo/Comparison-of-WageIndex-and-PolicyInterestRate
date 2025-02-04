DROP TABLE IF EXISTS Medalvextir CASCADE;
DROP TABLE IF EXISTS Brottfarir CASCADE;



CREATE TABLE Medalvextir(
    month VARCHAR(20) PRIMARY KEY,
    Medaldaglan FLOAT,
    Medalvidskipti FLOAT,
    Medalstyrivextir FLOAT

);


CREATE TABLE Brottfarir(
    month VARCHAR(20) PRIMARY KEY,
    folksfjoldi INT
);

createdb -U postgres "H1-DB"
psql -U postgres -q -f "h1.sql" "H1-DB"                                                                                                                                     
