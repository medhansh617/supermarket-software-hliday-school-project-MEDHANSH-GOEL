import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import simpledialog,messagebox


#create the main window
root = tk.Tk()
root.title("Super Market Management System")
root.geometry("1920x1080")
image=Image.open("supermarket.jpg")
image=image.resize((1920,1080))
bg_photo=ImageTk.PhotoImage(image)

background_label=tk.Label(root,image=bg_photo)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

products={}
selected_item=None
bill_items={}
grand_total=0

#title
title=tk.Label(root,text="SUPERMARKET LOGIN",font=("Arial",20,"bold"))
title.pack(pady=20)

#username
username_Label=tk.Label(root,text="Username:", font=("Arial",12))
username_Label.pack()

username_entry=tk.Entry(root, width=30)
username_entry.pack(pady=5)

#password
password_Label=tk.Label(root,text="Password:", font=("Arial",12))
password_Label.pack()

password_entry=tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

products_listbox=tk.Listbox(root, width=30, height=10, font=("Arial",14))
bill_listbox=tk.Listbox(root, width=40, height=10, font=("Arial",14))



#all functions for below labels, entries and buttons

def add_item():
   item=inventory_item_entry.get()
   price_text=price_entry.get()
   if item=="" or price_text=="":
       return
   price=int(price_text)
   products[item]=price
   product_text=""
   for item_name, item_price in products.items():
       product_text+=f"{item_name}: ₹{item_price}\n"
   products_listbox.delete(0, tk.END)
   for item in products_listbox.get(0, tk.END):
       products_listbox.delete(0)
   for item_name, item_price in sorted(products.items()):
       products_listbox.insert(tk.END, f"{item_name}: ₹{item_price}")
   inventory_item_entry.delete(0, tk.END)
   price_entry.delete(0, tk.END)

def delete_item():
   print("button clicked")
   selected=products_listbox.curselection()
   if not selected:
       return
   item_text=products_listbox.get(selected[0])
   item_name=item_text.split(":")[0].strip()
   del products[item_name]
   products_listbox.delete(0, tk.END)
   for item_name, item_price in sorted(products.items()):
       products_listbox.insert(tk.END, f"{item_name}: ₹{item_price}")

add_item_button=tk.Button(root, text="Add Item",command=add_item)
delete_button=tk.Button(root,text="Delete product",command=delete_item)


#all labels, entries and buttons
customer_label=tk.Label(root,text="Customer Name:")
customer_entry=tk.Entry(root, width=30)

inventory_item_label=tk.Label(root,text="Item Name:")
inventory_item_entry=tk.Entry(root,width=30)

price_label=tk.Label(root,text="Price Per Unit:")
price_entry=tk.Entry(root,width=30)



item_label=None
item_entry=None
quantity_label=None
quantity_entry=None
total_label=None
calculate_button=None



def dashboard():
     title.config(text="SUPERMARKET DASHBOARD")
     billing_button.pack(pady=10)
     inventory_button.pack(pady=10)
     logout_button.pack(pady=10)
     if back_button:
        back_button.place_forget()
     if item_label:
         item_label.pack_forget()
     if item_entry:
        item_entry.pack_forget()
     if quantity_label:
        quantity_label.pack_forget()
     if quantity_entry:
        quantity_entry.pack_forget()
     if total_label:
        total_label.pack_forget()
     if calculate_button:
        calculate_button.pack_forget()
     if customer_label:
        customer_label.pack_forget()
     if customer_entry:
        customer_entry.pack_forget()
     if inventory_item_label:
        inventory_item_label.place_forget()
     if inventory_item_entry:
        inventory_item_entry.place_forget()
     if price_label:
        price_label.place_forget()
     if price_entry:
        price_entry.place_forget()
     if add_item_button:
        add_item_button.place_forget()
     if delete_button:
        delete_button.pack_forget()
     if products_listbox:
        products_listbox.pack_forget()
     if bill_listbox:
        bill_listbox.pack_forget()
     if add_to_bill_button:
        add_to_bill_button.pack_forget()
     if clear_bill_button:
         clear_bill_button.pack_forget()
     if clear_bill_button:
         clear_bill_button.place_forget()
     if clear_inventory_button:
         clear_inventory_button.place_forget()
     if search_label:
         search_label.pack_forget()
     if search_entry:
         search_entry.pack_forget()
     if search_button:
         search_button.pack_forget()
     if edit_button:
        edit_button.pack_forget()
    
     




back_button=tk.Button(root,text="Back", font=("Arial",14), width=20, command=dashboard)
total_label=tk.Label(root,text="Grand Total: ₹0",font=("Arial",14,"bold"))

def calculate_total():
      total_label.config(text=f"Grand Total: ₹{grand_total}")
