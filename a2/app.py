from google.appengine.ext import ndb
import webapp2

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
	self.response.write("hello world")
# [END main_page]

# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
# [END app]
