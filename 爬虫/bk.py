from datetime import datetime, dat
today = datetime.today()
persons_on_duty = ['raymondzhu', 'yakovliu', 'shabbywu', 'bluesyu']

trans = today.isocalendar()[1] % len(persons_on_duty)
person_on_duty = persons_on_duty[trans]

print(person_on_duty)