# dmtoolkit

!!!!!!!!!!!!!!!!!!!! NO LONGHER UNDER DEVELOPMENT - FOLDED INTO ANOTHER PROJECT !!!!!!!!!!!!!!!!!!!!!!!!

- **[pypi](https://pypi.org/project/dmtoolkit/)**
- **[github](https://github.com/Sallenmoore/dmtoolkit)**

## Overview

Completely rewritten from the ground up as a TTRPG worldbuilding tool using AI to generate entire worlds.

Much more to come...

## Setup

Add the following to your .env file:

```bash
### DB Config
REDIS_PORT=
REDIS_HOST=
RQ_DEFAULT_CONNECTION=
REDIS_DB=
REDIS_DECODE=
REDIS_USERNAME=
REDIS_PASSWORD=
#### OpenAI Config
OPENAI_KEY=

### Cloudinary Config
CLOUD_NAME=
CLOUDINARY_KEY=
CLOUDINARY_SECRET=

### WikiJS Config

WIKIJS_TOKEN = ""
WIKIJS_URL = ""

# DEV OPTIONS

DEBUG=True
TESTING=True
LOG_LEVEL=INFO
```

## Features

- TBD

---

## Developer Notes

### TODO

- A TODO list

### Issue Tracking

- None

## Make Commands

### Tests

```sh
make tests
```

### package

1. Update version in `/src/dmtoolkit/__init__.py`
2. ```sh
   make package
   ```
