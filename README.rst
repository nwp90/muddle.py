muddle.py
=========

About
-----
A rather incomplete python client for the Moodle 2.0 Web API. Feel free to give it some love.

.. image:: https://badge.fury.io/py/muddle.png
    :target: http://badge.fury.io/py/muddle

API Coverage
-----------
* ??% core API coverage
* Covers parts of course, group, users, category WS functionality

Usage
-----

basic usage::

  import muddle

  API_KEY = '133bf54a4adf1e21aff0c29034c038e2'
  API_URL = 'https://your.moodle.server'

  m = muddle.Config(API_KEY, API_URL)
  mcatapi = muddle.category.API(m)
  mcrsapi = muddle.course.API(m)
  mgrpapi = muddle.group.API(m)
  musrapi = muddle.users.API(m)

  courselist = mcrsapi.get_courses([1,2,3])

etc. etc.

This is all still very much experimental.

Documentation
------------

Documentation is available from: <http://muddlepy.readthedocs.org/en/latest/>

Installation
------------

To install ``muddle.py``::

$ pip install muddle

Alternatively, if you're a bad person::

$ easy_install muddle


License
-------

Copyright (c) 2013-2017 Kit Randel, Nick Phillips

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


.. _muddle.py:        https://github.com/nwp90/muddle.py
