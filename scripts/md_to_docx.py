#!/usr/bin/env python3
"""Markdown → .docx with no dependencies. Headings, paragraphs, bullets, numbered lists, pipe tables, code blocks, bold/italic/code inline."""
import argparse, re, sys, zipfile, html, pathlib

NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'

def esc(t): return html.escape(t, quote=False)

def runs(text, mono=False):
    """Inline **bold**, *italic*, `code` → <w:r> elements."""
    out = []
    for tok in re.split(r"(\*\*.+?\*\*|\*.+?\*|`.+?`)", text):
        if not tok: continue
        props = []
        if tok.startswith("**") and tok.endswith("**"): tok = tok[2:-2]; props.append("<w:b/>")
        elif tok.startswith("`") and tok.endswith("`"): tok = tok[1:-1]; props.append('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>')
        elif tok.startswith("*") and tok.endswith("*"): tok = tok[1:-1]; props.append("<w:i/>")
        if mono: props.append('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="18"/>')
        rp = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
        out.append(f'<w:r>{rp}<w:t xml:space="preserve">{esc(tok)}</w:t></w:r>')
    return "".join(out)

def para(text, style=None, mono=False, numbered=False, bullet=False):
    pp = []
    if style: pp.append(f'<w:pStyle w:val="{style}"/>')
    if bullet: pp.append('<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>')
    if numbered: pp.append('<w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>')
    ppr = f"<w:pPr>{''.join(pp)}</w:pPr>" if pp else ""
    return f"<w:p>{ppr}{runs(text, mono)}</w:p>"

def table(rows):
    cells = lambda r, hdr: "".join(
        f'<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/></w:tcPr><w:p>{runs(("**" + c + "**") if hdr and c else c)}</w:p></w:tc>' for c in r)
    trs = "".join(f"<w:tr>{cells(r, i == 0)}</w:tr>" for i, r in enumerate(rows))
    borders = "".join(f'<w:{b} w:val="single" w:sz="4" w:space="0" w:color="999999"/>' for b in ("top", "left", "bottom", "right", "insideH", "insideV"))
    return f'<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/><w:tblBorders>{borders}</w:tblBorders></w:tblPr>{trs}</w:tbl>'

def convert(md, title=None):
    body = []
    if title: body.append(para(title, "Title"))
    lines = md.splitlines(); i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("```"):
            j = i + 1; block = []
            while j < len(lines) and not lines[j].startswith("```"): block.append(lines[j]); j += 1
            for b in block or [""]: body.append(para(b, mono=True))
            i = j + 1; continue
        if l.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            rows = []; j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                if not re.match(r"^\s*\|?\s*:?-{2,}", lines[j]):
                    rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1
            width = max(len(r) for r in rows)
            rows = [r + [""] * (width - len(r)) for r in rows]
            body.append(table(rows)); i = j; continue
        m = re.match(r"^(#{1,4})\s+(.*)", l)
        if m: body.append(para(m.group(2), f"Heading{len(m.group(1))}")); i += 1; continue
        if re.match(r"^\s*[-*]\s+", l): body.append(para(re.sub(r"^\s*[-*]\s+", "", l), bullet=True)); i += 1; continue
        if re.match(r"^\s*\d+[.)]\s+", l): body.append(para(re.sub(r"^\s*\d+[.)]\s+", "", l), numbered=True)); i += 1; continue
        if l.strip() in ("---", "***"): body.append(para("")); i += 1; continue
        if l.startswith(">"): body.append(para(l.lstrip("> "), "Quote")); i += 1; continue
        if not l.strip(): i += 1; continue
        # merge soft-wrapped paragraph lines
        j = i; buf = []
        while j < len(lines) and lines[j].strip() and not re.match(r"^(#{1,4}\s|\s*[-*]\s|\s*\d+[.)]\s|```|\||>)", lines[j]):
            buf.append(lines[j].strip()); j += 1
        body.append(para(" ".join(buf))); i = j
    return "".join(body)

STYLES = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles {NS}>
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:pPr><w:spacing w:after="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="40"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:pPr><w:keepNext/><w:spacing w:before="360" w:after="120"/></w:pPr><w:rPr><w:b/><w:sz w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:pPr><w:keepNext/><w:spacing w:before="280" w:after="100"/></w:pPr><w:rPr><w:b/><w:sz w:val="26"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:pPr><w:keepNext/><w:spacing w:before="200" w:after="80"/></w:pPr><w:rPr><w:b/><w:sz w:val="23"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading4"><w:name w:val="heading 4"/><w:rPr><w:b/><w:i/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Quote"><w:name w:val="Quote"/><w:pPr><w:ind w:left="567"/></w:pPr><w:rPr><w:i/><w:color w:val="555555"/></w:rPr></w:style>
</w:styles>'''

NUMBERING = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering {NS}>
<w:abstractNum w:abstractNumId="0"><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="567" w:hanging="283"/></w:pPr></w:lvl></w:abstractNum>
<w:abstractNum w:abstractNumId="1"><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%1."/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="567" w:hanging="283"/></w:pPr></w:lvl></w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num><w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num>
</w:numbering>'''

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>'''
RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''
DOC_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>'''

def write_docx(md_text, out_path, title=None):
    body = convert(md_text, title)
    doc = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {NS}><w:body>{body}<w:sectPr><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134"/></w:sectPr></w:body></w:document>'
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES); z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS); z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", STYLES); z.writestr("word/numbering.xml", NUMBERING)

def main(argv=None):
    ap = argparse.ArgumentParser(description="Convert a Markdown report to a clean .docx (no dependencies).")
    ap.add_argument("markdown"); ap.add_argument("-o", "--out"); ap.add_argument("--title")
    a = ap.parse_args(argv)
    src = pathlib.Path(a.markdown); out = pathlib.Path(a.out) if a.out else src.with_suffix(".docx")
    write_docx(src.read_text(encoding="utf-8"), out, a.title)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
