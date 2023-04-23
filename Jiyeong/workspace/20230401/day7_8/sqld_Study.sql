-- 2023 04 22
-- 오마 -> '행번호 토글'
-- <-플러그표시: 연결되어있음
-- ctrl + enter: 실행

CREATE TABLE test1
    (ENAME VARCHAR2(10),
     JOB   VARCHAR2(9),
     SAL   NUMBER,
     COMM  NUMBER);
     
--테이블 생성 , 삭제,  수정  
CREATE TABLE test1
    (
     SAL   NUMBER(10),
    ENAME VARCHAR2(10)
    
    );

DROP table test1;
ALTER TABLE test1 ADD (C NUMBER(10));


--내용 삽입,수정,삭제등등
INSERT into test1 values (1, 'a');
INSERT into test1 values (2, 'b',2);
INSERT into test1 values (11, 'c',11);
INSERT into test1 values (12, 'd',12);
INSERT into test1 values (13, 'e',13);

UPDATE test1 SET C=100 WHERE C is null

DELETE from test1 where C=2 or A=13;

SELECT * from test1;

-- 부정
!= , ^=, <>, where not
-- 포함
in (30,40)
sal BETWEEN ~ AND ~


-- TABLE.txt
select * from BONUS;
select * from EMP;


select SAL+COMM from EMP  -- NULL일 경우 연산결과도 NULL
    NVL( A,B) : A, NULL이면 B
    NVL2(A,B,C)
select SAL*1.15 from EMP  -- 연봉15% 인상
select  FLOOR(10.3) from DUAL  -- 정수 + 그냥버림(FLOOR) 소수 1번째에서
select  CEIL(10.3), CEIL(10.9) from DUAL  -- 정수 + 항상올림(CEIL) #11, 11
select ROUND(12.987), ROUND(12.345) from DUAL  -- 정수(실수가능) + 반올림
select ROUND(12.987, 1), ROUND(12.345, 2) from DUAL  --실수 + 자릿수지정 + 반올림: #13, 12.35 
select ROUND(12.987, -1), ROUND(3277.5, -2) from DUAL  -- #1자리, 2자리 기준 반올림 #10, 3300

select EMPNO            --CASE문으로 조회
 ,ENAME 
 ,CASE DEPTNO WHEN 10 THEN '영업1부'   -- WHEN DEPTNO = 10 THEN '영업1부'
              ELSE 'N/A'
  END as 부서 FROM EMP;

 -- CASE 예제) 급여별등급 
select EMPNO       
 ,ENAME, SAL
 ,CASE WHEN SAL >=1000 and SAL <=2000 THEN 'B등급'  
  ELSE 'N/A'
  END as 등급 
FROM EMP;

--집계함수 :NULL은 제외하고 계산됨
SUM, AVG, MAX, MIN, COUNT

select COUNT(COMM) form EMP 

--GROUP BY: 순서 from -> where -> GROUP BY -> HAVING(집계함수만가능) -> select --> order by끝
select ENAME,DEPTNO, SUM(sal)
from EMP
GROUP BY DEPTNO,ENAME
HAVING sum(sal)>=10000
order by DEPTNO

select JOB, sum(sal)
from emp where JOB='CLERK'
group by JOB
having min(sal) <= 1000

-- 등가조인
select * from EMP E JOIN DEPT D ON E.DEPTNO = D.DEPTNO

select sg.grade, sum(e.sal), ROUND(avg(e.sal) , 1), count(*), max(e.sal), min(e.sal) 
from emp e, salgrade sg
where e.sal <= sg.HISAL and e.sal >= sg.LOSAL
group by sg.grade
order by sg.grade


-- 서브쿼리
select ename, sum(sal) from emp --error: 단일 그룹의 그룹함수가 아닙니다
select ename, (select sum(sal) from emp)  --> success
from emp

--매니저가 ALLEN
select *
from emp 
where mgr = (select mgr from emp where ename ='ALLEN')

-- 한번에 가져오기 
select * from emp
WHERE ( mgr, deptno ) IN ( mgr, deptno from emp where ename = 'FORD')


--roll up : 소계가 마지막에 나옴
select sum(sal)
group by ROLLUP(deptno) 
group by ROLLUP(deptno , ename) -- 부서별소계 -> 이름별 소계 순서로 나옴

