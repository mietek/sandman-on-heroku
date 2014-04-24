**WORK IN PROGRESS**

---


Sandman on Heroku
=================

This a simple app showing how to connect the [Sandman][] database service to an existing [Heroku][] app using [Heroku Postgres][].


Deployment
----------

    git clone https://github.com/mietek/sandman-on-heroku.git
    cd sandman-on-heroku
    heroku create
    heroku config:set HEROKU_API_KEY=`heroku auth:token`
    heroku config:set DATABASE_OWNER_APP=${YOUR_EXISTING_HEROKU_APP_NAME}
    heroku config:set SANDMAN_USERNAME=${YOUR_NEW_SANDMAN_USERNAME}
    heroku config:set SANDMAN_PASSWORD=${YOUR_NEW_SANDMAN_PASSWORD}
    git push heroku master


Configuration
-------------

Variable             | Description
---------------------|------------
`HEROKU_API_KEY`     | Required; used to get `DATABASE_URL`
`DATABASE_OWNER_APP` | Required; used to get `DATABASE_URL`
`SANDMAN_USERNAME`   | Required; used to secure Sandman
`SANDMAN_PASSWORD`   | Required; used to secure Sandman
`GUNICORN_WORKERS`   | Optional; default: `1`


Questions
---------

For more information on Sandman, check the [Sandman documentation][], or the [Sandman source code][].

To learn more about deploying web apps on Heroku, try the excellent [Heroku Hacker’s Guide][], written by [Randall Degges][].


Meta
----

Available under the MIT License.

Written by [Miëtek Bak][].  Say hello@mietek.io


[Sandman]:               http://sandman.io
[Sandman documentation]: https://sandman.readthedocs.org
[Sandman source code]:   https://github.com/jeffknupp/sandman
[Heroku]:                https://www.heroku.com
[Heroku Postgres]:       https://www.heroku.com/postgres
[Heroku Hacker’s Guide]: http://www.theherokuhackersguide.com
[Randall Degges]:        http://www.rdegges.com
[Miëtek Bak]:            http://mietek.io
