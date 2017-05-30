# StalkHub

[![Open Source Society University - Computer Science](https://img.shields.io/badge/OSSU-computer--science-blue.svg)](https://github.com/open-source-society/computer-science)
[![Build Status](https://travis-ci.org/aman-roy/StalkHub.svg?branch=master)](https://travis-ci.org/aman-roy/StalkHub)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
[![Join the chat at https://gitter.im/jstriebel/badges](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/StalkHub/Lobby)
<br>

<a href="https://stalkhub.amanroy.me">StalkHub</a> is a <a href="http://flask.pocoo.org/">Flask-based</a> web app which uses <a href="https://developer.github.com/v3/">GitHub API v3</a> to retrieve users data and renders it beautifully.

<p align="center">
  <a href="https://stalkhub.amanroy.me/" target='_blank'>
    <img alt="StalkHub Page" title="StalkHub ScreenShot" src="https://preview.ibb.co/gmYBLv/stalkhub.jpg">
  </a>
</p>

<hr>

## Installation

### Deploy on Heroku

Install Heroku

```
git clone https://github.com/aman-roy/StalkHub.git
cd StalkHub
heroku login
heroku create
git push heroku master
heroku open
```
#### For extending rate limit(optional)
Create github app <a href="https://github.com/settings/applications/new">here</a> and get <strong>Client ID</strong> and <strong>Client Secret.</strong>

```
heroku config:set CLID=xxxxx
heroku config:set CLSEC=yyyyy
``` 
Here xxxxx = Client ID and yyyyy = Client Secret

### Run locally

For running this locally follow the instructions below

```
sudo pip install virtualenv
git clone https://github.com/aman-roy/StalkHub.git
cd StalkHub
virtualenv venv
source venv/bin/activate
sudo pip install -r requirements.txt
python app.py 
```

For accessing the app, open
```
http://0.0.0.0:5000
```


## Contributing

All contributions and suggestions are welcome!

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request


## Getting Help

If you have questions or need further guidance on using this template, please [file an issue](https://github.com/aman-roy/StalHub/issues). I will do my best to respond to all issues in a timely manner. You can also use <a href="https://gitter.im/StalkHub/Lobby">gitter</a>.

## MIT License

> Copyright (c) 2017 Aman Roy http://amanroy.me

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.