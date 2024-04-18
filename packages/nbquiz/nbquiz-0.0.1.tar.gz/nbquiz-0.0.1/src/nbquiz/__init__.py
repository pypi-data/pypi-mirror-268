''' NBQuiz: Make ipywidgets-based quizzes for use in Jupyter notebooks '''
import ipywidgets as widgets
from IPython.display import display
from IPython.core.getipython import get_ipython
from IPython.utils.capture import capture_output
import operator
import math
from types import SimpleNamespace

__all__ = [
    'check_variable',
    'check_code',
    'check_answer',
    'multiple_choice',
    'number_input',
    'text_input',
    'results'
]

_data = SimpleNamespace(qcount=0, correct=0, complete=False)


def get_variable(name):
    return get_ipython().ev(name)


def set_variable(**variables):
    get_ipython().push(variables)


def get_previous_cell():
    hist = get_ipython().ev('_ih')
    return hist[-2]


def check_variable(name, expected, comparison=operator.eq):
    def _inner():
        # try:
        if comparison(get_variable(name), expected):
            return True, ''
        else:
            return False, ''
        # except:
        #     return False, 'There is an error in your code!'
    return _inner


def check_code(contains=[], notcontains=[]):
    def _inner():
        cell = get_previous_cell()
        res = True
        msg = ''
        for el in contains:
            if el not in cell:
                res = False
                msg = msg + f'Your code should contain {el}!\n'

        for el in notcontains:
            if el in cell:
                res = False
                msg = msg + f'Your code shouldn\'t contain {el}!\n'
        return res, msg
            
    return _inner


def check_stdout(expected, runwith=None):
    def _inner():
        if runwith is not None:
            set_variable(**runwith)
        with capture_output(display=False) as c:
            get_ipython().run_cell(get_previous_cell(), silent=True)
            output = c.stdout.strip()
            if (expected == output):
                return True, ''
            else:
                msg = f'Your code printed {output}, but {expected} was expected!'
                if runwith:
                    msg = msg + '\n' + ', '.join([f'{k} = {v}' for k, v in runwith.items()])
                return False, msg
    return _inner


def check_answer(*funcs):
    output = widgets.Output()
    button = widgets.Button(description="Check answer", icon="check")
    # Update question counters
    if _data.complete:
        # On reload of a notebook, the import of this module remains, but all widgets are reset.
        # In this case, reset the correct counter, but keep the question count
        _data.correct = 0
    else:
        _data.qcount += 1
    def _inner_check(button):
        with output:
            # Only allow one answer
            button.disabled = True
            # Call checker function(s)
            res = True
            msgs = []
            for func in funcs:
                r, m = func()
                res = res and r
                msgs.append(m)
            msg = ('Correct!\n' if res else 'Incorrect!\n') + '\n'.join(msgs)
            output.outputs = [{'name': 'stdout', 'text': msg, 'output_type': 'stream'}]
            # Update question result counter
            if res:
                _data.correct += 1
    button.on_click(_inner_check)
    display(button, output)


def multiple_choice(*options, correct=0, multi=False):
    if multi:
        if isinstance(correct, int):
            correct = [correct]
        wid = widgets.Box(
            [widgets.Checkbox(False, description=opt) for opt in options]                
        )
        def _inner():
            wid.disabled = True
            for idx, el in enumerate(wid.children):
                if (el.value and idx not in correct) or (not el.value and idx in correct):
                    return False, ''
            return True, ''
    else:
        wid = widgets.RadioButtons(
                options=options,
                layout={'width': 'max-content'},
                style=dict(text_color='black')
            )
        def _inner():
            wid.disabled = True
            return (wid.index == correct), ''

    display(wid)
    return _inner


def number_input(correct):
    if isinstance(correct, int):
        wid = widgets.IntText(
            value=0,
            description='Answer:',
            disabled=False
        )
        def _inner():
            wid.disabled = True
            return (wid.value == correct), ''
    else:
        wid = widgets.FloatText(
            value=0.0,
            description='Answer:',
            disabled=False
        )
        def _inner():
            wid.disabled = True
            return math.isclose(wid.value, correct), ''
    display(wid)
    return _inner


def text_input(correct):
    wid = widgets.Text(
        value='',
        placeholder='Your answer',
        description='Answer:',
        disabled=False   
    )
    def _inner():
        wid.disabled = True
        return (wid.value == correct), ''
    display(wid)
    return _inner


def results():
    output = widgets.Output()
    button = widgets.Button(description="Check quiz score", icon="circle-exclamation")
    # This function should be called last in a quiz notebook, so we can use it to
    # determine that all questions have been defined.
    _data.complete = True
    def _inner_check(button):
        with output:
            # Call checker function(s)
            msg = f'You\'ve answered {_data.correct}/{_data.qcount} questions correctly!'
            output.outputs = [{'name': 'stdout', 'text': msg, 'output_type': 'stream'}]

    button.on_click(_inner_check)
    display(button, output)