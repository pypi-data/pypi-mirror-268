from typing import Dict, Any, List
import logging


class RefinedSnapshot:
    def __init__(self):
        self.pdbs = []
        self.workloads = WorkloadObject()
        self.karpenter_flag = False
        self.windows_flag = False


class WorkloadObject:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self.deployments = []
        self.replica_sets = []
        self.daemon_sets = []
        self.stateful_sets = []
        self.jobs = []

    def get_workload_type(self, workload_type: str) -> List[Any]:
        try:
            return vars(self)[workload_type]
        except Exception as e:
            self._logger.error(f"Error returning internal sub-object of WorkloadObject workload_type={workload_type}")
            return []

    def add_item(self, item_type: str, item_data: Dict[str, Any]) -> None:
        match item_type:
            case 'deployments':
                item_data["index"] = len(self.deployments)
                self.deployments.append(item_data)
            case 'replica_sets':
                item_data["index"] = len(self.replica_sets)
                self.replica_sets.append(item_data)
            case 'daemon_sets':
                item_data["index"] = len(self.daemon_sets)
                self.daemon_sets.append(item_data)
            case 'stateful_sets':
                item_data["index"] = len(self.stateful_sets)
                self.stateful_sets.append(item_data)
            case 'jobs':
                item_data["index"] = len(self.jobs)
                self.jobs.append(item_data)
            case _:
                raise ValueError(f"Invalid item type: {item_type}")
