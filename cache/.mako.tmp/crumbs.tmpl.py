# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1588547036.2203646
_enable_loop = True
_template_filename = 'themes/hamelin/templates/crumbs.tmpl'
_template_uri = 'crumbs.tmpl'
_source_encoding = 'utf-8'
_exports = ['bar']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        breadcrumb_separator = context.get('breadcrumb_separator', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if crumbs:
            __M_writer('<div class="site-breadcrumbs">\r\n')
            for idx, [link, text] in enumerate(crumbs):
                if not idx:
                    if link == '#':
                        __M_writer('                ')
                        __M_writer(str(text.rsplit('.html', 1)[0]))
                        __M_writer('\r\n')
                    else:
                        __M_writer('                <a href="')
                        __M_writer(str(link))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\r\n')
                else:
                    if breadcrumb_separator:
                        if link == '#':
                            __M_writer('                     &nbsp;')
                            __M_writer(str(breadcrumb_separator))
                            __M_writer('&nbsp;')
                            __M_writer(str(text.rsplit('.html', 1)[0]))
                            __M_writer('\r\n')
                        else:
                            __M_writer('                     &nbsp;')
                            __M_writer(str(breadcrumb_separator))
                            __M_writer('&nbsp;<a href="')
                            __M_writer(str(link))
                            __M_writer('">')
                            __M_writer(str(text))
                            __M_writer('</a>\r\n')
                    else:
                        if link == '#':
                            __M_writer('                     &nbsp;&gt;&nbsp;')
                            __M_writer(str(text.rsplit('.html', 1)[0]))
                            __M_writer('\r\n')
                        else:
                            __M_writer('                     &nbsp;&gt;&nbsp;<a href="')
                            __M_writer(str(link))
                            __M_writer('">')
                            __M_writer(str(text))
                            __M_writer('</a>\r\n')
            __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hamelin/templates/crumbs.tmpl", "uri": "crumbs.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "27": 3, "33": 3, "34": 4, "35": 5, "36": 6, "37": 7, "38": 8, "39": 9, "40": 9, "41": 9, "42": 10, "43": 11, "44": 11, "45": 11, "46": 11, "47": 11, "48": 13, "49": 14, "50": 15, "51": 16, "52": 16, "53": 16, "54": 16, "55": 16, "56": 17, "57": 18, "58": 18, "59": 18, "60": 18, "61": 18, "62": 18, "63": 18, "64": 20, "65": 21, "66": 22, "67": 22, "68": 22, "69": 23, "70": 24, "71": 24, "72": 24, "73": 24, "74": 24, "75": 29, "81": 75}}
__M_END_METADATA
"""
