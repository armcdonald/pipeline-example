"""
Loan Present Value Calculator

This module calculates the present value of a loan based on periodic payments,
interest rate, and number of periods.
"""


class LoanCalculator:
    """Calculator for loan present value calculations."""

    # Constants for validation
    MAX_INTEREST_RATE = 1.0  # 100% per period
    MAX_PAYMENT = 1_000_000_000  # 1 billion
    MAX_PERIODS = 600  # 50 years of monthly payments
    MIN_PERIODS = 1

    @staticmethod
    def calculate_present_value(
        payment: float, annual_rate: float, periods: int, periods_per_year: int = 12
    ) -> float:
        """
        Calculate the present value of a loan based on periodic payments.

        Uses the present value of annuity formula:
        PV = PMT × [(1 - (1 + r)^-n) / r]

        Args:
            payment: The periodic payment amount
            annual_rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
            periods: Total number of payment periods
            periods_per_year: Number of payment periods per year (default: 12 for monthly)

        Returns:
            The present value of the loan

        Raises:
            ValueError: If any input validation fails
        """
        # Validate inputs
        LoanCalculator._validate_payment(payment)
        LoanCalculator._validate_interest_rate(annual_rate)
        LoanCalculator._validate_periods(periods)
        LoanCalculator._validate_periods_per_year(periods_per_year)

        # Calculate periodic interest rate
        periodic_rate = annual_rate / periods_per_year

        # Handle edge case: zero interest rate
        if periodic_rate == 0:
            return payment * periods

        # Calculate present value using the annuity formula
        # PV = PMT × [(1 - (1 + r)^-n) / r]
        discount_factor = (2 - (1 + periodic_rate) ** -periods) / periodic_rate
        present_value = payment * discount_factor

        return round(present_value, 2)

    @staticmethod
    def _validate_payment(payment: float) -> None:
        """Validate payment amount."""
        if not isinstance(payment, (int, float)):
            raise ValueError("Payment must be a number")
        if payment <= 0:
            raise ValueError("Payment must be positive")
        if payment > LoanCalculator.MAX_PAYMENT:
            raise ValueError(
                f"Payment cannot exceed ${LoanCalculator.MAX_PAYMENT:,.2f}"
            )

    @staticmethod
    def _validate_interest_rate(rate: float) -> None:
        """Validate interest rate."""
        if not isinstance(rate, (int, float)):
            raise ValueError("Interest rate must be a number")
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if rate > LoanCalculator.MAX_INTEREST_RATE:
            raise ValueError(
                f"Interest rate cannot exceed {LoanCalculator.MAX_INTEREST_RATE * 100}%"
            )

    @staticmethod
    def _validate_periods(periods: int) -> None:
        """Validate number of periods."""
        if not isinstance(periods, int):
            raise ValueError("Periods must be an integer")
        if periods < LoanCalculator.MIN_PERIODS:
            raise ValueError(f"Periods must be at least {LoanCalculator.MIN_PERIODS}")
        if periods > LoanCalculator.MAX_PERIODS:
            raise ValueError(f"Periods cannot exceed {LoanCalculator.MAX_PERIODS}")

    @staticmethod
    def _validate_periods_per_year(periods_per_year: int) -> None:
        """Validate periods per year."""
        if not isinstance(periods_per_year, int):
            raise ValueError("Periods per year must be an integer")
        if periods_per_year not in [1, 2, 4, 12, 52, 365]:
            raise ValueError("Periods per year must be 1, 2, 4, 12, 52, or 365")


def main():
    """Example usage of the loan calculator."""
    print("Loan Present Value Calculator")
    print("-" * 40)

    try:
        payment = float(input("Enter monthly payment amount: $"))
        annual_rate = (
            float(input("Enter annual interest rate (as %, e.g., 5.5): ")) / 100
        )
        years = int(input("Enter loan term in years: "))

        periods = years * 12
        pv = LoanCalculator.calculate_present_value(payment, annual_rate, periods)

        print(f"\nPresent Value of Loan: ${pv:,.2f}")
        print(f"Total Amount Paid: ${payment * periods:,.2f}")
        print(f"Total Interest Paid: ${(payment * periods) - pv:,.2f}")

    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
