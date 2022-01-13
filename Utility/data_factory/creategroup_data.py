from faker import Faker


class CreategroupData:

    createGrp_mandatorydetails = {
        "group_name": "",
        "group_description": "",
        "sub_therapy_area": ""
    }

    createGrp_all_details = {
        "group_name": "",
        "group_description": "",
        "sub_therapy_area": "",
        "email_id": ""
    }

    def generate_group_mandatory_details(createGrp_mandatorydetails):
        fake_data = Faker("en_US")
        createGrp_mandatorydetails["group_name"] = "Group_Name_" + \
            str(fake_data.random_int(10000000, 9999999999999))
        createGrp_mandatorydetails["group_description"] = "Group_Description_"+str(
            fake_data.random_int(10000000, 9999999999999))
        createGrp_mandatorydetails["sub_therapy_area"] = "SRA_"+str(
            fake_data.random_int(100, 999))
        return createGrp_mandatorydetails

    def generate_grp_alldetails(createGrp_all_details):
        fake_data = Faker("en_US")
        createGrp_all_details["group_name"] = "Group_Name_" + \
            str(fake_data.random_int(10000000, 9999999999999))
        createGrp_all_details["group_description"] = "Group_Description_"+str(
            fake_data.random_int(10000000, 9999999999999))
        createGrp_all_details["sub_therapy_area"] = "SRA_"+str(
            fake_data.random_int(100, 999))
        createGrp_all_details["email_id"] = fake_data.email()
        return createGrp_all_details
