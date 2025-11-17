import tkinter as tk  # Import Tkinter library to create GUI applications

# FUNCTION TO PERFORM CALCULATIONS
def calculate(operation):
    """
    This function reads the two numbers from input fields, 
    performs the selected arithmetic operation (+, -, *, /), 
    displays the result in the GUI, and logs it into the history list.
    """
    try:
        # Step 1: Get numbers from user input
        # Convert to float to handle decimal numbers
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Step 2: Perform the chosen operation
        if operation == "+":        # Addition
            result = num1 + num2
        elif operation == "-":      # Subtraction
            result = num1 - num2
        elif operation == "*":      # Multiplication
            result = num1 * num2
        elif operation == "/":      # Division
            if num2 == 0:          # Prevent division by zero
                raise ZeroDivisionError
            result = num1 / num2

        # Step 3: Create a readable string to show result
        result_text = f"{num1} {operation} {num2} = {result}"

        # Step 4: Display result in the result label (instead of popup)
        result_label.config(text=result_text)

        # Step 5: Add calculation to history list (bottom of listbox)
        history_list.insert(tk.END, result_text)

    # Error Handling
    except ZeroDivisionError:
        # Show friendly error if user divides by zero
        result_label.config(text="Error: Cannot divide by zero!")
    except ValueError:
        # Show error if input is not a number
        result_label.config(text="Error: Please enter valid numbers!")
    except Exception as e:
        # Catch all other unexpected errors
        result_label.config(text=f"Unexpected error: {e}")

# FUNCTION TO CLEAR INPUTS AND RESULT
def clear_inputs():
    """
    Clears both input fields and resets the result display.
    Allows user to start a completely fresh calculation.
    """
    entry_num1.delete(0, tk.END)  # Clear first number input field
    entry_num2.delete(0, tk.END)  # Clear second number input field
    result_label.config(text="Result will appear here")  # Reset result label

# FUNCTION TO CLEAR HISTORY
def clear_history():
    """
    Clears all past calculations from the history panel.
    """
    history_list.delete(0, tk.END)  # Remove all items from listbox

# BUILDING THE MAIN WINDOW
window = tk.Tk()  # Create the main window for the calculator
window.title("Enhanced Calculator with History")  # Set window title
window.geometry("450x500")  # Set fixed size (width x height)
window.resizable(False, False)  # Disable resizing to maintain layout consistency

# Title Label
title_label = tk.Label(
    window, 
    text="FULL CALCULATOR",          # Title text
    font=("Arial", 18, "bold"),      # Font style and size
    fg="darkblue"                    # Text color
)
title_label.pack(pady=10)            # Add vertical spacing (padding) above/below


# -------------------------
# Input Fields Section
# -------------------------
# First number input
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.pack()                       # Place the label in the window
entry_num1 = tk.Entry(window, width=30) # Input field for first number
entry_num1.pack(pady=5)                 # Add spacing below input field

# Second number input
label_num2 = tk.Label(window, text="Enter second number:")
label_num2.pack()                       # Place the label in the window
entry_num2 = tk.Entry(window, width=30) # Input field for second number
entry_num2.pack(pady=5)                 # Add spacing below input field

# Operation Buttons (+, -, *, /)
button_frame = tk.Frame(window)       # Frame to hold operation buttons neatly
button_frame.pack(pady=15)            # Add spacing around frame

# Addition button
btn_add = tk.Button(
    button_frame, 
    text="+", 
    width=5, 
    font=("Arial", 14), 
    command=lambda: calculate("+")    # Calls calculate() with "+"
)
btn_add.grid(row=0, column=0, padx=5) # Position in grid, add horizontal padding

# Subtraction button
btn_sub = tk.Button(
    button_frame, 
    text="-", 
    width=5, 
    font=("Arial", 14), 
    command=lambda: calculate("-")
)
btn_sub.grid(row=0, column=1, padx=5)

# Multiplication button
btn_mul = tk.Button(
    button_frame, 
    text="×", 
    width=5, 
    font=("Arial", 14), 
    command=lambda: calculate("*")
)
btn_mul.grid(row=0, column=2, padx=5)

# Division button
btn_div = tk.Button(
    button_frame, 
    text="÷", 
    width=5, 
    font=("Arial", 14), 
    command=lambda: calculate("/")
)
btn_div.grid(row=0, column=3, padx=5)

# Result Display Label
result_label = tk.Label(
    window, 
    text="Result will appear here",  # Default placeholder text
    font=("Arial", 14),              # Font for result
    fg="green"                       # Green text indicates a successful calculation
)
result_label.pack(pady=10)           # Add spacing around result

# History Panel (Listbox + Scrollbar)
history_label = tk.Label(
    window, 
    text="Calculation History:", 
    font=("Arial", 12, "bold")       # Bold font for history section title
)
history_label.pack(pady=5)           # Add spacing above/below

history_frame = tk.Frame(window)     # Frame to hold listbox and scrollbar
history_frame.pack(pady=5)

# Vertical scrollbar for history
scrollbar = tk.Scrollbar(history_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Place scrollbar on the right, fill vertically

# Listbox to display all past calculations
history_list = tk.Listbox(
    history_frame, 
    width=50, 
    height=12, 
    yscrollcommand=scrollbar.set,   # Connect listbox to scrollbar
    bg="#f0f0f0"                  # Light gray background for readability
)
history_list.pack(side=tk.LEFT, fill=tk.BOTH) # Fill remaining space beside scrollbar

scrollbar.config(command=history_list.yview)  # Ensure scrollbar moves the listbox

# Clear Buttons Section
clear_btn_frame = tk.Frame(window)
clear_btn_frame.pack(pady=15)

# Button to clear input fields AND result
btn_clear_inputs = tk.Button(
    clear_btn_frame, 
    text="Clear Inputs", 
    width=15, 
    command=clear_inputs
)
btn_clear_inputs.grid(row=0, column=0, padx=10)

# Button to clear calculation history
btn_clear_history = tk.Button(
    clear_btn_frame, 
    text="Clear History", 
    width=15, 
    command=clear_history
)
btn_clear_history.grid(row=0, column=1, padx=10)

# START THE GUI APPLICATION
window.mainloop()  # Keeps the window open until the user closes it

# With AI