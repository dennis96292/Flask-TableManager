# Flask Table Manager 🚀  
## Inspired by Andy Huang

📊 **A modern and lightweight table management system built with Flask.**  
🔒 Secure, 🌙 Dark Mode, ⚡ Fast, 💾 Persistent.  

---

## ✨ Features  
✔ **User Authentication** (Admin & Regular Users)  
✔ **Add, Edit, Delete** rows & columns dynamically  
✔ **Data Persistence** with SQLite  
✔ **Modern Dark UI** (Built with Bootstrap)  
✔ **Auto-refresh Table Data** (Ensures real-time updates)  

---

## 🔦 Tech Stack  
- **Backend:** Flask + SQLite  
- **Frontend:** HTML, CSS (Bootstrap), JavaScript  
- **Deployment:** Works in **Offline Linux Bash Environment**  

---

## 🔐 Default Credentials  
| Role  | Username | Password  |
|--------|----------|-----------|
| Admin  | admin    | 123456    |

> **Note:** The admin password is stored as a hashed password using `werkzeug.security.generate_password_hash()`.

---

## 📂 Project Directory Structure  
```
TABLE_HTML/
️│── instance/
️│   ├── database.db                # SQLite Database
️│── packages/                      # Downloaded Python dependencies (offline installation)
️│── templates/                      # HTML Templates
️│   ├── admin_login.html
️│   ├── edit.html
️│   ├── login.html
️│   ├── register.html
️│   └── table.html
️│── venv/                           # Python Virtual Environment (ignored by Git)
️│── .gitignore                       # Files to be ignored by Git
️│── app.py                           # Main Flask Application
️│── LICENSE                          # License Information
️│── README.md                        # Project Documentation
️│── requirements.txt                  # Required Python Packages
```

---

## 📄 Pages & Features  

### 🏠 `table.html` (Main Page - Table Display)
- **功能：**  
  - 讀取 `/api/load` 來顯示表格數據  
  - 每 **5 秒** 自動更新數據
  - 提供 **"前往編輯"** 按鈕，進入編輯頁面

- **按鈕功能：**  
  - `前往編輯` 🔹 **連結至 `/edit` 頁面**，用於修改表格數據  

---

### 🔑 `login.html` (User Login Page)
- **功能：**  
  - 讓使用者登入以便修改表格  
  - 若帳號/密碼錯誤，則顯示錯誤訊息

- **按鈕功能：**  
  - `回首頁` 🔹 **返回 `/` 主頁**  
  - `登入` 🔹 **提交登入表單**  

---

### 🔑 `admin_login.html` (Admin Login Page)
- **功能：**  
  - 讓 **Admin** 登入以管理使用者帳號  
  - 需輸入 **admin** 帳號和密碼  

- **按鈕功能：**  
  - `回首頁` 🔹 **返回 `/` 主頁**  
  - `登入` 🔹 **提交管理員登入請求**  

---

### 👥 `register.html` (User Management Page)
- **功能：**  
  - 讓 **Admin** 管理所有帳號  
  - 允許 **新增**、**刪除** 帳號（`admin` 無法刪除）

- **按鈕功能：**  
  - `登出` 🔹 **返回 `/` 主頁並登出**  
  - `刪除` 🔹 **刪除選定帳號**  
  - `新增` 🔹 **新增新帳號**  

---

### 🖊️ `edit.html` (Table Editing Page)
- **功能：**  
  - 允許使用者 **修改表格內容**  
  - **新增/刪除** 行與列  
  - **儲存變更至資料庫**  

- **按鈕功能：**  
  - `刪除最後一列` 🔹 **刪除表格最後一行**  
  - `新增列` 🔹 **新增一行**  
  - `新增行` 🔹 **新增一列**  
  - `刪除最後一行` 🔹 **刪除表格最後一列**  
  - `完成` 🔹 **儲存變更**  
  - `取消` 🔹 **取消修改並返回 `/`**  

---

## 🚀 Setup & Run  

### 🏛️ 1. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 🔧 2. Run Flask App  
```bash
python app.py
```

### 🌍 3. Open in Browser  
```bash
http://127.0.0.1:5000
```

---

## 📸 UI Preview  
🌙 **Dark & Modern Interface**  
 

---

## 📝 License  
🌍 This project is licensed under the **MIT License**.  

---

### 🌟 **Star the Repo if you like it!** ⭐  
💬 Feel free to contribute or report issues. 🚀  