def add_to_bill():
    global grand_total
    item=item_entry.get().lower()
    if item not in products:
        total_label.config(text="Item not found in inventory")
        return
    quantity=int(quantity_entry.get())
    price=products[item]
    subtotal=price*quantity
    global grand_total
    grand_total+=subtotal
    bill_listbox.insert(tk.END, f"{item} x {quantity} = ₹{subtotal}")
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

add_to_bill_button=tk.Button(root,text="Add to Bill", command=add_to_bill)



def clear_bill():
   global grand_total
   if bill_listbox.size() == 0:
       messagebox.showinfo("Bill", "Bill is already empty.")
       return
   if messagebox.askyesno("Confirm", "Are you sure you want to clear the bill?"):
      grand_total=0
      bill_listbox.delete(0, tk.END)
      total_label.config(text="Grand Total: ₹0")
      messagebox.showinfo("Success", "Bill cleared successfully.")



clear_bill_button=tk.Button(root,text="Clear Bill", command=clear_bill)
    
def open_billing():
    title.config(text="BILLING PAGE")
    global item_label, item_entry, quantity_label, quantity_entry, total_label, calculate_button
    billing_button.pack_forget()
    inventory_button.pack_forget()
    sales_button.pack_forget()
    logout_button.pack_forget()
    customer_label.pack()
    customer_entry.pack()
    item_label=tk.Label(root,text="Item Name:")
    item_label.pack()
    item_entry=tk.Entry(root, width=30)
    item_entry.pack()
    quantity_label=tk.Label(root,text="Quantity:")
    quantity_label.pack()
    quantity_entry=tk.Entry(root, width=30)
    quantity_entry.pack()
    add_to_bill_button.pack(pady=10)
    clear_bill_button.place(x=1000,y=560)
    bill_listbox.pack(pady=10)
    total_label.pack()
    calculate_button=tk.Button(root,text="Calculate Total",command=calculate_total)
    calculate_button.pack(pady=5)
    add_to_bill_button.pack(pady=5)
    total_label.pack(pady=10)
    back_button.place(x=10,y=560)

   
def clear_inventory():
      if not products:
          messagebox.showinfo("Clear Inventory", "Inventory is already empty.")
          return
      if messagebox.askyesno("Clear Inventory", "Are you sure you want to clear the inventory?"):
         products.clear()
         products_listbox.delete(0, tk.END)
         messagebox.showinfo("success", "Inventory cleared successfully.")



clear_inventory_button=tk.Button(root,text="Clear Inventory", command=clear_inventory)



def edit_item():
    global selected_item
    if products_listbox.curselection():
        index=products_listvox,curselection()[0]
        text=products_listbox.get(index)
        item=text.split("-")[0]
    elif selected_item is not None:
            item=selected_item
    else:
                messagebox.showinfo("edit item", "please select or search for an item first")
                return



edit_button=tk.Button(root,text="Edit Item", command=edit_item)
search_label=tk.Label(root,text="Search Item:")
search_entry=tk.Entry(root,width=30)




def open_inventory():
    title.config(text="INVENTORY PAGE")
    inventory_button.pack_forget()
    billing_button.pack_forget()
    sales_button.pack_forget()
    logout_button.pack_forget()
    inventory_item_label.place(x=10,y=100)
    inventory_item_entry.place(x=10,y=130)
    price_label.place(x=10,y=160)
    price_entry.place(x=10,y=190)
    add_item_button.place(x=10,y=220)
    delete_button.pack(pady=5)
    products_listbox.pack(pady=10)
  
    back_button.place(x=10,y=560)
    clear_inventory_button.place(x=1000,y=560)

   

def open_sales():
    title.config(text="SALES PAGE")
    sales_button.pack_forget()
    billing_button.pack_forget()
    inventory_button.pack_forget()
    logout_button.pack_forget()
    back_button.place(x=10,y=560)
    

def logout():
    root.destroy()


billing_button=tk.Button(root,text="Billing", font=("Arial",14), width=20, command=open_billing)
inventory_button=tk.Button(root,text="Inventory", font=("Arial",14), width=20, command=open_inventory)
sales_button=tk.Button(root,text="Sales", font=("Arial",14), width=20, command=open_sales)
logout_button=tk.Button(root,text="Logout", font=("Arial",14), width=20, command=logout)



def open_dashboard():
    title.config(text="SUPERMARKET DASHBOARD")
    username_Label.pack_forget()
    username_entry.pack_forget()
    password_Label.pack_forget()
    password_entry.pack_forget()    
    login_button.pack_forget()

    
    billing_button.pack(pady=10)
    inventory_button.pack(pady=10)
    logout_button.pack(pady=10)
    back_button.place_forget()


    

def check_login():
    username=username_entry.get()
    password=password_entry.get()
    if username=="admin" and password=="1234":
        open_dashboard()
    else:
        title.config(text="Invalid username or password")

#login button
login_button=tk.Button(root,text="Login", font=("Arial",12), command=check_login)
login_button.pack(pady=20)

#keep the window open
root.mainloop()

