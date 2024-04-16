from htmlmin import minify as minify_xml
from os import makedirs, path
from staticjinja import Site
from jinja2 import Template
from jsmin import jsmin


def minify_xml_template(site: Site, template: Template, **kwargs) -> None:
    """Minify XML output (HTML/RSS/Atom) from a rendered Jinja template"""
    out = path.join(site.outpath, template.name)

    makedirs(path.dirname(out), exist_ok=True)

    with open(out, 'w', encoding=site.encoding) as f:
        f.write(
            minify_xml(
                site.get_template(template.name).render(**kwargs),
                remove_optional_attribute_quotes=False,
                remove_empty_space=True,
                remove_comments=True
            )
        )


def minify_json_template(site: Site, template: Template, **kwargs) -> None:
    """Minify JSON output from a rendered Jinja template"""
    out = path.join(site.outpath, template.name)

    makedirs(path.dirname(out), exist_ok=True)

    with open(out, 'w', encoding=site.encoding) as f:
        f.write(
            jsmin(
                site.get_template(template.name).render(**kwargs)
            )
        )
