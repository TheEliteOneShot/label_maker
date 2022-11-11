from fpdf import FPDF
import random
#pip install fpdf2

pdf = FPDF(unit='in',format=(8.5,11))

# define one column and one row margins
pdf.set_margins(0.137,0.5)
pdf.set_font('helvetica','B',7)
pdf.set_auto_page_break(False)
pdf.add_page()

#define total rows containing labels. 
rows=10
# define total columns containing labels
cols=3
#The width of each column
columnsize=2.625
#The width between the inner columns (not the last column)
inner_cell_margin=0.118
# Output location
output_location="C:\\Users\\Zachary Laney\\Documents\\labels\\labels.pdf"

def get_random_name():
    return random.choice(["John Doe", "Mary Jane"])

def get_random_address():
    return f"{random.randrange(1, 1000)} My Address Unit #{random.randrange(100, 1000, 2)}"

for i in range(rows):
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.cell(w=this_columnsize,h=1,fill=False, align="C", border=1)
    pdf.ln(0.25)
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.set_font('helvetica','B',10)
        pdf.cell(w=this_columnsize,h=0.2,txt=get_random_name(), align="C")
    pdf.ln(0.2)
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.set_font('helvetica','B',8)
        pdf.cell(w=this_columnsize,h=0.15,txt=get_random_address(), align="C")
        if j < cols:
            #pdf.cell(w=0.118,h=1,ln=0,fill=False, align="C", border=0)
            None
    pdf.ln(0.2)
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.set_font('helvetica','B',8)
        pdf.cell(w=this_columnsize,h=0.1,txt="Honolulu, HI, 96860", align="C")
    pdf.ln(0.35)

pdf.add_page()

#TODO: Add logic to create multiple pages

for i in range(rows):
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.cell(w=this_columnsize,h=1,fill=False, align="C", border=1)
    pdf.ln(0.25)
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.set_font('helvetica','B',10)
        pdf.cell(w=this_columnsize,h=0.2,txt=get_random_name(), align="C")
    pdf.ln(0.2)
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.set_font('helvetica','B',8)
        pdf.cell(w=this_columnsize,h=0.15,txt=get_random_address(), align="C")
        if j < cols:
            #pdf.cell(w=0.118,h=1,ln=0,fill=False, align="C", border=0)
            None
    pdf.ln(0.2)
    for j in range(cols):
        this_columnsize=columnsize
        if j < cols:
            this_columnsize = this_columnsize + inner_cell_margin
        pdf.set_font('helvetica','B',8)
        pdf.cell(w=this_columnsize,h=0.1,txt="Honolulu, HI, 96860", align="C")
    pdf.ln(0.35)

pdf.output(output_location)