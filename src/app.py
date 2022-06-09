
from flask import Flask, jsonify
from collections import Counter


app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def ping():
#     return jsonify({"response": "hello world"})

@app.route('/')
def main():
    str = (input('enter a word \n'))

    length = len(str)
    stringLower= str.lower()
    makingSplit = stringLower.split()
    finalString = "".join(makingSplit)
    reverseString = ''.join(reversed(finalString))
    collection = Counter(stringLower)


    if finalString == reverseString:

        return jsonify(name=str,
                       palindrome=True,
                       length= length,
                       sorted= collection)
    else:
        return jsonify(name=str,
                       palindrome=False)





if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=4000, debug=True)

