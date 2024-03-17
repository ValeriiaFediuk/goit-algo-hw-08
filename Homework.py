import heapq

def merge_cables(cables):
    heapq.heapify(cables)
    total = 0

    while len(cables) > 1:
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)

        merged_cable = shortest1 + shortest2
        total += merged_cable

        heapq.heappush(cables, merged_cable)

    return total

cables = [3, 5, 2, 7]
min = merge_cables(cables)
print(f"Мінімальні витрати на об'єднання кабелів: {min}")

