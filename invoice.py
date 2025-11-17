# MINI INVOICE PRINTER PROGRAM
# This program prints a neatly formatted invoice using:
# .ljust() → left alignment
# .rjust() → right alignment
# .center() → center alignment
# These functions help us print text like a real printed bill.

# TOP BORDER
# Print a row of "=" to make the invoice look framed and clean
print('=' * 30)

# BASIC INVOICE DETAILS (like variables or input data)
Topic = "Invoice"              # Title or heading of the invoice
invoice_no = "INV-0007"        # Invoice number or bill ID
customer_name = "john doe"     # Customer name
items = "Cell Phone"           # Product or service name
Qty = 1                        # Quantity purchased
amount = 199.99                # Price or total amount

# PRINT THE TITLE (Invoice heading)
# .upper() turns text into uppercase
# .center(28) centers the text in a space of 28 characters
print(f"{Topic.upper()}".center(28))

# PRINT THE INVOICE NUMBER
# We right-align (rjust) the numeric part to keep formatting even
# .rjust(5, '0') → fills empty space with zeros from the left
# .center(31) → centers the whole line
print(f"Invoice No: INV-{str(invoice_no).rjust(5, '0')}".center(31))

# PRINT THE CUSTOMER NAME
# .title() capitalizes each word (e.g., 'john doe' → 'John Doe')
# .center(28) aligns it neatly in the middle
print(f"Customer: {customer_name.title()}".center(28))

# PRINT THE ITEM DETAILS (Product, Quantity, Price)
# .ljust(10) → left aligns the item name within 10 spaces
# .rjust(8) → right aligns the quantity
# .rjust(10) → right aligns the price for clean column layout
print(f"{items.ljust(10)} {str(Qty).rjust(8)} {str(amount).rjust(10)}")

# Example visual:
# Cell Phone           1     199.99
# (Left column → Item, middle → Qty, right → Price)

# PRINT THE TOTAL AMOUNT LINE
# .center(28) → makes the total amount line appear nicely centered
print(f"Amount: ${amount}".center(28))

# BOTTOM BORDER
# Same as the top — closes the visual box of the invoice
print('=' * 30)

# self class