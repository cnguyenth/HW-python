def calculate_apr(principal, interest_rate, years):
        """
        Calculate investment amount after x years.

        Given a principal amount of money and an interest rate, calculate the total amount
        of money in the investment after x years.

        Parameters
        ----------
        principal : int
                Inital amount of money in investment.
        interest_rate : float
                Interest rate.
        years : int
                Years after initial investment.

        Returns
        -------
        float
                Total investment amount.

        Examples
        --------
        >>> calculate_apr(500, 0.03, 65)
        3414.9913672928196
        """
        
        if isinstance(principal, float) or isinstance(principal, int) and isinstance(interest_rate, float) and isinstance(years, int):
                investment = float(principal)
                for i in range(years):
                        investment = investment*(1.0+interest_rate)

                return investment
        else:
                return False
