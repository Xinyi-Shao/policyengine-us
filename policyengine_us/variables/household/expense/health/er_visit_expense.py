from policyengine_us.model_api import *


class er_visit_expense(Variable):
    value_type = float
    entity = Person
    label = "ER visit expenses"
    unit = USD
    definition_period = YEAR
