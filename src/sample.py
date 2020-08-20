import falcon

import pyper as pr

# https://falcon.readthedocs.io/en/stable/user/faq.html#how-do-i-implement-cors-with-falcon
class CORSComponent(object):
    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Access-Control-Allow-Origin', '*')
        if (req_succeeded
            and req.method == 'OPTIONS'
            and req.get_header('Access-Control-Request-Method')
        ):
            allow = resp.get_header('Allow')
            resp.delete_header('Allow')
            allow_headers = req.get_header(
                'Access-Control-Request-Headers',
                default='*'
            )
            resp.set_headers((
                ('Access-Control-Allow-Methods', allow),
                ('Access-Control-Allow-Headers', allow_headers),
                ('Access-Control-Max-Age', '86400'), # 24 hours
            ))

class FaithfulResource:
    def on_get(self, req, resp):
        r = pr.R()
        # https://www.r-tutor.com/elementary-statistics/quantitative-data/frequency-distribution-quantitative-data
        r("duration = faithful$eruptions")
        r("breaks = seq(1.5, 5.5, by=0.5)")
        r("duration.cut = cut(duration, breaks, right=FALSE)")
        r("duration.freq = table(duration.cut)")
        resp.body = r("duration.freq")

api = falcon.API(middleware=[CORSComponent()])
api.add_route('/faithful', FaithfulResource())
