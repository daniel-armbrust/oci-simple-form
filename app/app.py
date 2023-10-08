#
# app.py
#

from secrets import token_hex

from flask import Flask, render_template, redirect, url_for, flash, request
from forms import PesquisaForm

from nosql import Nosql

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(24)

@app.route('/', methods=['GET', 'POST'])
def pesquisa_form():
    """Exibe o formulário de pesquisa."""
    form = PesquisaForm()

    if request.method == 'POST':
        if form.validate_on_submit():   
            values = form.data

            # Remove o token de proteção do formulário submetido.
            del values['csrf_token']
                      
            nosql = Nosql()
            nosql.add(values)

            return redirect(url_for('obrigado'))
        else:            
            flash('Erro ao processar os dados do formulário.')

    return render_template('form.html', form=form)


@app.route('/obrigado', methods=['GET'])
def obrigado():    
    return render_template('obrigado.html')