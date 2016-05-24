from bottle import route, run


@route('/hello/<name>')
def hello(name):
    return "<h1>Hello World!{{name}}</h1>".format(name)


run(host='localhost', port=8080)
