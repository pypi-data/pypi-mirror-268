from cubicweb import _
from logilab.mtconverter import xml_escape
from cubicweb_web.views import boxes
from cubicweb_web.component import EntityCtxComponent, EmptyComponent
from cubicweb_web.htmlwidgets import BoxLink, BoxWidget
from cubicweb.predicates import is_instance, authenticated_user


# XXX move to cmt
class TalkStatusBox(boxes.BoxTemplate):
    __regid__ = "talk-status"
    __select__ = boxes.BoxTemplate.__select__ & authenticated_user()
    context = "left"
    title = _("your talks")
    order = 2

    def call(self, **kwargs):
        _cw = self._cw
        rset = _cw.execute(
            "Any T WHERE T is Talk, U leads T, U eid %(x)s, "
            'T in_conf C, C in_state S, S name "scheduled"',
            {"x": _cw.user.eid},
        )
        if not rset:
            return
        talks = {}
        for talk in rset.entities():
            talks.setdefault(talk.cw_adapt_to("IWorkflowable").state, []).append(talk)
        box = BoxWidget(_cw._(self.title), id=self.__regid__, islist=True)
        rql_ = (
            "Any T,C WHERE T is Talk, T in_conf C, U leads T, U eid %s, "
            'T in_state S, S name "%%s", C in_state CS, CS name "scheduled"'
            % _cw.user.eid
        )
        for state in "draft submitted inreview correction accepted rejected".split():
            msg = _cw._("Your talks in state %s") % _cw._(state)
            if state in talks:
                box.append(
                    BoxLink(
                        _cw.build_url("view", rql=rql_ % state, vtitle=msg),
                        xml_escape(f"{len(talks[state])} {state}"),
                    )
                )
        box.render(w=self.w)


# XXX move to cmt
class ReviewStatusBox(boxes.BoxTemplate):
    __regid__ = "review-status"
    __select__ = boxes.BoxTemplate.__select__ & authenticated_user()

    context = "left"
    title = _("your reviews")
    order = 3

    def call(self, **kwargs):
        _cw = self._cw
        rset = self._cw.execute(
            "Any T WHERE T is Talk, U reviews T, U eid %(x)s", {"x": _cw.user.eid}
        )
        if not rset:
            return
        talks = {}
        for talk in rset.entities():
            talks.setdefault(talk.cw_adapt_to("IWorkflowable").state, []).append(talk)
        box = BoxWidget(_cw._(self.title), id=self.__regid__, islist=True)
        rql_ = (
            "Any T,C WHERE T is Talk, T in_conf C, U reviews T, U eid %s, "
            'T in_state S, S name "%%s"' % _cw.user.eid
        )
        for state in ["inreview", "correction", "accept_pending", "reject_pending"]:
            msg = _cw._("Talks you have to review (in state %s)") % self._cw._(state)
            if state in talks:
                box.append(
                    BoxLink(
                        _cw.build_url("view", rql=rql_ % state, vtitle=msg),
                        xml_escape(f"{len(talks[state])} {state}"),
                    )
                )
        if box.items:
            box.render(w=self.w)


# XXX move to cmt
class CallForPaperBox(boxes.BoxTemplate):
    __regid__ = "callbox"

    context = "left"
    title = _("Call for paper")
    order = 1

    def call(self, **kwargs):
        _cw = self._cw
        rset = _cw.execute("Any C WHERE C is Conference, C call_open True")
        if not rset:
            return
        w = self.w
        w('<div class="conferenceBox">')
        w('<div id="confCallForPaper">')
        if _cw.session.anonymous_session:
            msg = _cw._(
                "You need to create an account and sign in "
                "before you can submit an abstract"
            )
            url = xml_escape(
                _cw.build_url(
                    "view",
                    vid="login_or_register",
                    __message=msg,
                    __redirectpath="add/Talk",
                )
            )
        elif _cw.user.leads:
            msg = _cw._("Remember you have already submitted a talk.")
            url = xml_escape(_cw.build_url("add/Talk", __message=msg))
        else:
            url = xml_escape(_cw.build_url("add/Talk"))
        w(f"<a href=\"{url}\">{xml_escape(_cw._('Answer the call for talks !'))}</a>")
        w("</div></div>")


class SponsorBox(EntityCtxComponent):
    __regid__ = domid = "sponsorbox"
    __select__ = EntityCtxComponent.__select__ & is_instance("Conference", "Talk")
    context = "right"
    title = "Sponsors"

    def init_rendering(self):
        if self.entity.e_schema.type == "Conference":
            rql = (
                "Any L, X, I WHERE I is File, X has_logo I, X is_sponsor S, S level L, "
                "S sponsoring_conf C, C eid %(conf)s"
            )
            self.cw_rset = self._cw.execute(rql, {"conf": self.entity.eid})
        elif self.entity.e_schema.type == "Talk":
            rql = (
                "Any L, X, I WHERE I is File, X has_logo I, X is_sponsor S, S level L, "
                "S sponsoring_conf C, T in_conf C, T eid %(talk)s"
            )
            self.cw_rset = self._cw.execute(rql, {"talk": self.entity.eid})

    def render_body(self, w):
        # we can't use EmptyComponent in init_rendering cos we want to display
        # an informational message at the end
        _cw = self._cw
        sponsors = [(level, seid, imgeid) for (level, seid, imgeid) in self.cw_rset]
        if sponsors:
            # sort sponsor by level
            lhash = {"Gold": 3, "Silver": 2, "Bronze": 1, "Media": 1}
            sponsors.sort(key=lambda x: lhash[x[0]])
            sponsors.reverse()
            _level = None
            for level, sponsor_eid, image_eid in sponsors:
                if level != _level:
                    w(f"<div>{level}</div>")
                    _level = level
                sponsor = _cw.entity_from_eid(sponsor_eid)
                img = _cw.entity_from_eid(image_eid)
                url = img.cw_adapt_to("IDownloadable").download_url()
                # adapt image size
                w(f'<div class="{level}">')
                w(
                    '<a href="%s"><img src="%s" alt="%s"/></a>'
                    % (sponsor.url, url, xml_escape(img.dc_title()))
                )
                w("</div>")
        w(
            '<p>%s <a href="mailto:%s">%s</a></p>'
            % (
                _cw._("If you are interested in sponsoring or partnering"),
                _cw.property_value("ui.sponsor-contact-email"),
                _cw._("please contact us"),
            )
        )


class AtTheSameTimeBox(EntityCtxComponent):
    __regid__ = "atthesametimebox"
    __select__ = EntityCtxComponent.__select__ & is_instance("Talk")
    context = "incontext"
    title = _("At the same time")

    def init_rendering(self):
        self.at_the_same_time = []
        rql = (
            "Any T WHERE T is Talk, NOT T eid %(eid)s, NOT T start_time NULL "
            "AND NOT T end_time NULL"
        )
        rset = self._cw.execute(rql, {"eid": self.entity.eid})
        start, end = self.entity.start_time, self.entity.end_time
        if rset and start is not None and end is not None:
            for talk in rset.entities():
                s = talk.start_time
                e = talk.end_time
                if (start <= s < end) or (start < e <= end):
                    self.at_the_same_time.append(talk)
        if not self.at_the_same_time:
            raise EmptyComponent()

    def render_body(self, w):
        for talk in self.at_the_same_time:
            w(
                '<p><a href="%s">%s</a></p>'
                % (talk.absolute_url(), xml_escape(talk.dc_title()))
            )
