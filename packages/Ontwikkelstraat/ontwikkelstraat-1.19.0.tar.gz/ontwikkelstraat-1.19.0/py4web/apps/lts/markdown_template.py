import os
from pathlib import Path

import yatl
from markdown2 import markdown
from yatl import XML

from py4web.core import Template, request

# from .handlebars import Handlebars
# class MarkdownTemplate(Template):
#     def __init__(self, filename, template=None, folder=None, extras: list = None):
#         self.filename = filename
#         self.templates_path = Path(folder or Handlebars.templates_foldername())
#
#         if template is None:
#             self.template = self.templates_path / "layouts/generic.hbs"
#         else:
#             self.template = template
#         if extras is None:
#             self.extras = ["fenced-code-blocks"]
#         else:
#             self.extras = extras
#
#         self.hbs = Handlebars(filename=self.template)
#
#     def transform(self, output, shared_data=None):
#         html = self.load_from_md(self.filename)
#         if not self.template:
#             return html
#         else:
#             return self.hbs.transform(
#                 {
#                     "content": html,
#                     **output,
#                 }
#             )
#
#     def load_from_md(self, filename):
#         mdfile = self.templates_path / filename
#         with mdfile.open(encoding="utf-8") as f:
#             return markdown(f.read(), extras=self.extras)
#
#     def on_success(self, context):
#         context["output"] = self.transform(context["output"], context)


class MarkdownTemplate(Template):
    def __init__(self, filename, template=None, folder=None, extras: list = None):
        self.filename = filename
        self.template = template
        self.folder = folder

        if extras is None:
            self.extras = ["fenced-code-blocks"]
        else:
            self.extras = extras

    def _templates_folder(self):
        # from super().on_success:
        app_folder = os.path.join(os.environ["PY4WEB_APPS_FOLDER"], request.app_name)
        return os.path.join(app_folder, "templates")

    def _setup_template_folder(self):
        self.templates_path = Path(self.folder or self._templates_folder())

        if self.template is None:
            self.template = self.templates_path / "layouts/markdown.html"
        else:
            self.template = self.template

    def transform(self, output, shared_data=None):
        self._setup_template_folder()

        html = self.load_from_md(self.filename)
        if not self.template:
            return html
        else:
            return yatl.render(
                filename=self.template,
                context={
                    "content": XML(html),
                    **output,
                },
                delimiters="[[ ]]",
            )

    def load_from_md(self, filename):
        mdfile = self.templates_path / filename
        with mdfile.open(encoding="utf-8") as f:
            return markdown(f.read(), extras=self.extras)

    def on_success(self, context):
        context["output"] = self.transform(context["output"], context)
