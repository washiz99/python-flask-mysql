CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

DROP TABLE IF EXISTS user;
CREATE TABLE user (
  id              int unsigned  not null auto_increment,
  username        varchar(100)  not null,
  email           varchar(128)  not null,
  PRIMARY KEY (id),
  UNIQUE UQ_user_email (email)
);
