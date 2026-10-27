import math
from decimal import Decimal, getcontext
from typing import Optional, Dict

# Set decimal precision
getcontext().prec = 10


class CandlePriceCalculator:
    """
    A calculator for candle production cost and final retail price.

    It supports:
    - Wax cost
    - Aroma oil cost based on percentage
    - Fixed packaging cost
    - Extra material costs
    - Individual multipliers for wax, aroma, packaging and extras

    All amounts are in EUR. Totals are rounded up to a whole euro.
    """

    def __init__(
        self,
        # Defaults converted from the old BGN rates (18.00 / 0.20 / 7.10)
        # at the fixed rate 1 EUR = 1.95583 BGN.
        wax_price_per_kg_eur: Decimal = Decimal("9.20"),
        oil_price_per_g_eur: Decimal = Decimal("0.1023"),
        base_pack_cost_eur: Decimal = Decimal("3.63"),
        aroma_percent_default: Decimal = Decimal("6.0"),
        wax_multiplier: Decimal = Decimal("3.0"),
        aroma_multiplier: Decimal = Decimal("2.0"),
        packaging_multiplier: Decimal = Decimal("2.0"),
        extras_multiplier: Decimal = Decimal("1.0"),
    ):
        self.wax_price_per_kg_eur = wax_price_per_kg_eur
        self.oil_price_per_g_eur = oil_price_per_g_eur
        self.base_pack_cost_eur = base_pack_cost_eur
        self.aroma_percent_default = aroma_percent_default

        # Multipliers
        self.wax_multiplier = wax_multiplier
        self.aroma_multiplier = aroma_multiplier
        self.packaging_multiplier = packaging_multiplier
        self.extras_multiplier = extras_multiplier

        # Precalculate price per gram of wax
        self.wax_price_per_g = self.wax_price_per_kg_eur / Decimal("1000")

    def calculate(
        self,
        wax_grams: float,
        aroma_percent: Optional[float] = None,
        extra_costs_eur: Optional[Dict[str, float]] = None,
        candle_type: str = "Body Candle Type #5",
    ) -> dict:
        """
        Calculate total cost and retail price for a candle.

        :param wax_grams: Weight of wax in grams.
        :param aroma_percent: Percentage of aroma oil (defaults to class value).
        :param extra_costs_eur: Dict of extra material costs.
        :param candle_type: Human-readable label for this candle.
        :return: Dictionary with cost breakdown.
        """

        if extra_costs_eur is None:
            extra_costs_eur = {}

        if aroma_percent is None:
            aroma_percent = float(self.aroma_percent_default)

        # Convert to decimals
        wax_g = Decimal(str(wax_grams))
        aroma_pct = Decimal(str(aroma_percent))

        # Wax cost
        wax_cost = wax_g * self.wax_price_per_g

        # Aroma cost
        aroma_grams = wax_g * aroma_pct / Decimal("100")
        aroma_cost = aroma_grams * self.oil_price_per_g_eur

        # Packaging cost
        packaging_cost = self.base_pack_cost_eur

        # Extra materials total
        extra_total = sum(Decimal(str(v)) for v in extra_costs_eur.values())

        # Production cost (sebestoimost)
        production_cost = wax_cost + aroma_cost + packaging_cost + extra_total

        # Final price using multipliers
        final_price = (
            wax_cost * self.wax_multiplier
            + aroma_cost * self.aroma_multiplier
            + packaging_cost * self.packaging_multiplier
            + extra_total * self.extras_multiplier
        )

        return {
            "candle_type": candle_type,
            "input": {
                "wax_grams": float(wax_g),
                "aroma_percent": float(aroma_pct),
                "extra_costs_eur": extra_costs_eur,
            },
            "total_eur": {
                "production_cost": math.ceil(float(production_cost)),
                "final_price": math.ceil(float(final_price)),
            },
            "currency": "EUR",
        }




calc = CandlePriceCalculator()

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
    print(f"{item['name']}: Production Cost = {result['total_eur']['production_cost']} EUR, Final Price = {result['total_eur']['final_price']} EUR")