from cubicweb_web.devtools.testlib import WebCWTC


class ConferenceTC(WebCWTC):
    def setup_database(self):
        with self.admin_access.repo_cnx() as cnx:
            self.location = cnx.create_entity(
                "PostalAddress",
                street="1, rue du chat qui pêche",
                postalcode="75005",
                city="Paris",
            ).eid
            cnx.commit()
