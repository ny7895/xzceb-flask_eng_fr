from machinetranslation import translator
from flask import flask, render_template, request
import json

app = flask("Web Translator")

@app.route(/englishToFrench)
    def englishToFrench():

            textToTranslate = request.args.get("Text to Translate")
            english_text= translator.french_to_english(textToTranslate)
        return english_text

@app.route(/frenchToEnglish)
    def englishToFrench():

            textToTranslate = request.args.get("Text to Translate")
            french_text= translator.english_to_french(textToTranslate)
        return french_text  

@app.route("/")
    def renderindexpage():

            return render_template("index.html")

if __name__ == "__main__":
    
        app.run(host="0.0.0.0", port=8080)