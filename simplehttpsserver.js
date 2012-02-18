var fs = require('fs');

function onConnection(req, res) {
  console.log(req);
  console.log(res);
  res.setHeader('Content-Type', 'text/plain');
  res.end("Hello World!\n");
}

var options = {
ca:   fs.readFileSync('/Users/seshadri/.siriproxy/ca.pem'),
key:  fs.readFileSync('/Users/seshadri/.siriproxy/server.passless.key'),
cert: fs.readFileSync('/Users/seshadri/.siriproxy/server.passless.crt')
};

require('https').createServer(options, onConnection).listen(443);