--*----*----*----*----*-- 데이터생성용 --*----*----*----*--
CREATE TABLE BONUS
        ( ENAME VARCHAR2(10),
         JOB   VARCHAR2(9),
         SAL   NUMBER,
         COMM  NUMBER );

CREATE TABLE EMP
       (EMPNO NUMBER(4) NOT NULL,
        ENAME VARCHAR2(10),
        JOB VARCHAR2(9),
        MGR NUMBER(4),
        HIREDATE DATE,
        SAL NUMBER(7, 2),
        COMM NUMBER(7, 2),
        DEPTNO NUMBER(2));

INSERT INTO EMP VALUES
        (7369, 'SMITH',  'CLERK',     7902,
        TO_DATE('17-12-1980', 'DD-MM-YYYY'),  800, NULL, 20);
INSERT INTO EMP VALUES
        (7499, 'ALLEN',  'SALESMAN',  7698,
        TO_DATE('20-02-1981', 'DD-MM-YYYY'), 1600,  300, 30);
INSERT INTO EMP VALUES
        (7521, 'WARD',   'SALESMAN',  7698,
        TO_DATE('22-02-1981', 'DD-MM-YYYY'), 1250,  500, 30);
INSERT INTO EMP VALUES
        (7566, 'JONES',  'MANAGER',   7839,
        TO_DATE('2-04-1981', 'DD-MM-YYYY'),  2975, NULL, 20);
INSERT INTO EMP VALUES
        (7654, 'MARTIN', 'SALESMAN',  7698,
        TO_DATE('28-09-1981', 'DD-MM-YYYY'), 1250, 1400, 30);
INSERT INTO EMP VALUES
        (7698, 'BLAKE',  'MANAGER',   7839,
        TO_DATE('1-05-1981', 'DD-MM-YYYY'),  2850, NULL, 30);
INSERT INTO EMP VALUES
        (7782, 'CLARK',  'MANAGER',   7839,
        TO_DATE('9-06-1981', 'DD-MM-YYYY'),  2450, NULL, 10);
INSERT INTO EMP VALUES
        (7788, 'SCOTT',  'ANALYST',   7566,
        TO_DATE('09-12-1982', 'DD-MM-YYYY'), 3000, NULL, 20);
INSERT INTO EMP VALUES
        (7839, 'KING',   'PRESIDENT', NULL,
        TO_DATE('17-11-1981', 'DD-MM-YYYY'), 5000, NULL, 10);
INSERT INTO EMP VALUES
        (7844, 'TURNER', 'SALESMAN',  7698,
        TO_DATE('8-09-1981', 'DD-MM-YYYY'),  1500, 0, 30);
INSERT INTO EMP VALUES
        (7876, 'ADAMS',  'CLERK',     7788,
        TO_DATE('12-01-1983', 'DD-MM-YYYY'), 1100, NULL, 20);
INSERT INTO EMP VALUES
        (7900, 'JAMES',  'CLERK',     7698,
        TO_DATE('3-12-1981', 'DD-MM-YYYY'),   950, NULL, 30);
INSERT INTO EMP VALUES
        (7902, 'FORD',   'ANALYST',   7566,
        TO_DATE('3-12-1981', 'DD-MM-YYYY'),  3000, NULL, 20);
INSERT INTO EMP VALUES
        (7934, 'MILLER', 'CLERK',     7782,
        TO_DATE('23-01-1982', 'DD-MM-YYYY'), 1300, NULL, 10);

CREATE TABLE DEPT
       (DEPTNO NUMBER(2),
        DNAME VARCHAR2(14),
        LOC VARCHAR2(13) );

INSERT INTO DEPT VALUES (10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO DEPT VALUES (20, 'RESEARCH',   'DALLAS');
INSERT INTO DEPT VALUES (30, 'SALES',      'CHICAGO');
INSERT INTO DEPT VALUES (40, 'OPERATIONS', 'BOSTON');

CREATE TABLE SALGRADE
        (GRADE NUMBER,
         LOSAL NUMBER,
         HISAL NUMBER);

INSERT INTO SALGRADE VALUES (1,  700, 1200);
INSERT INTO SALGRADE VALUES (2, 1201, 1400);
INSERT INTO SALGRADE VALUES (3, 1401, 2000);
INSERT INTO SALGRADE VALUES (4, 2001, 3000);
INSERT INTO SALGRADE VALUES (5, 3001, 9999);

COMMIT;




