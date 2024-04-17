runpython = """

const scripts = document.querySelectorAll('script[type="text/python"]')
console.log("Python running...")
scripts.forEach(function(obj) {
    pywebview.api.evalpy(obj.textContent)
})

null"""