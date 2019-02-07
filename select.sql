-- 테이블 값 모두 가져오기
SELECT * FROM classmates;
-- 특정 column만 가져오기
SELECT id, name FROM classmates
-- 가져오는 row(레코드)의 갯수를 지정하기
SELECT * FROM classmates LIMIT 3;
-- 가져오는 row(레코드)의 시작위치 지정하기;
SELECT * FROM classmates LIMIT 3 OFFSET 2;
-- 특정한 값을 가진 row(레코드)aks 가져오기
SELECT * FROM classmates WHERE id = 2;
SELECT * FROM classmates WHERE address = '서울';
-- 대전에 사는 사람 이름은?
SELECT name FROM classmates WHERE address = '대전';