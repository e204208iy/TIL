# https://atcoder.jp/contests/abc355/submissions/me
## 回答コード
```python
N, M = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
C = A + B
C.sort()
for i in range(N + M - 1):
    if C[i] in A and C[i + 1] in A:
        print("Yes")
        exit()
print("No")
```
## 解説
- Aに現れる要素がCの中で連続するかどうか判定するので、Cの要素の前後を比較する。
- Cの長さはN＋MでCのインデックスは０から始まるので-1をする。
- 
