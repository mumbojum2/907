from flask import Flask, render_template, request
import openai


app = Flask(__name__)

openai.api_key = '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
'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

