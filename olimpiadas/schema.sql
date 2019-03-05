DROP TABLE IF EXISTS facultad;
DROP TABLE IF EXISTS deporte;
DROP TABLE IF EXISTS alumno;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE facultad (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT UNIQUE NOT NULL
);

CREATE TABLE deporte (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT UNIQUE NOT NULL
);

CREATE TABLE alumno (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  dni TEXT UNIQUE NOT NULL,
  path_foto TEXT UNIQUE NOT NULL,
  deporte_id INTEGER NOT NULL,
  facultad_id INTEGER NOT NULL,
  FOREIGN KEY (deporte_id) REFERENCES deporte (id),
  FOREIGN KEY (facultad_id) REFERENCES facultad (id)
);