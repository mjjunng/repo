# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from typing import List
import math

# OOP 방식
# O(nlogn)
class Park:

    def __init__(self,default_time:int,default_fee:int,unit_time:int,unit_fee:int) -> None:
        self.cars=dict()
        self.default_time:int=default_time
        self.default_fee:int=default_fee
        self.unit_time:int=unit_time
        self.unit_fee:int=unit_fee

    def update_car_in_and_out(self,number:str,type:str,time:str)->None:
        if number not in self.cars:
            self.cars[number] = [type,time,0]

        last_in_time=self.cars[number][1]
        total_parking_minutes=self.cars[number][2]
        if type=="IN":
            self.cars[number]=[type,time,total_parking_minutes]
        else:
            minutes = self._get_parking_minutes(time,last_in_time)
            self.cars[number]=[type,time,total_parking_minutes+minutes]

    def _get_parking_minutes(self,out_time:str,in_time:str)->int:
        out_hour,out_min=int(out_time.split(":")[0]),int(out_time.split(":")[1])
        in_hour,in_min=int(in_time.split(":")[0]),int(in_time.split(":")[1])

        if out_min<in_min:
            min = 60+out_min-in_min
            hour = out_hour-1-in_hour
        else:
            min = out_min-in_min
            hour = out_hour-in_hour
        return 60 * hour + min
    
    def _get_total_parking_minutes(self,car:tuple)->None:
        number = car[0]
        if self.cars[number][0]=="IN":
            last_in_time=self.cars[number][1]
            total_parking_minutes=self.cars[number][2]
            minutes = self.get_parking_minutes("23:59",last_in_time)
            return total_parking_minutes + minutes
        return car[1][2]
            

    def impose(self)->List:
        answer = []

        for car in sorted(self.cars.items()):
            car_total_parking_minute = self._get_total_parking_minutes(car)

            if car_total_parking_minute < self.default_time:
                answer.append(self.default_fee)
            else:
                plus_fee = math.ceil((car_total_parking_minute-self.default_time)/self.unit_time) * self.unit_fee
                answer.append(self.default_fee + plus_fee)

        
        return answer


class Solution:
    def solution(self,fees, records):
        park = Park(int(fees[0]),int(fees[1]),int(fees[2]),int(fees[3]))

        for record in records: # O(1000)
            info = record.split()

            time=info[0] # 06:00
            number=info[1] # 5453
            type=info[2] # IN

            park.update_car_in_and_out(number,type,time)
            
        return park.impose()

                
s = Solution()
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(s.solution(fees,records))