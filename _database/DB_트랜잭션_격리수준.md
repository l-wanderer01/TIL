---
title: "DB 트랜잭션 격리수준"
date: 2026-08-25
tags: [Database, Transaction]
---

## Q. DB 트랜잭션 격리수준에 대해 아는거 말씀해주세요

## A. 핵심 답변
트랜잭션 격리수준은 ANSI SQL 표준 기준 4단계로 나뉜다.

1. Read Uncommitted: 커밋되지 않은 변경을 읽을 수 있음(Dirty Read 허용). 실무에서 거의 사용하지 않음
2. Read Committed: 커밋된 데이터만 읽음. Dirty Read는 차단되나 Non-Repeatable Read 발생. PostgreSQL, Oracle, SQL Server 기본값
3. Repeatable Read: 트랜잭션 시작 시점의 스냅샷을 유지해 동일 쿼리가 항상 같은 값을 반환. 최신 값이 아닐 수 있음. MySQL(InnoDB), MariaDB 기본값
4. Serializable: 동시 실행 결과가 순차 실행 결과와 동일함을 보장. 잠금 경합 또는 직렬화 실패로 인한 성능 저하와 재시도 비용 발생

## 왜 그런가 / 장단점
- 격리수준을 낮출수록 동시성은 올라가고 데이터 정합성은 떨어진다
- Read Committed: 조회 성능이 좋으나 같은 트랜잭션 내 반복 조회 값이 달라질 수 있음
- Repeatable Read: 정합성이 높으나 언두 로그 유지 비용이 늘고, 장시간 트랜잭션 시 언두 영역이 비대해짐
- Serializable: 정합성 최상이나 처리량 저하가 커서 특수한 경우에만 사용

## 참고 자료
- MySQL 공식 문서 - InnoDB Transaction Isolation Levels
- PostgreSQL 공식 문서 - Transaction Isolation

## 더 알아볼 것
- MVCC와 언두 로그 동작 방식
- Next-Key Lock, Gap Lock
- Lost Update와 Write Skew
