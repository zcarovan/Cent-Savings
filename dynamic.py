class CentSavings:
    def __init__(self, memo):
        self.memo = memo

    def cent_savings(self, i, n, d, p):

        min_cost = 30000000

        #If no more dividers left, output rounded sum of rest of elements.
        if not d:
            total_cost = 0
            for q in range(i, n):
                total_cost += p[q]
            self.memo[n - 1][i] = round(total_cost, -1)
            return round(total_cost, -1)

        #If this entry in the table is already filled in, output from the table.
        if self.memo[n - 1][i] != 30000000:
            return self.memo[n - 1][i]

        #If 1 item, no dividers needed in between.
        if n - i == 1:
            self.memo[n - 1][i] = round(p[i], -1)
            return round(p[i], -1)

        #otherwise, recurse through solutions to get answer.
        for k in range(i + 1, n):
            total_price = 0
            for j in range(i, k):
                total_price += p[j] 
            total_price = round(total_price, -1)
            new_cost = total_price + self.cent_savings(k, n, d - 1, p)
            min_cost = min(min_cost, new_cost)
        
        #Is the price with no dividers cheaper?
        no_div_price = 0
        for m in range(i, n):
            no_div_price += p[m]
        no_div_price = round(no_div_price, -1)
        min_cost = min(min_cost, no_div_price)

        self.memo[n - 1][i] = min_cost
        return min_cost

def main():
    line_one = input()
    line_two = input()
    n_d_list = line_one.split()
    string_p_list = line_two.split()
    p = []
    for i in string_p_list:
        p.append(int(i))
    n = int(n_d_list[0])
    d = int(n_d_list[1])
    m = [[30000000 for _ in range(n)] for _ in range(n)]
    c = CentSavings(m)

    min_cost = c.cent_savings(0, n, d, p)
    print(min_cost)

if __name__ == "__main__":
    main()
'''
     __________________________________________________
    | rows = # of items on belt                        |
    | columns = index started at                       |
    | start at 0, 1 item)       (start at 1, 1 item)   |
    | start at 0, 2 items)       (start at 1, 2 items) |
    | start at 0, 3 items)       (start at 1, 3 items) |
    | start at 0, 4 items)       (start at 1, 4 items) |
    | start at 0, 5 items)       (start at 1, 5 items) |
     __________________________________________________
'''
