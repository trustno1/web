import wsgiref.handlers
import web
from google.appengine.ext import webapp


class MainPage(webapp.RequestHandler):
  def get(self):
	self.response.headers['Content-Type'] = 'text/plain'
	self.response.out.write('Hello, webapp World!')


def main():
  application = webapp.WSGIApplication(
                                       [('/', MainPage)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

def main2():
  application = get_wsgi_application()
  wsgiref.handlers.CGIHandler().run(application)
  
if __name__ == "__main__":
	main2()
