<h1 align="center"><b>III API base</b></h1>

<div align="center">
<a href="https://pypi.org/project/iii-api-helper" target="_blank">
  <img src="https://img.shields.io/pypi/v/iii-api-helper.svg?logo=pypi&logoColor=gold&label=PyPI" alt="PyPI - Version">
</a>
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/iii-api-helper.svg?logo=python&label=Python&logoColor=gold">
<br />
<a href="https://pepy.tech/project/iii-api-helper" >
  <img alt="Downloads" src="https://static.pepy.tech/badge/iii-api-helper"/>
</a>
<a href="https://pepy.tech/project/iii-api-helper" >
  <img alt="Weekly downloads" src="https://static.pepy.tech/badge/iii-api-helper/week"/>
</a>
<a href="https://pepy.tech/project/iii-api-helper" >
  <img alt="Monthly downloads" src="https://static.pepy.tech/badge/iii-api-helper/month"/>
</a>
<br />
<a href="https://github.com/pypa/hatch">
  <img alt="Hatch project" src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg">
</a>
<a href="https://github.com/astral-sh/ruff">
  <img alt="linting - Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json">
</a>
<p align="center">
III FastAPI Common base
<br />
<a href="https://pypi.org/project/iii-api-helper/"><strong>Go to pypi now</strong></a>
</p>
</div>

---

## Usage

### Config

> The later config will override the previous one.

This table shows the predefined environment variables.

| Keyword    | Type    | Default     | Description                                                                        |
|------------|---------|-------------|------------------------------------------------------------------------------------|
| `DEBUG`    | boolean | false       | To set the logging as `DEBUG` state, you can pass `debug=True` to application too. |
| `RELOAD`   | boolean | false       | To auto reload the FastAPI application, you can pass `reload=True` to `run` too.   |
| `APP_NAME` | string  | Backend API | The application name use on FastAPI.                                               |

```python
from pathlib import Path

from api_helper.config import load_config

# Load config
load_config(Path(__file__).parent / ".env")

# Load default config in the directory (.env)
load_config(Path(__file__).parent)
```

### FastAPI example

> To config the FastAPI by env, read the [Config](#config) section.

```python
from pathlib import Path

from api_helper import FastAPI, success_response

app: FastAPI = FastAPI(base_folder=Path(__file__).parent)
# Optional to setup sentry
app.setup_sentry("sentry_dsn")


@app.get("/")
def home():
    return success_response("Hello, World!")


# Start the app and enjoy
app.run("127.0.0.1", 5000)

# Start the app with OpenAPI, for example
app.run(show_swagger=True)
```

#### Use FastAPI with auto-reload

To use the reload method, you need to pass `reload=True` and `app="main:app"` to the `run` method.  
If you don't pass them, the reload will not work. See the sample code below.

```python
from pathlib import Path

from api_helper import FastAPI

# Must declared before running into main code block
app: FastAPI = FastAPI(base_folder=Path(__file__).parent.parent)

if __name__ == "__main__":
    # Pass the app as a string to uvicorn.run to enable auto-reload
    app.run(app="test:app", reload=True)
```

#### Custom Logger Format

If you want to customize the Logger format, you can pass `log_builder` to the FastAPI object.  
The following example shows how to customize the logger format.  
See below sample for more information.

```python
from pathlib import Path

from api_helper import FastAPI
from api_helper.config import LoggerBuilder

# To customize the logger format, you can pass the log_builder to FastAPI
log_builder: LoggerBuilder = LoggerBuilder(Path(__file__).parent)
log_builder.formatters = {}  # For example, we change the formatter to empty
app: FastAPI = FastAPI(base_folder=Path(__file__).parent, log_builder=log_builder)

# Or if you prefer the default, you can extend the default formatter
# For example, you can change the root level to DEBUG with default formatter
log_builder: LoggerBuilder = LoggerBuilder(Path(__file__).parent, config={"root": {"level": "DEBUG"}})
app: FastAPI = FastAPI(base_folder=Path(__file__).parent, log_builder=log_builder)

# Or pass as parameter start with the `logging_` keyword, it will be passed to the LoggerBuilder
# It is the same as the previous example
app: FastAPI = FastAPI(base_folder=Path(__file__).parent, logging_config={"root": {"level": "DEBUG"}})
```
