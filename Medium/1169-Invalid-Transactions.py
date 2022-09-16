class Solution:
    def invalidTransactions(self, transactions):
        store = {}
        res = []
        for transaction in transactions:
            val = transaction.split(",")
            if val[0] not in store:
                store[val[0]] = []
            store[val[0]].append([transaction, False])
            
            if len(store[val[0]]) == 1:
                if int(val[2]) > 1000:
                    res.append(transaction)
                    store[val[0]][-1][-1] = True
            else:
                for i in range(len(store[val[0]])-1):
                    lastTransaction = store[val[0]][i][0]
                    lastTransactionTime = int(store[val[0]][i][0].split(",")[1])
                    lastTransactionLocation = store[val[0]][i][0].split(",")[3]
                    if (abs((int(val[1])-lastTransactionTime)) <= 60 and val[3] != lastTransactionLocation):
                        if not store[val[0]][-1][-1]:
                            res.append(transaction)
                            store[val[0]][-1][-1] = True
                        if not store[val[0]][i][-1]:
                            res.append(lastTransaction)
                            store[val[0]][i][-1] = True
                if int(val[2]) > 1000 and not store[val[0]][-1][-1]:
                    res.append(transaction)
                    store[val[0]][-1][-1] = True
        return res