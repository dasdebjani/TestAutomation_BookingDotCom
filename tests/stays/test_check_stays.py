from pages.stays.stays_page import StaysPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestBookingDotCom(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.stayPageObject = StaysPage(self.driver)

    @pytest.mark.run(order=1)
    def testDestinationParis(self):
        self.stayPageObject.stays("Saint Ann Parish")