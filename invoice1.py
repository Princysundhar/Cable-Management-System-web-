from fpdf import FPDF
from datetime import datetime


def generate_invoice_pdff(invoice_number, customer_name, items, filename,data):
    # Calculate total
    # total = sum(item['price'] * item['quantity'] for item in items)

    # Current date
    date = datetime.now()

    # Create instance of FPDF class
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="INVOICE", ln=True, align="C")
    pdf.cell(200, 10, ln=True)  # Empty line
    for i in data:
    # Invoice details
        pdf.cell(200, 10, txt=f"Invoice Number: {invoice_number}", ln=True, align="L")
        pdf.cell(200, 10, txt=f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="L")
        pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True, align="L")
        pdf.cell(200, 10, ln=True, align="L")
        # pdf.cell(200, 10, txt="Items:", ln=True, align="L")


        print(items)
        # Items

        pdf.cell(400, 20,
                 txt=f"PACKAGE NAME\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAMOUNT\t\t\t\t\t\t\t\t\t\t\t\tDURATION",
                 ln=True, align="L")

        for item in items:
            pdf.cell(200, 10,
                     txt=f"{item['name']}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{item['amount']}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{item['Duration']}",
                     ln=True, align="L")

    # Total
    # pdf.cell(200, 10, txt=f"Total: ${total}", ln=True, align="L")

    # Save the PDF to file

    pdf.output(r"C:\Users\rithi\OneDrive\Desktop\New folder (3)\COM_SYSTEM\COM_SYSTEM\App\static\pdf\\" + filename)

# Example data
# invoice_number = "INVOICE"
# customer_name = "John Doe"
# items = [
#     {"name": "Product A", "quantity": 2, "price": 10},
#     {"name": "Product B", "quantity": 1, "price": 20},
#     {"name": "Product C", "quantity": 3, "price": 15}
# ]
#
# # Generate the invoice PDF
# generate_invoice_pdf(invoice_number, customer_name, items, "invoice.pdf")
