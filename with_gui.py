from tkinter import *
from tkinter import messagebox

USER_BALANCE = 500

available_coffee = [
    {"id": 1, "name": "Black Coffee",   "price": 100, "quantity": 2},
    {"id": 2, "name": "Choco Latte",    "price": 150, "quantity": 2},
    {"id": 3, "name": "Mocha Coffee",   "price": 200, "quantity": 2},
    {"id": 4, "name": "Caramel Coffee", "price": 250, "quantity": 2},
]

curr_balance = USER_BALANCE
order = []

window = Tk()
window.geometry("460x720")
window.title("Simple Coffee Shop")
window.config(background="#c1c1c1")

try:
    icon = PhotoImage(file='assets/icons/buymeacoffee.png')
    window.iconphoto(True, icon)
except TclError:
    pass

title = Label(window, text="☕ Coffee Shop ☕",
              font=('Arial', 22, 'bold'), bg="#c1c1c1", fg="#3b2a1a")
title.pack(pady=(20, 5))

balance_label = Label(window, text=f"Balance: ₱{curr_balance}",
                      font=('Arial', 14, 'bold'), bg="#c1c1c1", fg="#1a5c1a")
balance_label.pack()

menu_frame = Frame(window, bg="#c1c1c1")
menu_frame.pack(pady=15, fill="x", padx=20)

order_frame = LabelFrame(window, text=" Your Order ",
                         font=('Arial', 12, 'bold'),
                         bg="#c1c1c1", fg="#3b2a1a", padx=10, pady=10)
order_frame.pack(pady=10, padx=20, fill="both", expand=True)

order_listbox = Listbox(order_frame, font=('Consolas', 11),
                        bg="#fafafa", height=8, activestyle="none")
order_listbox.pack(fill="both", expand=True)

total_label = Label(window, text="Total: ₱0",
                    font=('Arial', 14, 'bold'), bg="#c1c1c1", fg="#3b2a1a")
total_label.pack(pady=(0, 10))

def refresh_menu():
    for coffee in available_coffee:
        w = coffee_widgets[coffee["id"]]
        w["stock"].config(text=f"x{coffee['quantity']}")
        if coffee["quantity"] <= 0:
            w["button"].config(state=DISABLED, bg="#8a8a8a")
        else:
            w["button"].config(state=NORMAL, bg="#f5deb3")


def refresh_order():
    order_listbox.delete(0, END)
    total = 0
    for item in order:
        order_listbox.insert(END, f"{item['name']:<16} ₱{item['price']}")
        total += item["price"]
    total_label.config(text=f"Total: ₱{total}")


def refresh_balance():
    balance_label.config(text=f"Balance: ₱{curr_balance}")


def add_to_order(coffee):
    if coffee["quantity"] <= 0:
        messagebox.showwarning("Out of Stock", f"{coffee['name']} is out of stock.")
        return

    current_total = sum(i["price"] for i in order)
    if current_total + coffee["price"] > curr_balance:
        messagebox.showwarning(
            "Not Enough Balance",
            f"Adding {coffee['name']} would exceed your balance."
        )
        return

    coffee["quantity"] -= 1
    order.append({
        "id": coffee["id"],
        "name": coffee["name"],
        "price": coffee["price"],
        "ref": coffee,
    })

    refresh_menu()
    refresh_order()


def clear_order():
    for item in order:
        item["ref"]["quantity"] += 1
    order.clear()
    refresh_menu()
    refresh_order()


def checkout():
    global curr_balance

    if not order:
        messagebox.showinfo("Empty Order", "Your order is empty.")
        return

    total = sum(i["price"] for i in order)

    if curr_balance < total:
        messagebox.showerror(
            "Insufficient Balance",
            f"Total is ₱{total}, but you only have ₱{curr_balance}."
        )
        return

    curr_balance -= total
    order.clear()

    refresh_balance()
    refresh_order()
    refresh_menu()

    messagebox.showinfo(
        "Checkout Successful",
        f"Thank you! Remaining balance: ₱{curr_balance}"
    )

coffee_widgets = {}


def build_menu():
    for coffee in available_coffee:
        row = Frame(menu_frame, bg="#c1c1c1")
        row.pack(fill="x", pady=5)

        Label(row, text=f"{coffee['name']}  —  ₱{coffee['price']}",
              font=('Arial', 12), bg="#c1c1c1", anchor="w").pack(side=LEFT)

        stock_lbl = Label(row, text=f"x{coffee['quantity']}",
                          font=('Arial', 12, 'bold'), bg="#c1c1c1", fg="#555")
        stock_lbl.pack(side=RIGHT, padx=(0, 10))

        add_btn = Button(row, text="Add",
                         font=('Arial', 10, 'bold'),
                         bg="#f5deb3", activebackground="#e0c89a",
                         width=6,
                         command=lambda c=coffee: add_to_order(c))
        add_btn.pack(side=RIGHT)

        coffee_widgets[coffee["id"]] = {"stock": stock_lbl, "button": add_btn}


build_menu()

btn_frame = Frame(window, bg="#c1c1c1")
btn_frame.pack(pady=(0, 20))

Button(btn_frame, text="Checkout", font=('Arial', 12, 'bold'),
       bg="#8fd18f", activebackground="#6bb96b",
       width=12, command=checkout).grid(row=0, column=0, padx=8)

Button(btn_frame, text="Clear Order", font=('Arial', 12, 'bold'),
       bg="#f0a0a0", activebackground="#d98080",
       width=12, command=clear_order).grid(row=0, column=1, padx=8)

refresh_menu()
refresh_order()
refresh_balance()

window.mainloop()