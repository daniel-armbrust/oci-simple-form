#
# forms.py
#

from flask_wtf import FlaskForm 
from wtforms import StringField, EmailField, RadioField, SelectField
from wtforms.validators import DataRequired, Length

class PesquisaForm(FlaskForm):
    nome = StringField(validators=[DataRequired(), Length(min=5, max=300)])        

    email = EmailField(validators=[DataRequired()])    

    esporte = RadioField(choices=[('futebol', 'Futebol'), ('basquete', 'Basquete'),
                                  ('voleibol', 'Voleibol'), 
                                  ('artes-marciais', 'Artes Marciais')])

    atvfisica = SelectField('Você pratica atividade física regularmente?',
                                   choices=[('', ''), (True, 'Sim'), (False, 'Não')],
                                   validators=[DataRequired()], coerce=bool)
