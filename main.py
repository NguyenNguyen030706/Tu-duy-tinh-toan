# main.py
import http.server
import socketserver
import os

# --- Cấu hình ---
PORT = 8000  # Bạn có thể đổi cổng nếu muốn, ví dụ: 8080, 3000
# -----------------

# Lấy đường dẫn thư mục nơi file main.py đang chạy
WEB_DIR = os.path.dirname(os.path.abspath(__file__))

# Chuyển vào thư mục đó để server biết nơi lấy file
os.chdir(WEB_DIR)

# Thiết lập handler để phục vụ file
Handler = http.server.SimpleHTTPRequestHandler

try:
    # Khởi tạo server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Máy chủ đang chạy tại http://localhost:{PORT}")
        print("   Nhấn Ctrl+C để dừng máy chủ.")
        
        # Giữ máy chủ chạy mãi mãi cho đến khi bị ngắt (Ctrl+C)
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\n[INFO] Đã dừng máy chủ.")
except OSError as e:
    if e.errno == 98: # Mã lỗi "Address already in use"
        print(f"[LỖI] Cổng {PORT} đã được sử dụng.")
        print("   Vui lòng chọn một cổng khác trong file main.py hoặc dừng chương trình đang dùng cổng đó.")
    else:
        print(f"[LỖI] {e}")