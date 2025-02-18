# Let's use binary search to find posts on a dictionary using their timestamps.

def find_post_by_timestamp(posts, target_timestamp):
    if not posts:
        return None
    
    start = 0
    end = len(posts) - 1
    
    
    while start <= end:
        mid = (start + end) // 2
        if posts[mid]["timestamp"] == target_timestamp:
            return posts[mid]
        if posts[mid]["timestamp"] < target_timestamp:
            start = mid + 1
        else:
            end = mid - 1
    
    return f"Post with timestamp {target_timestamp} not found"

# test cases
posts = [
    {"timestamp": 1000, "content": "First post!"},
    {"timestamp": 1500, "content": "Having lunch"},
    {"timestamp": 2000, "content": "Coding is fun"},
    {"timestamp": 2500, "content": "Going home"}
]
print(find_post_by_timestamp(posts, 1500))  # Should return {"timestamp": 1500, "content": "Having lunch"}
print(find_post_by_timestamp(posts, 3000))  # Post with timestamp 3000 not found
print(find_post_by_timestamp([], 1000))  # None

def binary_search_by_key(items, target, key_func):
    if not items:
        return None
    
    start = 0
    end = len(items) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if key_func(items[mid]) == target:
            return items[mid]
        if key_func(items[mid]) < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return f"Item with key {target} not found"

# test cases
# Test data with multiple fields
posts = [
    {"timestamp": 1000, "author": "Alice", "likes": 5, "content": "First post!"},
    {"timestamp": 1500, "author": "Bob", "likes": 10, "content": "Hello world"},
    {"timestamp": 2000, "author": "Charlie", "likes": 15, "content": "Python rules"},
    {"timestamp": 2500, "author": "David", "likes": 20, "content": "Binary search!"}
]

# Test cases
def run_tests():
    # Test 1: Search by timestamp
    print("Test 1: Search by timestamp")
    result = binary_search_by_key(posts, 1500, lambda x: x["timestamp"])
    print(f"Expected: Bob's post, Got: {result}")

    # Test 2: Search non-existent timestamp
    print("\nTest 2: Search non-existent timestamp")
    result = binary_search_by_key(posts, 1750, lambda x: x["timestamp"])
    print(f"Expected: None, Got: {result}")

    # Test 3: Empty list
    print("\nTest 3: Empty list")
    result = binary_search_by_key([], 1000, lambda x: x["timestamp"])
    print(f"Expected: None, Got: {result}")

    # Test 4: Search by likes (assuming sorted by likes)
    posts_by_likes = sorted(posts, key=lambda x: x["likes"])
    print("\nTest 4: Search by likes")
    result = binary_search_by_key(posts_by_likes, 15, lambda x: x["likes"])
    print(f"Expected: Charlie's post, Got: {result}")

run_tests()