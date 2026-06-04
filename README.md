# 🚀 E-Commerce Label Sorter

A Python-based warehouse automation tool that extracts SKUs from shipping-label PDFs and automatically reorganizes pages SKU-wise, reducing manual sorting effort and improving dispatch workflow efficiency for eCommerce operations.

---

## 📖 Overview

In many eCommerce warehouses, shipping labels are often received as large PDF files containing hundreds of pages. Manually sorting these labels by SKU is time-consuming, error-prone, and inefficient.

This project automates the entire process by:

* Extracting SKU information from shipping-label PDFs
* Grouping pages belonging to the same SKU
* Reorganizing labels SKU-wise
* Generating a clean, sorted output PDF ready for warehouse processing

The result is a faster and more reliable dispatch workflow.

---

## ✨ Key Features

### 📦 Intelligent SKU Extraction

Automatically identifies and extracts SKU values from shipping labels using custom regex patterns.

### 📄 PDF Processing Automation

Reads and processes multi-page PDF files efficiently.

### 🔄 SKU-Wise Page Reordering

Groups labels with identical SKUs together and rearranges pages automatically.

### ⚡ Batch Processing

Supports large shipping-label files commonly used in eCommerce fulfillment.

### 📊 Processing Logs

Provides detailed processing information and execution feedback.

### 🛠 Easy Configuration

Simple folder-based setup with minimal configuration required.

---

## 🏗 Problem Statement

Warehouse teams often receive shipping labels in random order.

Challenges include:

* Manual SKU sorting consumes significant time
* Increased risk of dispatch errors
* Reduced warehouse productivity
* Difficult handling of large label batches

This project was built to eliminate these bottlenecks through automation.

---

## 💡 Solution

The application scans each PDF page, extracts SKU information, groups matching SKUs together, and generates a newly sorted PDF file.

This enables warehouse staff to process orders faster with minimal manual intervention.

---

## 🛠 Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Core Development              |
| pdfplumber | PDF Text Extraction           |
| pypdf      | PDF Manipulation & Generation |
| Regex      | SKU Detection & Matching      |

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/E-commerce-Label-Sorter.git
cd E-commerce-Label-Sorter
```

### Install Dependencies

```bash
pip install pdfplumber pypdf
```

---

## ▶ Usage

Configure input and output folders:

```python
INPUT_FOLDER = r"C:\Labels\Input"
OUTPUT_FOLDER = r"C:\Labels\Output"
```

Place shipping-label PDFs inside the input folder.

Run:

```bash
python sku_sorter.py
```

The application will automatically generate a sorted output PDF.

---

## 🔄 Workflow

1. Load PDF files from the input directory
2. Read pages individually
3. Extract text content
4. Detect SKU using regex matching
5. Group pages by SKU
6. Rearrange pages SKU-wise
7. Generate organized output PDF
8. Display processing summary

---

## 📈 Business Impact

### Before Automation

* Manual SKU sorting
* Higher processing time
* Greater chance of human error

### After Automation

* Faster dispatch preparation
* Reduced manual effort
* Improved warehouse productivity
* Better operational consistency

---

## 🎯 Use Cases

* eCommerce Warehouses
* Logistics Operations
* Shipping Label Management
* Bulk Order Fulfillment
* Dispatch Automation

---

## 📸 Screenshots

Add screenshots here:

### Input PDF

![Input Screenshot](screenshots/input.png)

### Processing Output

![Processing Screenshot](screenshots/process.png)

### Sorted PDF Result

![Output Screenshot](screenshots/output.png)

---

## 🚀 Future Enhancements

* Desktop GUI Application
* Drag & Drop PDF Upload
* Barcode & QR Code SKU Detection
* CSV/Excel Reports
* Web Dashboard
* Multi-User Support
* Cloud Storage Integration

---

## 👨‍💻 Author

**Vedant Vijay**

Built as a real-world automation solution for eCommerce and warehouse operations, focusing on reducing manual effort and improving dispatch efficiency through Python automation.

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
