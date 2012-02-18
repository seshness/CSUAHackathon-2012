# from cherrypy import wsgiserver

# def my_crazy_app(environ, start_response):
#     status = '200 OK'
#     response_headers = [('Content-type','text/plain')]
#     start_response(status, response_headers)
#     return ['Hello world!']

# server = wsgiserver.CherryPyWSGIServer(
#             ('0.0.0.0', 443), my_crazy_app,
#             server_name='localhost')
# server.ssl_adaptor = wsgiserver.SSLAdapter('sesh-ca-cert.crt',
#                                            'sesh-ca-private.key',
#                                            certificate_chain=None)
# server.start()

import cherrypy

class RootServer:
    @cherrypy.expose
    def index(self, **keywords):
        items = [x + ': ' + y for x,y in cherrypy.request.headers.items()]
        print
        print "\n".join(items)
        print
        return "it works!"

    @cherrypy.expose
    def ace(self, **keywords):
        items = [x + ': ' + y for x,y in cherrypy.request.headers.items()]
        print
        print "\n".join(items)
        print
        return ''

if __name__ == '__main__':
    server_config={
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 443,

        'server.ssl_module':'pyopenssl',
        'server.ssl_certificate':'sesh-ca-cert.crt',
        'server.ssl_private_key':'sesh-ca-private.key',
        'server.ssl_certificate_chain':'sesh-ca-cert.crt'
    }

    cherrypy.config.update(server_config)
    cherrypy.quickstart(RootServer())
