#!/usr/bin/env bash
# Build the four layout-comparison sites and a landing page, mirroring the
# deployed layout under  site/matcalc_docu/preview/<variant>/ .
#
#   pip install -r requirements.txt        # needs mkdocs-material
#   ./build-previews.sh
#   (cd site && python -m http.server)     # then open:
#   http://localhost:8000/matcalc_docu/preview/
#
# The authoritative preview is the GitHub Pages deploy (.github/workflows/pages.yml);
# this script is for a quick local check.
set -euo pipefail
cd "$(dirname "$0")"

OUT="site/matcalc_docu/preview"
rm -rf site

for v in current handbook companion atlas; do
  echo "=== building: $v ==="
  mkdocs build --clean -f "mkdocs.$v.yml" -d "$OUT/$v"
  if [ -d "preview-assets/t1/$v" ]; then
    # overlay the Tutorial-1 screenshots recoloured for this direction
    # (regenerate with: python tools/gen-preview-images.py)
    cp preview-assets/t1/"$v"/*.png "$OUT/$v/tutorials/t1/img/"
  fi
  # the DokuWiki scrape left absolute /matcalc_docu/... links all through the
  # page content (cross-refs and images); without this they jump out to the
  # live site. keep them inside this preview.
  find "$OUT/$v" -name '*.html' -exec \
    sed -i "s#\([\"'( ]\)/matcalc_docu/#\1/matcalc_docu/preview/$v/#g" {} +
done

cp previews-landing.html "$OUT/index.html"

echo
echo "done.  (cd site && python -m http.server)  ->  http://localhost:8000/matcalc_docu/preview/"
