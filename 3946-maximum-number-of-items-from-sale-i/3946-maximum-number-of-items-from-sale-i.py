class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0]*(budget+1)
        cheapest_item = min(x for _,x in items)

        for factor,price in items:
            cnt = sum(fac%factor==0 for fac,_ in items)

            for j in range(budget,price-1,-1):
                f[j] = max(f[j] , cnt + f[j - price])
            
        return max(f[i] + (budget-i)//cheapest_item for i in range(budget+1))