from staticjinjaplus.http import EnhancedThreadingHTTPServer, SimpleEnhancedHTTPRequestHandler
from staticjinjaplus import staticjinja_helpers, jinja_helpers
from webassets import Environment as AssetsEnvironment
from importlib import util as importlib_util
from jinja2 import select_autoescape
from staticjinja import Site, logger
from shutil import copytree, rmtree
from os import makedirs, path
from subprocess import call
from environs import Env
from typing import Dict
import locale


def load_config() -> Dict:
    """Load configuration from both `config.py` in the directory where staticjinjaplus is executed and environment
    variables, returning a dict representation of this configuration. Only uppercase variables are loaded"""

    # Set default config values
    serve_port = 8080

    config = {
        'LOCALE': None,
        'SERVE_PORT': serve_port,
        'BASE_URL': f'http://localhost:{serve_port}/',
        'MINIFY_XML': False,
        'MINIFY_JSON': False,
        'TEMPLATES_DIR': 'templates',
        'OUTPUT_DIR': 'output',
        'STATIC_DIR': 'static',
        'ASSETS_DIR': 'assets',
        'ASSETS_BUNDLES': [],
        'CONTEXTS': [],
        'GLOBALS': {},
        'FILTERS': {},
        'EXTENSIONS': [],
    }

    # Load and erase default config values from config.py, if the file exists
    try:
        spec = importlib_util.spec_from_file_location('config', 'config.py')
        actual_config = importlib_util.module_from_spec(spec)
        spec.loader.exec_module(actual_config)

        config.update({
            k: v for k, v in vars(actual_config).items() if k.isupper()
        })
    except FileNotFoundError:
        pass

    return config


def set_locale(config: Dict) -> None:
    """Set the system locale based on the LOCALE config"""
    if not config['LOCALE']:
        return

    locale_successfully_set = False

    for code in config['LOCALE']:
        try:
            locale.setlocale(locale.LC_ALL, code)

            locale_successfully_set = True

            logger.info(f'System locale set to {code}')

            break
        except locale.Error:
            pass

    if not locale_successfully_set:
        logger.error('Unable to set system locale')


def build(config: Dict, watch: bool = False) -> None:
    """Build the site"""
    set_locale(config)

    webassets_cache = path.join(config['ASSETS_DIR'], '.webassets-cache')

    makedirs(webassets_cache, exist_ok=True)
    makedirs(config['STATIC_DIR'], exist_ok=True)
    makedirs(config['OUTPUT_DIR'], exist_ok=True)
    makedirs(config['ASSETS_DIR'], exist_ok=True)

    logger.info('Copying static files from "{STATIC_DIR}" to "{OUTPUT_DIR}"...'.format(**config))

    copytree(
        config['STATIC_DIR'],
        config['OUTPUT_DIR'],
        dirs_exist_ok=True
    )

    logger.info('Building from "{TEMPLATES_DIR}" to "{OUTPUT_DIR}"...'.format(**config))

    rules = [
        r for r in [
            (r'.*\.(xml|html|rss|atom)', staticjinja_helpers.minify_xml_template) if config['MINIFY_XML'] else None,
            (r'.*\.json', staticjinja_helpers.minify_json_template) if config['MINIFY_JSON'] else None,
        ] if r is not None
    ]

    jinja_globals = {
        'config': config,
        'url': jinja_helpers.url(config),
        'icon': jinja_helpers.icon(config),
    }

    jinja_globals.update(config['GLOBALS'])

    jinja_filters = {
        'tojsonm': jinja_helpers.tojsonm(config),
        'dictmerge': jinja_helpers.dictmerge,
    }

    jinja_filters.update(config['FILTERS'])

    jinja_extensions = [
        'webassets.ext.jinja2.AssetsExtension',
    ]

    jinja_extensions.extend(config['EXTENSIONS'])

    site = Site.make_site(
        searchpath=config['TEMPLATES_DIR'],
        outpath=config['OUTPUT_DIR'],
        mergecontexts=True,
        env_globals=jinja_globals,
        filters=jinja_filters,
        contexts=config['CONTEXTS'] or None,
        rules=rules or None,
        extensions=jinja_extensions,
        env_kwargs={
            'trim_blocks': True,
            'lstrip_blocks': True,
            'autoescape': select_autoescape(enabled_extensions=('html', 'htm', 'xml', 'rss', 'atom')),
        }
    )

    site.env.assets_environment = AssetsEnvironment(
        directory=config['OUTPUT_DIR'],
        url='/',
        cache=webassets_cache
    )

    site.env.assets_environment.append_path(config['ASSETS_DIR'])

    for name, args, kwargs in config['ASSETS_BUNDLES']:
        site.env.assets_environment.register(name, *args, **kwargs)

    site.render(watch)


def clean(config: Dict) -> None:
    """Delete and recreate the output directory"""
    logger.info('Deleting and recreating "{OUTPUT_DIR}"...'.format(**config))

    if path.isdir(config['OUTPUT_DIR']):
        rmtree(config['OUTPUT_DIR'])

    makedirs(config['OUTPUT_DIR'], exist_ok=True)


def publish(config: Dict) -> None:
    """Build and publish the site (using `rsync` through SSH)"""
    logger.info('Overriding some configuration values from environment variables...')

    env = Env()

    config.update({
        'BASE_URL': env.str('BASE_URL'),
        'MINIFY_XML': env.bool('MINIFY_XML', config['MINIFY_XML']),
        'MINIFY_JSON': env.bool('MINIFY_JSON', config['MINIFY_JSON']),
        'SSH_USER': env.str('SSH_USER'),
        'SSH_HOST': env.str('SSH_HOST'),
        'SSH_PORT': env.int('SSH_PORT', default=22),
        'SSH_PATH': env.str('SSH_PATH'),
    })

    clean(config)
    build(config)

    exit(call(
        'rsync --delete --exclude ".DS_Store" -pthrvz -c '
        '-e "ssh -p {SSH_PORT}" '
        '{} {SSH_USER}@{SSH_HOST}:{SSH_PATH}'.format(
            config['OUTPUT_DIR'].rstrip('/') + '/', **config
        ),
        shell=True
    ))


def serve(config: Dict) -> None:
    """Serve the rendered site directory through HTTP"""
    with EnhancedThreadingHTTPServer(
            ('', config['SERVE_PORT']),
            SimpleEnhancedHTTPRequestHandler,
            directory=config['OUTPUT_DIR']
    ) as server:
        msg = 'Serving "{OUTPUT_DIR}" on http://localhost:{SERVE_PORT}/'.format(**config)

        if server.has_dualstack_ipv6:
            msg += ' and http://[::1]:{SERVE_PORT}/'.format(**config)

        logger.info(msg)

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
