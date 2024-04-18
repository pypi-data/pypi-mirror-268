# Basics
PyHTML is an implementation to run Python in a Proton app, similar to Brython.
A python script is defined using the `text/python` MIME type, applied to a script.

Example:
``` {.html linenums="1" title="Hello, World!"}
<script type=text/python>
    print("Hello, World!")
</script>
```
Each script is ran once the backend (PyWebview) loads.