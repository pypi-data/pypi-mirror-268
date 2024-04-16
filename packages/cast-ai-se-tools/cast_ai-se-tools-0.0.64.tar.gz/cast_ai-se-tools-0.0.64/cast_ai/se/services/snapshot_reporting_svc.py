import logging
from typing import Dict, Any, List
import pandas as pd
from datetime import datetime

from cast_ai.se.constants import WORKLOAD_TYPES, POD_SPEC_KEYWORDS, K8S_WORKLOAD_TYPES, WORKLOAD_MAP, CSV_REPORT_HEADERS
from cast_ai.se.models.misc_data_models import ReportDetailLevel
from cast_ai.se.models.refined_snapshot import RefinedSnapshot
from cast_ai.se.models.refined_snapshot_analysis import RefinedSnapshotAnalysis


class SnapshotReporter:
    def __init__(self, rs_metadata: RefinedSnapshotAnalysis, refined_snapshot: RefinedSnapshot):
        self._logger = logging.getLogger(__name__)
        self._rs_metadata = rs_metadata
        self._refined_snapshot = refined_snapshot

    def generate_refined_snapshot_csv_report(self, cluster_id: str) -> None:
        timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        report_filename = f"{cluster_id}.{timestamp}.csv"
        df = pd.DataFrame(columns=CSV_REPORT_HEADERS)
        for workload_type in K8S_WORKLOAD_TYPES:
            workloads = getattr(self._refined_snapshot.workloads, WORKLOAD_MAP[workload_type])
            if len(workloads):
                for workload in workloads:
                    workload_row = [WORKLOAD_MAP[workload_type], workload["name"], workload["namespace"], "", "", "",
                                    "", "", ""]
                    for refined_reason in POD_SPEC_KEYWORDS:
                        if refined_reason in workload["refined_reason"]:
                            # if refined_reason == "affinity":
                            #     print("")
                            report = ""
                            if isinstance(workload[refined_reason], Dict):
                                report = self._add_dictspec_to_report(workload[refined_reason], report, 1)
                            elif isinstance(workload[refined_reason], List):
                                report = self._add_listspec_to_report(workload[refined_reason], report, 1)
                            report = report.replace("│ \t", "  ")
                            report = report.replace("│   ", "")
                            workload_row[POD_SPEC_KEYWORDS.index(refined_reason) + 3] = report
                    if "no_requests" in workload["refined_reason"]:
                        workload_row[8] = "No Requests set."
                    data_dict = pd.Series(workload_row, index=df.columns).to_dict()
                    workload_df = pd.DataFrame([data_dict])
                    df = pd.concat([df, workload_df], ignore_index=True)
        df = df.loc[:, df.ne('').any(axis=0)]
        df.to_csv(report_filename, index=False)

    def generate_refined_snapshot_report(self, detail_lvl: ReportDetailLevel = ReportDetailLevel.BASIC) -> str:
        report = "┌" + "─" * 52 + f"< {detail_lvl.value} Report >" + "─" * (57 - len(str(detail_lvl.value))) + "┐\n"
        if self._refined_snapshot.karpenter_flag:
            report += "│ Karpenter Present !\n"
        if self._refined_snapshot.windows_flag:
            report += "│ Windows nodes Present !\n"
        report += (f"│ {self._rs_metadata.total_counters['total_workloads']} "
                   f"Workloads with scheduling-challenging settings:\n")
        report = self._add_refinement_metrics_to_report(report)
        report = self._add_workloads_to_report(detail_lvl, report)
        report += "├" + "─" * 120 + "┤\n"
        report += f"│ {self._rs_metadata.total_counters['total_pdbs']} PDBs\n"
        if detail_lvl != ReportDetailLevel.BASIC:
            report = self._add_pdbs_to_report(detail_lvl, report)
        report += "└" + "─" * 120 + "┘\n"
        return report

    def _add_refinement_metrics_to_report(self, report: str) -> str:
        if self._rs_metadata.total_counters["total_workloads"]:
            report += "├" + "─" * 120 + "┤\n"
            report += "│ Refinements reasons metrics:\n"
            for reason in POD_SPEC_KEYWORDS + ["no_requests"]:
                if self._rs_metadata.total_counters[reason]:
                    report += f"│   - {self._rs_metadata.total_counters[reason]} workloads with {reason}\n"
            report += "├" + "─" * 120 + "┤\n"
        return report

    def _add_workloads_to_report(self, detail_lvl: ReportDetailLevel, report: str):
        for workload_type in WORKLOAD_TYPES:
            workloads = self._refined_snapshot.workloads.get_workload_type(workload_type)
            if len(workloads):
                report += f"│   - {len(workloads)} {workload_type}\n"
                if detail_lvl.value != "BASIC":
                    report = self._add_workloads_to_non_basic_report(detail_lvl, report, workload_type)
        return report

    def _add_workloads_to_non_basic_report(self, detail_lvl, report, workload_type):
        for namespace in self._rs_metadata.workloads_observed[workload_type].keys():
            report += f"│ \t\t [{namespace}]\n"
            for workload_name, workload_index in self._rs_metadata.workloads_observed[workload_type][namespace].items():
                report += f"│ \t\t\t- {workload_name}\n"
                if detail_lvl.value != "DETAILED":
                    report = self._add_extra_detailed_workloads_to_report(workload_index, workload_type, report)
        return report

    def _add_pdbs_to_report(self, detail_lvl: ReportDetailLevel, report: str) -> str:
        for namespace in self._rs_metadata.pdbs_observed["namespaces"].keys():
            report += f"│ \t [{namespace}]\n"
            for pdb_name, pdb_index in self._rs_metadata.pdbs_observed["namespaces"][namespace].items():
                report += f"│ \t\t- {pdb_name}\n"
                if detail_lvl == ReportDetailLevel.EXTRA:
                    report = self._add_extra_detailed_pdb_to_report(pdb_index, report)
        return report

    def _add_extra_detailed_pdb_to_report(self, pdb_index: int, report: str) -> str:
        refined_pdb = self._refined_snapshot.pdbs[pdb_index]
        report = self._add_dictspec_to_report(refined_pdb["spec"], report, 3)
        return report

    def _add_extra_detailed_workloads_to_report(self, workload_index: int, workload_type: str, report: str) -> str:
        refined_workload = vars(self._refined_snapshot.workloads)[workload_type][workload_index]
        for refined_reason in refined_workload["refined_reason"]:
            if refined_reason == "no_requests":
                report += "│ \t\t\t\t* No Requests!\n"
            elif refined_workload[refined_reason]:
                report += f"│ \t\t\t\t* {refined_reason}:\n"
                if isinstance(refined_workload[refined_reason], Dict):
                    report = self._add_dictspec_to_report(refined_workload[refined_reason], report, 5, "\t")
                elif isinstance(refined_workload[refined_reason], List):
                    report = self._add_listspec_to_report(refined_workload[refined_reason], report, 5)
                else:
                    self._logger.critical("Unexpected object type: {refined_workload[refined_reason]}")
            else:
                self._logger.warning(f"Empty definitions of {refined_reason} for "
                                     f"{refined_workload['namespace']}/{refined_workload['name']}")
        return report

    def _add_listspec_to_report(self, spec: List[Any], report: str, depth: int = 0) -> str:
        for key in spec:
            pre_hyphen = "  - " if len(spec) > 1 else "\t"
            if isinstance(key, dict):
                report = self._add_dictspec_to_report(key, report, depth, pre_hyphen)
            else:
                report += "│ " + "\t" * depth + f"{pre_hyphen}{str(key)}\n"
        return report

    def _add_dictspec_to_report(self, spec: Dict[str, Any], report: str, depth: int = 0, pre_hyphen: str = "\t") -> str:
        for index, (key, value) in enumerate(spec.items()):
            if index and pre_hyphen == "  - ":
                pre_hyphen = "\t"
            if not isinstance(value, dict) and not isinstance(value, list):
                report += "│ " + "\t" * (depth - 1) + f"{pre_hyphen}{str(key)}: {str(value)}\n"
            elif isinstance(value, list):
                report = self._add_listspec_to_report(value, report, depth)
            elif isinstance(value, dict):
                report += "│ " + "\t" * (depth - 1) + f"{pre_hyphen}{str(key)}:\n"
                if key == "matchLabels" and len(value.items()) > 1:
                    report = self._add_dictspec_to_report(value, report, depth + 1, pre_hyphen="  - ")
                else:
                    report = self._add_dictspec_to_report(value, report, depth + 1)
        return report
