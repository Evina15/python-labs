'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def wrap_in_tag(html):
    def decoration(*args):
        return html(*args)
        html(*args)
        return html(*args)
    return decoration

@wrap_in_tag
def html(tag):
    return f"<{tag}>Hello world</{tag}>"


print(html("h1"))
