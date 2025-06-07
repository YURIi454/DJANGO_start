from http.server import BaseHTTPRequestHandler, HTTPServer
import os.path

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Специальный класс, который отвечает за
        обработку входящих запросов от клиентов"""

    root_dir = os.path.dirname(__file__)

    paths = {
        "GET":
            {
                "main": root_dir + "/main.html",
                "settings": root_dir + "/settings.html",
                "catalog": root_dir + "/catalog.html",
                "pay": root_dir + "/pay.html"
            }
    }

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        paths = self.paths["GET"]
        if self.path in paths:
            url_pt = paths[self.path]
        else:
            url_pt = paths["main"]

        with open(url_pt, mode="r", encoding="UTF-8") as file:
            self.wfile.write(bytes(file.read().encode()))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:

        webServer.serve_forever()
    except KeyboardInterrupt:

        pass

    webServer.server_close()
    print("Server stopped.")
