def calculate_apr(principal, interest_rate, years):
        investment = float(principal)
        if principal < 0 or interest_rate < 0 or years < 0:
                return false
        else:
                for i in range(years):
                        investment = investment*(1.0+interest_rate)

        return investment
def main():
        print(calculate_apr(500, 0.03, 65))
