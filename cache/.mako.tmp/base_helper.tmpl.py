# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1588547036.2803707
_enable_loop = True
_template_filename = 'themes/hamelin/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_js', 'html_stylesheets', 'html_feedlinks', 'html_translations']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        description = context.get('description', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        striphtml = context.get('striphtml', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\r\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\r\n<!--[if lt IE 7]><html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->\r\n<!--[if (IE 7)&!(IEMobile)]><html class="no-js lt-ie9 lt-ie8" lang="en"><![endif]-->\r\n<!--[if (IE 8)&!(IEMobile)]><html class="no-js lt-ie9" lang="en"><![endif]-->\r\n<!--[if gt IE 8]><!--> <html class="no-js" lang="en"><!--<![endif]-->\r\n<head>\r\n    <meta charset="utf-8">\r\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\r\n')
        __M_writer('    <!-- http://t.co/dKP3o1e -->\r\n    <meta name="HandheldFriendly" content="True">\r\n    <meta name="MobileOptimized" content="320">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\r\n\r\n\r\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\r\n    <!-- Load Modernizr -->\r\n    <!--script src="//mmistakes.github.io/hpstr-jekyll-theme/assets/js/vendor/modernizr-2.6.2.custom.min.js"></script-->\r\n    <script src="/assets/js/modernizr-2.6.2.custom.min.js" type="text/javascript"></script>\r\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\r\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\r\n')
        __M_writer('\r\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\r\n')
        __M_writer('\r\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\r\n')
        __M_writer('\r\n')
        if prevlink:
            __M_writer('        <button><link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html"></button>\r\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\r\n')
        __M_writer('\r\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\r\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\r\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\r\n')
        __M_writer('\r\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\r\n    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="/assets/js/scripts.min.js"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if use_bundles:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\r\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/main.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/extra.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/w3.css" rel="stylesheet" type="text/css" >\r\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\r\n')
        __M_writer('\r\n    <!-- Webfonts -->\r\n    <link href="//fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic" rel="stylesheet" type="text/css">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_atom = context.get('generate_atom', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\r\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\r\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\r\n')
        if generate_atom:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\r\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <ul class="translations">\r\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\r\n')
        __M_writer('    </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hamelin/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 72, "23": 77, "24": 95, "25": 119, "26": 129, "32": 3, "59": 3, "60": 6, "61": 7, "62": 8, "63": 10, "64": 11, "65": 13, "66": 14, "67": 15, "68": 17, "69": 18, "70": 21, "71": 21, "72": 21, "73": 28, "74": 29, "75": 29, "76": 29, "77": 31, "78": 35, "79": 35, "80": 35, "81": 35, "82": 38, "83": 38, "84": 42, "85": 42, "86": 43, "87": 44, "88": 44, "89": 44, "90": 46, "91": 47, "92": 48, "93": 49, "94": 49, "95": 49, "96": 49, "97": 49, "98": 49, "99": 49, "100": 52, "101": 53, "102": 54, "103": 54, "104": 54, "105": 56, "106": 57, "107": 58, "108": 58, "109": 58, "110": 60, "111": 61, "112": 61, "113": 61, "114": 63, "115": 64, "116": 64, "117": 65, "118": 66, "119": 67, "120": 68, "121": 68, "122": 68, "123": 70, "124": 71, "125": 71, "131": 74, "135": 74, "141": 79, "147": 79, "148": 80, "149": 81, "150": 82, "151": 83, "152": 88, "153": 89, "154": 92, "160": 98, "170": 98, "171": 99, "172": 100, "173": 100, "174": 100, "175": 101, "176": 102, "177": 103, "178": 104, "179": 104, "180": 104, "181": 104, "182": 104, "183": 106, "184": 107, "185": 107, "186": 107, "187": 110, "188": 111, "189": 112, "190": 113, "191": 113, "192": 113, "193": 113, "194": 113, "195": 115, "196": 116, "197": 116, "198": 116, "204": 121, "213": 121, "214": 123, "215": 124, "216": 125, "217": 125, "218": 125, "219": 125, "220": 125, "221": 125, "222": 125, "223": 128, "229": 223}}
__M_END_METADATA
"""
