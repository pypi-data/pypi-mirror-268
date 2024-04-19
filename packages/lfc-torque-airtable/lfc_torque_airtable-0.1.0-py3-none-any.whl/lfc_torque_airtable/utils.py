from pyairtable import Table
from pyairtable.formulas import match


class AirtableUtils:
    competition_mapping = [
        ("100&Change 2021", "100Change2020"),
        ("Larsen Lam ICONIQ Impact Award", "LLIIA2020"),
        ("Lone Star Prize", "LoneStar2020"),
        ("Economic Opportunity Challenge", "EO2020"),
        ("100&Change 2017", "100Change2017"),
        ("2030 Climate Challenge", "Climate2030"),
        ("Equality Can't Wait Challenge", "ECW2020"),
        ("Racial Equity 2030", "RacialEquity2030"),
        ("Stronger Democracy Award", "Democracy22"),
        ("Chicago Prize", "ChicagoPrize"),
        ("LEGO Build a World of Play Challenge", "BaWoP22"),
        ("Maternal and Infant Health Award", "MIHA"),
        ("Yield Giving Open Call", "YGOC23"),
    ]

    sdg_mapping = [
        ("SDG 1 - No Poverty", "1"),
        ("SDG 2 - Zero Hunger", "2"),
        ("SDG 3 - Good Health & Well-Being", "3"),
        ("SDG 4 - Quality Education", "4"),
        ("SDG 5 - Gender Equality", "5"),
        ("SDG 6 - Clean Water & Sanitation", "6"),
        ("SDG 7 - Affordable & Clean Energy", "7"),
        ("SDG 8 - Decent Work & Economic Growth", "8"),
        ("SDG 9 - Industry, Innovation, & Infrastructure", "9"),
        ("SDG 10 - Reduced Inequalities", "10"),
        ("10: Reduced Inequality", "10"),
        ("SDG 11 - Sustainable Cities & Communities", "11"),
        ("SDG 12 - Responsible Consumption & Production", "12"),
        ("SDG 13 - Climate Action", "13"),
        ("SDG 14 - Life Below Water", "14"),
        ("SDG 15 - Life on Land", "15"),
        ("SDG 16 - Peace, Justice, & Strong Institutions", "16"),
        ("SDG 17 - Partnerships for the Goals", "17"),
    ]

    official_sdgs = [
        "No Poverty",
        "Zero Hunger",
        "Good Health and Well-Being",
        "Quality Education",
        "Gender Equality",
        "Clean Water and Sanitation",
        "Affordable and Clean Energy",
        "Decent Work and Economic Growth",
        "Industry, Innovation and Infrastructure",
        "Reduced Inequality",
        "Sustainable Cities and Communities",
        "Responsible Consumption and Production",
        "Climate Action",
        "Life Below Water",
        "Life on Land",
        "Peace, Justice and Strong Institutions",
        "Partnership for the Goals",
    ]

    operating_budget_mapping = [
        ("Less than $1 Million", "Less than $1 Million"),
        # ("$1.0 to 5 Million", "$1 to $5 Million"),
        ("$1.1 to 5 Million", "$1 to $5 Million"),
        ("$5.1 to 10 Million", "$5 to $10 Million"),
        ("$10.1 to 25 Million", "$10 to $25 Million"),
        ("$25.1 to 50 Million", "$25 to $50 Million"),
        ("$50.1 to 100 Million", "$50 to $100 Million"),
        ("$100.1 to 500 Million", "$100 to $500 Million"),
        ("$100.1 to 250 Million", "$100 to $250 Million"),
        ("$200.1 to 500 Million", "$200 to 500 Million"),
        ("$250.1 Million to $500 Million", "$250 to $500 Million"),
        ("$500.1 Million to $750 Million", "$500 to $750 Million"),
        ("$500.1 Million to $1 Billion", "$500 Million to $1 Billion"),
        ("$750.1 Million to $1 Billion", "$750 Million to $1 Billion"),
        ("$750.1 Million to $ 1 Billion", "$750 Million to $1 Billion"),
        ("$1 Billion +", "$1 Billion +"),
        ("$5.1 to 10 Million", "&lt;$10 Million"),
        ("$5.1 to 10 Million", "<$10 Million"),
        ("$25.1 to 50 Million", "$10 to 50 Million"),
        ("$100.1 to 250 Million", "$100 to 200 Million"),
        ("$1.1 to 5 Million", "$1.0 to 5.0 Million"),
        ("$5.1 to 10 Million", "Greater than $5.0 Million"),
    ]

    number_full_time_employees_mapping = [
        ("Fewer than 10 Full-time Employees", "Up to 10 Full-time Employees"),
        ("10 to 25 Full-time Employees", "10 to 25 Full-time Employees"),
        ("26 to 50 Full-time Employees", "26 to 50 Full-time Employees"),
        ("51 to 100 Full-time Employees", "51 to 100 Full-time Employees"),
        ("101 to 300 Full-time Employees", "101 to 300 Full-time Employees"),
        ("301 to 500 Full-time Employees", "301 to 500 Full-time Employees"),
        ("501 to 1,000 Full-time Employees", "501 to 1,000 Full-time Employees"),
        ("1,000+ Full-time Employees", "1,000+ Full-time Employees"),
        ("26 to 50 Full-time Employees", "<50 Full-time Employees"),
        ("51 to 100 Full-time Employees", ">50 to 100 Full-time Employees"),
        ("301 to 500 Full-time Employees", "&gt;300 to 500 Full-time Employees"),
        # From EO 2020
        ("Fewer than 10 Full-time Employees", "Up to 10 Full-time Employees"),
        ("10 to 25 Full-time Employees", "&gt;10 to 25 Full-time Employees"),
        ("26 to 50 Full-time Employees", "&gt;25 to 50 Full-time Employees"),
        ("26 to 50 Full-time Employees", "<50 Full-time Employees"),
        ("51 to 100 Full-time Employees", "&gt;50 to 100 Full-time Employees"),
        ("51 to 100 Full-time Employees", ">50 to 100 Full-time Employees"),
        ("101 to 300 Full-time Employees", "&gt;100 to 300 Full-time Employees"),
        ("301 to 500 Full-time Employees", "&gt;300 to 500 Full-time Employees"),
        ("301 to 500 Full-time Employees", ">300 to 500 Full-time Employees"),
        # Other
        ("51 to 100 Full-time Employees", "50 to 100 Full-time Employees"),
        ("Fewer than 10 Full-time Employees", "Fewer than 10 Full-time Employees"),
    ]

    def __init__(self, airtable_api_key):
        airtable_base_id = "appWnH0EdGdSAPuKt"
        self.proposal_table = Table(
            airtable_api_key, airtable_base_id, "tblaI0NbCBgaT2Pm6"
        )
        self.subject_area_table = Table(
            airtable_api_key, airtable_base_id, "tblQ0AbIJg58hObxQ"
        )
        self.priority_populations_table = Table(
            airtable_api_key, airtable_base_id, "tblg2hjhcLsrGKorU"
        )
        self.organization_table = Table(
            airtable_api_key, airtable_base_id, "tblRZxhvfDMPTVvrF"
        )
        self.contact_table = Table(
            airtable_api_key, airtable_base_id, "tbljK83b3Vsa5DBak"
        )
        self.competitions_table = Table(
            airtable_api_key, airtable_base_id, "tbljbQhKWgAgSJsA9"
        )
        self.domestic_table = Table(
            airtable_api_key, airtable_base_id, "tblZmgx5okHqRJyc7"
        )
        self.global_table = Table(
            airtable_api_key, airtable_base_id, "tblWtdnKs3jeBv4Si"
        )
        self.subregion_table = Table(
            airtable_api_key, airtable_base_id, "tblskz8JxmfrYG2vU"
        )

    def map_to_airtable(self, tuples, val):
        if not val:
            return None

        for airtable, torque in tuples:
            if val == torque:
                return airtable

        return val

    def map_to_torque(self, tuples, val):
        for airtable, torque in tuples:
            if val == airtable:
                return torque

        raise Exception("Could not find airtable mapping for " + str(val))

    def map_competition_to_airtable(self, comp):
        competition = self.competitions_table.all(
            formula=match(
                {
                    "Official Competition Name": self.map_to_airtable(
                        self.competition_mapping, comp
                    )
                }
            )
        )
        if len(competition) == 0:
            raise Exception("Couldn't find country %s" % location["Country"])

        return competition[0]["id"]

    def map_competition_to_torque(self, comp):
        competition = self.competitions_table.get(comp)
        return self.map_to_torque(
            self.competition_mapping, competition["fields"]["Official Competition Name"]
        )

    def map_sdg_to_airtable(self, sdg):
        return self.map_to_airtable(self.sdg_mapping, str(sdg["number"]))

    def map_sdg_to_torque(self, sdg):
        num = int(self.map_to_torque(self.sdg_mapping, sdg))
        return {
            "number": num,
            "title": official_sdgs[num - 1],
        }

    def map_operating_budget_to_airtable(self, operation_budget):
        return self.map_to_airtable(self.operating_budget_mapping, operation_budget)

    def map_operating_budget_to_torque(self, operation_budget):
        return self.map_to_torque(self.operating_budget_mapping, operation_budget)

    def map_number_full_time_employees_to_airtable(self, number_full_time_employees):
        return self.map_to_airtable(
            self.number_full_time_employees_mapping, number_full_time_employees
        )

    def map_number_full_time_employees_to_torque(number_full_time_employees):
        return self.map_to_torque(
            self.number_full_time_employees_mapping, number_full_time_employees
        )
