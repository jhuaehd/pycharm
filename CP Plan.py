import math

call_minutes = float(input())
text_message = float(input())
cc_fee = 25.00

print("Call minutes:", call_minutes)
print("Text messages:", text_message)

# computer for exceed minutes in call
ex_callmin = call_minutes - 60

# computer for exceed in sms
ex_sms = text_message - 100

if call_minutes > 60:
    ex_callmin = ex_callmin * 6.50
    print("Excess minute charges: {:.2f}".format(ex_callmin))
else:
    ex_callmin = 0
    zero = float(0)
    print("Excess minute charges: {:.2f}".format(zero))
if text_message > 100:
    ex_sms = ex_sms * 1
    print("Excess SMS charges: {:.2f}".format(ex_sms))
else:
    ex_sms = 0
    zero = float(0)
    print("Excess SMS charges: {:.2f}".format(zero))

print("911 fee: {:.2f}".format(cc_fee))
taxed = (799 + ex_callmin + ex_sms + cc_fee) * 0.05
print("Tax: {:.2f}".format(taxed))
total_bill = 799 + ex_callmin + ex_sms + cc_fee + taxed
print("Total bill: {:.2f}".format(total_bill))


