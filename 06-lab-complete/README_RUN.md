# AI Agent Production - Lab 06

## 1. Chuẩn bị môi trường
- Cài đặt Docker và Docker Compose
- (Tùy chọn) Cài Python 3.11+ nếu muốn chạy local không dùng Docker

## 2. Cấu hình biến môi trường
- Copy file `.env.example` thành `.env.local`
- Mở `.env.local` và điền các giá trị:
  - `OPENAI_API_KEY` (nếu muốn dùng OpenAI thật)
  - `AGENT_API_KEY` (chuỗi bí mật tự tạo)
  - `JWT_SECRET` (chuỗi bí mật tự tạo)
  - Các biến khác giữ mặc định hoặc chỉnh theo nhu cầu

## 3. Chạy bằng Docker Compose
```bash
cd 06-lab-complete
# Build image
docker compose build
# Khởi động agent và redis
docker compose up
```

## 4. Kiểm tra API
- Health check:
  ```bash
  curl http://localhost:8000/health
  ```
- Gửi câu hỏi (thay <API_KEY> bằng AGENT_API_KEY trong .env.local):
  ```bash
  curl -H "X-API-Key: <API_KEY>" \
       -X POST http://localhost:8000/ask \
       -H "Content-Type: application/json" \
       -d '{"question": "Docker là gì?"}'
  ```

## 5. Chạy local không dùng Docker (tùy chọn)
```bash
cd 06-lab-complete
python -m venv .venv
.venv\Scripts\activate  # Windows
# hoặc
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 6. Kiểm tra production readiness
```bash
python check_production_ready.py
```

## 7. Deploy lên Railway/Render
- Xem hướng dẫn chi tiết trong README.md gốc hoặc file `railway.toml`, `render.yaml`.

---
**Lưu ý:**
- Đảm bảo file `.env.local` KHÔNG commit lên GitHub.
- Nếu không có `OPENAI_API_KEY`, agent sẽ trả lời mock (giả lập).
- Để dùng OpenAI thật, cần nạp đúng key và model.
