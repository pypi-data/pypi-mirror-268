from datetime import date

from logilab.common.testlib import unittest_main

from test.utils import ConferenceTC


class ConferenceHooksTC(ConferenceTC):
    def test_url_identifier(self):
        with self.admin_access.repo_cnx() as cnx:
            conf1 = cnx.create_entity(
                "Conference",
                title="conference test",
                url_id="conf",
                start_on=date(2010, 3, 1),
                end_on=date(2010, 3, 5),
                take_place_at=self.location,
                description="short description",
            )
            cnx.commit()
            self.assertEqual(conf1.url_id, "conf")
            conf2 = cnx.create_entity(
                "Conference",
                title="conference test2",
                start_on=date(2010, 3, 1),
                end_on=date(2010, 3, 5),
                take_place_at=self.location,
                description="short description",
            )
            cnx.commit()
            self.assertEqual(conf2.url_id, "conference_test2")

    def test_url_identifier_with_several_conferences(self):
        with self.admin_access.repo_cnx() as cnx:
            conf1 = cnx.create_entity(
                "Conference",
                title="conFerence test",
                start_on=date(2010, 3, 1),
                end_on=date(2010, 3, 5),
                take_place_at=self.location,
                description="short description",
            )
            conf2 = cnx.create_entity(
                "Conference",
                title="conference test2",
                start_on=date(2010, 3, 1),
                end_on=date(2010, 3, 5),
                take_place_at=self.location,
                description="short description",
            )
            cnx.commit()
            self.assertEqual(conf1.url_id, "conference_test")
            self.assertEqual(conf2.url_id, "conference_test2")

    def test_url_identifier_with_same_url_id(self):
        with self.admin_access.repo_cnx() as cnx:
            conf1 = cnx.create_entity(
                "Conference",
                title="conFerence test",
                start_on=date(2010, 3, 1),
                end_on=date(2010, 3, 5),
                take_place_at=self.location,
                description="short description",
            )
            conf2 = cnx.create_entity(
                "Conference",
                title="conference test",
                start_on=date(2010, 3, 1),
                end_on=date(2010, 3, 5),
                take_place_at=self.location,
                description="short description",
            )
            cnx.commit()
            self.assertEqual(conf1.url_id, "conference_test")
            self.assertEqual(conf2.url_id, "conference_test_1")


if __name__ == "__main__":
    unittest_main()
