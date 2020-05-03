# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1588547036.0733538
_enable_loop = True
_template_filename = 'themes/hamelin/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content', 'extra_head', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        image_plugin = _import_ns.get('image_plugin', context.get('image_plugin', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        image_plugin = _import_ns.get('image_plugin', context.get('image_plugin', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n<div class="site-gallery site-card mdl-grid">\r\n    <div class="mdl-cell mdl-cell--12-col">\r\n        ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\r\n    </div>\r\n    <div class="mdl-card mdl-cell mdl-cell--12-col mdl-shadow--4dp">\r\n        <div class="mdl-card__media"></div>\r\n')
        if title:
            __M_writer('        <div class="mdl-card__title">\r\n            <h1 class="mdl-card__title-text">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\r\n        </div>\r\n')
        __M_writer('        <div class="mdl-grid mdl-card__supporting-text">\r\n            <div class="mdl-cell mdl-cell--12-col">\r\n')
        if post:
            __M_writer('                ')
            __M_writer(str(post.text()))
            __M_writer('\r\n')
        __M_writer('            </div>\r\n            <div class="mdl-cell mdl-cell--12-col">\r\n')
        if folders:
            __M_writer('                <ul class="mdl-list">\r\n')
            for folder, ftitle in folders:
                __M_writer('                    <li class="mdl-list__item">\r\n                        <span class="mdl-list__item-primary-content">\r\n                            <i class="material-icons mdl-list__item-icon">Abrir galería</i>\r\n                            <a href="')
                __M_writer(str(folder))
                __M_writer('">')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a>\r\n                        </span>\r\n                    </li>\r\n')
            __M_writer('                </ul>\r\n')
        __M_writer('            </div>\r\n        </div>\r\n')
        if photo_array:
            __M_writer('        <div class="mdl-grid mdl-card__supporting-text image-gallery">\r\n')
            for image in photo_array:
                __M_writer('                <div class="mdl-card mdl-cell mdl-cell--3-col mdl-shadow--2dp gallery-cell">\r\n                    <div class="mdl-card__media mdl-color--white">\r\n')
                if image_plugin and image_plugin == 'lightbox':
                    __M_writer('                        <a href="')
                    __M_writer(str(image['url']))
                    __M_writer('" data-lightbox="image-gallery"\r\n                           data-title="')
                    __M_writer(str(image['title']))
                    __M_writer('"\r\n                           class="thumbnail image-reference"\r\n                           title="')
                    __M_writer(str(image['title']))
                    __M_writer('">\r\n                            <img src="')
                    __M_writer(str(image['url_thumb']))
                    __M_writer('" alt="')
                    __M_writer(filters.html_escape(str(image['title'])))
                    __M_writer('" />\r\n                        </a>\r\n')
                else:
                    __M_writer('                        <a href="')
                    __M_writer(str(image['url']))
                    __M_writer('" class="thumbnail image-reference" title="')
                    __M_writer(str(image['title']))
                    __M_writer('">\r\n                            <img src="')
                    __M_writer(str(image['url_thumb']))
                    __M_writer('" alt="')
                    __M_writer(filters.html_escape(str(image['title'])))
                    __M_writer('" />\r\n                        </a>\r\n')
                __M_writer('                    </div>\r\n                    <div class="mdl-card__actions mdl-card--border">\r\n                      <a class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--colored mdl-button--accent" title="')
                __M_writer(str(image['title']))
                __M_writer('" href="')
                __M_writer(str(image['url']))
                __M_writer('">')
                __M_writer(str(image['title']))
                __M_writer('</a>\r\n                    </div>\r\n                </div>\r\n')
            __M_writer('        </div>\r\n')
        if site_has_comments and enable_comments:
            __M_writer('        <div class="mdl-color-text--primary-contrast mdl-card__supporting-text comments hidden-print">\r\n            ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\r\n        </div>\r\n')
        __M_writer('    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_js():
            return render_extra_js(context)
        image_plugin = _import_ns.get('image_plugin', context.get('image_plugin', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if image_plugin and image_plugin == 'colorbox':
            __M_writer('<script>\r\n$("a.thumbnail").colorbox({rel:"gal", maxWidth:"100%",maxHeight:"100%",scalePhotos:true});\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hamelin/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "32": 0, "59": 2, "60": 3, "61": 4, "66": 5, "71": 72, "76": 77, "86": 5, "99": 7, "118": 7, "119": 10, "120": 10, "121": 14, "122": 15, "123": 16, "124": 16, "125": 19, "126": 21, "127": 22, "128": 22, "129": 22, "130": 24, "131": 26, "132": 27, "133": 28, "134": 29, "135": 32, "136": 32, "137": 32, "138": 32, "139": 36, "140": 38, "141": 40, "142": 41, "143": 42, "144": 43, "145": 45, "146": 46, "147": 46, "148": 46, "149": 47, "150": 47, "151": 49, "152": 49, "153": 50, "154": 50, "155": 50, "156": 50, "157": 52, "158": 53, "159": 53, "160": 53, "161": 53, "162": 53, "163": 54, "164": 54, "165": 54, "166": 54, "167": 57, "168": 59, "169": 59, "170": 59, "171": 59, "172": 59, "173": 59, "174": 63, "175": 65, "176": 66, "177": 67, "178": 67, "179": 70, "185": 74, "194": 74, "195": 75, "196": 75, "202": 79, "211": 79, "212": 80, "213": 81, "219": 213}}
__M_END_METADATA
"""
