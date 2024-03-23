
class car:
    def company(self,name):
        i=['Toyota','Mercedes','suzuki']
        if name in i:
            print("welcome to",name)
    def model(self,name):
        d={'Toyota':['Fortuner','Innova'],'Mercedes':['amg'],'Suzuki':['swift','alto']}
        if name in d:
            print(d[name])
    def price(self,name,m):
        print("you have selected",m)
        prices_list={'Fortuner':7500000,'Innova':5000000,'amg':100000000,'Swift':3000000,'Alto':100000}
        if m in prices_list:
            car_price=prices_list[m]
            gst=0.1*car_price
        insurance=100000
        final_price=car_price+gst+insurance
        print("finalprice:",final_price)
n=input("enter the car company:")
c=car()
c.company(n)
c.model(n)
m=input("enter model of car:")
c.price(n,m)
   
