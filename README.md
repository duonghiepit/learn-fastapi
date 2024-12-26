# FastAPI với PostgreSQL

## Yêu cầu hệ thống
- Python 3.10 hoặc mới hơn
- PostgreSQL 15 hoặc mới hơn
- pip (công cụ quản lý gói Python)

---

## Bước 1: Tạo môi trường ảo
1. **Tạo môi trường ảo:**
   ```bash
   python -m venv env
   ```

2. **Kích hoạt môi trường ảo:**
   - **Windows:**
     ```bash
     .\env\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source env/bin/activate
     ```

---

## Bước 2: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

---

## Bước 3: Thiết lập cấu hình kết nối PostgreSQL
1. **Chỉnh sửa file kết nối:**
   Mở file ```database.py``` chứa cấu hình database và thay đổi các thông số sau:

   ```python
   # Đường dẫn kết nối tới PostgreSQL
   URL_DATABASE = 'postgresql://<username>:<password>@localhost:5432/<database_name>'
   ```

   - `<username>`: Tên người dùng PostgreSQL (mặc định là `postgres`).
   - `<password>`: Mật khẩu của bạn (ví dụ: `admin123`).
   - `<database_name>`: Tên cơ sở dữ liệu bạn muốn kết nối (ví dụ: `QuizApplication`).

2. **Tạo database trong PostgreSQL:**
   Sử dụng lệnh SQL sau để tạo database nếu chưa có:
   ```sql
   CREATE DATABASE QuizApplication;
   ```

---

## Bước 4: Chạy ứng dụng FastAPI
1. **Khởi chạy ứng dụng:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Kiểm tra API:**
   - **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Endpoint mặc định:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Lưu ý
- Đảm bảo PostgreSQL đã chạy và database tồn tại trước khi khởi chạy ứng dụng.
- Để lưu các thư viện đã cài đặt:
  ```bash
  pip freeze > requirements.txt
  ```
- Để cài đặt lại thư viện trong môi trường khác:
  ```bash
  pip install -r requirements.txt
  ```

Chúc bạn thành công!