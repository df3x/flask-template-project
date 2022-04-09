from email.policy import default
from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired, NumberRange


class GameForm(FlaskForm):
    state = HiddenField()
    choice = HiddenField()
    direction = RadioField('Куда пойти',
        validators=[DataRequired()],
        coerce=int,
        choices=[(1,'вперед'),(2,'назад'),(3,'вправо'),(4,'влево')],
        #render_kw={'class':'form-control'}
        )
    steps = IntegerField('Количество шагов', 
        validators=[NumberRange(min=1, max=3), DataRequired()],
        default=1, 
        render_kw={'class':'form-control'}
        )
    submit = SubmitField('Пойти', render_kw={'class':'btn btn-primary'})

class EndForm(FlaskForm):
    state = HiddenField()
    choice = SelectField('Выберите приз',
        coerce=int,
        choices=[(1,'пицца'),(2,'монетка'),(3,'конфетка')],
        render_kw={'class':'form-control'}
        )
    submit = SubmitField('Завершить', render_kw={'class':'btn btn-success'}, )