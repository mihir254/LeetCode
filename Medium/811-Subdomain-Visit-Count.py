class Solution:
    def subdomainVisits(self, cpdomains):
        store = {}
        for domain in cpdomains:
            count, dom = domain.split(" ")
            subd = dom.split(".")
            while subd:
                subdomain = ".".join(subd)
                if subdomain not in store:
                    store[subdomain] = 0
                store[subdomain] += int(count)
                subd.pop(0)
        res = []
        for k,v in store.items():
            ele = str(v)+" "+k
            res.append(ele)
        return res