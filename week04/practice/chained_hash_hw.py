from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
	# 체인법으로 해시 구현에서 사용하는 노드 클래스
	def __init__(self, key: Any, value: Any, next: Node) -> None:
		self.key = key
		self.value = value
		self.next = next

# 체인법으로 해시 구현
class ChainedHash:

	# 생성자
	def __init__(self, capacity: int) -> None:
		self.capacity = capacity
		self.table = [None] * self.capacity
		
	# 해시값 계산 메소드
	def hash_value(self, key: Any) -> int:
		if isinstance(key, int):
			return key % self.capacity
		return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

	
	# 키로 값을 검색하는 메소드
	def search(self, key: Any) -> Any:
		hash_index = self.hash_value(key)
		node = self.table[hash_index]
		
		while node is not None:
			if node.key == key:
				return node.value
			node = node.next

		return None

	# 키와 값을 추가하는 메소드
	def add(self, key: Any, value: Any) -> bool:
		hash_index = self.hash_value(key)
		node = self.table[hash_index]

		while node is not None:
			if node.key == key:
				return False
			node = node.next

		temp = Node(key, value, self.table[hash_index])
		self.table[hash_index] = temp
		return True

	# 키를 삭제하는 메소드
	def remove(self, key: Any) -> bool:
		hash_index = self.hash_value(key)
		node = self.table[hash_index]
		prev = None

		while node is not None:
			if node.key == key: # 키를 발견
				if prev is None:
					self.table[hash_index] = node.next
				else:
					prev.next = node.next
				return True # 키를 발견하여 삭제 성공
			prev = node
			node = node.next
		return False # 키를 발견하지 못하여 삭제 실패

	# 해시 테이블의 내용을 출력하는 메소드
	def dump(self) -> None:
		for i in range(self.capacity):
			node = self.table[i]

			if node is not None:
				print(f"Bucket {i}:", end="")
				while node is not None:
					print(f" -> {node.key} ({node.value})", end="")
					node = node.next
				print()