"""Build the $10K Statement of Credit PDFs for the Ad Studio Hackathon.

Reads companies.csv (company, contact, qr, details) and writes to out/. qr is an
optional image file in this folder, printed top left on that company's page.
details is an optional URL, added as condition f.
  SOC-NYC-1027-blank.pdf     generic certificate with blank name and number lines
  SOC-NYC-1027-NN_<Company>.pdf   one per company, numbered in CSV order

Usage: python3 build_certificates.py
"""
import csv
import html
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PREFIX = "SOC-NYC-1027"


def render(cert_no, client_block, holder_name, stem, qr_block="", details_item=""):
    page = (HERE / "certificate_template.html").read_text()
    page = (page.replace("{{CERT_NO}}", cert_no)
                .replace("{{CLIENT_BLOCK}}", client_block)
                .replace("{{HOLDER_NAME}}", holder_name)
                .replace("{{QR_BLOCK}}", qr_block)
                .replace("{{DETAILS_ITEM}}", details_item))
    src = OUT / f"{stem}.html"
    src.write_text(page)
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={OUT / (stem + '.pdf')}", src.as_uri()],
        check=True, capture_output=True)
    src.unlink()
    return OUT / f"{stem}.pdf"


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "zaelot.svg").write_bytes((HERE / "zaelot.svg").read_bytes())

    made = [render(f"{PREFIX}-____",
                   '<div class="client"><span class="line"></span></div>',
                   "", f"{PREFIX}-blank")]

    with open(HERE / "companies.csv", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["company"].strip()]
    for n, row in enumerate(rows, 1):
        company = row["company"].strip()
        contact = (row.get("contact") or "").strip()
        cert_no = f"{PREFIX}-{n:02d}"
        safe = re.sub(r"[^A-Za-z0-9]+", "-", company).strip("-")
        qr = (row.get("qr") or "").strip()
        qr_block = ""
        if qr and not (HERE / qr).exists():
            print(f"  {company}: {qr} not found, built without QR")
        elif qr:
            (OUT / qr).write_bytes((HERE / qr).read_bytes())
            qr_block = f'<div class="qr"><img src="{html.escape(qr)}" alt=""></div>'
        details = (row.get("details") or "").strip()
        details_item = (f'<li>f. Additional details here: {html.escape(details)}</li>'
                        if details else "")
        made.append(render(cert_no,
                           f'<div class="client filled">{html.escape(company)}</div>',
                           html.escape(contact), f"{cert_no}_{safe}", qr_block,
                           details_item))

    for p in made:
        print(p.relative_to(HERE))


if __name__ == "__main__":
    main()
