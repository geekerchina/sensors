def application(environ, start_response):
    status = '200 OK'
    output = 'This is the admin page of sensors network!(Geekerchina)'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
