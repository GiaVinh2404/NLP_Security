from src.data_collector.file_reader import process_log_file

# Giả lập file log
test_log = """
Normal login: user=admin&pass=123
SELECT * FROM users WHERE id = 1
<script>alert('XSS')</script>
Benchmark(1000000) test case
""".strip()

# Ghi file log giả lập
log_path = "test_log.txt"
with open(log_path, "w", encoding="utf-8") as f:
    f.write(test_log)

# Đọc và kiểm tra log
process_log_file(log_path)
