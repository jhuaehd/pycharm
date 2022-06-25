month = str(input())
numOfNights = int(input())

Deluxe = (100, 112.50, 125.66)
Premium = (85, 90.58, 100.50)
months = ('May', 'October', 'July', 'September', 'June', 'August')

if month[0].isupper():
    # for Month of May and October !!
    if month == months[0] or month == months[1]:
        if 14 > numOfNights > 7:
            # deluxe discounted already
            deluxe_type = (numOfNights * Deluxe[0])
            discounted_deluxe = deluxe_type - (deluxe_type * 0.05)
            print("Deluxe: {:.2f} dollars".format(discounted_deluxe))
            premium_type = (numOfNights * Premium[0])
            print("Premium: {:.2f} dollars".format(premium_type))
        elif numOfNights > 14:
            deluxe_type = (numOfNights * Deluxe[0])
            discounted_deluxe = deluxe_type - (deluxe_type * 0.30)
            print("Deluxe: {:.2f} dollars".format(discounted_deluxe))
            premium_type = (numOfNights * Premium[0])
            discounted_premium = premium_type - (premium_type * 0.10)
            print("Premium: {:.2f} dollars".format(discounted_premium))
        else:
            deluxe_type = (numOfNights * Deluxe[0])
            print("Deluxe: {:.2f} dollars".format(deluxe_type))
            premium_type = (numOfNights * Premium[0])
            print("Premium: {:.2f} dollars".format(premium_type))
    # July and September !!
    if month == months[2] or month == months[3]:
        if numOfNights > 14:
            deluxe_type = (numOfNights * Deluxe[1])
            discounted_deluxe = deluxe_type - (deluxe_type * 0.20)
            print("Deluxe: {:.2f} dollars".format(discounted_deluxe))
            premium_type = (numOfNights * Premium[1])
            discounted_premium = premium_type - (premium_type * 0.20)
            print("Premium: {:.2f} dollars".format(discounted_premium))
        else:
            deluxe_type = (numOfNights * Deluxe[1])
            print("Deluxe: {:.2f} dollars".format(deluxe_type))
            premium_type = (numOfNights * Premium[1])
            print("Premium: {:.2f} dollars".format(premium_type))
    # For June and August
    if month == months[4] or month == months[5]:
        if numOfNights > 14:
            deluxe_type = (numOfNights * Deluxe[2])
            discounted_deluxe = deluxe_type - (deluxe_type * 0.10)
            print("Deluxe: {:.2f} dollars".format(discounted_deluxe))
            premium_type = (numOfNights * Premium[2])
            discounted_premium = premium_type - (premium_type * 0.10)
            print("Premium: {:.2f} dollars".format(discounted_premium))
        else:
            deluxe_type = (numOfNights * Deluxe[2])
            print("Deluxe: {:.2f} dollars".format(deluxe_type))
            premium_type = (numOfNights * Premium[2])
            print("Premium: {:.2f} dollars".format(premium_type))
else:
    print("Month's first letter must be capitalize!")
