import logging
from typing import Dict, Any

from cast_ai.se.models.misc_data_models import ReportDetailLevel
from cast_ai.se.services.snapshot_refinery_svc import SnapshotRefinery


class SnapshotAnalyzer:
    def __init__(self, raw_snapshot: Dict[str, Any], auto_refine: bool = True):
        self._logger = logging.getLogger(__name__)
        self._raw_snapshot = raw_snapshot
        self._refinery = SnapshotRefinery()
        if auto_refine:
            self.refine_snapshot()

    def refine_snapshot(self):
        self._refinery.refine_snapshot(self._raw_snapshot)

    def get_refined_snapshot_report(self, detail_lvl: ReportDetailLevel = ReportDetailLevel.BASIC):
        return self._refinery.reporter.generate_refined_snapshot_report(detail_lvl)

    def get_refined_snapshot_csv_report(self):
        self._refinery.reporter.generate_refined_snapshot_csv_report(cluster_id=self._raw_snapshot["clusterId"])
