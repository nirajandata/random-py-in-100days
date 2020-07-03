import turtle as t, random
for _ in range(800):
    ran=random.random()*100
    a=random.choice([-ran,ran])
    random.choice([t.forward,t.backward])(a)
    b=random.choice([90,-90])
    random.choice([t.right,t.left])(b)
