from application import salary as s
from application.db import people as p
from datetime import datetime
import requests

sal = s.Salary()
pip = p.People()

if __name__ == '__main__':
    print(sal.calculate_salary())
    print(pip.get_employees())
    print(datetime.now())


