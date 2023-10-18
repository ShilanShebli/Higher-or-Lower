from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTk0YWM0YTIyNzBiOTExYmNhNjcxZTg1YzhkZWJiYTUzOTY3ZDI3NCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


random_number = random.randint(0, 9)

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return "<h1>Too Low!</h1><img src='https://media3.giphy.com/media/3oxHQEmqjJasd00K7S/giphy.gif?cid=ecf05e47rm0pffchv43wz8vp09vlgwjv60a5w3hxelthtjtt&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif guess > random_number:
        return "<h1>Too High!<h1><img src='https://media0.giphy.com/media/dtHSULwMPmBaVMB8Pu/giphy.gif?cid=ecf05e47kf0zs382zwv9oxqqk8jp30jiu5w8cvnahs9kqkxj&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    else:
        return "<h1>Correct!<h1><img src='https://media1.giphy.com/media/XE8iJs1sT7xTM5lafa/giphy.gif?cid=ecf05e47p45dn6xcd8oycpgcv7hg26p7u8d1wvu2rulory8a&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"



if __name__ == "__main__":
    app.run(debug=True)

