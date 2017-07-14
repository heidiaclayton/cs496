from google.appengine.ext import ndb
import webapp2
import json

class Boat(ndb.Model):
    ID = ndb.StringProperty(required=True)
    name = ndb.StringProperty()

class BoatHandler(webapp2.RequestHandler):
    def post(self):
        boat_data = json.loads(self.request.body)
        self.response.write(json.dumps(boat_data))

class MainPage(webapp2.RequestHandler):

    def get(self):
	self.response.write("hello world")

allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fish', FishHandler)
], debug=True)

