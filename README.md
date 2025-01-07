Cписок QuerySet запросов в порядке вызовов, которые использовали для внесения изменений в БД

>>> from task1.models import Buyer 
>>> Buyer.objects.all()
<QuerySet []>
>>> Buyer.objects.create(name='Murat', balance=900000, age=36)
<Buyer: Murat>
>>> Buyer.objects.create(name='Ivan', balance=7600000, age=17)  
<Buyer: Ivan>
>>> Buyer.objects.create(name='Jon', balance=600000, age=27)   
<Buyer: Jon>
>>> from task1.models import Game                              

>>> Game.objects.create(title='NeedforSpeed', cost=899, size=156000, description='Гоночная компьютерная игра', age_limited=True)              

>>> Game.objects.create(title='CS', cost=600, size=16780, description='Компьютерная игра в жанре шутер', age_limited=False)        

>>> Game.objects.create(title='Tank', cost=100, size=100, description='Игра симулятор', age_limited=True)                    

>>> first_buyer=Buyer.objects.get(age__lt=18) 
>>> second_buyer, third_buyer=Buyer.objects.filter(age__gt=18) 
>>> Game.objects.get(id=3).buyer.set((first_buyer, second_buyer, third_buyer))
>>> Game.objects.get(id=2).buyer.set((first_buyer, third_buyer)) 
>>> Game.objects.get(id=1).buyer.set((first_buyer,)) 
