from flask import Flask, request

app = Flask(__name__)
print(app.template_folder)
from app import views

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/gen-pass/<int:pass_len>/<int:pass_count>', 'gen_pass', views.gen_pass)
