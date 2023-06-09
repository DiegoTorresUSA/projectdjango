-- USER SQL
CREATE USER visitor
    IDENTIFIED BY "NiKolas1984*"
ACCOUNT UNLOCK;

-- ADD ROLES
GRANT create session TO visitor;
GRANT create session TO visitor with admin option;

GRANT CREATE VIEW, CREATE PROCEDURE, CREATE SEQUENCE, CREATE TRIGGER, CREATE TABLE to visitor;