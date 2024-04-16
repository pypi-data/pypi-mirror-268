from . import primitives
from . import transforms
from . import vector_text

import datetime
import math

class Plot:
    def __init__(
        self,
        title='plot',
        *,
        transform=None,
        hide_axes=False,
        primitive=None,
        datetime_unit=1,
        legend_displacement=(0, -1),
        legend_offset=(0, -1),
    ):
        self.title = title
        self.points = []
        self.lines = []
        self.rects = []
        self.late_vertexors = []
        self.texts = []
        self.static_texter = vector_text.Texter()
        self.x_min =  math.inf
        self.x_max = -math.inf
        self.y_min =  math.inf
        self.y_max = -math.inf
        self.epochs = {}
        self.series = 0
        self.transform = transform or transforms.Default()
        self.hide_axes = hide_axes
        self.set_primitive(primitive or primitives.Point())
        self.datetime_unit = datetime_unit
        self.legend_displacement = legend_displacement
        self.legend_offset = legend_offset

    def point(self, x, y, r=255, g=255, b=255, a=255):
        self.points.append([x, y, r, g, b, a])
        self._include(x, y)

    def line(self, xi, yi, xf, yf, r=255, g=255, b=255, a=255):
        self.lines.append([xi, yi, xf, yf, r, g, b, a])
        self._include(xi, yi)
        self._include(xf, yf)

    def rect(self, xi, yi, xf, yf, r=255, g=255, b=255, a=255):
        self.rects.append([xi, yi, xf, yf, r, g, b, a])
        self._include(xi, yi)
        self._include(xf, yf)

    def late_vertexor(self, vertexor, x, y, r=255, g=255, b=255, a=255):
        self.late_vertexors.append([vertexor, x, y, r, g, b, a])
        self._include(x, y)

    def text(self, s, x, y, r=255, g=255, b=255, a=255, max_w=math.inf, max_h=math.inf, scale=10):
        '`scale` is the number of pixels between the left side of each character.'
        self.texts.append([s, x, y, r, g, b, a, max_w, max_h, scale])
        self._include(x, y)

    def text_static(self, s, x, y, w=1, h=1, r=255, g=255, b=255, a=255):
        '`w` and `h` are for a single character.'
        if not s: return
        self.static_texter.text(s, x, y, w, h, r, g, b, a)
        self._include(*self.static_texter.bounds[0:2])
        self._include(*self.static_texter.bounds[2:4])

    def show(self, w=640, h=480):
        from .show import show
        show(self, w, h)

    def plot_list(self, l, **kwargs):
        for i, v in enumerate(l):
            self.primitive(**self.transform(i, v, i, self.series))
        self._plot_common(**kwargs)

    def plot_lists(self, ls, **kwargs):
        for l in ls: self.plot_list(l, **kwargs)

    def plot_scatter(self, x, y, **kwargs):
        for i in range(min(len(x), len(y))):
            self.primitive(**self.transform(x[i], y[i], i, self.series))
        self._plot_common(**kwargs)

    def plot_scatter_pairs(self, pairs, **kwargs):
        for i, pair in enumerate(pairs):
            self.primitive(**self.transform(pair[0], pair[1], i, self.series))
        self._plot_common(**kwargs)

    def plot_scatter_xs(self, xs, y, **kwargs):
        for x in xs: self.plot_scatter(x, y, **kwargs)

    def plot_scatter_ys(self, x, ys, **kwargs):
        for y in ys: self.plot_scatter(x, y, **kwargs)

    def plot_dict(self, d, **kwargs):
        for i, (x, y) in enumerate(d.items()):
            self.primitive(**self.transform(x, y, i, self.series))
        self._plot_common(**kwargs)

    def plot_dicts(self, ds, **kwargs):
        for d in ds: self.plot_dict(d, **kwargs)

    def plot_f(self, f, x=(-1, 1), steps=100, **kwargs):
        args_prev = None
        for i in range(steps):
            x_curr = x[0] + (x[1]-x[0]) * i/(steps-1)
            y_curr = f(x_curr)
            self.primitive(**self.transform(x_curr, y_curr, i, self.series))
        self._plot_common(**kwargs)

    def plot_2d(self, array, *, x_increment=1, y_increment=1, **kwargs):
        z_min = math.inf
        z_max = -math.inf
        for row in array:
            z_min = min(z_min, min(row))
            z_max = max(z_max, max(row))
        z_rng = z_max - z_min
        if z_rng == 0: return
        i = 0
        for y, row in enumerate(array):
            for x, z in enumerate(row):
                rect = {'a': float((z - z_min) / z_rng)}
                a = self.transform(x, y, i, self.series)
                rect['xi'] = a['x']
                rect['yi'] = a['y']
                if 'r' in a: rect['r'] = a['r']
                if 'g' in a: rect['g'] = a['g']
                if 'b' in a: rect['b'] = a['b']
                b = self.transform(self._increment(x, x_increment), self._increment(y, y_increment), i, self.series)
                rect['xf'] = b['x']
                rect['yf'] = b['y']
                self.rect(**rect)
        self._plot_common(**kwargs)

    def plot_heatmap(self, triples, *, x_increment=1, y_increment=1, **kwargs):
        z_min = math.inf
        z_max = -math.inf
        zs = [i[2] for i in triples]
        z_min = min(zs)
        z_max = max(zs)
        z_rng = z_max - z_min
        if z_rng == 0: return
        i = 0
        for x, y, z in triples:
            rect = {'a': float((z - z_min) / z_rng)}
            a = self.transform(x, y, i, self.series)
            rect['xi'] = a['x']
            rect['yi'] = a['y']
            if 'r' in a: rect['r'] = a['r']
            if 'g' in a: rect['g'] = a['g']
            if 'b' in a: rect['b'] = a['b']
            b = self.transform(self._increment(x, x_increment), self._increment(y, y_increment), i, self.series)
            rect['xf'] = b['x']
            rect['yf'] = b['y']
            self.rect(**rect)
        self._plot_common(**kwargs)

    def plot_empty(self, *args, **kwargs):
        self._plot_common(**kwargs)

    def plot(self, *args, **kwargs):
        plot_func = None
        if len(args) >= 1 and _is_empty(args[0]):
            plot_func = self.plot_empty
        elif len(args) == 1:
            if   _is_dim(args[0], 1): plot_func = self.plot_list
            elif _is_dim(args[0], 2): plot_func = self.plot_lists
            elif _type_r(args[0], 1) == _type_r([()]): plot_func = self.plot_scatter_pairs
            elif type(args[0]) == dict: plot_func = self.plot_dict
            elif _type_r(args[0]) == _type_r([{}]): plot_func = self.plot_dicts
            elif callable(args[0]): plot_func = self.plot_f
            elif type(args[0]).__name__ == 'ndarray' and len(args[0].shape) == 2: plot_func = self.plot_2d
        elif len(args) == 2:
            if   _is_dim(args[0], 1) and _is_dim(args[1], 1): plot_func = self.plot_scatter
            elif _is_dim(args[0], 2) and _is_dim(args[1], 1): plot_func = self.plot_scatter_xs
            elif _is_dim(args[0], 1) and _is_dim(args[1], 2): plot_func = self.plot_scatter_ys
        if not plot_func:
            raise Exception('unknown plot type for argument types {}'.format([_type_r(i) for i in args]))
        plot_func(*args, **kwargs)
        return self

    def next_series(self):
        self.series += 1
        self.primitive.reset()

    def set_primitive(self, primitive):
        self.primitive = primitive.set_plot(self)

    def _include(self, x, y):
        if type(x) == datetime.datetime:
            if 'x' in self.epochs:
                self.epochs['x']['min'] = min(x, self.epochs['x']['min'])
                self.epochs['x']['max'] = max(x, self.epochs['x']['max'])
            else:
                self.epochs['x'] = {'min': x, 'max': x}
        else:
            self.x_min = min(x, self.x_min)
            self.x_max = max(x, self.x_max)
        if type(y) == datetime.datetime:
            if 'y' in self.epochs:
                self.epochs['y']['min'] = min(y, self.epochs['y']['min'])
                self.epochs['y']['max'] = max(y, self.epochs['y']['max'])
            else:
                self.epochs['y'] = {'min': y, 'max': y}
        else:
            self.y_min = min(y, self.y_min)
            self.y_max = max(y, self.y_max)

    def _plot_common(
        self,
        next_series=True,
        legend=None,
        **kwargs,
    ):
        if legend:
            kwargs = self.transform(0, 0, 0, self.series)
            if hasattr(self.transform, 'series_insignificant'):
                series = self.transform.series_insignificant(self.series)
            else:
                series = self.series
            kwargs['x'] += self.legend_displacement[0] * series + self.legend_offset[0]
            kwargs['y'] += self.legend_displacement[1] * series + self.legend_offset[1]
            self.text(legend, max_h=abs(self.legend_displacement[1]) or 1, **kwargs)
        if next_series:
            self.next_series()

    def _increment(self, x, amount=1):
        if type(x) == datetime.datetime:
            return x + datetime.timedelta(seconds=self.datetime_unit) * amount
        else:
            return x + amount

def plot(
    *args,
    title='plot',
    transform=None,
    hide_axes=False,
    primitive=None,
    **kwargs,
):
    Plot(
        title,
        transform=transform,
        hide_axes=hide_axes,
        primitive=primitive,
    ).plot(*args, **kwargs).show()

def _type_r(v, max_depth=None, _depth=0):
    if type(v).__name__ in ['int', 'float', 'float64']: return 'number'
    if max_depth != None and _depth == max_depth:
        return str(type(v))
    try:
        v[0]
        return '{}({})'.format(type(v), _type_r(v[0], max_depth, _depth+1))
    except:
        return str(type(v))

def _is_dim(v, dim):
    u = 0
    for i in range(dim): u = [u]
    return _type_r(v, dim) == _type_r(u)

def _is_empty(v):
    try:
        return len(v) == 0
    except:
        return False
