# stdlib
from typing import Optional

# 3rd party
from domdf_python_tools.paths import PathPlus
from sphinx.application import Sphinx

# from sphinx_toolbox import latex


def replace_emoji(app: Sphinx, exception: Optional[Exception] = None):
	if exception:
		return

	if app.builder.name.lower() != "latex":
		return

	output_file = PathPlus(app.builder.outdir) / f"{app.builder.titles[0][1].lower()}.tex"

	output_content = output_file.read_text()
	output_content = output_content.replace('🐍', '')
	output_content = output_content.replace('📖', '')
	output_content = output_content.replace('\u2002', r'\enspace{}')
	output_content = output_content.replace('\u2003', r'\emspace{}')

	output_file.write_clean(output_content)


def setup(app: Sphinx):
	app.connect("build-finished", replace_emoji)
	# app.connect("build-finished", latex.replace_unknown_unicode)
