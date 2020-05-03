# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1588547036.136365
_enable_loop = True
_template_filename = 'themes/hamelin/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        header = _mako_get_namespace(context, 'header')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\r\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\r\n</head>\r\n<body id="post-index" class="feature">\r\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\r\n    ')
        __M_writer(str(header.html_header()))
        __M_writer('\r\n    <div class="w3-content" style="max-width:1400px">\r\n    \t<div class="w3-row">\r\n    \t\t<div class="w3-col l8 s12">\r\n\t\t\t    <div id="main" role="main">\r\n\t\t\t            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\t\t\t    </div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t\t<div class="w3-col l4">\r\n  \t\t\t<!-- About Card -->\r\n  \t\t\t\t<div class="w3-card w3-margin w3-margin-top">\r\n  \t\t\t\t<img src="./images/hamelin4.jpg" style="width:100%">\r\n    \t\t\t\t<div class="w3-container w3-white">\r\n      \t\t\t\t\t<h4><b>My Name</b></h4>\r\n      \t\t\t\t\t\t<p>Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. </p>\r\n    \t\t\t\t</div>\r\n  \t\t\t\t</div><hr>\r\n\r\n\r\n  \t\t\t\t\t<div class="w3-card w3-margin w3-margin-top">\r\n  \t\t\t\t\t\t<div class="w3-container w3-white">\r\n  \t\t\t\t\t\t\t<p>Colocar Aquí otros elementos HTML</p><br>\r\n  \t\t\t\t\t\t</div>\r\n  \t\t\t\t\t</div>\r\n\r\n\r\n  \t\t\t</div>\r\n\r\n\t</div>\r\n    \r\n    ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\r\n    ')
        __M_writer(str(body_end))
        __M_writer('\r\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\r\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hamelin/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 0, "53": 2, "54": 3, "55": 4, "56": 5, "57": 5, "58": 6, "59": 6, "64": 9, "65": 10, "66": 10, "67": 13, "68": 13, "69": 14, "70": 14, "75": 19, "76": 45, "77": 45, "78": 46, "79": 46, "80": 47, "81": 47, "82": 48, "83": 48, "89": 7, "99": 7, "105": 19, "120": 105}}
__M_END_METADATA
"""
