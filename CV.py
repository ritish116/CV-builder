import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf():
    # Gather inputs
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    education = text_education.get("1.0", tk.END).strip()    
    projects = text_projects.get("1.0", tk.END).strip()
    
    if not name or not email or not phone or not address:
        messagebox.showerror("Input Error", "Please fill in all required fields.")
        return
    
    # Create PDF
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save PDF"
    )
    
    if file_path:
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        
        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, height - 72, name)
        
        # Contact Information
        c.setFont("Helvetica", 12)
        c.drawString(72, height - 108, f"Email: {email}")
        c.drawString(72, height - 124, f"Phone: {phone}")
        c.drawString(72, height - 140, f"Address: {address}")
        
        # Education
        c.setFont("Helvetica-Bold", 14)
        c.drawString(72, height - 180, "Education")
        c.setFont("Helvetica", 12)
        c.drawString(72, height - 196, education)
        
       
        
        # Projects
        c.setFont("Helvetica-Bold", 14)
        c.drawString(72, height - 300, "Projects")
        c.setFont("Helvetica", 12)
        c.drawString(72, height - 316, projects)
        
        c.save()
        messagebox.showinfo("Success", "CV saved successfully!")

# Create the main window
root = tk.Tk()
root.title("CV Generator")

# Create and place the widgets
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root, width=50)
entry_name.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=50)
entry_email.pack(pady=5)

tk.Label(root, text="Phone:").pack(pady=5)
entry_phone = tk.Entry(root, width=50)
entry_phone.pack(pady=5)

tk.Label(root, text="Address:").pack(pady=5)
entry_address = tk.Entry(root, width=50)
entry_address.pack(pady=5)

tk.Label(root, text="Education:").pack(pady=5)
text_education = tk.Text(root, height=5, width=50)
text_education.pack(pady=5)

tk.Label(root, text="Experience:").pack(pady=5)
text_experience = tk.Text(root, height=5, width=50)
text_experience.pack(pady=5)

tk.Label(root, text="Projects:").pack(pady=5)
text_projects = tk.Text(root, height=5, width=50)
text_projects.pack(pady=5)

generate_button = tk.Button(root, text="Generate CV", command=generate_pdf)
generate_button.pack(pady=10)


root.mainloop()
