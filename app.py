from flask import Flask, flash, redirect, render_template, \
     request, url_for
from config import Config
from project.forms import GameForm, EndForm
import game as g

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    g.Game(True)
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    error = None
    l = g.Game()    
    form = GameForm()
    print(f"State: {form.state.data}")
    if form.state.data == '1':
        return redirect('end/' + form.choice.data)
    if form.validate_on_submit():
        r = l.move(form.direction.data, form.steps.data)
        if r == 'Done':
            flash('Вы прошли лабиринт', 'success')
            form=EndForm()
            form.state.data = 1
            return render_template(
                'game.html',
                form=form
                )
        else:
            flash(r, 'info' if r.find('нельзя') == -1 else 'warning')

    return render_template(
        'game.html',
        form=form,
        error=error,
    )

@app.route('/end/<int:img_number>')
def end(img_number):
    return render_template('game_off.html', img=img_number)

if __name__ == '__main__':
    app.run()