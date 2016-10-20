SHOW databases;
CREATE DATABASE assetallocdb;
USE assetallocdb;
CREATE TABLE equity(
DATE_ID DATE,
INDEX_ID VARCHAR(30),
PRICE FLOAT(23,8),
TOTAL_RETURN FLOAT(23,8),
DIV_YLD FLOAT(23,8),
DIV_PAYOUT FLOAT(23,8),
PE FLOAT(23,8),
PS FLOAT(23,8),
PB FLOAT(23,8),
PCF FLOAT(23,8))

CREATE TABLE macro(
DATE_ID DATE,
COUNTRY_ID CHAR(2),
INFLATION FLOAT(23,8),
FX_RATE FLOAT(23,8),
PPP FLOAT(23,8),
CPI FLOAT(23,8),
PPI FLOAT(23,8))

CREATE TABLE country(
COUNTRY_NAME VARCHAR(50),
COUNTRY_ID CHAR(2),
CURRENCY CHAR(3),
EQ_INDEX VARCHAR(30),
FI_INDEX VARCHAR(30))

