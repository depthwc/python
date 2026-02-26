from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3), reraise=True)
def test_function():
    print("Trying...")
    raise Exception("Error!")

test_function() 