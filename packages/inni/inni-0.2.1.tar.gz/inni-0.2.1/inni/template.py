from jinja2 import Environment, FunctionLoader, meta

ENV = Environment(loader=FunctionLoader(lambda i: i))


def template_to_vars(source: str) -> set[str]:
    """
    Returns the variables present in the template
    """
    return meta.find_undeclared_variables(ENV.parse(source))


def render_template(source: str, **kwargs):
    template = ENV.get_template(source)
    return template.render(**kwargs)
