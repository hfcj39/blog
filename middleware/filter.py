from flask import Markup
from bleach import clean
from misaka import Markdown, HtmlRenderer


def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)


def safe_clean(text):
    tags = ['b', 'i', 'font', 'br', 'div', 'h2', 'blockquote', 'ul', 'li', 'a',
            'p', 'strong', 'span', 'h1', 'pre', 'code', 'img', 'h3', 'h4',
            'em', 'hr', 'ol', 'h5', 'table', 'colgroup', 'col', 'th', 'td',
            'tr', 'tbody', 'thead']
    attrs = {
        '*': ['style', 'id', 'class'],
        'font': ['color'],
        'a': ['href'],
        'img': ['src', 'alt']
    }
    styles = ['color']
    return clean(text, tags=tags, attributes=attrs, styles=styles)


def safe_markdown(text):
    renderer = HtmlRenderer()
    md = Markdown(renderer, extensions=('fenced-code',))
    return Markup(safe_clean(md(text)))
