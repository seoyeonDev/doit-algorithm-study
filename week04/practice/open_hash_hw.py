from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 선형 조사법으로 해시 구현
class Status(Enum):
    OCCUPIED = 0 # 데이터가 존재하는 상태
    EMPTY = 1 # 데이터가 없는 상태
    DELETED = 2 # 과거에 데이터가 존재했지만 삭제된 상태

# 버킷 클래스
class Bucket:
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat

# 선형 조사법으로 해시 구현
class OpenHash:
    # 생성자
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    # 해시값 계산 메소드
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    # 재해시 메소드
    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity

    # 키로 버킷을 검색하는 메소드
    def search_node(self, key: Any) -> int:
        hash_index = self.hash_value(key)
        p = self.table[hash_index]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash_index = self.rehash_value(key)
            p = self.table[hash_index]
        return None

    # 키로 값을 검색하는 메소드
    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    # 키와 값을 추가하는 메소드
    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(key)
            p = self.table[hash]
        return False

    # 키를 삭제하는 메소드
    def remove(self, key: Any) -> bool:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True

    # 해시 테이블의 내용을 출력하는 메소드
    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.DELETED:
                print('-- 삭제된 버킷 --')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 버킷이 비어 있음 --')
