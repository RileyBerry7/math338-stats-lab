from scipy.stats import norm

def ptostr(p: float):
    return f"{100*p:6.2f}".rstrip('0').rstrip('.') + "%"

class HypothesisTest:
    def __init__(self):
        self.null = 0  # Assumption for x
        self.tail = "" #
        self.sl = 0.05
        self.n  = 0 # Sample size
        self.s  = 0 # Sample deviation
        self.pe = 0 # Point Estimate of x
        self.se = 0 # Standard error of 'Point Estimate'
        self.ts = 0 # Test-statistic
        self.pv = 0 # P-value
    
    def compute_pval(self): 

        # Under approximate normal of our point estimate
        zscore = self.ts
        self.pv = 2 * (1 - norm.cdf(abs(zscore)))
        print("P-value: " + str(self.pv)) # Two-tailed
        # p = 1 - norm.cdf(z) # Right-tailed
        # p = norm.cdf(z)     # Left-tailed

    def conclusion(self):
        sig_lvl = ptostr(self.sl) 
        pval    = ptostr(self.pv)

        if self.pv <= self.sl:
            print("Because " + pval + " < " + sig_lvl)
            print("We reject the null hypothesis.")
        else:
            print("Because " + pval + " > " + sig_lvl)
            print("We fail to reject the null hypothesis.")

def main():
    print("Hype Time!")


    test = HypothesisTest()
    test.ts = 2
    test.compute_pval()
    test.conclusion()

if __name__ == "__main__":
    main()
