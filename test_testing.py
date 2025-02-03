import pytest

from tests1.Performance import Dashboard


@pytest.mark.usefixtures("setup")
class TestDashboard:

    def test_login_and_navigate_performance(self):
        dashboard = Dashboard(self.driver)
        dashboard.navigate_to_performance_page()
        dashboard.navigate_to_employee_tracker()
        dashboard.select_employee("Peter Mac Anderson")
        dashboard.change_include_option("Past Employees Only")
        dashboard.search_and_reset()  # Optional: reset before adding a log
        dashboard.add_log("Agility", "Positive", "Finish the work")

    def test_add_log_my_tracker(self):
        """Test case for adding a log entry on My Trackers page."""
        dashboard = Dashboard(self.driver)
        dashboard.navigate_to_my_tracker_page()
        dashboard.view_log()
        dashboard.add_log_to_my_tracker("Time Management", "Negative", "Try to improve")
