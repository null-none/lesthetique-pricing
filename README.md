### lesthetique-pricing

Pricing toolkit for L’esthétique. Calculates material cost, aroma load, packaging and final retail grams.

```python

from .pricing_calculator import CandlegramsCalculator

calc = CandlegramsCalculator()

data = [
    {
        "name": "bubble heart",
        "grams": 160
    },
    {
        "name": "Aelin",
        "grams": 650
    },
    {
        "name": "David",
        "grams": 450
    },
    {
        "name": "BUBBLE HEART + PEONY",
        "grams": 230
    },
    {
        "name": "Sage L",
        "grams": 250
    },
    {
        "name": "Sage L+S",
        "grams": 335
    },
    {
        "name": "СЕТ GIRLS LUISA & STEFANI",
        "grams": 210
    },
    {
        "name": "PALM LEAF",
        "grams": 580
    },
    {
        "name": "TOOTH",
        "grams": 130
    },
    {
        "name": "Face",
        "grams": 330
    },
    {
        "name": "Lotus",
        "grams": 530
    },
    {
        "name": "Knot",
        "grams": 500
    }
]


for item in data:
    result = calc.calculate(
        wax_grams=item["grams"],
        aroma_percent=6.0,
        extra_costs_eur={}
    )
    print(result)

```