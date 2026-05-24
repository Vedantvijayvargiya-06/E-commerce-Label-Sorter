"""

SETUP (one-time):
    pip install pdfplumber pypdf

RUN:
    python sku_sorter.py
"""

# ══════════════════════════════════════════════════════════════
#  ✏️  CHANGE ONLY THESE TWO LINES
# ══════════════════════════════════════════════════════════════

INPUT_FOLDER  = r"C:\Users\YourName\Desktop\Labels\Input"   # folder with your PDFs
OUTPUT_FOLDER = r"C:\Users\YourName\Desktop\Labels\Output"  # sorted PDFs go here

# ══════════════════════════════════════════════════════════════
#  Everything below is automatic – no need to touch
# ══════════════════════════════════════════════════════════════

import re
import sys
import time
import logging
from collections import defaultdict
from pathlib import Path

try:
    import pdfplumber
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("\n[ERROR] Missing libraries.  Run this once:\n")
    print("    pip install pdfplumber pypdf\n")
    sys.exit(1)

# ── Logging ──────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── SKU extraction ────────────────────────────────────────────
# Matches the Product Details table header and grabs the SKU
# value that appears before "Free Size" on the next line.
# Works for: CE-WALL-526_AD, BL 23_DD, BKC Kitchen the home, etc.
_PRIMARY = re.compile(
    r"SKU\s+Size\s+Qty\s+Color\s+Order\s+No\.?\s*\n(.+?)\s+Free\s+Size",
    re.IGNORECASE | re.DOTALL,
)
_FALLBACK = re.compile(r"\bSKU\b\s*\n([^\n]+)", re.IGNORECASE)


def extract_sku(text: str) -> str:
    """Pull SKU from page text. Returns 'UNKNOWN_SKU' if not found."""
    # 1 — primary (most reliable)
    m = _PRIMARY.search(text)
    if m:
        return m.group(1).strip()

    # 2 — fallback: first non-header line after "SKU"
    m = _FALLBACK.search(text)
    if m:
        candidate = m.group(1).strip()
        if candidate and "Size" not in candidate and "Order" not in candidate:
            return candidate

    # 3 — last resort: scan line by line
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().upper().startswith("SKU"):
            for nxt in lines[i + 1:]:
                nxt = nxt.strip()
                if nxt and nxt not in ("Size", "Qty", "Color"):
                    parts, sku_parts = nxt.split(), []
                    for p in parts:
                        if re.search(r"[A-Za-z_\-]", p):
                            sku_parts.append(p)
                        else:
                            break
                    if sku_parts:
                        return " ".join(sku_parts)

    return "UNKNOWN_SKU"


# ── Core functions ────────────────────────────────────────────

def index_pages(pdf_path: Path) -> dict:
    """Read every page, return {sku: [page_indices]} in first-seen order."""
    sku_map   = defaultdict(list)
    seen_order = []

    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            sku = extract_sku(page.extract_text() or "")
            if sku not in sku_map:
                seen_order.append(sku)
            sku_map[sku].append(i)
            if (i + 1) % 50 == 0 or (i + 1) == total:
                log.info("    Scanned %d / %d pages", i + 1, total)

    return {sku: sku_map[sku] for sku in seen_order}


def build_sorted_pdf(input_path: Path, sku_index: dict, output_path: Path):
    """Write a new PDF with pages grouped by SKU."""
    reader = PdfReader(str(input_path))
    writer = PdfWriter()

    for sku, indices in sku_index.items():
        for idx in indices:
            writer.add_page(reader.pages[idx])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as fh:
        writer.write(fh)


def print_report(pdf_name: str, sku_index: dict, elapsed: float):
    total_pages = sum(len(v) for v in sku_index.values())
    print(f"\n{'─'*58}")
    print(f"  File : {pdf_name}")
    print(f"  Pages: {total_pages}   |   Unique SKUs: {len(sku_index)}   |   Time: {elapsed:.1f}s")
    print(f"{'─'*58}")
    print(f"  {'SKU':<38} {'Count':>6}")
    print(f"  {'─'*38}  {'─'*6}")
    for sku, pages in sorted(sku_index.items(), key=lambda kv: -len(kv[1])):
        print(f"  {sku:<38} {len(pages):>6}")
    print(f"{'─'*58}\n")


# ── Main ──────────────────────────────────────────────────────

def process_folder(input_folder: str, output_folder: str):
    inp = Path(input_folder)
    out = Path(output_folder)

    if not inp.exists():
        log.error("Input folder not found: %s", inp)
        sys.exit(1)

    pdf_files = sorted(inp.glob("*.pdf"))
    if not pdf_files:
        log.warning("No PDF files found in: %s", inp)
        return

    out.mkdir(parents=True, exist_ok=True)
    log.info("Found %d PDF file(s) in: %s", len(pdf_files), inp)

    for pdf_path in pdf_files:
        log.info("Processing: %s", pdf_path.name)
        t0 = time.perf_counter()

        try:
            sku_index   = index_pages(pdf_path)
            output_path = out / f"{pdf_path.stem}_sorted_by_sku.pdf"
            build_sorted_pdf(pdf_path, sku_index, output_path)
            elapsed = time.perf_counter() - t0
            print_report(pdf_path.name, sku_index, elapsed)
            log.info("Saved → %s", output_path.name)

        except Exception as e:
            log.error("Failed to process %s: %s", pdf_path.name, e)

    log.info("All done.  Output folder: %s", out)


if __name__ == "__main__":
    process_folder(INPUT_FOLDER, OUTPUT_FOLDER)