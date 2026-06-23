import webview 

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" >
    <title></title>
</head>
<style>
    body {
        background: whitesmoke;
        color: black;
        font-family: sans-serif;
        font-size: medium;
        font-weight: bolder;
        font-style: initial;
        padding: 0;
        margin: 0;
        max-width: 1920px;
        width: 100%;
        max-height: 1080px;
        height: 100%;
    }
</style>
<body>
    <input id="fl" type="file" />
    <br><br>

    <video id="pl" width="800" height="600" ></video>
</body>
<script>
    const fl = document.getElementById("fl");
    const pl = document.getElementById("pl");

    const file = this.files[0];
    fl.addEventListener("change", function () {
        if (file) {
            const url = URL.createObjectURL(file);
            pl.src = url;
            pl.play();
        }
    });
</script>
</html>
"""

def script():
    webview.create("UI", html=html)
    webview.run()
