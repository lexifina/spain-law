"""Shared reading of the BOE consolidated-legislation XML: one block version -> the lines of its file.

A block (`<bloque id tipo titulo>`) holds every version of one provision. Each `<version id_norma fecha_publicacion
fecha_vigencia>` is the provision's text from fecha_vigencia on, as written by the norm id_norma. A version's children
are paragraphs (`<p class>`), quoted or note blocks (`<blockquote>`) and tables (`<table>`).

The file of a block version is its paragraphs, one per line with a blank line between, so `git blame` names the norm
for each paragraph. Markup only, never words, is added: `## ` before headings (article, title, chapter ...), `> `
before publisher notes and quoted paragraphs, `| a | b |` for table rows (with a `| --- |` line after the first row;
a literal `|` in a cell is written `\\|`), and `![imagen](URL)` for images. Table captions are lines of their own,
where they stand. Whitespace runs collapse to one space and soft hyphens and zero-width marks are dropped.
"""
from __future__ import annotations

import datetime as dt
import re
import xml.etree.ElementTree as ET
from typing import List, Optional

BASE = "https://www.boe.es"
WS = re.compile(r"[\s­​﻿]+")
SOFT = re.compile(r"[­​﻿]")
HEADING = {"articulo", "titulo", "titulo_num", "titulo_tit", "capitulo", "capitulo_num", "capitulo_tit", "seccion",
           "subseccion", "libro", "libro_num", "libro_tit", "anexo", "anexo_num", "anexo_tit", "parte", "parte_num",
           "parte_tit", "centro_negrita"}
NOTE = {"nota_pie", "nota_pie_2", "textoCompleto"}
BLOCKY = {"p", "table", "blockquote", "div", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "dl", "dt", "dd"}
SEPARATE = BLOCKY | {"tr", "td", "th", "br", "img", "thead", "tbody", "tfoot", "caption"}
PIPE = "|"
ESCAPED_PIPE = "\\|"


def clean(s: str) -> str:
    """Words as one line: soft hyphens and zero-width marks removed, whitespace runs to one space."""
    return WS.sub(" ", SOFT.sub("", s)).strip()


def _walk(e: ET.Element):
    """The text of an element, with a space at every block-level boundary (cells, rows, paragraphs, breaks)."""
    if e.text:
        yield e.text
    for c in e:
        sep = " " if c.tag in SEPARATE else ""
        yield sep
        yield from _walk(c)
        yield sep
        if c.tail:
            yield c.tail


def text_of(e: ET.Element) -> str:
    return clean("".join(_walk(e)))


def images(e: ET.Element) -> List[str]:
    out = []
    for img in e.iter("img"):
        src = img.get("src") or ""
        if src.startswith("/"):
            src = BASE + src
        out.append(f"![imagen]({src})")
    return out


def table_lines(e: ET.Element) -> List[str]:
    rows: List[str] = []
    ncells = [0]

    def walk(t: ET.Element) -> None:
        for c in t:
            if c.tag == "caption":
                cap = text_of(c)
                if cap:
                    rows.append(cap)
            elif c.tag == "tr":
                cells = [text_of(td).replace(PIPE, ESCAPED_PIPE) for td in c if td.tag in ("td", "th")]
                rows.append("| " + " | ".join(cells) + " |")
                if not ncells[0]:
                    ncells[0] = max(1, len(cells))
                    rows.append("|" + " --- |" * ncells[0])
            elif c.tag in ("thead", "tbody", "tfoot"):
                walk(c)

    walk(e)
    return rows + images(e)


def lines_of(e: ET.Element, quoted: bool = False) -> List[str]:
    """The lines one child of a version gives, in order."""
    tag = e.tag
    pre = "> " if quoted else ""
    if tag == "table":
        return [pre + r for r in table_lines(e)]
    if tag == "blockquote":
        return container(e, True)
    if tag in ("div", "ul", "ol", "dl") and any(c.tag in BLOCKY for c in e):
        return container(e, quoted)
    out = []
    t = text_of(e)
    if t:
        cls = e.get("class") or ""
        if not quoted and cls in NOTE:
            out.append("> " + t)
        elif not quoted and cls in HEADING:
            out.append("## " + t)
        else:
            out.append(pre + t)
    out += [pre + i for i in images(e)]
    return out


def container(e: ET.Element, quoted: bool) -> List[str]:
    """A version, blockquote or div: block children give their own lines; text between them (the element's own
    text, inline children and tails) gives a line of its own where it stands."""
    pre = "> " if quoted else ""
    out: List[str] = []
    buf: List[str] = []
    imgs: List[str] = []

    def flush() -> None:
        t = clean("".join(buf))
        if t:
            out.append(pre + t)
        out.extend(pre + i for i in imgs)
        buf.clear()
        imgs.clear()

    if e.text:
        buf.append(e.text)
    for c in e:
        if c.tag in BLOCKY:
            flush()
            out.extend(lines_of(c, quoted))
        else:
            if c.tag == "br":
                buf.append(" ")
            buf.extend(_walk(c))
            imgs.extend(images(c))
        if c.tail:
            buf.append(c.tail)
    flush()
    return out


def render(version: ET.Element) -> str:
    """The file of one block version."""
    lines = container(version, False)
    out: List[str] = []
    prev_table = False
    for l in lines:
        is_table = l.lstrip("> ").startswith(PIPE)
        if out and not (is_table and prev_table):
            out.append("")
        out.append(l)
        prev_table = is_table
    return "\n".join(out) + "\n" if out else ""


MARKUP = {"##", ">", PIPE, "---"}


def words_of_file(text: str) -> List[str]:
    """The words of a block file with the added markup taken out (for the word-for-word check)."""
    out: List[str] = []
    for line in text.split("\n"):
        if line.lstrip("> ").startswith("![imagen]("):
            continue
        out += [w for w in line.replace(ESCAPED_PIPE, PIPE).split(" ") if w and w not in MARKUP]
    return out


def _alltext(e: ET.Element):
    """Independent of render(): every text node in document order, a space only at block-element boundaries."""
    if e.text:
        yield e.text
    for c in e:
        sep = " " if c.tag in SEPARATE else ""
        yield sep
        yield from _alltext(c)
        yield sep
        if c.tail:
            yield c.tail


def words_of_xml(version: ET.Element) -> List[str]:
    """Every word in a version's XML, read independently of render()."""
    return [w for w in clean("".join(_alltext(version))).split(" ") if w and w not in MARKUP]


def date(s: Optional[str]) -> str:
    """aaaammdd -> YYYY-MM-DD, or '' if absent or not a real date."""
    s = (s or "").strip()
    if not re.fullmatch(r"\d{8}", s):
        return ""
    try:
        dt.date(int(s[:4]), int(s[4:6]), int(s[6:]))
    except ValueError:
        return ""
    return f"{s[:4]}-{s[4:6]}-{s[6:]}"


def law_dir(rslug: str, ident: str) -> str:
    """estatal/<rango>/<year>/<BOE id>: the year (from the id) keeps folders under GitHub's 1,000-entry listing limit
    and keeps the trees fast-import rewrites on each commit small."""
    parts = ident.split("-")
    year = parts[2] if len(parts) > 2 and parts[2].isdigit() else "otros"
    return f"estatal/{rslug}/{year}/{ident}"
