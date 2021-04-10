from flask import Flask, render_template, request

app = Flask(__name__)

#class Item():
#    def __init__(self, name, amount):
#        self.name = name
#        self.amount = amount


@app.route('/')
def hello():
    #items = [
    #    Item("Apfel", 5),
    #    Item("Computer", 1),
    #    Item("Birne", 4)
    #]

    items = [
        {"name": "Apfel", "amount": 5},
        {"name": "Computer", "amount": 1},
        {"name": "Birne", "amount": 4}
    ]

    person = ("Max", "Mustermann")
    return render_template("start.html", items=items, person=person)


@app.route('/test')
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)


@app.route('/change')
def change():
    curr1 = request.args.get("curr1", "EUR")
    curr2 = request.args.get("curr2", "DM")

    step = int(request.args.get("step", 10))
    amount = int(request.args.get("amount", 10))
    rate = float(request.args.get("rate", 1.95583))

    table = []
    i = 1
    while i < amount + 1:
        table.append((i * step, round(i * step * rate, 2)))
        i += 1

    table_rev = []
    i = 1
    while i < amount + 1:
        table_rev.append((i * step, round((i * step) / rate, 2)))
        i += 1

    return render_template("change.html",
                           curr1=curr1,
                           curr2=curr2,
                           step=step,
                           amount=amount,
                           rate=rate,
                           table=table,
                           table_rev=table_rev)

if __name__ == '__main__':
    app.run()
