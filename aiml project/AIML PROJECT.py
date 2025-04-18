promo_codes = {
    "SAVE10": "10% off on orders over $50",
    "FREESHIP": "Free shipping on all orders",
    "WELCOME15": "15% off for new customers",
    "SUMMER20": "20% off on summer collection",
    "BLACKFRIDAY": "30% off on Black Friday sales",
    "WINTER25": "25% off on winter apparel",
    "SPRINGSALE": "15% off on spring collection",
    "BOGO": "Buy one get one free on select items",
    "CLEARANCE30": "30% off on clearance items",
    "LOYALTY5": "5% off for loyalty program members",
    "STUDENT10": "10% off for students with valid ID",
    "NEWYEAR2023": "20% off for New Year celebrations",
    "EASTER15": "15% off for Easter weekend",
    "HALLOWEEN20": "20% off on Halloween costumes",
    "VALENTINE10": "10% off on Valentine's Day gifts",
    "MOTHER10": "10% off for Mother's Day",
    "FATHER15": "15% off for Father's Day",
    "BIRTHDAY20": "20% off on your birthday month",
    "GIFT10": "10% off on gift cards",
    "TRAVEL15": "15% off on travel packages",
    "TECH20": "20% off on tech gadgets",
    "KITCHEN15": "15% off on kitchen appliances",
    "HEALTH10": "10% off on health products",
    "PET15": "15% off on pet supplies",
    "BOOKS20": "20% off on all books",
    "TOYS10": "10% off on toys for kids",
    "OUTDOOR25": "25% off on outdoor gear",
    "FASHION30": "30% off on fashion items",
    "ELECTRONICS15": "15% off on electronics",
    "HOMEDECOR10": "10% off on home decor items",
    "GARDEN20": "20% off on garden supplies",
    "FURNITURE15": "15% off on furniture purchases",
    "CLEANING10": "10% off on cleaning products",
    "BEAUTY20": "20% off on beauty products",
    "SPORTS15": "15% off on sports equipment",
    "MUSIC10": "10% off on music instruments",
    "MOVIES20": "20% off on movie rentals",
    "GAMES15": "15% off on video games",
    "CLOTHING10": "10% off on clothing items",
    "SHOES20": "20% off on shoes",
    "ACCESSORIES15": "15% off on accessories",
    "JEWELRY10": "10% off on jewelry",
    "WEDDING20": "20% off on wedding items",
    "PARTY15": "15% off on party supplies",
    "FESTIVAL10": "10% off during festival season",
    "SALE30": "30% off sitewide sale",
    "FLASHSALE": "Limited time flash sale - 50% off",
    "VIP20": "20% off for VIP customers",
    "REFERRAL10": "10% off for referring a friend",
    "BUNDLE15": "15% off on bundled products",
    "LOYALTY20": "20% off for loyalty program members",
    "EXTRA5": "Extra 5% off on your next purchase",
    "FIRSTORDER10": "10% off on your first order",
    "REPEATCUSTOMER15": "15% off for repeat customers",
    "SEASONAL20": "20% off on seasonal items",
    "LIMITEDTIME": "Limited time offer - 25% off",
    "CLEARANCE50": "50% off on clearance items",
}

def check_promo_code(promo_code):
    """Check if the promo code exists and return its conditions or detect abuse."""
    if promo_code in promo_codes:
        return f"Promo Code: {promo_code} - Conditions: {promo_codes[promo_code]}"
    else:
        return "Abuse Detected: Invalid Promo Code"

def main():
    """Main function to run the promo code checker."""
    user_input = input("Enter the promo code: ").strip()
    result = check_promo_code(user_input)
    print(result)

if __name__ == "__main__":
    main()