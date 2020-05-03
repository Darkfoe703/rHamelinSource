# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1588547036.3293724
_enable_loop = True
_template_filename = 'themes/hamelin/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_navigation_links', 'html_translation_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_site_title():
            __M_caller = context.caller_stack._push_frame()
            try:
                _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
                blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
                lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
                title = _import_ns.get('title', context.get('title', UNDEFINED))
                abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
                __M_writer = context.writer()
                __M_writer('\r\n            <div class="header-title">\r\n                <div class="header-title-wrap">\r\n                    <h1 id="brand"><a href="')
                __M_writer(str(abs_link(_link("root", None, lang))))
                __M_writer('" title="')
                __M_writer(str(blog_title))
                __M_writer('" rel="home">\r\n                    ')
                __M_writer(str(blog_title))
                __M_writer('</a></h1>\r\n                     <h2>')
                __M_writer(str(title))
                __M_writer('</h2>\r\n                </div><!-- /.header-title-wrap -->\r\n            </div><!-- /.header-title -->\r\n        ')
                return ''
            finally:
                context.caller_stack._pop_frame()
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(str(html_navigation_links()))
        __M_writer('\r\n<div class="entry-header">\r\n<!-- FIXME: get credit from settings -->\r\n  <!--div class="image-credit">Image source: <a href="http://www.dargadgetz.com/ios-7-abstract-wallpaper-pack-for-iphone-5-and-ipod-touch-retina/">dargadgetz</a></div--><!-- /.image-credit -->\r\n    <div class="entry-image">\r\n      <img src="./images/bg2.jpg" alt="Latest Posts">\r\n        ')
        __M_writer('\r\n    </div><!-- /.entry-image -->\r\n      ')
        __M_writer(str(html_site_title()))
        __M_writer('\r\n</div><!-- /.entry-header -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n    <nav id="dl-menu" class="dl-menuwrapper" role="navigation">\r\n    <button class="dl-trigger">Open Menu</button>\r\n    <ul class="dl-menu">\r\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li>\r\n                <a href="#">')
                __M_writer(str(text))
                __M_writer('</a>\r\n                <ul class="dl-submenu">\r\n')
                for suburl, text in url:
                    __M_writer('                    <li><a href="')
                    __M_writer(str(suburl))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\r\n')
                __M_writer('                </ul>\r\n')
            else:
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a></li>\r\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\r\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\r\n    </ul>\r\n    </nav>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\r\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\r\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hamelin/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 23, "35": 48, "36": 57, "42": 4, "58": 11, "59": 14, "60": 14, "61": 14, "62": 14, "63": 15, "64": 15, "65": 16, "66": 16, "71": 4, "72": 5, "73": 5, "74": 19, "75": 21, "76": 21, "82": 27, "93": 27, "94": 31, "95": 32, "96": 33, "97": 34, "98": 34, "99": 36, "100": 37, "101": 37, "102": 37, "103": 37, "104": 37, "105": 39, "106": 40, "107": 41, "108": 41, "109": 41, "110": 41, "111": 41, "112": 44, "113": 44, "114": 44, "115": 45, "116": 45, "122": 50, "132": 50, "133": 51, "134": 52, "135": 53, "136": 53, "137": 54, "138": 54, "144": 138}}
__M_END_METADATA
"""
