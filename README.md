# Risk Utility Curve Analysis

This project explores risk-based decision-making using utility functions, implemented in Python. The goal is to evaluate a company's preferences when faced with guaranteed outcomes versus probabilistic gains, and visualize those preferences using a utility curve.

---

### Objective

Analyze and graphically represent the **risk utility preferences** for a company using the exponential utility function:

\[
$U(M) = e^{M/50} - 1$
\]

Where `M` is the monetary value associated with either a guaranteed return or a probabilistic (risky) option.

---

### 📊 Financial Options Compared

- **Option A:** Guaranteed to make $M
- **Option B:** M% chance to make 100, (100 − M)% chance to make 0

The goal is to compute and compare the **expected utility** of both options for various values of M.

---

### Features & Tasks Completed

- Derived and coded utility equations for both financial options
- Calculated and **graphed utility values** for M ranging from 0 to 100 in steps of 10
- Analyzed and identified the company's **risk preference**
- Calculated and compared utility values for M = 40 and 70
- Determined the **equivalent gamble percentage** that yields the same utility as a guaranteed $70
- Fully documented and explained all decisions in code and graphically

---

### Example Output

- Utility graph (`utility_plot.png`) clearly shows the comparison between guaranteed vs. risky options
- Terminal outputs provide specific utility values and explain decision preferences
- Output example:
  ```
  --- For M = $40 ---
  Utility Option A (UA): 1.2255
  Utility Option B (UB): 2.5556
  Preferred Option: B (Gamble)
  Reason: The expected utility of the gamble is higher...

  --- Equivalent Gamble % for $70 Guaranteed ---
  A guaranteed $70 has a utility of: 3.0552
  To match this utility, the company would accept a gamble with a 47.82% chance of receiving $100.
  ```

---

### Skills Demonstrated

- Python scripting & visualization (NumPy, Matplotlib, SciPy)
- Risk analysis and decision theory
- Clean code organization and documentation
- Data storytelling through visual and numerical analysis

---

### 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/risk-utility-curve.git
   cd risk-utility-curve
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install matplotlib numpy scipy
   ```

4. Run the script:
   ```bash
   python risk_utility_curve.py
   ```

---

### Authors & Credits

Developed by John Dawood as part of a project assignment on risk utility modeling and Python data analysis.

### 📬 License

MIT License. Feel free to use this code as a learning reference or build upon it.

