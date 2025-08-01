from reportlab.pdfgen import canvas
from openpyxl import Workbook

def generate_low_stock_report_pdf(products):
    """Generate a PDF report for low-stock items."""
    c = canvas.Canvas("low_stock_report.pdf")
    c.drawString(100, 750, "Low Stock Report")
    y = 700
    for product in products:
        if product[2] < 10:  # Assuming quantity is at index 2
            c.drawString(100, y, f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}")
            y -= 20
    c.save()

def generate_sales_summary_excel(sales_data):
    """Generate an Excel sales summary."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Sales Summary"
    # reporting.py

from reportlab.pdfgen import canvas
from openpyxl import Workbook

def generate_low_stock_report_pdf(products):
    c = canvas.Canvas("low_stock_report.pdf")
    c.drawString(100, 750, "Low Stock Report")
    y = 700
    for product in products:
        if product[2] < 10:
            c.drawString(100, y, f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}")
            y -= 20
    c.save()

def generate_sales_summary_excel(sales_data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Sales Summary"

    headers = ["Product Name", "Quantity Sold", "Total Revenue"]
    ws.append(headers)

    for sale in sales_data:
        ws.append(sale)

    wb.save("sales_summary.xlsx")

    headers = ["Product Name", "Quantity Sold", "Total Revenue"]
    ws.append(headers)
    
    for sale in sales_data:
        ws.append(sale)
        
    wb.save("sales_summary.xlsx")