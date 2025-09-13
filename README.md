## Table of Contents
* [Development Setup](#development-setup)
    * [Prerequisites](#prerequisites)
    * [Initial Setup](#initial-setup)
    * [API Documentation](#view-api-documentation)

## Development Setup

### Prerequisites
---------------------
- python >= 3.13
- Git
- uv

### Initial Setup
---------------------
- Clone main repository locally.
```
    $ git clone git@github.com:jenish1231/fastapi-starter.git
    $ cd fastapi-starter
```

- Create a virtualenv
```
    $ virtualenv venv --python=python3.13
    $ source venv/bin/activate
```

on Windows,
```
    > env\Scripts\activate
```
- install development dependencies.
```
   $ uv sync
```

## View API Documentation
--------------------------

- http://localhost:8000/docs
> Note: Considering your application is running on localhost at port 8000.
