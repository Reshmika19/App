# python
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from jinja2 import Template

app = FastAPI()

# Template string for the form page (includes simple CSS)
template_form = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Enter Name</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f3f4f6; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .card { background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); width: 320px; }
    h1 { font-size: 20px; margin: 0 0 12px 0; color: #111827; }
    form { display: flex; flex-direction: column; gap: 12px; }
    input[type="text"] { padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; }
    button { padding: 10px; background: #2563eb; color: white; border: none; border-radius: 6px; cursor: pointer; }
    button:hover { background: #1e40af; }
  </style>
</head>
<body>
  <div class="card">
    <h1>What's your name?</h1>
    <form action="/submit" method="post">
      <input type="text" name="name" placeholder="Enter your name" required>
      <button type="submit">Submit</button>
    </form>
  </div>
</body>
</html>
"""

# Template string for the welcome page
template_welcome = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Welcome</title>
  <style>
    body { font-family: Arial, sans-serif; background: linear-gradient(135deg,#eef2ff,#f0fdf4); display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .card { background: #ffffffcc; padding: 28px; border-radius: 10px; box-shadow: 0 6px 20px rgba(0,0,0,0.08); text-align: center; }
    h1 { margin: 0 0 8px 0; color: #0f172a; }
    p { margin: 0; color: #334155; }
    a { display:inline-block; margin-top:12px; color:#2563eb; text-decoration:none; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Welcome, {{ name }}!</h1>
    <p>Glad to see you here.</p>
    <a href="/">Go back</a>
  </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_form():
    tmpl = Template(template_form)
    return tmpl.render()

@app.post("/submit", response_class=HTMLResponse)
async def submit(name: str = Form(...)):
    tmpl = Template(template_welcome)
    # Note: Template.render safely substitutes the value. If you need autoescaping for user content, consider using Jinja2 Environment with autoescape enabled.
    return tmpl.render(name=name)
