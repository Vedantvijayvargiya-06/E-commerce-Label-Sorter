# E-commerce-Label-Sorter
🚀 Built a Python-based SKU Label Sorter that automatically extracts SKUs from shipping-label PDFs and reorganizes pages SKU-wise for faster warehouse processing. Uses pdfplumber, pypdf, and regex automation to reduce manual sorting effort and improve eCommerce dispatch workflow efficiency. 📦⚡
# 📦 SKU Label Sorter

An automated Python tool that extracts SKUs from shipping-label PDFs and rearranges pages SKU-wise for faster and more efficient warehouse processing. Designed for eCommerce businesses handling bulk shipping labels, this project helps reduce manual sorting effort and improves dispatch workflow efficiency.

## 🚀 Features

* Automatic SKU extraction from PDF labels
* Smart regex-based SKU detection
* Bulk PDF processing support
* SKU-wise page grouping and sorting
* Generates organized output PDFs automatically
* Detailed logs and processing reports
* Beginner-friendly configuration setup

## 🛠️ Tech Stack

* Python
* pdfplumber
* pypdf
* Regex Pattern Matching

## ⚙️ Installation

```bash
pip install pdfplumber pypdf
```

## ▶️ Usage

1. Update input and output folder paths inside the script.

```python
INPUT_FOLDER  = r"C:\Labels\Input"
OUTPUT_FOLDER = r"C:\Labels\Output"
```

2. Add shipping-label PDFs to the input folder.

3. Run the script:

```bash
python sku_sorter.py
```

## 📄 Workflow

* Reads all PDF files from the input folder
* Extracts text page-by-page
* Detects SKU using custom extraction logic
* Groups pages with identical SKUs
* Rearranges pages SKU-wise
* Generates a sorted output PDF automatically

## 💡 Use Cases

* eCommerce warehouse management
* Shipping-label organization
* Logistics automation
* Bulk order processing
* Dispatch workflow optimization

## 🔥 Benefits

* Saves manual sorting time
* Improves warehouse efficiency
* Reduces operational errors
* Handles large PDF batches easily

## 📌 Future Improvements

* GUI/Desktop Application
* Drag & Drop PDF Upload
* Barcode-based SKU extraction
* CSV Export Reports

## 👨‍💻 Author

Built as a practical automation solution for real-world eCommerce and warehouse operations.
