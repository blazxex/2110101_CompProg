def total(pocket):
    amount = 0
    for x in pocket:
        amount+= x*pocket[x]
    return amount

def take(pocket,money_in):
    for bill in money_in:
        if bill in pocket:
            pocket[bill]+= money_in[bill]
        else:
            pocket[bill] = money_in[bill]
    

# def pay(pocket,amt):
#     cash_out = {}
#     initail_amt = amt
#     if amt<=total(pocket):
#         for bill in sorted(pocket.keys(),reverse=True):
            
#             num_bill_use = amt//bill
#             if num_bill_use != 0:
#                 if pocket[bill]>= num_bill_use:
#                     amt-= num_bill_use*bill
#                     cash_out[bill] = num_bill_use
#                     pocket[bill]-= num_bill_use
#                 else:
#                     amt -= bill*pocket[bill]
#                     cash_out[bill] = pocket[bill]
#                     pocket[bill]-=pocket[bill]
#             if amt==0:
#                 break
#         if initail_amt!= total(cash_out):
#             take(pocket,cash_out)
#             return {}
#     return cash_out

def pay(pocket,amt):
    cash_out = {}
    a = amt
    
    if amt>total(pocket):
        return {}
    else:
        # pocket = sorted(pocket.keys(),reverse=True)
        # min_bill = list(pocket.keys())[-1]
        while amt%10> 1*pocket[1]:
            try:
                pocket[5]-=1
                cash_out[5]=1
                amt-=5
            except:
                return {}
            
        for bill in sorted(pocket.keys(),reverse=True):
            num_bill_use = amt//bill
            if num_bill_use != 0:
                if pocket[bill]>= num_bill_use:
                    amt-= num_bill_use*bill
                    if bill in cash_out:
                        cash_out[bill] += num_bill_use
                    else: cash_out[bill] = num_bill_use
                    pocket[bill]-= num_bill_use
                else:
                    amt -= bill*pocket[bill]
                    cash_out[bill] = pocket[bill]
                    pocket[bill]-=pocket[bill]
            if amt==0:
                break
        
    return cash_out
        


exec(input().strip())