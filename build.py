#!/usr/bin/env python3
from csv import DictReader
from pathlib import Path


def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


p = Path('input.csv')

addresses = []
with p.open(newline='') as f:
    reader = DictReader(f)
    for row in reader:
        address = {k.lower().replace(' ', '_'): v for k, v in row.items()}
        addresses.append(
            """\
  <div class="address">
    <span>{title} {initial} {first_name} {surname}</span>
    <span>{address_1}</span>
    <span>{address_2}</span>
    <span>{address_3}</span>
    <span>{town}</span>
    <span>{post_code}</span>
  </div>""".format(**address)
        )

pages = []

for adr in chunk(addresses, 21):
    pages.append('<div class="page">\n{}\n</div>'.format('\n'.join(adr)))


styles = """\
<style>
  html, body {
    margin: 0;
    padding: 0;
  }
  .page {
    width: 210mm;
    height: 297mm;
    box-sizing: border-box;
    padding-top: 12mm;
    padding-bottom: 17mm;
    padding-left: 7mm;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(7, 1fr);
    page-break-after: always;
    border: 1px solid #ddd;
  }
  @media print
  {
    .page {
      border: none;
    }
  }
  .address {
    font-size: 0.9rem;
    margin: 0 5.5mm;
    padding-top: 6.5mm;
  }
  .address span {
    display: block;
  }
</style>
"""
all = '\n'.join(pages)
Path('out/output.html').write_text(f"""\
{styles}
{all}
"""
)
