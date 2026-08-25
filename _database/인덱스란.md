---
title: "인덱스란 무엇인가?"
date: 2026-08-24
tags: [Database, Index]
---

## Q. 인덱스란 무엇인가?

## A. 핵심 답변
B-tree 구조로 되어있고 인덱스로 생성하면 빠르게 접근할 수 있는 장점이 있다.
다만 인덱스 생성 자체도 메모리를 소요하기에 많이 생성하면 메모리 비용이 소모된다.

## 왜 그런가 / 장단점
- 장점: WHERE, JOIN, ORDER BY 대상 컬럼의 탐색 속도가 O(log n)으로 개선된다.
- 단점(트레이드오프): INSERT/UPDATE/DELETE 시 인덱스도 함께 갱신되어야 하므로 쓰기 비용과 저장 공간이 늘어난다.

## 참고 자료
- [MySQL 공식 문서 - Index](https://dev.mysql.com/doc/refman/8.0/en/mysql-indexes.html)

## 더 알아볼 것 (선택)
- 커버링 인덱스(Covering Index)
- B-tree vs Hash 인덱스 차이
