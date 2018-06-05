import tornado.ioloop
import tornado.web
import os.path


class MainHandler(tornado.web.RequestHandler):

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.request.body("message"))

# This tells tornado where to find the static files
setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

# r"/" == root website address
apllication = tornado.web.Application([
    (r"/", MainHandler)
], **setting)

# Start the server at port n
if __name__ == "__main__":
    print('Server Running...')
    print('Press ctrl + c to close')
    apllication.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
