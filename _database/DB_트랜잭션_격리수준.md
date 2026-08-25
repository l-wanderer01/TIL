---
title: "DB 트랜잭션 격리수준"
date: 2026-08-25
tags: [Database, Index]
---

## Q. DB 트랜잭션 격리수준에 대해 아는거 말씀해주세요

## A. 핵심 답변
트랜잭션 격리수준은 총 4개로 나뉜다.
1. Read Uncommitted : 가장 낮은 격리 수준으로 서로 다른 트랜잭션이 동일한 자원에 대해 읽기 쓰기가 가능
2. Read Committed : 커밋된 자원에 대해서 읽기만 가능 PostgreSQL, MySQL이 이 방식을 택함
3. Repeatable Read : 동일 트랜잭션에서 일관된 값을 읽을 수 있지만, 읽은 값이 가장 최신의 값이 아닐 수 있음, Oracle, MariaDB가 이 방식을 사용
4. Serializable : 가장 높은 격리 수준으로 하나의 자원에 대해 하나의 트랜잭션만 접근해 읽기와 쓰기가 가능함. 자원에 대한 점유가 정말 필요한 경우에만 사용하고, 이를 사용하게 된다면 DB 성능 저하가 생길 수 있음

## 왜 그런가 / 장단점
- 장점: WHERE, JOIN, ORDER BY 대상 컬럼의 탐색 속도가 O(log n)으로 개선된다.
- 단점(트레이드오프): INSERT/UPDATE/DELETE 시 인덱스도 함께 갱신되어야 하므로 쓰기 비용과 저장 공간이 늘어난다.

## 참고 자료
- [MySQL 공식 문서 - Index](https://dev.mysql.com/doc/refman/8.0/en/mysql-indexes.html)

## 더 알아볼 것 (선택)
- 커버링 인덱스(Covering Index)
- B-tree vs Hash 인덱스 차이
