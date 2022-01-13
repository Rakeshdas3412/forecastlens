from faker import Faker
import random


class CreateNewSceanrio:

    create_new_sceanario = {
        "scenario_name": "",
        "scenario_desc": "",
        "start_month": "",
        "end_month": "",
        "country_name": ""

    }

    APAC_Region = ["Australia",
                   "Bangladesh", "Bhutan", "China", "Cambodia"]

    def generate_new_scenario_data(create_new_sceanario):
        fake_data = Faker("en_US")
        create_new_sceanario["scenario_name"] = "Scearnio_name_" + \
            str(fake_data.random_int(10000000, 9999999999999))
        create_new_sceanario["scenario_desc"] = "Scearnio_desc_" + \
            str(fake_data.random_int(10000000, 9999999999999))
        create_new_sceanario["start_month"] = "Sep-2014"
        create_new_sceanario["end_month"] = "Jul-2022"
        create_new_sceanario["country_name"] = random.choice(
            CreateNewSceanrio.APAC_Region)
        return create_new_sceanario
