## Items in english
def items_in_english():
    print("\nAvailable items:")
    print("1. Doritos - AED2.50")
    print("2. Ferrero Rocher - AED3.50")
    print("3. Sandwich - AED5.00")
    print("4. Oman Chips - AED1.00")
    print("5. Water - AED1.00")
    print("6. Kinza - AED2.00")
    print("7. Pepsi - AED1.50")
    print("8. Coffee - AED3.00")

## Items in Arabic
def items_in_arabic():
    print("\العناصر المتاحة:")
    print("1. دوريتوس - AED2.50")
    print("2. فيريرو روشيه - AED3.50")
    print("3. ساندويتش - AED5.00")
    print("4. رقائق عمان - AED1.00")
    print("5. ماء - AED1.00")
    print("6. كينزا - AED2.00")
    print("7. بيبسي - AED1.50")
    print("8. قهوة - AED3.00")

def main():                              ## Main function for vending machine
    ## Language selection
    language = {
        "1": "Arabic",
        "2": "English"
    }
     ## User to choose language option
    language_code = input("Please select the language (1 - Arabic, 2 - English): ")   
    if language_code == "1":
        print("العربية المختارة")
        selected_language = "Arabic"
        display_items = items_in_arabic
    elif language_code == "2":
        print("Selected English")
        selected_language = "English"
        display_items = items_in_english
    else:
        print("Invalid language selection.")                    
        language_code = input("Please select the language (1 - Arabic, 2 - English): ")    ## Default to choose language

    ## Items, prices and stock list
    items = {
        "1": {"name": {"English": "Doritos", "Arabic": "دوريتوس"}, "price": 2.50, "stock": 7},
        "2": {"name": {"English": "Ferrero Rocher", "Arabic": "فيريرو روشيه"}, "price": 3.50, "stock": 5},
        "3": {"name": {"English": "Sandwich", "Arabic": "ساندويتش"}, "price": 5.00, "stock": 8},
        "4": {"name": {"English": "Oman Chips", "Arabic": "رقائق عمان"}, "price": 1.00, "stock": 10},
        "5": {"name": {"English": "Water", "Arabic": "ماء"}, "price": 1.00, "stock": 10},
        "6": {"name": {"English": "Kinza", "Arabic": "كينزا"}, "price": 2.00, "stock": 8},
        "7": {"name": {"English": "Pepsi", "Arabic": "بيبسي"}, "price": 1.50, "stock": 5},
        "8": {"name": {"English": "Coffee", "Arabic": "قهوة"}, "price": 3.00, "stock": 7}
    }
    ## User balance
    balance = 0

    while True:
        ## Display after choosing language
        if selected_language == "English":
            print(f"\nCurrent balance: AED {balance:.2f}")
            print("1. Add money")
            print("2. Buy an item")
            print("3. Exit")
        else:
            print(f"\nرصيدك الحالي: AED {balance:.2f}")
            print("1. اضافة مال")
            print("2. شراء عنصر")
            print("3. خروج")

        ## User choice
        choice = input("Enter your choice (1, 2, 3): " if selected_language == "English" else "ادخل اختيارك (1، 2، 3): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount : AED" if selected_language == "English" else " أدخل المبلغ : AED"))
                if amount > 0:
                    balance += amount
                    print(f"Added AED {amount:.2f}." if selected_language == "English" else f"وأضاف AED {amount:.2f}.")
                else:
                    print("Please enter a positive amount." if selected_language == "English" else "يرجى إدخال مبلغ إيجابي.")
            except ValueError:
                print("Invalid. Please enter a number." if selected_language == "English" else " غير صالح. الرجاء إدخال رقم .")

        elif choice == "2":
            display_items()
            item_choice = input("Enter the item number : " if selected_language == "English" else " أدخل رقم البند : ")

            if item_choice in items:
                item = items[item_choice]
                item_name = item["name"][selected_language]
                item_price = item["price"]

                if item["stock"] > 0:
                    if balance >= item_price:       ## Price and Stock decrease
                        balance -= item_price
                        item["stock"] -= 1
                        print(f"You bought {item_name} AED {item_price:.2f}." if selected_language == "English" else f"اشتريت {item_name} AED {item_price:.2f}.")
                        print(f"Remaining balance: AED {balance:.2f}" if selected_language == "English" else f"رصيد متبقي: AED {balance:.2f}")
                    else:
                        print("Insufficient balance. Add money." if selected_language == "English" else ". رصيد غير كاف.أضف المال .")
                else:
                    print(f"Sorry, {item_name} not available." if selected_language == "English" else f"عذرًا، {item_name} غير متوفر.")
            else:
                print("Invalid item. Try again." if selected_language == "English" else ".عنصر غير صالح. حاول ثانية ")

        elif choice == "3":         
            print("Thank you for using the vending machine." if selected_language == "English" else " !.شكرا لك على استخدام آلة البيع ")
            break     ## Exit

        else:
            print("Invalid choice.Try again." if selected_language == "English" else ".خيار غير صالح. حاول ثانية")

if __name__ == "__main__":
    main()

