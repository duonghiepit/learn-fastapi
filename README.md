# FastAPI

Kho lưu trữ này chứa các ví dụ và hướng dẫn chi tiết về việc sử dụng FastAPI với các hệ quản trị cơ sở dữ liệu và xây dựng API cơ bản. Bao gồm:

1. **FastAPI với PostgreSQL** - Kết nối và làm việc với PostgreSQL.
2. **FastAPI với MongoDB** - Sử dụng MongoDB làm cơ sở dữ liệu.
3. **RESTful API với FastAPI** - Xây dựng RESTful API cơ bản.

---

## Yêu cầu hệ thống
- Python 3.10 hoặc mới hơn
- PostgreSQL 15 hoặc mới hơn (cho PostgreSQL)
- MongoDB Community Edition (cho MongoDB)
- pip (công cụ quản lý gói Python)

---

## FastAPI với PostgreSQL

### Bước 1: Tạo môi trường ảo
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

### Bước 2: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

### Bước 3: Thiết lập cấu hình kết nối PostgreSQL
1. **Chỉnh sửa file `database.py`:**
   ```python
   URL_DATABASE = 'postgresql://<username>:<password>@localhost:5432/<database_name>'
   ```

2. **Tạo database trong PostgreSQL:**
   ```sql
   CREATE DATABASE QuizApplication;
   ```

### Bước 4: Chạy ứng dụng FastAPI
1. **Khởi chạy ứng dụng:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Kiểm tra API:**
   - **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## FastAPI với MongoDB

### Bước 1: Cài đặt MongoDB
- Tải và cài đặt **MongoDB Community Edition** từ [mongodb.com](https://www.mongodb.com/try/download/community).
- Chạy MongoDB trên cổng mặc định `27017`.

### Bước 2: Cài đặt thư viện kết nối MongoDB
```bash
pip install motor pymongo
```

### Bước 3: Thiết lập kết nối MongoDB
1. Mở file `database.py` trong thư mục `fastapi_mongo` và thay đổi cấu hình kết nối MongoDB. 

2. Để cấu hình với MongoDB Atlas (kết nối cloud), thay đổi `MONGO_URL` trong file như sau:
   ```python
   client = MongoClient(
       "mongodb+srv://<username>:<password>@<clustername>.dswr0.mongodb.net/?retryWrites=true&w=majority&appName=<database_name>"
   )
   ```

   - **Thay đổi các thông tin sau:**
     - `<username>`: Tài khoản MongoDB của bạn (ví dụ: `admin`).
     - `<password>`: Mật khẩu tương ứng (ví dụ: `admin`).
     - `<database_name>`: Tên cơ sở dữ liệu MongoDB (ví dụ: `FastAPI`).

3. Để kết nối với MongoDB cục bộ (local), thay đổi `MONGO_URL` thành:
   ```python
   MONGO_URL = "mongodb://localhost:27017"
   ```

4. Nếu chưa tạo database hoặc collection, sử dụng script hoặc MongoDB CLI để khởi tạo.

### Bước 4: Chạy ứng dụng
1. **Chạy ứng dụng:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Kiểm tra API MongoDB:**
   - **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## RESTful API với FastAPI

### Mô tả
Thư mục `restful_api` cung cấp ví dụ về cách xây dựng RESTful API cơ bản với FastAPI. Bao gồm các thao tác CRUD (Create, Read, Update, Delete) trên một đối tượng đơn giản như "User" hoặc "Item".

### Bước 1: Tạo môi trường ảo
Thực hiện các bước tương tự như phần PostgreSQL.

### Bước 2: Cài đặt các thư viện cần thiết
```bash
pip install fastapi uvicorn
```

### Bước 3: Chạy ứng dụng
1. Chạy ứng dụng trong thư mục `restful_api`:
   ```bash
   uvicorn main:app --reload
   ```

2. **Kiểm tra API:**
   - **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Lưu ý
- Các thư viện cần thiết được quản lý trong file `requirements.txt`. Để cài đặt lại:
  ```bash
  pip install -r requirements.txt
  ```
- Đảm bảo các dịch vụ cơ sở dữ liệu (PostgreSQL hoặc MongoDB) đang hoạt động trước khi chạy ứng dụng.

---

Chúc bạn học tập và làm việc hiệu quả với FastAPI!
```

Nếu bạn cần chỉnh sửa thêm hoặc thêm phần nào khác, hãy cho mình biết nhé! 😊