var request = require('request');
var util = require('util');

var user_login_string = null;

var ua_string =
    'Piazza/1.2.0.1 CFNetwork/548.0.4 Darwin/11.0.0';

var user_status_string =
    '{"method":"user.status","params":'
    + '{"mobile_type":"ios","mobile_version":"1.2.0.1"}}';

var req_headers = {
  'Host': 'www.piazza.com'
  , 'User-Agent': 'Piazza/1.2.0.1 CFNetwork/548.0.4 Darwin/11.0.0'
  , 'Accept': '*/*'
  , 'Content-Type': 'json'
  , 'Accept-Language': 'en-us'
  , 'Connection': 'keep-alive'
  , 'Proxy-Connection': 'keep-alive'
};

var make_login_request = function () {
  request({uri: 'https://www.piazza.com/logic/api'
          , method: 'POST'
          , proxy: 'http://127.0.0.1:8888'
          , headers: req_headers
          , body: user_login_string},
    function (error, response, body) {
      if (!error && response.statusCode == 200) {
        //console.log(response);
        console.log(body);
        make_status_request();
      }
    });
};

util.exec('python -c "import getpass; print getpass.getpass()"',
          function (error, stdout, stderr) {
            var l = '{"method":"user.login","params":{"pass":"'
                + stdout.slice(0, stdout.length - 1)
                + '","mobile_version":"1.2.0.1",'
                + '"email":"seshadri@berkeley.edu","mobile_type":"ios"}}';
            user_login_string = l;
            make_login_request();
          });

var make_status_request = function () {
  request({uri: 'http://www.piazza.com/logic/api'
          , method: 'POST'
          , json: true
          , headers: req_headers
          , body: user_status_string},
    function (error, response, body) {
      if (!error && response.statusCode == 200) {
        console.log(body)
            }
    });
};
