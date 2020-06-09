# Query all Costumers in database
# variableName = ModelClass.objects.all()
costumers = Costumer.objects.all()

'''
getting the first data. same goes by .last()
'''
costumer = Costumer.objects.first()

'''
return single data by filtering the field
'''
costumer = Costumer.objects.get(name="John Doe")

'''
returning orders by a costumer.. so basically getting one to many
'''
# use related object set. query Costumer and chain it downwards
orders = costumer.modellowercase_set.all()

'''
gettin products
'''
# filter() with zero parameter will act as all()
products = Product.objects.filter()

'''
sorting the query
'''
products = Product.objects.all().order_by("id")
products = Product.objects.all().order_by("-id")

'''
MANY TO MANY QUERY
'''
products = Product.objects.filter(field__fieldName="asd")