# TODO

Pencil icon changes to a green check mark once export for that file is correct. Else an error symbol.


# bootstrap-studio-to-django-template
[![Build Status](https://travis-ci.org/AbcSxyZ/bootstrap-studio-to-django-template.svg?branch=master)](https://travis-ci.org/AbcSxyZ/bootstrap-studio-to-django-template)
[![Coverage Status](https://coveralls.io/repos/github/AbcSxyZ/bootstrap-studio-to-django-template/badge.svg?branch=coverall)](https://coveralls.io/github/AbcSxyZ/bootstrap-studio-to-django-template?branch=coverall)

Export a [Bootstrap Studio](https://bootstrapstudio.io/) design into a [Django](https://www.djangoproject.com/) project folder.  

*Credit: Improvement of [lingster/django-bootstrap-studio-tools](https://github.com/lingster/django-bootstrap-studio-tools)*

**Index**
- [How it works](#how-it-works)
- [Installation](#installation)
- [Features](#features)
- [Contribute](#contribute)
- [License](#license)

## How it works

This export script will allow you to create custom HTML attributes while developing design with Bootstrap Studio. Those attributes will be convert to their corresponding django template tag inside an export directory.

Finally, export script will move all html/css/js/img generated by Bootstrap Studio to a `DJANGO_PROJECT`.

Django is having an application based architecture, **Bootstrap Studio developement must follow this architecture**, create app subfolder and move file inside it. In Boostrap Studio, always create application subfolder inside `Pages`, `Styles`, `JavaScript`, `Fonts` and `Images` folders. (see [tests](test/tree_script/mixed/multiple_assets_type))


## Installation

#### Python 
**WARNING: Require python 3.6 or higher**

Install project dependencies :
```
pip install -r requirements.txt
```
You can use a virtual env inside directory of the export script, and specify folder in `env` file using `VIRTUAL_ENV` (see [env file](#env-file)).

#### Bootstrap studio

Go to `Export Options`.
- In `Advanced > Export Script`, specify the **absolute path** of `django_export.sh` on your local machine.
- Enable options `Use a CDN for libraries`, `Use absolute paths`
- Specify `Export destination` as well

`Save` your configuration for later export.

#### Env file
Rename `env.template` to `env`.  

Available variables:
- `DJANGO_PROJECT` **(mandatory)** : Absolute path of your django project folder.
- `VIRTUAL_ENV` **(optionnal)** : relative path of virtual env directory, **MUST BE** within this script folder.

#### Test
To see if everything is running properly : `python -m unittest discover test`

## Features

See all [available features](features.md)

## Contribute
Your help is welcome ! Here some contribution example:
- [Ask/work for new feature](community_asked_features.md)
- Add issue/fix for bug
- Correct spelling/English mistake
- Improve documentation
- Code review
- Test coverage
- Whatever you have in mind for the software :)

## License

Free software under [AGPL](LICENSE). Please share your modification to respect term of license :)  
