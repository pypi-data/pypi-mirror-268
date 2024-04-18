import webview as wv
class Document:
    def __init__(self, window):
        self.webview: wv.Window = window.webview
    @property
    def body(self):
        """Returns the <body> object."""
        return self.querySelector("body")
    @property
    def head(self):
        """Returns the <head> object."""
        return self.querySelector("head")
    def querySelector(self, selector):
        """Returns the first object that matches the selector."""
        return self.webview.dom.get_elements(selector)[0]
    def querySelectorAll(self, selector):
        """Returns all of the objects that match the selector."""
        return self.webview.dom.get_elements(selector)
    @property
    def characterSet(self):
        """Returns the character set."""
        return self.webview.evaluate_js("document.characterSet")
    @property
    def childElementCount(self):
        """Returns the number of children that the Document has. Usually 1."""
        return self.webview.evaluate_js("document.childElementCount")
    @property
    def children(self):
        """Returns the children that the Document has. Usually just 1."""
        return self.webview.evaluate_js("document.children")
    @property
    def compatMode(self):
        """Returns BackCompat if quirks mode is enabled, and CSS1Compat if quirks is disabled."""
        return self.webview.evaluate_js("document.compatMode")
    @property
    def contentType(self):
        """Returns the MIME type of the current page."""
        return self.webview.evaluate_js("document.contentType")
     #TODO: Implement cookie, currentScript, defaultView, designMode and dir.
    @property
    def doctype(self):
        """Returns the Document Type Declaration (DTD) in a dict."""
        return self.webview.evaluate_js("document.doctype")
    @property
    def documentElement(self):
        """Returns the <html> object."""
        return self.querySelector("html")
    @property
    def documentURI(self):
        """Returns the current URI of the page."""
        return self.doctype["baseURI"]
    #TODO: Implement embeds
    @property
    def firstElementChild(self):
        """Returns the <html> object."""
        return self.querySelector("html")
    #TODO: Implement fonts+
    def append(self, element):
        """Appends an object to the document. Accepts any object with an __str__ function."""
        self.webview.dom.document.append(element)
    def createElement(self, html):
        """Creates an element."""
        return self.webview.dom.create_element(html)
    #TODO: Implement createElementNS
    def getElementById(self, id):
        """Returns the elements with the specified name."""
        return self.webview.dom.get_element("#" + id)
    def getElementsByName(self, name):
        """Returns the elements with the specified name."""
        return self.webview.dom.get_elements(f"[name={name}]")
    #TODO: Implement getElementsByTagName(NS)
