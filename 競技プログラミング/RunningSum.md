# 累積和の計算
```python
N = 5
A = [1,1,1,1,1]
Q = 3
L = [1,3,4]
R = [5,4,5]

# 累積和を求める
Atari = [ 0 ] * (N + 1)
Hazure = [ 0 ] * (N + 1)

for i in range(1,N+1):
    Atari[i] = Atari[i - 1]
    if A[i-1] == 1:
        Atari[i] += 1
    Hazure[i] = Hazure[i - 1]
    if A[i-1] == 0:
        Hazure[i] += 1

#質問に答える
for i in range(Q):
    NumAtari = Atari[R[i]] - Hazure[L[i] - 1]
    NumHazure = Hazure[R[i]] - Hazure[L[i] - 1]
    if NumAtari > NumHazure:
        print("win")
    elif NumAtari == NumHazure:
        print("draw")
    else:
        print("lose")

```
