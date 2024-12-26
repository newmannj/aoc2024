import math
from collections import defaultdict

numbers = []
with open("input.txt") as file:
    for line in file:
        numbers.append(int(line.strip()))

def mix_and_prune(value, secret):
    mixed = value ^ secret
    pruned = mixed % 16777216
    return pruned

# numbers = [1, 2, 3, 2024]
price_after_seqs = defaultdict(list)
p1 = 0
for n_i, n in enumerate(numbers):
    _prev = n
    _n = n
    prev_four_changes = []
    prev_price = int(str(n)[-1])
    for x in range(2000):
        # Step 1:
        _n = _n * 64
        _n = mix_and_prune(_n, _prev)
        # Step 2:
        _prev = _n
        _n = int(math.floor(_n / 32))
        _n = mix_and_prune(_n, _prev)
        # Step 3:
        _prev = _n
        _n = _n * 2048
        _n = mix_and_prune(_n, _prev)
        _prev = _n
        # P2: WTF
        price = int(str(_n)[-1])
        change = price - prev_price
        if len(prev_four_changes) == 4:
            prev_four_changes = prev_four_changes[1:] + [change]
            key = "".join([str(c) for c in prev_four_changes])
            # If we haven't yet seen this key at all, we should pad with 0s
            if not key in price_after_seqs:
                price_after_seqs[key] = [0 for _ in range(n_i)]
            # If we haven't yet added to this sequence, then we can just add
            if n_i >= len(price_after_seqs[key]):
                price_after_seqs["".join([str(c) for c in prev_four_changes])] += [price]
            # else:
            #     if price > price_after_seqs[key][n_i]:
            #         price_after_seqs[key][n_i] = price
        else:
            prev_four_changes.append(change)
            
        prev_price = price
    for v in price_after_seqs.values():
        while(len(v) != n_i + 1):
            v.append(0)
            
    p1 += _n

max = 0
max_key = None
for k, v in price_after_seqs.items():
    lsum = sum(v)
    if lsum > max:
        max = lsum
        max_key = k

print(max_key)
print(max)
print(price_after_seqs[max_key])
print(len(numbers))
