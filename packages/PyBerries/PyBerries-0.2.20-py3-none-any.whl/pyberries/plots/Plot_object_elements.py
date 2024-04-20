import numpy as np
import pandas as pd
import seaborn.objects as so


def Add_significance(p, x1, x2, y, h=0, text=''):

    coords = pd.DataFrame({'x': [x1, x1, x2, x2], 'y': [y, y+h, y+h, y]})
    text = pd.DataFrame({'x': [np.mean([x1, x2])], 'y': [y], 'text': [text]})
    p = (p
         .add(so.Line(color='.2'), data=coords, x='x', y='y', legend=False)
         .add(so.Text(color='.2', valign='bottom'), data=text, x='x', y='y', text='text')
         )
    return p
