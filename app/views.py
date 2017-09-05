from flask import render_template

from app.utils import id_generator

def index():
    return render_template('index.html')

def gen_pass(pass_len, pass_count):
    context = {
        "passwords": [id_generator(pass_len) for i in range(pass_count)],
        "pass_len": pass_len,
        "pass_count": pass_count,
    }
    return render_template('passwords.html', context=context)
