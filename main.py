import tornado.ioloop
import tornado.web
import os.path
import requests



class MainHandler(tornado.web.RequestHandler):

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.request.body())

    def pretty_print_POST(req):
        """
        At this point it is completely built and ready
        to be fired; it is "prepared".

        However pay attention at the formatting used in
        this function because it is programmed to be pretty
        printed and may differ from the actual request.
        """
        print('{}\n{}\n{}\n\n{}'.format(
            '-----------START-----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            req.body,
        ))

 





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
    print('request accepted')
    print('close window')
    apllication.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
