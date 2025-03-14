import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash  # 🔹 加密密碼

app = Flask(__name__)

# 🔹 設定 SQLite 資料庫
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)  # 產生隨機密鑰

db = SQLAlchemy(app)

# 🔹 定義帳號管理模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

# 🔹 定義表格數據模型
class TableData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)

# 🔹 初始化資料庫（如果沒有 `database.db` 則建立）
with app.app_context():
    db.create_all()
    # 確保 admin 帳號存在
    if not User.query.filter_by(username="admin").first():
        admin_user = User(username="admin", password=generate_password_hash("cts20516997"))
        db.session.add(admin_user)
        db.session.commit()

# 🔹 瀏覽頁面
@app.route('/')
def index():
    return render_template('table.html')

# 🔹 檢查登入狀態
@app.route('/api/check_login')
def check_login():
    return jsonify({"logged_in": 'user' in session})

# 🔹 使用者登入
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user'] = username
            return redirect(url_for('edit'))

        return render_template('login.html', error="帳號或密碼錯誤")

    return render_template('login.html')

# 🔹 管理員登入（進入帳號管理頁面）
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin":
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                session['user'] = "admin"
                return redirect(url_for('register'))

        return render_template('admin_login.html', error="帳號或密碼錯誤")

    return render_template('admin_login.html')

# 🔹 帳號管理頁面
@app.route('/register')
def register():
    if 'user' not in session or session['user'] != "admin":
        return redirect(url_for('admin_login'))
    return render_template('register.html')

# 🔹 取得所有帳號
@app.route('/api/get_accounts')
def get_accounts():
    users = User.query.all()
    accounts = [{"username": user.username, "password": "******" if user.username == "admin" else user.password} for user in users]
    return jsonify(accounts)

# 🔹 新增帳號
@app.route('/api/add_account', methods=['POST'])
def add_account():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"success": False, "message": "帳號與密碼不可為空"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"success": False, "message": "該帳號名稱已被使用"}), 400

    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "帳號新增成功"})

# 🔹 刪除帳號
@app.route('/api/delete_account/<username>', methods=['DELETE'])
def delete_account(username):
    if username == "admin":
        return jsonify({"status": "error", "message": "無法刪除 admin"}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"status": "success"})

    return jsonify({"status": "error", "message": "帳號不存在"}), 404

# 🔹 載入表格數據
@app.route('/api/load', methods=['GET'])
def load_data():
    entry = TableData.query.first()
    return jsonify(entry.data if entry else {"headerOrder": [], "tableData": []})

# 🔹 儲存表格數據
@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.json
    if not data or 'tableData' not in data or 'headerOrder' not in data:
        return jsonify({"status": "error", "message": "Invalid data format"}), 400

    TableData.query.delete()
    db.session.add(TableData(data=data))
    db.session.commit()

    return jsonify({"status": "success"})

# 🔹 編輯頁面
@app.route('/edit')
def edit():
    return render_template('edit.html')

# 🔹 登出
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
