import random
import sqlite3

from generators.generators import GeneratorBase
 
conn = sqlite3.connect('src/roadname.db')
cursor = conn.cursor()

cursor.execute("SELECT count(*) FROM address_kr")
count_addr = cursor.fetchone()
count_addr = count_addr[0]

class Address(GeneratorBase):
    def __init__(self) :
        index = random.randint(1, count_addr)
        cursor.execute("SELECT * FROM address_kr WHERE id=?;", [index])
        result = cursor.fetchone()
        
        si = result[1]
        sgg = result[2]
        road = result[3]

        roadNum = random.randint(1, 100)

        self.address = f'{si} {sgg} {road} {roadNum}'

    def generate(self):
        return self.address
    