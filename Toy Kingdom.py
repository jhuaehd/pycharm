import math

target_donation = int(input())
puzzles = int(input())
tDolls = int(input())
tBears = int(input())
p_plushie = int(input())
bb_truck = int(input())

purchase = puzzles + tDolls + tBears + p_plushie + bb_truck

discount = float(0)

if purchase > 50:
    discount = float(0.25)

puzz = float(puzzles) * 14
dolls = float(tDolls) * 3
bears = float(tBears) * 20.2
plush = float(p_plushie) * 8.2
truck = float(bb_truck) * 10.65

total_amount = puzz + dolls + bears + plush + truck
total_amount = total_amount - (total_amount * discount)

store_rental = total_amount * 0.1
total_amount = total_amount - store_rental
donation = total_amount - target_donation

if total_amount > target_donation:
    print("Yes! {} dollars left.".format(format(donation, '.2f')))
else:
    print("Not enough money! {} dollars needed.".format(format(abs(donation), '.2f')))
