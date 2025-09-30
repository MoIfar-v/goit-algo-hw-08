import heapq

def min_merge_cost_with_order(lengths):
    if not lengths:
        return 0, []
    if len(lengths) == 1:
        return 0, []

    heap = list(lengths)
    heapq.heapify(heap)

    total_cost = 0
    merges = []  # зберігаємо пари (a, b) та їх суму

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        merges.append((a, b, cost))
        heapq.heappush(heap, cost)

    return total_cost, merges


if __name__ == "__main__":
    lengths = [8, 4, 6, 12]
    total, merges = min_merge_cost_with_order(lengths)

    print("Довжини:", lengths)
    print("Мінімальна загальна вартість:", total)
    print("Порядок злиттів (a, b, cost):")
    for a, b, c in merges:
        print(f"  {a} + {b} = {c}")