[![Build Status](https://travis-ci.org/ymattw/heroku-deploy-demo.svg?branch=master)](https://travis-ci.org/ymattw/heroku-deploy-demo)

_Just a toy project to test auto deploy to heroku._

```
$ ./demo_server.py --help
Usage: demo_server.py [options]

Options:
  -h, --help            show this help message and exit
  -b BIND, --bind=BIND  Bind address, default 127.0.0.1, use "0.0.0.0" for all
  -p PORT, --port=PORT  Listen port, default is 8080

$ ./demo_server.py &

$ curl -s localhost:8080
Hello world!
```
