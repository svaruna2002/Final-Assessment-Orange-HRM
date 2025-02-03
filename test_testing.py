import pytest

from Manager_review import Manager
from My_review import My
from employee_review import Employee
from kpi import Kpi
from trackers import Trackers


@pytest.mark.usefixtures("setup")
class TestKpi:
    def test_performance_kpi(self):
        obj = Kpi(self.driver)
        obj.performance_kpi()
        obj.key_performance()
        obj.checkbox_performance()
        obj.delete_performance()
        obj.edit_perfformance("1234567","55")
        obj.add_performance("Customer")

    def test_performance_trackers(self):
        obj1 = Trackers(self.driver)
        obj1.performance_tracker()
        obj1.tracker_search("pet")
        obj1.delete_tracker()
        obj1.edit_tracker("Service","pet","jam")
        obj1.add_tracker("Service","tho","tim")

    def test_performance_manager(self):
        obj2 = Manager(self.driver)
        obj2.performance_manager("pet", "pet")

    def test_performance_myreview(self):
        obj3 = My(self.driver)
        obj3.performance_myreview()
        obj3.performance_comments("10","Poor","20","Not bad","30","Good","40","Cool","50","Very bad")

    def test_performance_employee(self):
        obj4 = Employee(self.driver)
        obj4.performance_employee()
        obj4.performance_empl("pet")




