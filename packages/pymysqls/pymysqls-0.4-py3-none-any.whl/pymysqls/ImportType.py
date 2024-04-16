from enum import Enum


class ImportType(Enum):
    COST_ITEMS = 0
    PRODUCTS = 1
    CALCULATION = 2
    PRODUCTION_PLAN = 3


class ImportTypeTranslation:
    data = {
        "COST_ITEMS": "Статьи затрат",
        "PRODUCTS": "Изделия",
        "CALCULATION": "Калькуляции",
        "PRODUCTION_PLAN": "Планы выпуска"
    }
