from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # <-- Add this line
df = pd.read_csv('metaphysics.csv')  # Your CSV file

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    message = data.get('message', '').lower()
    message_words = set(message.split())
    best_count = 0
    best_sentences = []

    for _, row in df.iterrows():
        sentence = str(row['sentence']).lower()
        sentence_words = set(sentence.split())
        match_count = len(message_words & sentence_words)
        if match_count > best_count:
            best_count = match_count
            best_sentences = [row['sentence']]
        elif match_count == best_count and match_count > 0:
            best_sentences.append(row['sentence'])

    # Only return if there is at least one match
    if best_count > 0:
        return jsonify([{'sentence': s} for s in best_sentences])
    else:
        return jsonify([])

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



# # commit 3 - successfully returns matched philosophy quotes - 01-06-25
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)  # <-- Add this line
# df = pd.read_csv('metaphysics.csv')  # Your CSV file

# @app.route('/search', methods=['POST'])
# def search():
#     data = request.json
#     message = data.get('message', '').lower()
#     message_words = set(message.split())
#     best_count = 0
#     best_sentences = []

#     for _, row in df.iterrows():
#         sentence = str(row['sentence']).lower()
#         sentence_words = set(sentence.split())
#         match_count = len(message_words & sentence_words)
#         if match_count > best_count:
#             best_count = match_count
#             best_sentences = [row['sentence']]
#         elif match_count == best_count and match_count > 0:
#             best_sentences.append(row['sentence'])

#     # Only return if there is at least one match
#     if best_count > 0:
#         return jsonify([{'sentence': s} for s in best_sentences])
#     else:
#         return jsonify([])

# if __name__ == '__main__':
#     app.run(debug=True)




## commit 2 - searches but returns too many blank results - 01-06-25
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)  # <-- Add this line
# df = pd.read_csv('metaphysics.csv')  # Your CSV file

# @app.route('/search', methods=['POST'])
# def search():
#     data = request.json
#     message = data.get('message', '').lower()
#     results = []
#     for _, row in df.iterrows():
#         sentence = str(row['sentence']).lower()
#         if any(word in sentence for word in message.split()):
#             results.append({'sentence': row['sentence']})
#     return jsonify(results)

# if __name__ == '__main__':
#     app.run(debug=True)


## commit 1 - searches but returns no results - 01-06-25
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)  # <-- Add this line
# df = pd.read_csv('metaphysics.csv')  # Your CSV file

# @app.route('/search', methods=['POST'])
# def search():
#     data = request.json
#     message = data.get('message', '').lower()
#     # Example: search for rows where any cell contains a term from the message
#     results = []
#     for _, row in df.iterrows():
#         for cell in row:
#             if str(cell).lower() in message:
#                 results.append(row.to_dict())
#                 break
#     return jsonify(results)

# if __name__ == '__main__':
#     app.run(debug=True)