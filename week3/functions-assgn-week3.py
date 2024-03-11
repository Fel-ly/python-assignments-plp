def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

def main():
    price_input = input("Enter the original price of the item: $")
    discount_input = input("Enter the discount percentage: ")

    if price_input.isdigit() and discount_input.isdigit():
        price = float(price_input)
        discount_percent = float(discount_input)
        final_price = calculate_discount(price, discount_percent)
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
