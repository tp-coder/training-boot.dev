# Doc2Doc makes using markdown a breeze. This includes adding images to markdown documents.
# 
# 1. Complete the create_markdown_image function using currying. It takes a string input, 
# alt_text, and returns an inner function.
#  - It should enclose the alt_text in square brackets prefixed with an exclamation point ![alt_text].
# 
# 2. Create the inner function returned by create_markdown_image. It also takes a string input, 
# url, and returns an innermost function.
#  - The inner function should first escape any parentheses in the URL by replacing them with encoded sequences.
#    - Use the .replace() string method to change any opening parenthesis ( into %28.
#    - Do the same to change any closing parenthesis ) into %29.
#  - Enclose the url with parentheses (url).
#  - Add the enclosed url to the end of the enclosed alt_text: ![alt_text](url)
#
# 3. Create the innermost function returned by the inner function. It should take an optional string 
# input for the title.
#  - If a title is passed:
#    - Enclose it in double quotes.
#    - Then add the quoted title to the image syntax by first removing the closing parenthesis ) from the end of the image syntax.
#    - Add a space and the quoted title with a closing parenthesis ) to the end of the image syntax: ![alt_text](url "title")
#  - Return the finished image syntax.

def create_markdown_image(alt_text):

    def create_mkdown_image_url(url):
        mkdown_url = url.replace("(", "%28").replace(")", "%29")

        def create_mkdown_image_title (title=""):
            nonlocal alt_text, mkdown_url
            if title == "":
                return f'![{alt_text}]({mkdown_url})'
            return f'![{alt_text}]({mkdown_url} "{title}")'

        return create_mkdown_image_title
    
    return create_mkdown_image_url

alt_text = "seal"
url = "https://imgur.com/oglPAXK"
title = "this is a seal"
test = create_markdown_image(alt_text)(url)(title)
print(test)

alt_text1 = "seal"
url1 = "https://imgur.com/(oglPAXK)"
test1 = create_markdown_image(alt_text1)(url1)()
print(test1)

