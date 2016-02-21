var http = require('http')
http.createServer(function(req, resp) {
    resp.writeHead(200, {
        'Content-Type': "text/html"
    });
    var result = "Hello,World!"
    resp.end(result)
}).listen(8080, "127.0.0.1");
console.log("Server Running at http://127.0.0.1:8080/")