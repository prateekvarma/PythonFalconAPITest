import json
import falcon

class Resource(object):
    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href' : '/images/1.png'
                }
            ]
        }
        #create json
        resp.body = json.dump(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200