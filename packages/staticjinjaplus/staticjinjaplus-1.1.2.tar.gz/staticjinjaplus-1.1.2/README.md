# staticjinjaplus

A sweet spot between [staticjinja](https://staticjinja.readthedocs.io/en/latest/) and a full-blown static  site generator.

![Python versions](https://img.shields.io/pypi/pyversions/staticjinjaplus.svg) ![Version](https://img.shields.io/pypi/v/staticjinjaplus.svg) ![License](https://img.shields.io/pypi/l/staticjinjaplus.svg)

[PyPI](https://pypi.org/project/staticjinjaplus/) - [Documentation](https://github.com/EpocDotFr/staticjinjaplus?tab=readme-ov-file#readme) - [Source Code](https://github.com/EpocDotFr/staticjinjaplus) - [Issue Tracker](https://github.com/EpocDotFr/staticjinjaplus/issues) - [Changelog](https://github.com/EpocDotFr/staticjinjaplus/releases)

Citing staticjinja's documentation, "most static site generators are cumbersome to use". While I fully agree, and while
I find staticjinja to be an awesome piece of software, there's still some gaps here and there that needs to be filled in
order to be able to generate a static website that will actually be ready for real world usage.

staticjinjaplus try to fill these gaps, while still being built on staticjinja and its philosophy: keep it simple, stupid.
Note staticjinjaplus is opinionated: choices have been made to cover some use cases, but not all. This is not your average
static site generator.

## Features

All of [staticjinja](https://staticjinja.readthedocs.io/en/latest/)'s features, plus:

  - Simple, file-based configuration to centralize *a handful* of configuration values
  - Build improvements
    - Set system locale before building anything (useful when formatting dates to localized strings)
    - Automatically copy static files to output directory
    - Define staticjinja contexts in config file
    - Define [webassets](https://webassets.readthedocs.io/en/latest/) bundles to allow CSS/JS concatenation/minification
    - Automatically minify XML (including HTML, RSS and Atom)/JSON output
  - Jinja improvements
    - A few new Jinja globals/filters to make your life easier
    - Autoescape is enabled for XML, HTML, RSS and Atom templates
  - Serve the generated site through a local HTTP server
    - URL rewrite emulation (for HTML files)
    - Custom HTTP error pages emulation
    - IPv6 loopback address support
  - Publish the generated site through rsync over SSH

**Planned:**

  - Generic support of Markdown-formatted templates collections (forget about the usual "pages" or "articles/blog posts" feature)

## Prerequisites

  - Python >= 3.9

## Installation

From PyPI:

```bash
$ pip install staticjinjaplus
```

Locally, after cloning/downloading the repo:

```bash
$ pip install .
```

A CLI (`staticjinjaplus`) will be made available upon installation.

## Usage

### Templates

You'll want to write your site's Jinja templates first: write them as usual. By default, staticjinjaplus searches for
Jinja templates in the `templates` directory where it is invoked. You can change that by using the `TEMPLATES_DIR`
[configuration value](#configpy).

staticjinjaplus offers the following additional Jinja facilities.

#### Globals

| Name/signature                                  | Type     | Description                                                                                                                                                                                                         |
|-------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `config`                                        | Dict     | Configuration values loaded from [`config.py`](#configpy) (defaults are guaranteed to be provided for built-in values). Only uppercase variables are loaded by staticjinjaplus                                      |
| `url(path: str, absolute: bool = False) -> str` | Callable | Build (by default) a relative URL to a file located in the `OUTPUT_DIR` directory. Setting `absolute` to `True` prefixes the URL with `BASE_URL`. See [configuration values](#configpy)                             |
| `icon(name: str) -> markupsafe.Markup`          | Callable | Return the file content of the given SVG icon, marked as safe to be rendered by Jinja. Icons must be saved in the form of `{ASSETS_DIR}/icons/{name}.svg`. Useful to embed SVG icons directly in the generated HTML |

**Usage examples:**

```html+jinja
{{ config.BASE_URL }}         {# http://localhost:8080/ (by default) #}
{{ config.MY_CUSTOM_CONFIG }} {# Whatever you defined in your config.py (uppercase variables only) #}

{# url() doesn't care whether an extension is given or not #}
{{ url('/about.html') }} {# /about.html #}
{{ url('/about') }}      {# /about #}
{{ url('about') }}       {# /about #}

{# url() doesn't care about whether a static file is targeted or not #}
{{ url('/images/logo.png') }} {# /images/logo.png #}
{{ url('images/logo.png') }}  {# /images/logo.png #}

{# URL is simply prefixed with BASE_URL when generating absolute URLs #}
{{ url('/images/logo.png', absolute=True) }} {# http://localhost:8080/images/logo.png (by default) #}
{{ url('images/logo.png', absolute=True) }}  {# http://localhost:8080/images/logo.png (by default) #}

{{ icon('github') }} {# <svg xmlns="http://www.w3.org/2000/svg" ... </svg> #}
```

#### Filters

| Signature                                      | Description                                                                                                                                                                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<data: Dict>\|tojsonm -> str`                 | Serialize the given dictionary to a JSON string. Automatically takes into account the `MINIFY_JSON` [configuration value](#configpy) to minify (or not) the resulting output. Useful for e.g serializing [Schema.org](https://schema.org/)'s JSON-LD-formatted data |
| `<left: Dict>\|dictmerge(right: Dict) -> Dict` | Merge two dictionaries. Does not modify existing ones, a new one will be created. Does **not** merge deeply                                                                                                                                                         |

**Usage examples:**

```html+jinja
{{ dict(yes=True)|tojsonm }} {# With config['MINIFY_JSON'] == False:
                                 {
                                     "yes": true
                                 }
                             #}

{{ dict(yes=True)|tojsonm }} {# With config['MINIFY_JSON'] == True:
                                 {"yes":true}
                             #}

{{ dict(yes=True)|dictmerge(dict(no=False)) }} {# {"yes": True, "no": False} #}
```

### Command line interface

The `staticjinjaplus` CLI is your main and only way to interact with staticjinjaplus. The following commands are available.

#### `staticjinjaplus build`

Build the site by rendering your templates from the `TEMPLATES_DIR` directory in the `OUTPUT_DIR` directory.

**Options:**

  - `-w, --watch` Automatically rebuild the site when templates are modified

staticjinjaplus will first try to set the system's locale to the first working locale identifier set in the `LOCALE`
[configuration value](#configpy) (if set).

It will then copy the tree contained in the `STATIC_DIR` directory in the `OUTPUT_DIR`, as-is.

staticjinja will be then initialized with the given `CONTEXTS` and Jinja's `GLOBALS`/`FILTERS`/`EXTENSIONS`,
[webassets bundles](https://webassets.readthedocs.io/en/latest/bundles.html) will be registered, and the actual rendering
process is started.

`.html`, `.xml`, `.rss`, `.atom` and `.json` template output will be automatically minified, according to the `MINIFY_XML`
and `MINIFY_JSON` configuration values.

#### `staticjinjaplus clean`

Delete and recreate the `OUTPUT_DIR` directory.

#### `staticjinjaplus publish`

> [!NOTE]
> This feature requires a Linux-like environment.

Apply configuration values override from [environment variables](#environment-variables), then successively run
`staticjinjaplus build` and `staticjinjaplus clean` prior remotely syncing the `OUTPUT_DIR` directory content using
`rsync` through SSH.

#### `staticjinjaplus serve`

Serve the `OUTPUT_DIR` directory using Python's built-in HTTP server, plus a couple improvements:

  - URL rewrite for HTML files is emulated, i.e. both `/about.html` and `/about` will work
  - Custom HTTP error pages are emulated, if they are found saved as `{status code}.html` in the output directory
  - The server will listen to both IPv4 *and* IPv6 loopback addresses if possible

By default, you can browse your generated site at http://localhost:8080/ or http://[::1]:8080/. Port can be changed
by defining the `SERVE_PORT` [configuration value](#configpy).

## Configuration

### `config.py`

Your project's configuration happens in a single `config.py` file in the root directory (where the `staticjinjaplus`
CLI should be executed). You'll find the available configuration values below.

> [!NOTE]
>   - All paths are relative to the root directory, unless otherwise stated.
>   - None of these configuration values are required, so is `config.py`.
>   - Only uppercase variables are loaded by staticjinjaplus.

| Name             | Type                                            | Default                          | Description                                                                                                                                                                                                                                                                            |
|------------------|-------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `LOCALE`         | List[str]                                       | `None`                           | Locale identifiers passed to [`locale.setlocale()`](https://docs.python.org/3.12/library/locale.html#locale.setlocale) before a build is executed. The first working identifier will be used                                                                                           |
| `SERVE_PORT`     | int                                             | `8080`                           | Listening port of the HTTP server started by `staticjinjaplus serve`                                                                                                                                                                                                                   |
| `BASE_URL`       | str                                             | `http://localhost:{SERVE_PORT}/` | Protocol and domain name to use to generate meaningful absolute URLs. Set host part to `[::1]` if you plan to use IPv6                                                                                                                                                                 |
| `MINIFY_XML`     | bool                                            | `False`                          | Enable XML minification                                                                                                                                                                                                                                                                |
| `MINIFY_JSON`    | bool                                            | `False`                          | Enable JSON minification                                                                                                                                                                                                                                                               |
| `TEMPLATES_DIR`  | str                                             | `templates`                      | Directory containing the Jinja templates to be processed                                                                                                                                                                                                                               |
| `OUTPUT_DIR`     | str                                             | `output`                         | Directory where the rendered site will be saved                                                                                                                                                                                                                                        |
| `STATIC_DIR`     | str                                             | `static`                         | Directory containing static files                                                                                                                                                                                                                                                      |
| `ASSETS_DIR`     | str                                             | `assets`                         | Directory containing assets, i.e. files that needs prior processing before being able to be used by the rendered site                                                                                                                                                                  |
| `ASSETS_BUNDLES` | List[Tuple[str, Tuple[str,...], Dict[str, str]] | `[]`                             | [webassets bundles](https://webassets.readthedocs.io/en/latest/bundles.html) to be registered. These are passed to [`register()`](https://webassets.readthedocs.io/en/latest/environment.html#registering-bundles). Sources are relative to `ASSETS_DIR`, destinations to `OUTPUT_DIR` |
| `CONTEXTS`       | List[Tuple[str, Any]]                           | `[]`                             | [staticjinja contexts](https://staticjinja.readthedocs.io/en/stable/user/advanced.html#loading-data) to be used by templates                                                                                                                                                           |
| `GLOBALS`        | Dict                                            | `{}`                             | [jinja globals](https://jinja.palletsprojects.com/en/3.1.x/api/#jinja2.Environment.globals) to be made available in all templates                                                                                                                                                      |
| `FILTERS`        | Dict                                            | `{}`                             | [jinja filters](https://jinja.palletsprojects.com/en/3.1.x/api/#jinja2.Environment.filters) to be made available in all templates                                                                                                                                                      |
| `EXTENSIONS`     | List[Union[str, jinja2.ext.Extension]]          | `[]`                             | [jinja extensions](https://jinja.palletsprojects.com/en/3.1.x/extensions/) to load                                                                                                                                                                                                     |

### Environment variables

Some configuration values may/must be overridden by environment variables of the same name when publishing your site
(`staticjinjaplus publish` command), typically in a deployment environment. You'll find the list below.

| Name          | Type   | Required?                      | Default                           | Description                                                          |
|---------------|--------|--------------------------------|-----------------------------------|----------------------------------------------------------------------|
| `BASE_URL`    | str    | Yes                            |                                   | Protocol and domain name to use to generate meaningful absolute URLs |
| `MINIFY_XML`  | bool ¹ | No, but activation recommended | `MINIFY_XML` configuration value  | Enable XML minification                                              |
| `MINIFY_JSON` | bool ¹ | No, but activation recommended | `MINIFY_JSON` configuration value | Enable JSON minification                                             |
| `SSH_USER`    | str    | Yes                            |                                   | SSH username                                                         |
| `SSH_HOST`    | str    | Yes                            |                                   | SSH hostname                                                         |
| `SSH_PORT`    | int    | No                             | `22`                              | SSH port                                                             |
| `SSH_PATH`    | str    | Yes                            |                                   | Absolute path to the deployment directory on the SSH host            |

¹ Any [falsy](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Boolean.falsy) or
[truthy](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Boolean.truthy) string
representation of boolean values allowed by marshmallow

## Development

### Getting source code and installing the package with dev dependencies

  1. Clone the repository
  2. From the root directory, run: `pip install -e .[dev]` on Linux or `pip install -e ".[dev]"` on Windows

### Releasing the package

From the root directory, run `python setup.py upload`. This will build the package, create a git tag and publish on PyPI.

`__version__` in `staticjinjaplus/__version__.py` must be updated beforehand. It should adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

An associated GitHub release must be created following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.