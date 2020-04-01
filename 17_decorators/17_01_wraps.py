'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def wrap_in_tag(html):
    def decoration():
        return f"<p>{html()}</p>"
    return decoration

@wrap_in_tag
def html():
    return "Hello world"

print(html())