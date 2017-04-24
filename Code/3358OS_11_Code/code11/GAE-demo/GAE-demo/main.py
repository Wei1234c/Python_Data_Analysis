import webapp2
import numpy as np

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!<br/>')
        np.random.seed(42)
        self.response.out.write('NumPy sum = ' + str(np.random.randn(7).sum()))

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
