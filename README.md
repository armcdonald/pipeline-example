# Loan Present Value Calculator

A Python application that calculates the present value of a loan based on periodic payments, interest rate, and loan term.

**Python Version:** 3.14 (latest stable)  
**Package Manager:** uv (recommended) or pip  
**Testing:** pytest with 80% coverage requirement

---

## 🚀 Quick Start

### Step 1: Install uv (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# OR via Homebrew
brew install uv

# OR via pip
pip install uv
```

### Step 2: Install Dependencies

```bash
uv pip install -r requirements.txt
```

### Step 3: Run Tests

```bash
uv run pytest test_loan_calculator.py -v
```

### Step 4: Run with Coverage

```bash
uv run pytest test_loan_calculator.py --cov=loan_calculator --cov-report=html
```

---

## 📁 Project Structure

```
loan-calculator/
├── .github/
│   └── workflows/
│       └── python-ci.yml       # GitHub Actions CI/CD pipeline
├── loan_calculator.py          # Main calculator module
├── test_loan_calculator.py     # Pytest test suite (30 tests)
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project configuration
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

---

## 💻 Usage

### As a Command-Line Tool

```bash
python loan_calculator.py
```

Then enter:
- Monthly payment amount
- Annual interest rate (as percentage)
- Loan term in years

### As a Module

```python
from loan_calculator import LoanCalculator

# Calculate PV for a $1,000/month payment at 5% annual rate for 5 years
pv = LoanCalculator.calculate_present_value(
    payment=1000,
    annual_rate=0.05,
    periods=60,
    periods_per_year=12
)
print(f"Present Value: ${pv:,.2f}")
```

---

## 🧪 Running Tests

### Run all tests
```bash
uv run pytest test_loan_calculator.py -v
```

### Run with coverage
```bash
uv run pytest test_loan_calculator.py --cov=loan_calculator --cov-report=html
```

### View HTML coverage report
```bash
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

---

## 🔄 CI/CD Pipeline Setup

### What the Pipeline Does

On every push/PR to `main` or `develop`:
- ✅ Runs 30 tests on Python 3.14
- ✅ Generates coverage reports (must be ≥80%)
- ✅ Checks code quality with flake8
- ✅ Verifies formatting with black
- ✅ Checks import sorting with isort
- ✅ Uploads coverage artifacts
- ✅ Displays coverage in GitHub Actions summary

### Setup Instructions

1. **Copy all files to your repository**
2. **Commit and push**:
   ```bash
   git add .
   git commit -m "Add loan calculator with CI/CD pipeline"
   git push
   ```
3. **View pipeline**: Go to GitHub → Actions tab

---

## 📊 Features

### Calculation
- Present value of annuity formula: `PV = PMT × [(1 - (1 + r)^-n) / r]`
- Handles zero interest rate edge case
- Supports multiple payment frequencies (annual, semi-annual, quarterly, monthly, weekly, daily)
- Results rounded to 2 decimal places

### Validation
- **Payment**: Must be positive, ≤ $1,000,000,000
- **Interest Rate**: Must be non-negative, ≤ 100% per period
- **Periods**: Must be integer between 1 and 600
- **Periods per Year**: Must be 1, 2, 4, 12, 52, or 365

### Testing
- 30 comprehensive test cases
- 82%+ code coverage
- Tests validation, calculations, edge cases, and consistency

---

## 📝 Examples

### 30-Year Mortgage
```python
pv = LoanCalculator.calculate_present_value(
    payment=2000,
    annual_rate=0.04,
    periods=360,  # 30 years × 12 months
    periods_per_year=12
)
# Result: $418,922.48
```

### 5-Year Car Loan
```python
pv = LoanCalculator.calculate_present_value(
    payment=500,
    annual_rate=0.06,
    periods=60,  # 5 years × 12 months
    periods_per_year=12
)
# Result: $25,863.78
```

### 10-Year Personal Loan (Quarterly Payments)
```python
pv = LoanCalculator.calculate_present_value(
    payment=3000,
    annual_rate=0.08,
    periods=40,  # 10 years × 4 quarters
    periods_per_year=4
)
# Result: $81,725.67
```

---

## 🛠️ Development

### Code Quality Tools

```bash
# Format code with black
uv run black loan_calculator.py test_loan_calculator.py

# Check with flake8
uv run flake8 loan_calculator.py test_loan_calculator.py --max-line-length=100

# Sort imports with isort
uv run isort loan_calculator.py test_loan_calculator.py
```

### Pre-commit Checklist
- [ ] All tests pass: `uv run pytest`
- [ ] Coverage ≥80%: `uv run pytest --cov=loan_calculator`
- [ ] Code formatted: `uv run black .`
- [ ] No linting errors: `uv run flake8 .`
- [ ] Imports sorted: `uv run isort .`

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `uv run pytest`
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

The CI/CD pipeline will automatically run on your PR!

---

## 📚 Requirements

- Python ≥3.14
- pytest ≥7.4.0
- pytest-cov ≥4.1.0
- coverage[toml] ≥7.3.0

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🔍 Troubleshooting

### Tests failing locally?
```bash
# Make sure dependencies are installed
uv pip install -r requirements.txt

# Run tests with verbose output
uv run pytest test_loan_calculator.py -v
```

### Coverage below 80%?
```bash
# View detailed coverage report
uv run pytest --cov=loan_calculator --cov-report=html
open htmlcov/index.html

# See which lines aren't covered
uv run pytest --cov=loan_calculator --cov-report=term-missing
```

### GitHub Actions failing?
- Check the Actions tab for detailed error messages
- Ensure all files are committed (especially `.github/workflows/python-ci.yml`)
- Verify Python 3.14 is specified in the workflow

### uv not found?
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use pip instead
pip install -r requirements.txt
pytest test_loan_calculator.py -v
```

---

**Made with ❤️ using Python 3.14 and uv**
