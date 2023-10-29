CREATE DATABASE open_door;
USE open_door;
CREATE TABLE access(
    pk_access INT PRIMARY KEY AUTO_INCREMENT,
    description_access VARCHAR( 100 ) NOT NULL
);
INSERT INTO access (pk_access,description_access)
VALUES
    (`authorized`),
    (`suspended`),
    (`bloqued`);
CREATE TABLE user(
    pk_user INT PRIMARY KEY AUTO_INCREMENT,
    name_person VARCHAR(100) NOT NULL,
    fk_access INT NOT NULL,
    FOREING KEY (fk_access) REFERENCES access (pk_access)
);
INSERT INTO person (pk_person,name_person,fk_access)
VALUES
    ('Lucy',`1`),
    ('Maya',`2`),
    ('Dory',`3`);