from src.model.predict import is_malicious

test_cases = [
    "Normal traffic: user=admin&pass=123",
    "SELECT * FROM users WHERE id = 1",
    "<script>alert('Hacked')</script>",
    "Benchmark(1000000) to test response time",
]

for text in test_cases:
    result = is_malicious(text)
    print(f"Input: {text}\nMalicious: {result}\n")
