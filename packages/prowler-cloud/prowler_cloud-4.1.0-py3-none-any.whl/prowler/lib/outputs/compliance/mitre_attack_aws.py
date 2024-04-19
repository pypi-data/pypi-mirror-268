from csv import DictWriter

from colorama import Fore, Style
from tabulate import tabulate

from prowler.config.config import orange_color, timestamp
from prowler.lib.outputs.compliance.models import Check_Output_MITRE_ATTACK
from prowler.lib.outputs.csv.csv import generate_csv_fields
from prowler.lib.outputs.utils import unroll_list
from prowler.lib.utils.utils import outputs_unix_timestamp


def write_compliance_row_mitre_attack_aws(
    file_descriptors, finding, compliance, output_options, provider
):
    compliance_output = compliance.Framework
    if compliance.Version != "":
        compliance_output += "_" + compliance.Version
    if compliance.Provider != "":
        compliance_output += "_" + compliance.Provider

    compliance_output = compliance_output.lower().replace("-", "_")
    csv_header = generate_csv_fields(Check_Output_MITRE_ATTACK)
    csv_writer = DictWriter(
        file_descriptors[compliance_output],
        fieldnames=csv_header,
        delimiter=";",
    )
    for requirement in compliance.Requirements:
        requirement_description = requirement.Description
        requirement_id = requirement.Id
        requirement_name = requirement.Name
        attributes_aws_services = ", ".join(
            attribute.AWSService for attribute in requirement.Attributes
        )
        attributes_categories = ", ".join(
            attribute.Category for attribute in requirement.Attributes
        )
        attributes_values = ", ".join(
            attribute.Value for attribute in requirement.Attributes
        )
        attributes_comments = ", ".join(
            attribute.Comment for attribute in requirement.Attributes
        )
        compliance_row = Check_Output_MITRE_ATTACK(
            Provider=finding.check_metadata.Provider,
            Description=compliance.Description,
            AccountId=provider.identity.account,
            Region=finding.region,
            AssessmentDate=outputs_unix_timestamp(
                output_options.unix_timestamp, timestamp
            ),
            Requirements_Id=requirement_id,
            Requirements_Description=requirement_description,
            Requirements_Name=requirement_name,
            Requirements_Tactics=unroll_list(requirement.Tactics),
            Requirements_SubTechniques=unroll_list(requirement.SubTechniques),
            Requirements_Platforms=unroll_list(requirement.Platforms),
            Requirements_TechniqueURL=requirement.TechniqueURL,
            Requirements_Attributes_AWSServices=attributes_aws_services,
            Requirements_Attributes_Categories=attributes_categories,
            Requirements_Attributes_Values=attributes_values,
            Requirements_Attributes_Comments=attributes_comments,
            Status=finding.status,
            StatusExtended=finding.status_extended,
            ResourceId=finding.resource_id,
            CheckId=finding.check_metadata.CheckID,
            Muted=finding.muted,
        )

        csv_writer.writerow(compliance_row.__dict__)


def get_mitre_attack_table(
    findings: list,
    bulk_checks_metadata: dict,
    compliance_framework: str,
    output_filename: str,
    output_directory: str,
    compliance_overview: bool,
):
    tactics = {}
    mitre_compliance_table = {
        "Provider": [],
        "Tactic": [],
        "Status": [],
        "Muted": [],
    }
    pass_count = []
    fail_count = []
    muted_count = []
    for index, finding in enumerate(findings):
        check = bulk_checks_metadata[finding.check_metadata.CheckID]
        check_compliances = check.Compliance
        for compliance in check_compliances:
            if (
                "MITRE-ATTACK" in compliance.Framework
                and compliance.Version in compliance_framework
            ):
                for requirement in compliance.Requirements:
                    for tactic in requirement.Tactics:
                        if tactic not in tactics:
                            tactics[tactic] = {"FAIL": 0, "PASS": 0, "Muted": 0}
                        if finding.muted:
                            if index not in muted_count:
                                muted_count.append(index)
                                tactics[tactic]["Muted"] += 1
                        else:
                            if finding.status == "FAIL":
                                if index not in fail_count:
                                    fail_count.append(index)
                                    tactics[tactic]["FAIL"] += 1
                            elif finding.status == "PASS":
                                if index not in pass_count:
                                    pass_count.append(index)
                                    tactics[tactic]["PASS"] += 1
    # Add results to table
    tactics = dict(sorted(tactics.items()))
    for tactic in tactics:
        mitre_compliance_table["Provider"].append(compliance.Provider)
        mitre_compliance_table["Tactic"].append(tactic)
        if tactics[tactic]["FAIL"] > 0:
            mitre_compliance_table["Status"].append(
                f"{Fore.RED}FAIL({tactics[tactic]['FAIL']}){Style.RESET_ALL}"
            )
        else:
            mitre_compliance_table["Status"].append(
                f"{Fore.GREEN}PASS({tactics[tactic]['PASS']}){Style.RESET_ALL}"
            )
        if tactics[tactic]["Muted"] > 0:
            mitre_compliance_table["Muted"].append(
                f"{orange_color}{tactics[tactic]['Muted']}{Style.RESET_ALL}"
            )
    if (
        len(fail_count) + len(pass_count) + len(muted_count) > 1
    ):  # If there are no resources, don't print the compliance table
        print(
            f"\nCompliance Status of {Fore.YELLOW}{compliance_framework.upper()}{Style.RESET_ALL} Framework:"
        )
        overview_table = [
            [
                f"{Fore.RED}{round(len(fail_count) / len(findings) * 100, 2)}% ({len(fail_count)}) FAIL{Style.RESET_ALL}",
                f"{Fore.GREEN}{round(len(pass_count) / len(findings) * 100, 2)}% ({len(pass_count)}) PASS{Style.RESET_ALL}",
                f"{orange_color}{round(len(muted_count) / len(findings) * 100, 2)}% ({len(muted_count)}) MUTED{Style.RESET_ALL}",
            ]
        ]
        print(tabulate(overview_table, tablefmt="rounded_grid"))
        if not compliance_overview:
            print(
                f"\nFramework {Fore.YELLOW}{compliance_framework.upper()}{Style.RESET_ALL} Results:"
            )
            print(
                tabulate(
                    mitre_compliance_table,
                    headers="keys",
                    tablefmt="rounded_grid",
                )
            )
            print(
                f"{Style.BRIGHT}* Only sections containing results appear.{Style.RESET_ALL}"
            )
            print(f"\nDetailed results of {compliance_framework.upper()} are in:")
            print(
                f" - CSV: {output_directory}/compliance/{output_filename}_{compliance_framework}.csv\n"
            )
