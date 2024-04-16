"""This is root of package."""

from atsphinx.helper.decorators import emit_only
from bs4 import BeautifulSoup
from sphinx.application import Sphinx
from sphinx.jinja2glue import BuiltinTemplateLoader
from sphinx.util.docutils import nodes

__version__ = "0.2.1"


class WithHtmxTemplateLoader(BuiltinTemplateLoader):  # noqa: D101
    def render(self, template: str, context: dict) -> str:  # noqa: D102
        out = super().render(template, context)
        if not template.endswith(".html"):
            return out
        soup = BeautifulSoup(out, "lxml")
        preload = context.get("htmx_boost_preload", "")
        if preload:
            soup.body.attrs["hx-ext"] = "preload"
        for a in soup.find_all("a", {"class": "internal"}):
            a["hx-boost"] = "true"
            a["preload"] = preload
        return str(soup)


@emit_only(formats=["html"])
def setup_custom_loader(app: Sphinx):
    """Inject extra values about htmx-boost into generated config."""
    app.config.template_bridge = "atsphinx.htmx_boost.WithHtmxTemplateLoader"
    app.builder.init()
    app.builder.add_js_file("https://unpkg.com/htmx.org@1.9.10")
    if app.config.htmx_boost_preload:
        app.builder.add_js_file("https://unpkg.com/htmx.org@1.9.10/dist/ext/preload.js")


@emit_only(formats=["html"])
def pass_extra_context(  # noqa: D103
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict,
    doctree: nodes.document,
):
    if app.config.htmx_boost_preload:
        context["htmx_boost_preload"] = app.config.htmx_boost_preload


def setup(app: Sphinx):
    """Load as Sphinx-extension."""
    app.connect("builder-inited", setup_custom_loader)
    app.connect("html-page-context", pass_extra_context)
    app.add_config_value("htmx_boost_preload", "", "env", [str])
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
    }
