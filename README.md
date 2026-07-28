# Gulf Electronics - Odoo Job Card Module

A custom **Odoo QWeb PDF Report** module designed for electronics repair shops and service centers. It generates a clean, professional, two-section **Job Card** printable report optimized for standard A4 paper.

---

## 📑 Features

* **Custom Printable Job Card (PDF)**: Clean black-and-white grid structure formatted with custom CSS.
* **Customer & Device Tracking**:
  * Job No., Serial No., Date, and Received By details.
  * Customer contact information and job specifics (Model No., Complain, Condition, Accessories).
* **Parts & Service Breakdown**:
  * Itemized table for Part Descriptions, Quantities, Unit Prices, and Amounts.
  * Dedicated rows for **Home Visit Charges**, **Service Charges**, and **Total Amount**.
  * Flexible layout that expands gracefully whether parts are added or left blank for manual notes.
* **Terms & Conditions Section**:
  * Integrated general service and repair terms.
  * Specialized Panel Repair agreement banner and conditions.

---

## 🛠️ Requirements & Tech Stack

* **Odoo**: 14.0 / 15.0 / 16.0 / 17.0+
* **Engine**: QWeb (wkhtmltopdf)
* **Language**: XML, Python, HTML/CSS

---

## 🚀 Installation

1. Clone or download this repository into your custom Odoo addons directory:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/gulf_electronics.command](https://github.com/YOUR-USERNAME/gulf_electronics.command)
