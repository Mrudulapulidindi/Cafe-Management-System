import streamlit as st

# Define menu with prices
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Title and greeting
st.title("Welcome to Khaane ki Kavitha")

st.write("Menu")

# Display menu items with images
for item, price in menu.items():
    st.image(f"{item.lower()}.jpg", width=150)
    st.write(f"{item} — Rs {price}")

st.write("---")

# Multiselect for ordering
selected_items = st.multiselect("Select items to order:", list(menu.keys()))

# Show order summary and total when button is clicked
if st.button("Place Order"):
    if selected_items:
        total = sum([menu[item] for item in selected_items])

        st.write("Order Summary")

        for item in selected_items:
            st.write(f"- {item}: Rs {menu[item]}")

        st.write(f"Total amount: Rs {total}")

        # Generate bill text
        bill_text = "Khaane ki Kavitha Bill\n\n"
        bill_text += "Items Ordered:\n"
        for item in selected_items:
            bill_text += f"- {item}: Rs {menu[item]}\n"
        bill_text += f"\nTotal: Rs {total}\n\nThank you for visiting!"

        # Download button for bill text file
        st.download_button("Download Bill as Text", bill_text, file_name="bill.txt")

    else:
        st.write("Please select at least one item to place an order.")

