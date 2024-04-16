

class RefinedSnapshotAnalysis:
    def __init__(self):
        self.workloads_observed = {}
        self.pdbs_observed = {
            "namespaces": {}
        }
        self.total_counters = {
            "nodeSelector": 0,
            "topologySpreadConstraints": 0,
            "affinity": 0,
            "runtimeClassName": 0,
            "no_requests": 0,
            "tolerations": 0,
            "total_pdbs": 0,
            "total_workloads": 0
        }

    def __getitem__(self, key):
        return self.workloads_observed[key]
