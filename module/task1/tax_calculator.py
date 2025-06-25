def tax(taxable_amount, rate):
    # tax amount = taxable amount * rate /100
    # total amount = tax amount + taxable amount
    tax_amount= taxable_amount * (rate/100) 
    total_amount =tax_amount + taxable_amount
    print('tax amount = ',tax_amount)
    print('total amount = ',total_amount)