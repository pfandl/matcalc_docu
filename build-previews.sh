#!/usr/bin/env bash
# Build the four layout-comparison sites into ./site/<variant>/ and drop a
# landing page at ./site/index.html.
#
# Requirements:  pip install -r requirements.txt   (needs mkdocs-material)
# Deploy:        push the contents of ./site/ somewhere static - e.g. a
#                'previews' branch served by GitHub Pages, or `mkdocs serve`
#                one config at a time for a local screen-share.
set -euo pipefail
cd "$(dirname "$0")"

rm -rf site

for v in current handbook companion atlas; do
  echo "=== building: $v ==="
  mkdocs build --clean -f "mkdocs.$v.yml" -d "site/$v"
done

cp previews-landing.html site/index.html

echo
echo "done.  open:  site/index.html"
