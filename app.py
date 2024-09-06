from flask import Flask, request
app = Flask(__name__)

import sente
import random

@app.route('/request_ply')
def request_ply():
  #return {"result":"D4"}
  game = request.args.get('game')
  size = 19

  while True:
    a=random.randint(1, size)
    b=random.randint(1, size)
    try:
      game.play(a, b)
      game.step_up()
      return {"result":"D4"}
    except:
      return {"result":None}
  
  

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001")
