import os

states = [
    ("Alabama", 0.05),
    ("Alaska", 0.00),
    ("Arizona", 0.025),
    ("Arkansas", 0.047),
    ("California", 0.09),
    ("Colorado", 0.044),
    ("Connecticut", 0.06),
    ("Delaware", 0.066),
    ("Florida", 0.00),
    ("Georgia", 0.0575),
    ("Hawaii", 0.08),
    ("Idaho", 0.058),
    ("Illinois", 0.0495),
    ("Indiana", 0.0323),
    ("Iowa", 0.057),
    ("Kansas", 0.057),
    ("Kentucky", 0.045),
    ("Louisiana", 0.0425),
    ("Maine", 0.0715),
    ("Maryland", 0.05),
    ("Massachusetts", 0.05),
    ("Michigan", 0.0425),
    ("Minnesota", 0.068),
    ("Mississippi", 0.05),
    ("Missouri", 0.054),
    ("Montana", 0.0675),
    ("Nebraska", 0.0684),
    ("Nevada", 0.00),
    ("New Hampshire", 0.00),
    ("New Jersey", 0.07),
    ("New Mexico", 0.059),
    ("New York", 0.0685),
    ("North Carolina", 0.0475),
    ("North Dakota", 0.029),
    ("Ohio", 0.0399),
    ("Oklahoma", 0.0475),
    ("Oregon", 0.0875),
    ("Pennsylvania", 0.0307),
    ("Rhode Island", 0.0599),
    ("South Carolina", 0.065),
    ("South Dakota", 0.00),
    ("Tennessee", 0.00),
    ("Texas", 0.00),
    ("Utah", 0.0485),
    ("Vermont", 0.067),
    ("Virginia", 0.0575),
    ("Washington", 0.00),
    ("West Virginia", 0.0512),
    ("Wisconsin", 0.053),
    ("Wyoming", 0.00)
]

