#!/usr/bin/env python3
from csv import DictReader
from pathlib import Path

THIS_DIR = Path(__file__).parent
p = THIS_DIR / 'input.csv'


entries = []
with p.open(newline='') as f:
    reader = DictReader(f)
    for row in reader:
        cls = row.pop('Class')
        number = row.pop('Number')
        name = row['Team Name']
        info = '\n'.join(f'<div class="info"><b>{k}:</b> {v}</div>' for k, v in row.items() if v)
        entries.append(
            f"""\
  <div class="entry">
    <h2>Class {cls}, No. {number} - {name}</h2>
    {info}
  </div>"""
        )

styles = """\
<style>
  html, body {
    margin: 0;
    padding: 0;
  }
  h2 {
    margin-bottom: 5px;
  }
  .entry {
    box-sizing: border-box;
    margin: 0 auto 20px;
    page-break-inside: avoid;
  }
  . info {
    margin-bottom: 10px;
  }
</style>
"""
all = '\n'.join(entries)
Path('out/output.html').write_text(f"""\
{styles}
{all}
"""
)
