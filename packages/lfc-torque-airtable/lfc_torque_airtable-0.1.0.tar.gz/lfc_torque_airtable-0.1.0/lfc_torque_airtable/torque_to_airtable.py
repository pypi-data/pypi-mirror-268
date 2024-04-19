from pyairtable.formulas import match
import requests


class TorqueToAirtable:
    def __init__(self, airtable_api_key, torque):
        from lfc_torque_airtable import AirtableUtils

        self.torque = torque
        self.airtable_utils = AirtableUtils(airtable_api_key)
        self.dry_run = False
        self.errors = []
        self.results = []

    def map_legal_status(self, legal_status):
        return {
            "A private foundation under section 501(c)(3) of the IRC": "A private foundation under section 501(c)(3)",
            "An entity under section 501(c)(3) and 509(a)(1) or (2) of the IRC": "An entity under section 501(c)(3) and 509(a)(1) or (2)",
            "An entity under section 501(c)(3) and 509(a)(1) or (2)": "An entity under section 501(c)(3) and 509(a)(1) or (2)",
            "A public college or university under section 501(c)(3) of the IRC that has received a tax determination letter from the IRS.": None,
            'An entity under section 501(c)(3) and 509(a)(1) or (2) of the Internal Revenue Code ("IRC") that has received a tax determination letter from the Internal Revenue Service ("IRS"), including but not limited to local nonprofit organizations pending federal tax exemption status.': "An entity under section 501(c)(3) and 509(a)(1) or (2)",
            "An entity that is registered and recognized under the law of the applicable jurisdiction as a non-governmental organization, an educational organization, a charitable organization, a social welfare organization, a not-for-profit organization, or similar-type entity that is not a for-profit organization or agency.": None,
            "An entity under section 501(c)(4) of the IRC": None,
            "A fiscally-sponsored nonprofit organization": None,
            "An entity that is recognized under the law of the applicable jurisdiction as a non-governmental organization, etc.": None,
            "Other: An equivalent to 501(c)(3) in Colombia (country)": None,
            "true": None,
            "": None,
        }[legal_status]

    def map_country(self, country):
        return {
            "United States": "United States of America",
            "British Virgin Islands": "Virgin Islands (British)",
            "United Kingdom": "United Kingdom of Great Britain and Northern Ireland",
            "Iran": "Iran (Islamic Republic of)",
            "Democratic Republic of the Congo": "Congo, Democratic Republic of the",
            "Venezuela": "Venezuela (Bolivarian Republic of)",
            "Palestinian Territory": "Palestine",
            "Ivory Coast": "Côte d'Ivoire",
            "Swaziland": "Eswatini",
        }.get(country, country)

    def map_state(self, state):
        return {
            "D.C.": "District of Columbia",
        }.get(state, state)

    def remove_brs(self, text):
        return text.replace("<br/>", "")

    def find_organization(self, torque_proposal):
        org = self.airtable_utils.organization_table.all(
            formula=match({"Account Name": torque_proposal["Organization Name"]})
        )
        if len(org) == 0:
            self.errors.append(
                {
                    "msg": "Couldn't find Organization with name: "
                    + torque_proposal["Organization Name"]
                }
            )
            return None
        else:
            return org[0]["id"]

    def find_contact(self, person):
        if "Email" in person and person["Email"]:
            contact = self.airtable_utils.contact_table.all(
                formula=match({"SF_Email": person["Email"]})
            )
            if len(contact) == 0:
                self.errors.append(
                    {"msg": "Couldn't find Contact with email: " + person["Email"]}
                )
                return None
            else:
                return contact[0]["id"]

    def update_organization(self, org, torque_proposal):
        # This isn't written yet
        pass

    def lookup_global_location(self, location):
        airtable_loc = self.airtable_utils.global_table.all(
            formula=match({"Country Name": self.map_country(location["Country"])})
        )
        if len(airtable_loc) == 0:
            raise Exception("Couldn't find country %s" % location["Country"])

        return airtable_loc[0]["id"]

    def lookup_domestic_location(self, location):
        airtable_loc = self.airtable_utils.domestic_table.all(
            formula=match({"State Name": self.map_state(location["State/Province"])})
        )
        if len(airtable_loc) != 0:
            return airtable_loc[0]["id"]

        airtable_loc = self.airtable_utils.domestic_table.all(
            formula=match({"State Code": self.map_state(location["State/Province"])})
        )
        if len(airtable_loc) != 0:
            return airtable_loc[0]["id"]

        raise Exception("Couldn't find state %s" % location["State/Province"])

    def create_airtable_dict(self, torque_proposal, airtable_proposal_fields={}):
        # Later:
        # UN Sustainable Development Goals (SDGs)
        # Key Partner Organizations (probably not)
        # Funder #1
        # Funder #1: Last Year of Funding
        # Funder #1: Amount of Funding
        # Funder #2
        # Funder #2: Last Year of Funding
        # Funder #2: Amount of Funding
        # Funder #3
        # Funder #3: Last Year of Funding
        # Funder #3: Amount of Funding
        # Sub Regions Covered
        # Regions Covered

        # Items that don't cause other requests to airtable
        potential_dict = {
            "Competition Name - Linked": [
                self.airtable_utils.map_competition_to_airtable(
                    torque_proposal["Competition Name"]
                )
            ],
            "Application #": int(torque_proposal.key),
            "Project Video": torque_proposal["Video"],
            "Executive Summary": self.remove_brs(torque_proposal["Executive Summary"]),
        }

        def in_airtable(key):
            return key in airtable_proposal_fields and airtable_proposal_fields[key]

        if (
            not in_airtable("Primary Subject Area")
            and torque_proposal["Primary Subject Area"]
        ):
            torque_subject_area = (
                torque_proposal["Primary Subject Area"]["Level 4"]
                or torque_proposal["Primary Subject Area"]["Level 3"]
                or torque_proposal["Primary Subject Area"]["Level 2"]
                or torque_proposal["Primary Subject Area"]["Level 1"]
            )
            subject_area = self.airtable_utils.subject_area_table.all(
                formula=match({"Candid Label": torque_subject_area})
            )
            if len(subject_area) == 0:
                self.errors.append(
                    {
                        "attribute": "Primary Subject Area",
                        "msg": "Couldn't find subject area in airtable: "
                        + torque_subject_area,
                    }
                )
            else:
                potential_dict["Primary Subject Area"] = [subject_area[0]["id"]]

        if not in_airtable("Priority Populations"):
            priority_populations = []
            for pop in torque_proposal["Priority Populations"]:
                airtable_pop_by_candid = (
                    self.airtable_utils.priority_populations_table.all(
                        formula=match({"Candid Label": pop})
                    )
                )
                airtable_pop_by_preferred = (
                    self.airtable_utils.priority_populations_table.all(
                        formula=match({"Preferred Label": pop})
                    )
                )
                if len(airtable_pop_by_candid) != 0:
                    priority_populations.append(airtable_pop_by_candid[0]["id"])
                elif len(airtable_pop_by_preferred) != 0:
                    priority_populations.append(airtable_pop_by_preferred[0]["id"])
                else:
                    self.errors.append(
                        {"msg": "Couldn't find population in Airtable: " + pop}
                    )
            potential_dict["Priority Populations"] = list(set(priority_populations))

        if not in_airtable("Global Current Work Locations"):
            current_global_work_locations = []
            current_domestic_work_locations = []
            for torque_location in torque_proposal["Current Work Locations"]:
                if (
                    torque_location["Country"] == "United States"
                    and "State/Province" in torque_location
                    and torque_location["State/Province"]
                ):
                    current_domestic_work_locations.append(
                        self.lookup_domestic_location(torque_location)
                    )
                current_global_work_locations.append(
                    self.lookup_global_location(torque_location)
                )
            potential_dict["Global Current Work Locations"] = list(
                set(current_global_work_locations)
            )
            potential_dict["U.S. Domestic Current Work Locations"] = list(
                set(current_domestic_work_locations)
            )

        if not in_airtable("Global Proposed Work Locations"):
            future_global_work_locations = []
            future_domestic_work_locations = []
            for torque_location in torque_proposal["Future Work Locations"]:
                if (
                    torque_location["Country"] == "United States"
                    and "State/Province" in torque_location
                    and torque_location["State/Province"]
                ):
                    future_domestic_work_locations.append(
                        self.lookup_domestic_location(torque_location)
                    )
                future_global_work_locations.append(
                    self.lookup_global_location(torque_location)
                )

            potential_dict["Global Proposed Work Locations"] = list(
                set(future_global_work_locations)
            )
            potential_dict["U.S. Domestic Proposed Work Locations"] = list(
                set(future_domestic_work_locations)
            )

        if not in_airtable("Lead Organization"):
            organization = self.find_organization(torque_proposal)
            if organization:
                potential_dict["Lead Organization"] = [organization]
            else:
                potential_dict["OTS_Lead Org"] = torque_proposal["Organization Name"]
                potential_dict["OTS_Lead Org Web"] = torque_proposal[
                    "Organization Website"
                ]
                potential_dict["OTS_Lead Org Address"] = torque_proposal[
                    "Organization Location"
                ]["Street Address"]
        else:
            self.update_organization(
                airtable_proposal_fields["Lead Organization"], torque_proposal
            )

        if (
            "Primary Contact" in torque_proposal.keys()
            and torque_proposal["Primary Contact"]
            and not in_airtable("Primary Contact")
        ):
            ots_contact = torque_proposal["Primary Contact"]
            contact = self.find_contact(ots_contact)
            if contact:
                pass
                # potential_dict["Primary Contact"] = [contact]
            else:
                potential_dict["OTS_Primary Contact"] = (
                    ots_contact["First Name"] + " " + ots_contact["Last Name"]
                )
                potential_dict["OTS_Primary Contact Email"] = ots_contact["Email"]

        if "Number of Employees" in torque_proposal.keys():
            potential_dict["Number of Full-Time Employees"] = (
                self.airtable_utils.map_number_full_time_employees_to_airtable(
                    torque_proposal["Number of Employees"]
                )
            )

        if "Annual Operating Budget" in torque_proposal.keys():
            potential_dict["Annual Operating Budget"] = (
                self.airtable_utils.map_operating_budget_to_airtable(
                    torque_proposal["Annual Operating Budget"]
                )
            )

        if "Project Description" in torque_proposal.keys():
            potential_dict["Project Description"] = torque_proposal[
                "Project Description"
            ]

        if "Project Title" in torque_proposal.keys():
            potential_dict["Project Title"] = torque_proposal["Project Title"]

        if "Applicant Tax Identification Number" in torque_proposal.keys():
            potential_dict["Lead Organization EIN"] = torque_proposal[
                "Applicant Tax Identification Number"
            ]

        if "Key Partners" in torque_proposal.keys():
            idx = 1
            for partner in torque_proposal["Key Partners"]:
                potential_dict["Key Partner %s" % idx] = partner["Name"]
                idx += 1

        if (
            "Organization Location" in torque_proposal.keys()
            and torque_proposal["Organization Location"]
            and "Country" in torque_proposal["Organization Location"]
        ):
            potential_dict["Lead Organization HQ City"] = torque_proposal[
                "Organization Location"
            ]["City"]
            potential_dict["Lead Organization HQ Country"] = [
                self.lookup_global_location(torque_proposal["Organization Location"])
            ]
            if "United States" == torque_proposal["Organization Location"]["Country"]:
                potential_dict["Lead Organization HQ State (US Only)"] = [
                    self.lookup_domestic_location(
                        torque_proposal["Organization Location"]
                    )
                ]

        if "Sustainable Development Goals" in torque_proposal.keys():
            potential_dict["UN Sustainable Development Goals (SDGs)"] = [
                self.airtable_utils.map_sdg_to_airtable(sdg)
                for sdg in torque_proposal["Sustainable Development Goals"]
            ]

        dict = {}
        for key in potential_dict.keys():
            if not in_airtable(key):
                dict[key] = potential_dict[key]

        return dict

    def get_information(self, competition, id):
        proposals = self.airtable_utils.proposal_table.all(
            formula=match(
                {
                    "Application #": int(id),
                }
            )
        )
        airtable_proposal = False
        airtable_competition = self.airtable_utils.map_competition_to_airtable(
            competition
        )
        if len(proposals) > 0:
            for proposal in proposals:
                if len(proposal["fields"]["Competition Name - Linked"]) == 0:
                    self.errors.append("Weirdness in finding matching proposals")
                elif len(proposal["fields"]["Competition Name - Linked"]) > 1:
                    self.errors.append(
                        "Lots of weirdness in finding matching proposals"
                    )
                else:
                    if (
                        airtable_competition
                        == proposal["fields"]["Competition Name - Linked"][0]
                    ):
                        if airtable_proposal:
                            raise Exception(
                                "We already found a matching proposal... but here's another one..."
                            )
                        else:
                            airtable_proposal = True

        self.results.append(
            {
                "competition": competition,
                "id": id,
                "title": self.torque.competitions[competition].proposals[id][
                    "GlobalView MediaWiki Title"
                ],
                "airtable": airtable_proposal,
            }
        )

    def convert_proposal(self, competition, id):
        proposals = self.airtable_utils.proposal_table.all(
            formula=match(
                {
                    "Application #": int(id),
                }
            )
        )
        airtable_proposal = None
        airtable_competition = self.airtable_utils.map_competition_to_airtable(
            competition
        )
        if len(proposals) > 0:
            for proposal in proposals:
                if len(proposal["fields"]["Competition Name - Linked"]) == 0:
                    self.errors.append(
                        {"msg": "Weirdness in finding matching proposals"}
                    )
                elif len(proposal["fields"]["Competition Name - Linked"]) > 1:
                    self.errors.append(
                        {"msg": "Lots of weirdness in finding matching proposals"}
                    )
                else:
                    if (
                        airtable_competition
                        == proposal["fields"]["Competition Name - Linked"][0]
                    ):
                        if airtable_proposal:
                            raise Exception(
                                "We already found a matching proposal... but here's another one..."
                            )
                        else:
                            airtable_proposal = proposal

        torque_proposal = self.torque.competitions[competition].proposals[id]
        if airtable_proposal:
            dict_for_update = self.create_airtable_dict(
                torque_proposal, airtable_proposal["fields"]
            )
            if (
                not airtable_proposal["fields"].get("OTS_Torque Flag")
                or airtable_proposal["fields"]["OTS_Torque Flag"]
                == "Exported - Reviewed"
            ):
                dict_for_update["OTS_Torque Flag"] = (
                    "Exported - Unreviewed and Modified"
                )

            if len(dict_for_update) > 0:
                if self.dry_run:
                    self.results.append(
                        {
                            "status": "Updated - Dry Run",
                            "competition": competition,
                            "id": id,
                            "fields_to_update": list(dict_for_update.keys()),
                        }
                    )
                else:
                    self.results.append(
                        {
                            "status": "Updated",
                            "competition": competition,
                            "id": id,
                            "numfields": len(dict_for_update),
                        }
                    )
                    for key, value in dict_for_update.items():
                        try:
                            self.airtable_utils.proposal_table.update(
                                airtable_proposal["id"], {key: value}
                            )
                        except requests.exceptions.HTTPError as err:
                            self.errors.append({"attribute": key, "msg": str(err)})
        else:
            try:
                dict_for_creation = self.create_airtable_dict(torque_proposal)
            except Exception as err:
                self.errors.append({"msg": str(err)})

            if not self.dry_run:
                self.results.append(
                    {
                        "status": "Created",
                        "competition": competition,
                        "id": id,
                    }
                )

                try:
                    airtable_proposal = self.airtable_utils.proposal_table.create(
                        {
                            "Competition Name - Linked": dict_for_creation[
                                "Competition Name - Linked"
                            ],
                            "Application #": dict_for_creation["Application #"],
                            "OTS_Torque Flag": "Exported - Unreviewed and Created",
                        }
                    )
                except requests.exceptions.HTTPError as err:
                    self.errors.append({"msg": str(err)})

                for key, value in dict_for_creation.items():
                    try:
                        self.airtable_utils.proposal_table.update(
                            airtable_proposal["id"], {key: value}
                        )
                    except requests.exceptions.HTTPError as err:
                        self.errors.append({"attribute": key, "msg": str(err)})
