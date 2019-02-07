-- AUTOINCREMENT는 INTEGER에만 지정 가능
-- NOT NULL: INSERT에서 반드시 값 있어야 함.
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
    );
    
-- 컬럼명 표기
.headers on
-- 표처럼 표기
.mode column