POPULAR_STATES_HTML = """
        <a href="california-salary-after-tax-calculator.html">California</a>
        <a href="texas-salary-after-tax-calculator.html">Texas</a>
        <a href="florida-salary-after-tax-calculator.html">Florida</a>
        <a href="new-york-salary-after-tax-calculator.html">New York</a>
        <a href="illinois-salary-after-tax-calculator.html">Illinois</a>
        <a href="georgia-salary-after-tax-calculator.html">Georgia</a>
        <a href="washington-salary-after-tax-calculator.html">Washington</a>
        <a href="states.html">All States</a>
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{state_name} Salary After Tax Calculator (2026)</title>
<meta name="description" content="Use this {state_name} salary after tax calculator to estimate take-home pay after federal and {state_name} state taxes in 2026. Compare gross salary vs net income instantly.">
<link rel="canonical" href="https://salary-calculator-site-blush.vercel.app/{state_slug}-salary-after-tax-calculator.html" />

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "{state_name} Salary After Tax Calculator",
  "url": "https://salary-calculator-site-blush.vercel.app/{state_slug}-salary-after-tax-calculator.html",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "All",
  "description": "Estimate take-home pay in {state_name} after federal and state taxes.",
  "offers": {{
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }}
}}
</script>

<style>
  body {{
    font-family: Arial, sans-serif;
    background: #f5f7fa;
    color: #222;
    margin: 0;
    line-height: 1.7;
  }}

  .container {{
    max-width: 1000px;
    margin: 0 auto;
    padding: 32px 20px 60px;
  }}

  .box {{
    background: #fff;
    border-radius: 12px;
    padding: 26px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
    margin-bottom: 24px;
  }}

  h1, h2, h3 {{
    line-height: 1.25;
  }}

  h1 {{
    font-size: 38px;
    margin-bottom: 14px;
  }}

  h2 {{
    font-size: 28px;
    margin-top: 0;
    margin-bottom: 14px;
  }}

  h3 {{
    font-size: 20px;
    margin-top: 24px;
    margin-bottom: 10px;
  }}

  p {{
    margin: 0 0 16px;
  }}

  .calculator-box {{
    background: #ffffff;
    border-radius: 12px;
    padding: 24px;
    border: 1px solid #e6ebf2;
  }}

  label {{
    display: block;
    font-weight: bold;
    margin-top: 12px;
    margin-bottom: 6px;
  }}

  input, select, button {{
    width: 100%;
    padding: 11px;
    font-size: 16px;
    border: 1px solid #d7dce3;
    border-radius: 8px;
    box-sizing: border-box;
  }}

  button {{
    margin-top: 16px;
    background: #1a73e8;
    color: white;
    border: none;
    font-weight: bold;
    cursor: pointer;
  }}

  button:hover {{
    background: #155ac2;
  }}

  .result-box {{
    margin-top: 16px;
    padding: 16px;
    border-radius: 10px;
    background: #eef6ff;
    border: 1px solid #d7e8ff;
    font-weight: bold;
  }}

  .ad-box {{
    margin: 20px 0;
    padding: 20px;
    background: #f2f2f2;
    text-align: center;
    border-radius: 10px;
  }}

  .quick-links {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 12px;
  }}

  .quick-links a {{
    background: #eef3fb;
    color: #1a73e8;
    text-decoration: none;
    padding: 8px 12px;
    border-radius: 20px;
    font-size: 14px;
  }}

  .quick-links a:hover {{
    text-decoration: underline;
  }}

  .nav {{
    margin-bottom: 18px;
    font-size: 14px;
  }}

  .nav a {{
    color: #1a73e8;
    text-decoration: none;
  }}

  .nav a:hover {{
    text-decoration: underline;
  }}

  .note {{
    font-size: 13px;
    color: #666;
    margin-top: 28px;
  }}

  @media (max-width: 700px) {{
    h1 {{
      font-size: 31px;
    }}

    h2 {{
      font-size: 24px;
    }}
  }}
</style>
</head>
<body>
  <div class="container">

    <div class="nav">
      <a href="index.html">Home</a> |
      <a href="calculator.html">Calculator</a> |
      <a href="states.html">All States</a> |
      <a href="how-it-works.html">How It Works</a> |
      <a href="state-income-tax-guide.html">State Tax Guide</a> |
      <a href="faq.html">FAQ</a> |
      <a href="about.html">About</a>
    </div>

    <section class="box">
      <h1>{state_name} Salary After Tax Calculator</h1>

      <p>
        This {state_name} salary after tax calculator helps estimate take-home pay after
        federal and {state_name} state taxes. It is useful for salary comparison, relocation planning,
        and understanding how much of your gross income you may actually keep.
      </p>

      <p>
        Use this page to estimate annual and monthly net income in {state_name},
        compare after-tax salary outcomes, and understand how state tax rules affect take-home pay.
      </p>
    </section>

    <section class="box">
      <div class="calculator-box">

        <label for="salary">Annual Salary ($)</label>
        <input type="number" id="salary" placeholder="50000">

        <label for="status">Filing Status</label>
        <select id="status">
          <option value="single">Single</option>
          <option value="married">Married</option>
        </select>

        <button onclick="calculate()">Calculate</button>

        <div class="result-box" id="output">
          Enter your salary to estimate after-tax income in {state_name}.
        </div>

      </div>
    </section>

    <div class="ad-box">
      Ad Space
    </div>

    <section class="box">
      <h2>How Taxes Work in {state_name}</h2>

      <p>
        Take-home pay in {state_name} depends on federal income tax, payroll taxes,
        and {state_name} state income tax rules. Some states use flat tax systems,
        while others apply progressive tax rates based on income level.
      </p>

      <p>
        Because of these tax differences, the same gross salary may produce a different
        net income in {state_name} than it would in another U.S. state.
        This calculator provides an estimate for salary planning and comparison purposes.
      </p>
    </section>

    <section class="box">
      <h2>Example Salaries in {state_name}</h2>

      <p>
        Here are common salary examples people often compare in {state_name}:
      </p>

      <ul>
        <li>$40,000 salary after tax in {state_name}</li>
        <li>$70,000 salary after tax in {state_name}</li>
        <li>$100,000 salary after tax in {state_name}</li>
      </ul>

      <p>
        Actual results may vary depending on filing status, deductions, benefits,
        payroll settings, and individual tax circumstances.
      </p>
    </section>

    <section class="box">
      <h2>Frequently Asked Questions</h2>

      <h3>Does {state_name} have state income tax?</h3>
      <p>
        {state_name} applies its own state income tax rules, and those rules affect
        final take-home pay. This calculator uses a simplified state tax assumption to estimate net income.
      </p>

      <h3>Why is my {state_name} take-home pay lower than my salary?</h3>
      <p>
        Gross salary is reduced by federal taxes, payroll taxes, and state tax rules.
        That is why net pay is lower than the salary number shown in a job offer.
      </p>

      <h3>Is this {state_name} salary calculator accurate?</h3>
      <p>
        This calculator is designed for estimation and salary comparison.
        Actual withholding may differ depending on deductions, credits, benefits,
        and employer payroll calculations.
      </p>
    </section>

    <section class="box">
      <h2>Explore Related State Pages</h2>

      <div class="quick-links">
{popular_states}
      </div>
    </section>

    <p class="note">
      Disclaimer: This page provides estimated salary after tax information for general informational purposes only.
      It should not be considered legal, financial, or tax advice.
    </p>

  </div>

<script>
function calculate() {{
  const salary = parseFloat(document.getElementById("salary").value);
  const status = document.getElementById("status").value;
  const output = document.getElementById("output");

  if (!salary || salary <= 0) {{
    output.innerHTML = "Please enter a valid salary amount.";
    return;
  }}

  const federalTaxRate = status === "single" ? 0.22 : 0.18;
  const federalTax = salary * federalTaxRate;
  const stateTax = salary * {state_tax_rate};
  const netAnnual = salary - federalTax - stateTax;
  const netMonthly = netAnnual / 12;

  output.innerHTML =
    "Estimated Federal Tax: $" + federalTax.toFixed(2) + "<br>" +
    "Estimated State Tax: $" + stateTax.toFixed(2) + "<br>" +
    "Estimated Annual Take-Home Pay: $" + netAnnual.toFixed(2) + "<br>" +
    "Estimated Monthly Take-Home Pay: $" + netMonthly.toFixed(2);
}}
</script>

</body>
</html>
"""


def slugify(state_name: str) -> str:
    return state_name.lower().replace(" ", "-")


def generate_page(state_name: str, state_tax_rate: float) -> str:
    return TEMPLATE.format(
        state_name=state_name,
        state_slug=slugify(state_name),
        state_tax_rate=state_tax_rate,
        popular_states=POPULAR_STATES_HTML.strip()
    )


def main():
    for state_name, state_tax_rate in states:
        filename = f"{slugify(state_name)}-salary-after-tax-calculator.html"
        html = generate_page(state_name, state_tax_rate)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"Generated: {filename}")

    print("All state pages generated successfully.")


if __name__ == "__main__":
    main()