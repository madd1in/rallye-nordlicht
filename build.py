#!/usr/bin/env python3
"""Wraps src/game.html (Artifact-Format, ohne Dokument-Geruest) zu index.html."""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(HERE, 'src', 'game.html'), encoding='utf-8').read()

cut = src.index('</style>') + len('</style>')
head, body = src[:cut], src[cut:]

doc = (
    '<!DOCTYPE html>\n'
    '<html lang="de">\n'
    '<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '<meta name="description" content="Rallye Nordlicht - Arcade-Rallye im Browser: drei Wertungspruefungen, Drift-Physik, Beifahrer-Ansagen.">\n'
    '<meta name="theme-color" content="#070910">\n'
    '<link rel="icon" href="data:image/svg+xml,'
    "%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2032'%3E"
    "%3Ctext%20y='26'%20font-size='26'%3E%F0%9F%8F%81%3C/text%3E%3C/svg%3E\">\n"
    + head.strip() + '\n'
    '</head>\n'
    '<body>\n'
    + body.strip() + '\n'
    '</body>\n'
    '</html>\n'
)

with io.open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(doc)
print('index.html geschrieben: %d Zeichen' % len(doc))
