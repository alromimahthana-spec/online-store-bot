# بوت متجر ملابس - ثناء | thanaa.codes
# يعرض الملابس، يحسب الفاتورة، ويستلم طلبات التوصيل

products = {
    "1": {"name": "فستان سهرة", "price": 180},
    "2": {"name": "عباية سوداء", "price": 220},
    "3": {"name": "تيشيرت", "price": 60},
    "4": {"name": "بنطلون جينز", "price": 120},
    "5": {"name": "حجاب", "price": 40},
    "6": {"name": "شنطة يد", "price": 150},
}

cart = []

def show_products():
    print("👗 أهلاً فيك في متجرنا!")
    print("اختاري من التشكيلة:")
    for key, item in products.items():
        print(f"{key}. {item['name']} - {item['price']} ريال سعودي")
    print("0. انهاء التسوق")

while True:
    show_products()
    choice = input("اكتبي رقم المنتج: ")
    if choice == "0":
        break
    if choice in products:
        qty = int(input(f"كم حبة تبغي من {products[choice]['name']}؟ "))
        size = input("المقاس (S / M / L / XL): ")
        cart.append({"item": products[choice]['name'], "price": products[choice]['price'], "qty": qty, "size": size})
        print(f"✅ اضفنا {qty} x {products[choice]['name']} - مقاس {size}")
    else:
        print("اختيار غلط، حاولي مرة ثانية")

print("\n--- فاتورتك ---")
total = 0
for c in cart:
    subtotal = c['price'] * c['qty']
    total += subtotal
    print(f"{c['item']} - مقاس {c['size']} x {c['qty']} = {subtotal} ريال")

print(f"المجموع: {total} ريال سعودي")
print(f"رسوم الشحن: 20 ريال")
print(f"الاجمالي: {total + 20} ريال سعودي")

name = input("\nاسمك: ")
phone = input("رقم جوالك: ")
address = input("عنوان التوصيل: ")
print(f"\n✅ شكراً {name}! طلبك بيوصلك خلال 2-3 أيام على {address} 📦")
print("📩 بنرسل لك رقم الشحنة عشان تتبعي طلبك!")
