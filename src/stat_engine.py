import math
class StatEngine:
    def init(self,data):
        if not data:
            raise TypeError("Data cannot be empty")
        datas=[]
        for i in data:
            if isinstance(i,(int,float)):
                datas.append(i)
            else:
                raise TypeError("invalid data type")
        self.data=datas

    #part one

    def get_mean(self):
        total=0
        for i in self.data:
            total +=i
        return total / len(self.data)
    def get_median(self):
        sor=sorted(self.data)
        n=len(self.data)
        mid=n//2
        if n%2==0:
            return (self.data[mid-1] + self.data[mid]) / 2
        else:
            return self.data[mid]
    def get_mode(self):
        freq={}

        for i in self.data:
            freq[i]=freq.get(i,0) + 1

        maxi = max(freq.values())
        if maxi ==1:
            return "all aree unique"
        return [i for i in freq 
        if freq[i] == maxi]
    #part two
    def get_variance(self,is_sample=True):
        mean = self.get_mean()
        n=len(self.data)
        
        total=0
        for i in self.data:
            total +=(i-mean) **2
        if is_sample:
            if n < 2:
                raise TypeError("it must be atleast 2 values")
            return total /(n-1)
        else:
            return total /n
    def get_standard_deviation(self,is_sample=True):
        return math.sqrt(self.get_variance(is_sample))
    
    # part three

    def get_outliers(self,threshold=2):
        mean=self.get_mean()
        std=self.get_standard_deviation()

        if std ==0:
            return []

        return [
            x for x in self.data
            if abs(x-mean) / std > threshold
        ]
if name =="main":

    user=input("enter number :")
    try:
        data = [float(x) for x in user.split()]
        engine = StatEngine(data)

        print("Mean :" ,engine.get_mean())
        print("Median :" ,engine.get_median())
        print("Mode :" ,engine.get_mode())
        print("sample variance :" ,engine.get_variance(True))
        print("population variance :" ,engine.get_variance(False))
        print("standard deviation :" ,engine.get_standard_deviation())
        print("outliers :" ,engine.get_outliers())
    except ValueError:
        print("error: enter valid numbers")
    except TypeError as e:
        print("error:" , e)
