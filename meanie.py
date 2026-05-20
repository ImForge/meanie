from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

insults = [
    "oh you're back. let me guess — tutorial #47 today?",
    "the fact that this is the most interesting thing happening in your life is genuinely tragic.",
    "your git commits read like a cry for help and your code looks like one too.",
    "you have the problem-solving instincts of a wet paper towel.",
    "imagine peaking in life by refreshing a localhost page. couldn't be me. is you though.",
    "your code reviews must feel like funerals for everyone involved.",
    "you type semicolons in python. i can tell. i can SMELL it on you.",
    "you've opened 14 stackoverflow tabs and the answer is still gonna be 'wrong question'.",
    "you're the human equivalent of a merge conflict no one wants to resolve.",
    "i bet you say 'it works on my machine' and mean it as a personality trait.",
    "your variable names are 'x', 'x1', 'xx', and 'finalx_FINAL'. seek help.",
    "you ctrl+c, ctrl+v'd your way into this career and we all know it.",
    "every time you push to main god kills a junior dev's motivation.",
    "your code has more nested if-statements than you have friends. and that's saying something.",
    "you're not built different. you're just built wrong.",
    "your linter filed a noise complaint.",
    "you debug by adding print statements and calling it 'methodology'.",
    "you opened devtools once and now you call yourself 'technical'.",
    "you're the reason rubber ducks unionized.",
    "imagine being outsmarted by your own regex. weekly.",
]

@app.get("/", response_class=HTMLResponse)
def roast():
    insult = random.choice(insults)
    return f"""
    <html>
        <head><title>meanie</title></head>
        <body style="background:#111; color:#ff4444; font-family:monospace; 
                     display:flex; align-items:center; justify-content:center; 
                     height:100vh; margin:0; text-align:center; padding:20px;">
            <h1>{insult}</h1>
        </body>
    </html>
    """