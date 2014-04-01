![Concentric Sky](https://concentricsky.com/media/uploads/images/csky_logo.jpg)


# Django Fumus

Django Fumus is an open-source Django library developed by [Concentric Sky](http://concentricsky.com/). It is a smoke-test app that currently tests for cache read/write and database readability.


## Installation and Usage

Install the library using pip:

    pip install git+https://github.com/concentricsky/django-fumus.git


Add 'fumus' to INSTALLED_APPS in settings.py:

    INSTALLED_APPS = (
        ...
        'fumus',
        ...

Include fumus in your urls:

    
    urlpatterns = patterns('',
        ...
        url(r'fumus/', include('fumus.urls')),
        ...
    )

To test that your server is running, perform a HEAD request on /fumus/. An HTTP 200 indicates pass, HTTP 500 indicates one or more errors.


## License

This project is licensed under the Apache License, Version 2.0. Details can be found in the LICENSE.md file.


## About Concentric Sky

_For nearly a decade, Concentric Sky has been building technology solutions that impact people everywhere. We work in the mobile, enterprise and web application spaces. Our team, based in Eugene Oregon, loves to solve complex problems. Concentric Sky believes in contributing back to our community and one of the ways we do that is by open sourcing our code on GitHub. Contact Concentric Sky at hello@concentricsky.com._
