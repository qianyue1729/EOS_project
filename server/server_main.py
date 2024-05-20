from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'F:\\course\\信息安全编程\\project\\server\\uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        print(filepath)
        return jsonify({'message': 'File uploaded successfully', 'file': filepath}), 200
    
@app.route('/get_files', methods=['GET'])
def get_files():
    search_type = request.args.get('type')
    search_value = request.args.get('value')
    
    if not search_type or not search_value:
        return jsonify([])

    # 根据搜索类型和搜索值进行过滤
    filtered_files = [
        file for file in files
        if file[search_type].lower().find(search_value.lower()) != -1
    ]
    
    return jsonify(filtered_files)

if __name__ == '__main__':
    app.run(host = "10.122.223.44",port=1234)
