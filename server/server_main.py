from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import yaml
import os
import hashlib

app = Flask(__name__)

# 配置数据库
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

# 设定文件上传的目录
UPLOAD_FOLDER = 'F:/second class of junior/EOS_project/server/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 登录路由
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    cur.close()
    if user:
        return jsonify({"success": True, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

# 注册路由
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE username=%s", (username,))
    if cur.fetchone():
        return jsonify({"success": False, "message": "Username already exists"}), 400
    cur.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
    mysql.connection.commit()
    cur.close()
    return jsonify({"success": True, "message": "Registration successful"}), 201

# 文件上传路由
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    user_id = request.form['user_id']
    if file and file.filename:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        filehash = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO file (filename, filepath, user_id, filehash) VALUES (%s, %s, %s, %s)",
                    (filename, filepath, user_id, filehash))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 200
    else:
        return jsonify({'error': 'No selected file'}), 400

# 获取文件路由
@app.route('/files', methods=['GET'])
def get_files():
    user_id = request.args.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM file WHERE user_id=%s", [user_id])
    files = cur.fetchall()
    cur.close()
    return jsonify(files)

@app.route('/verify_file', methods=['POST'])
def verify_file():
    # Check if the file and hash were provided
    if 'file' not in request.files or 'hash' not in request.form:
        return jsonify({'error': 'File or hash not provided'}), 400

    file = request.files['file']
    provided_hash = request.form['hash']

    # Save the file temporarily
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Calculate the file's MD5 hash
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    calculated_hash = hash_md5.hexdigest()

    # Compare the calculated hash against the provided hash
    if calculated_hash == provided_hash:
        result = "Hash match"
    else:
        result = "Hash mismatch"

    # Remove the temporary file to clean up
    os.remove(file_path)

    return jsonify({'result': result, 'calculated_hash': calculated_hash, 'provided_hash': provided_hash})


if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# import os
# import hashlib

# app = Flask(__name__)
# CORS(app)

# # 配置数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# UPLOAD_FOLDER = 'F:\\course\\信息安全编程\\project\\server\\uploads'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # 定义数据库模型
# class File(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     filename = db.Column(db.String(120), nullable=False)
#     filepath = db.Column(db.String(200), nullable=False)
#     user_id = db.Column(db.String(120), nullable=False)
#     data_id = db.Column(db.String(120), nullable=False)
#     block_id = db.Column(db.String(120), nullable=False)
#     filehash = db.Column(db.String(120), nullable=False)
# # 创建数据库表
# with app.app_context():
#     db.create_all()

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     ###test###
#     #print(type(request))
#     #print(request.data)
#     #print(request.files)
#     print(request.form['username'])
#     ##########
#     # if 'file' not in request.files or 'user_id' not in request.form:
#     #     return jsonify({'error': 'No file part or user_id'}), 400


#     file = request.files['file']
#     user_id = request.form['username']
#     ###test###
#     data_id = "1"
#     block_id = "1"
#     filehash = "123"
#     ##########
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     if file:
#         filename = file.filename
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
        
#         # 保存文件信息到数据库
#         new_file = File(filename=filename, 
#                         filepath=filepath, 
#                         user_id=user_id,
#                         data_id = data_id,
#                         block_id = block_id,
#                         filehash = filehash)
#         db.session.add(new_file)
#         db.session.commit()

#         #return jsonify({'message': 'File uploaded successfully', 'file': filepath}), 200
#         return "上传成功"

# @app.route('/get_files', methods=['GET'])
# def get_files():
#     #####test######
#     print(request.args)
#     ###############
#     search_type = request.args.get('searchtype')
#     search_value = request.args.get('searchValue')
#     user_id = request.args.get('username')
    

#     if not search_type or not search_value or not user_id:
#         return jsonify([])

#     if search_type == '0':
#         search_column = File.data_id
#     elif search_type == '1':
#         search_column = File.block_id
#     else:
#         return jsonify([])
#     # 根据用户ID和搜索条件过滤文件
#     filtered_files = File.query.filter_by(user_id=user_id).filter(
#         search_column.like(f"%{search_value}%")
#     ).all()
#     #####test######
#     print(filtered_files[0].filename)
#     print(filtered_files[0].data_id)
#     ###############
#     # 转换结果为字典列表
#     result = [{
#         'filename': file.filename,
#         'dataId': file.data_id,
#         'blockId': file.block_id,
#         'fileHash': file.filehash
#     } for file in filtered_files]

#     return jsonify(result)
# @app.route('/verify_file', methods=['POST'])
# def verify_file():
#     if 'file' not in request.files or 'hash' not in request.form:
#         return jsonify({'error': 'File or hash not provided'}), 400

#     file = request.files['file']
#     provided_hash = request.form['hash']

#     # 保存文件到本地
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(file_path)

#     # 计算文件的哈希值
#     hash_md5 = hashlib.md5()
#     with open(file_path, 'rb') as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     calculated_hash = hash_md5.hexdigest()

#     # 对比哈希值
#     if calculated_hash == provided_hash:
#         result = "计算哈希匹配提供哈希"
#     else:
#         result = "计算哈希不匹配提供哈希"

#     # 删除本地保存的文件
#     os.remove(file_path)

#     return jsonify({'result': result, 'calculated_hash': calculated_hash, 'provided_hash': provided_hash})

# if __name__ == '__main__':
#     app.run(host="10.122.223.44", port=1234)



# from flask import Flask, request, jsonify
# from flask_mysqldb import MySQL
# import yaml

# app = Flask(__name__)

# # 配置数据库
# db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

# mysql = MySQL(app)

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json  # 使用 JSON 来获取数据
#     username = data['username']
#     password = data['password']
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
#     user = cur.fetchone()
#     cur.close()
#     if user:
#         return jsonify({"success": True, "message": "Login successful"}), 200
#     else:
#         return jsonify({"success": False, "message": "Invalid credentials"}), 401

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.json  # 使用 JSON 来获取数据
#     username = data['username']
#     password = data['password']
    
#     # 检查用户名是否已存在
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM user WHERE username=%s", (username,))
#     existing_user = cur.fetchone()
#     if existing_user:
#         return jsonify({"success": False, "message": "Username already exists"}), 400

#     # 插入新用户数据
#     cur.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
#     mysql.connection.commit()
#     cur.close()
    
#     return jsonify({"success": True, "message": "Registration successful"}), 201

# if __name__ == '__main__':
#     app.run(debug=True)
