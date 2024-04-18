from ...zephyr_session import ZephyrSession


class StatusEndpoints:
    """Api wrapper for "Status" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_statuses(self, **kwargs):
        """Returns all statuses"""
        return self.session.get_paginated("statuses", params=kwargs)

    def get_status(self, status_id):
        """Returns a status for the given ID"""
        return self.session.get(f"statuses/{status_id}")
