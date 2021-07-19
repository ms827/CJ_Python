BEGIN TRANSACTION;
CREATE TABLE users( id INTEGER PRIMARY KEY,
          username TEXT,
          email TEXT,
          phone TEXT,
          regdate TEXT);
INSERT INTO "users" VALUES(1,'홍길동','hong@daum.net','010-2222-2222','2020-08-19 17:03:48.261698');
INSERT INTO "users" VALUES(2,'유관순','ryu@daum.net','010-4444-5555','2020-08-19 17:03:48.261698');
INSERT INTO "users" VALUES(3,'Lee','Lee@google.com','010-6666-6666','2020-08-19 17:03:48.261698');
INSERT INTO "users" VALUES(4,'Park','Park@google.com','010-8888-7777','2020-08-19 17:03:48.261698');
INSERT INTO "users" VALUES(5,'Cho','Cho@google.com','010-4567-9876','2020-08-19 17:03:48.261698');
COMMIT;
