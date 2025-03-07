#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
def canMakeBouquets(self, bloomDay, mid, m, k):
        count, bouquets = 0, 0
        for flower in bloomDay:
            if flower <= mid:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
        return bouquets >= m

def minDays(self, bloomDay, m, k):
    if len(bloomDay) < m * k:
        return -1
        
    start, end = min(bloomDay), max(bloomDay)
    while start <= end:
        mid = start + (end - start) // 2

        if self.canMakeBouquets(bloomDay, mid, m, k) == True:
            end = mid - 1
        else:
            start = mid + 1
    return start