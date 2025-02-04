from policyengine_us.model_api import *


class medicaid_income_level(Variable):
    value_type = float
    entity = Person
    label = "Medicaid/CHIP/ACA-related income level"
    unit = "/1"
    documentation = "Income for Medicaid/CHIP/ACA as a fraction of the federal poverty line for this person."
    definition_period = YEAR

    def formula(person, period, parameters):
        return person.tax_unit("tax_unit_medicaid_income_level", period)
