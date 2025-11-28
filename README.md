### lesthetique-pricing

Pricing toolkit for L’esthétique. Calculates material cost, aroma load, packaging and final retail price.

```python

from .pricing_calculator import CandlePriceCalculator

calc = CandlePriceCalculator()

result = calc.calculate(
    wax_grams=140,
    aroma_percent=6.0,
    extra_costs_bgn={}
)

print(result)

```