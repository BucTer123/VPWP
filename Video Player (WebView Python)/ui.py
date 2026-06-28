import webview 

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" >
    <title></title>
</head>
<body>
</body>
<script type="module">
  import kaboom from "https://unpkg.com/kaboom@3000.0.1/dist/kaboom.mjs";

  kaboom();

  kaboom({
      background: [140, 70, 130]
  })

  add ([
      text("Welcome!");
      pos(120, 70);
  ])

  function addButton(txt, p, f) {
      const btn = add ([
          rect(240, 80 {radius : 8}),
          pos(p),
          area(),
          anchor("center"),
          outline(4),
     ])

     btn.add ([
         text(txt),
         anchor("center"),
         color(0, 0, 0),
     ])

     btn.onHoverUpdate(() => {
         const t = time() * 10
         btn.color = hsl2rgb((t / 10) % 1, 0.6, 0.7);
         btn.scale = vec2(1.2)
         setCursor("pointe");
     })

     btn.onHoverEnd(() => {
         btn.scale = vec(1.2)
         btn.color = rgb()
     })

     btn.onClick(f)

     return btn
  }

  addButtton("Start", vec2(200, 100), () => window.location.href = "audio.html")
  addButton("Settings", vec2(200, 200), () => window.location.href = "settings.html")
  addButton("Site Kaboom.js", vec2(200, 300), () => window.location.href = "https://kaboomjs.com")
  addButton("Exit", vec2(200, 400), () => debug.log("Nope"))
</script>
</html>
"""

def script():
    webview.create("UI", html=html)
    webview.run()
