"""
Test cases for the Loan Calculator module.
"""

import pytest
from loan_calculator import LoanCalculator


class TestPresentValueCalculation:
    """Tests for present value calculation."""
    
    def test_basic_calculation(self):
        """Test basic present value calculation."""
        # $1000/month, 5% annual rate, 5 years (60 months)
        pv = LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
        # Expected PV ≈ $52,990.70
        assert abs(pv - 52990.70) < 1.0
    
    def test_zero_interest_rate(self):
        """Test calculation with zero interest rate."""
        # With 0% interest, PV should equal total of all payments
        pv = LoanCalculator.calculate_present_value(500, 0.0, 24, 12)
        assert pv == 500 * 24
    
    def test_high_interest_rate(self):
        """Test calculation with high interest rate."""
        # Higher interest means lower present value
        pv = LoanCalculator.calculate_present_value(1000, 0.20, 60, 12)
        assert pv < 1000 * 60  # PV should be less than total payments
        assert pv > 0
    
    def test_different_payment_frequencies(self):
        """Test calculations with different payment frequencies."""
        # Annual payments
        pv_annual = LoanCalculator.calculate_present_value(12000, 0.05, 5, 1)
        assert pv_annual > 0
        
        # Quarterly payments
        pv_quarterly = LoanCalculator.calculate_present_value(3000, 0.05, 20, 4)
        assert pv_quarterly > 0
    
    def test_single_period(self):
        """Test calculation with single payment period."""
        pv = LoanCalculator.calculate_present_value(1000, 0.05, 1, 12)
        # With one period, PV should be close to payment / (1 + rate)
        assert abs(pv - 995.85) < 1.0
    
    def test_long_term_loan(self):
        """Test calculation with long-term loan (30 years)."""
        pv = LoanCalculator.calculate_present_value(2000, 0.04, 360, 12)
        # 30-year mortgage calculation
        assert pv > 0
        assert abs(pv - 418922.48) < 10.0


class TestPaymentValidation:
    """Tests for payment validation."""
    
    def test_positive_payment(self):
        """Test that positive payment is accepted."""
        # Should not raise an error
        LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
    
    def test_zero_payment(self):
        """Test that zero payment raises error."""
        with pytest.raises(ValueError, match="Payment must be positive"):
            LoanCalculator.calculate_present_value(0, 0.05, 60, 12)
    
    def test_negative_payment(self):
        """Test that negative payment raises error."""
        with pytest.raises(ValueError, match="Payment must be positive"):
            LoanCalculator.calculate_present_value(-100, 0.05, 60, 12)
    
    def test_excessive_payment(self):
        """Test that excessively large payment raises error."""
        with pytest.raises(ValueError, match="Payment cannot exceed"):
            LoanCalculator.calculate_present_value(2_000_000_000, 0.05, 60, 12)
    
    def test_non_numeric_payment(self):
        """Test that non-numeric payment raises error."""
        with pytest.raises(ValueError, match="Payment must be a number"):
            LoanCalculator.calculate_present_value("1000", 0.05, 60, 12)


class TestInterestRateValidation:
    """Tests for interest rate validation."""
    
    def test_positive_rate(self):
        """Test that positive rate is accepted."""
        LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
    
    def test_zero_rate(self):
        """Test that zero rate is accepted."""
        LoanCalculator.calculate_present_value(1000, 0.0, 60, 12)
    
    def test_negative_rate(self):
        """Test that negative rate raises error."""
        with pytest.raises(ValueError, match="Interest rate cannot be negative"):
            LoanCalculator.calculate_present_value(1000, -0.05, 60, 12)
    
    def test_excessive_rate(self):
        """Test that excessively high rate raises error."""
        with pytest.raises(ValueError, match="Interest rate cannot exceed"):
            LoanCalculator.calculate_present_value(1000, 1.5, 60, 12)
    
    def test_non_numeric_rate(self):
        """Test that non-numeric rate raises error."""
        with pytest.raises(ValueError, match="Interest rate must be a number"):
            LoanCalculator.calculate_present_value(1000, "0.05", 60, 12)


class TestPeriodsValidation:
    """Tests for periods validation."""
    
    def test_valid_periods(self):
        """Test that valid period counts are accepted."""
        LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
        LoanCalculator.calculate_present_value(1000, 0.05, 1, 12)
        LoanCalculator.calculate_present_value(1000, 0.05, 360, 12)
    
    def test_zero_periods(self):
        """Test that zero periods raises error."""
        with pytest.raises(ValueError, match="Periods must be at least"):
            LoanCalculator.calculate_present_value(1000, 0.05, 0, 12)
    
    def test_negative_periods(self):
        """Test that negative periods raises error."""
        with pytest.raises(ValueError, match="Periods must be at least"):
            LoanCalculator.calculate_present_value(1000, 0.05, -10, 12)
    
    def test_excessive_periods(self):
        """Test that excessively large period count raises error."""
        with pytest.raises(ValueError, match="Periods cannot exceed"):
            LoanCalculator.calculate_present_value(1000, 0.05, 1000, 12)
    
    def test_non_integer_periods(self):
        """Test that non-integer periods raises error."""
        with pytest.raises(ValueError, match="Periods must be an integer"):
            LoanCalculator.calculate_present_value(1000, 0.05, 60.5, 12)


class TestPeriodsPerYearValidation:
    """Tests for periods per year validation."""
    
    def test_valid_periods_per_year(self):
        """Test that valid periods per year are accepted."""
        valid_frequencies = [1, 2, 4, 12, 52, 365]
        for freq in valid_frequencies:
            LoanCalculator.calculate_present_value(1000, 0.05, 60, freq)
    
    def test_invalid_periods_per_year(self):
        """Test that invalid periods per year raises error."""
        with pytest.raises(ValueError, match="Periods per year must be"):
            LoanCalculator.calculate_present_value(1000, 0.05, 60, 7)
    
    def test_non_integer_periods_per_year(self):
        """Test that non-integer periods per year raises error."""
        with pytest.raises(ValueError, match="Periods per year must be an integer"):
            LoanCalculator.calculate_present_value(1000, 0.05, 60, 12.5)


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""
    
    def test_very_small_payment(self):
        """Test with very small payment amount."""
        pv = LoanCalculator.calculate_present_value(0.01, 0.05, 60, 12)
        assert pv > 0
        assert pv < 1
    
    def test_very_small_interest_rate(self):
        """Test with very small interest rate."""
        pv = LoanCalculator.calculate_present_value(1000, 0.0001, 60, 12)
        assert pv > 0
    
    def test_rounding(self):
        """Test that result is properly rounded to 2 decimal places."""
        pv = LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
        # Check that we have at most 2 decimal places
        assert pv == round(pv, 2)
    
    def test_maximum_valid_values(self):
        """Test with maximum valid values."""
        pv = LoanCalculator.calculate_present_value(
            999_999_999,  # Just under max payment
            0.99,  # Just under max rate
            600,  # Max periods
            12
        )
        assert pv > 0


class TestCalculatorConsistency:
    """Tests for calculation consistency."""
    
    def test_same_inputs_same_output(self):
        """Test that same inputs always produce same output."""
        pv1 = LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
        pv2 = LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
        assert pv1 == pv2
    
    def test_proportional_payment(self):
        """Test that doubling payment doubles present value."""
        pv1 = LoanCalculator.calculate_present_value(1000, 0.05, 60, 12)
        pv2 = LoanCalculator.calculate_present_value(2000, 0.05, 60, 12)
        assert abs(pv2 - (2 * pv1)) < 0.01


if __name__ == "__main__":
    pytest.main([__file__, "-v"])