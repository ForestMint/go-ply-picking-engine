from flask import Flask
app = Flask(__name__)

import sente
import random

@app.route('/request_ply')
def request_ply():
  game = request.args.get('game')


  while True:
    a=random.randint(1, 19)
    b=random.randint(1, 19)
    try:
      game.play(a, b)
      return {"ply":"ply"}
    except:
      pass
  
  

if __name__ == "__main__":
    app.run()
