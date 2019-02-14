-------------------------------------------------------------------------------

This project is no longer maintained.

-------------------------------------------------------------------------------


Sandman on Heroku
=================

This a simple app showing how to connect the [Sandman][] database service to an existing [Heroku][] app using [Heroku Postgres][].


Deployment
----------

    git clone https://github.com/mietek/sandman-on-heroku.git
    cd sandman-on-heroku
    heroku create
    heroku config:set DATABASE_URL=...
    heroku config:set SANDMAN_USERNAME=...
    heroku config:set SANDMAN_PASSWORD=...
    git push heroku master


Configuration
-------------

Variable           | Description
-------------------|------------
`DATABASE_URL`     | Connection details for Heroku Postgres
`SANDMAN_USERNAME` | Username for Sandman
`SANDMAN_PASSWORD` | Password for Sandman
`GUNICORN_WORKERS` | Number of Gunicorn workers; optional; default: `1`


Hacking
-------


Questions
---------

For more information on Sandman, check the [Sandman documentation][], or the [Sandman source code][].

To learn more about deploying web apps on Heroku, try the excellent [Heroku Hacker’s Guide][], written by [Randall Degges][].


Meta
----

Available under the BSD license.

Written by [Miëtek Bak][].  Say hello@mietek.io


[Sandman]:               http://sandman.io
[Sandman documentation]: https://sandman.readthedocs.org
[Sandman source code]:   https://github.com/jeffknupp/sandman
[Heroku]:                https://www.heroku.com
[Heroku Postgres]:       https://www.heroku.com/postgres
[Heroku Hacker’s Guide]: http://www.theherokuhackersguide.com
[Randall Degges]:        http://www.rdegges.com
[Miëtek Bak]:            http://mietek.io
