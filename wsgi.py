from app import create_app
from app.extensions import db

app = create_app()

db.create_all()
# if __name__ == '__main__':
#   # from gevent.pywsgi import WSGIServer
#   # http_server = WSGIServer(('0.0.0.0', 8080), app)
#   # http_server.serve_forever()
# #   app.run(host='0.0.0.0', port=8181, debug=True)
#   app.run()