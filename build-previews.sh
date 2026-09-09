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
    # t1.md uses absolute /matcalc_docu/... image paths (DokuWiki scrape) which
    # would load the LIVE site's originals - repoint the T1 page at this build
    sed -i "s#/matcalc_docu/tutorials/t1/img/#/matcalc_docu/preview/$v/tutorials/t1/img/#g" \
      "$OUT/$v/tutorials/t1/index.html"
  fi
done

cp previews-landing.html "$OUT/index.html"

echo
echo "done.  (cd site && python -m http.server)  ->  http://localhost:8000/matcalc_docu/preview/"
