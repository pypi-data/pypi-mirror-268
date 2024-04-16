from . import media

import copy
import datetime
import math

class View:
    def __init__(self, x=None, y=None, w=None, h=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def tuple(self): return [self.x, self.y, self.w, self.h]

def fcolor(r, g, b, a):
    return [
        i if type(i) == float else i/255
        for i in [r, g, b, a]
    ]

def translate_x_date(plot, list_, component):
    for i in list_:
        x = i[component]
        x = (x - plot.epochs['x']['min']).total_seconds() / plot.datetime_unit
        i[component] = x

def translate_y_date(plot, list_, component):
    for i in list_:
        y = i[component]
        y = (y - plot.epochs['y']['min']).total_seconds() / plot.datetime_unit
        i[component] = y

def translate_dates(plot):
    if not plot.epochs: return
    if 'x' in plot.epochs:
        translate_x_date(plot, plot.late_vertexors, 1)
        translate_x_date(plot, plot.points, 0)
        translate_x_date(plot, plot.lines, 0)
        translate_x_date(plot, plot.lines, 2)
        translate_x_date(plot, plot.rects, 0)
        translate_x_date(plot, plot.rects, 2)
        plot.x_max = max(plot.x_max, (plot.epochs['x']['max'] - plot.epochs['x']['min']).total_seconds() / plot.datetime_unit)
        plot.x_min = min(plot.x_min, 0)
    if 'y' in plot.epochs:
        translate_y_date(plot, plot.late_vertexors, 2)
        translate_y_date(plot, plot.points, 1)
        translate_y_date(plot, plot.lines, 1)
        translate_y_date(plot, plot.lines, 3)
        translate_y_date(plot, plot.rects, 1)
        translate_y_date(plot, plot.rects, 3)
        plot.y_max = max(plot.y_max, (plot.epochs['y']['max'] - plot.epochs['y']['min']).total_seconds() / plot.datetime_unit)
        plot.y_min = min(plot.y_min, 0)

def construct(plot, view, w, h):
    plot.buffer = media.Buffer()
    plot.buffer_text = media.Buffer()
    # late vertexors
    if plot.late_vertexors:
        if hasattr(plot, 'original_points'):
            plot.points = copy.copy(plot.original_points)
            plot.lines = copy.copy(plot.original_lines)
        else:
            plot.original_points = copy.copy(plot.points)
            plot.original_lines = copy.copy(plot.lines)
        for vertexor, x, y, r, g, b, a in plot.late_vertexors:
            vertexor(plot, view, w, h, x, y, r, g, b, a)
    # points
    for x, y, r, g, b, a in plot.points:
        plot.buffer.add(x, y, *fcolor(r, g, b, a))
    points_f = len(plot.buffer)
    # lines & static text
    for xi, yi, xf, yf, r, g, b, a in plot.lines:
        plot.buffer.add(xi, yi, *fcolor(r, g, b, a))
        plot.buffer.add(xf, yf, *fcolor(r, g, b, a))
    for i in range(0, len(plot.static_texter.data), 6):
        x, y, r, g, b, a = plot.static_texter.data[i:i+6]
        plot.buffer.add(x, y, *fcolor(r, g, b, a))
    lines_f = len(plot.buffer)
    # rects
    for xi, yi, xf, yf, r, g, b, a in plot.rects:
        plot.buffer.add(xi, yi, *fcolor(r, g, b, a))
        plot.buffer.add(xf, yf, *fcolor(r, g, b, a))
        plot.buffer.add(xi, yf, *fcolor(r, g, b, a))
        plot.buffer.add(xi, yi, *fcolor(r, g, b, a))
        plot.buffer.add(xf, yf, *fcolor(r, g, b, a))
        plot.buffer.add(xf, yi, *fcolor(r, g, b, a))
    tris_f = len(plot.buffer)
    # draws
    plot.buffer.prep('static')
    plot.buffer.draws = [
        ('triangles',  lines_f, tris_f   - lines_f ),
        ('lines'    , points_f, lines_f  - points_f),
        ('points'   ,        0, points_f - 0       ),
    ]

def show(plot, w, h):
    media.init(w, h, title=plot.title)
    translate_dates(plot)
    if plot.x_min == plot.x_max:
        plot.x_min -= 1
        plot.x_max += 1
    if plot.y_min == plot.y_max:
        plot.y_min -= 1
        plot.y_max += 1
    dx = plot.x_max - plot.x_min
    dy = plot.y_max - plot.y_min
    plot.x_min -= dx / 16
    plot.y_min -= dy / 16
    plot.x_max += dx / 16
    plot.y_max += dy / 16
    view = View()
    def reset():
        view.x = plot.x_min
        view.y = plot.y_min
        view.w = plot.x_max - plot.x_min
        view.h = plot.y_max - plot.y_min
        if view.x == math.inf:
            view.x = 0
            view.y = 0
            view.w = 1
            view.h = 1
        if view.w == 0:
            view.w = 1
        if view.h == 0:
            view.h = 1
        media.view_set(*view.tuple())
    def move(view, dx, dy):
        view.x -= dx*view.w/media.width()
        view.y -= dy*view.h/media.height()
        media.view_set(*view.tuple())
    def zoom(view, zx, zy, x, y):
        # change view so (x, y) stays put and (w, h) multiplies by (zx, zy)
        new_view_w = view.w*zx
        new_view_h = view.h*zy
        view.x += x/media.width () * (view.w - new_view_w)
        view.y += y/media.height() * (view.h - new_view_h)
        view.w = new_view_w
        view.h = new_view_h
        media.view_set(*view.tuple())
    reset()
    construct(plot, view, w, h)
    def on_resize(w, h):
        zoom(view, w/media.width(), h/media.height(), w/2, h/2)
        if plot.late_vertexors:
            construct(plot, view, media.width(), media.height())
    def on_mouse_drag(dx, dy):
        move(view, dx, dy)
    def on_mouse_scroll(x, y, delta):
        z = 1.25 if delta > 0 else 0.8
        zoom(view, z, z, x, y)
    def on_key_press(key):
        moves = {
            'Left' : ( 10,   0),
            'Right': (-10,   0),
            'Up'   : (  0, -10),
            'Down' : (  0,  10),
        }
        if key in moves:
            move(view, *moves[key])
            return
        zooms = {
            'a': (1.25, 1),
            'd': (0.80, 1),
            'w': (1, 1.25),
            's': (1, 0.80),
        }
        if key in zooms:
            zoom(view, *zooms[key], media.width()/2, media.height()/2)
            return
        if key == ' ':
            reset()
            return
        if key == 'Return':
            media.capture()
            return
    def on_draw():
        media.clear()
        plot.buffer.draw()
        margin_x = 5.0 / media.width()  * view.w
        margin_y = 5.0 / media.height() * view.h
        # draw texts
        texter = media.Texter()
        for (s, x, y, r, g, b, a, max_w, max_h, scale) in plot.texts:
            text_w = scale / media.width()  * view.w
            text_h = scale * 3/2 / media.height() * view.h
            over = max(len(s) * text_w / max_w, text_h * 3 / 2 / max_h, 1)
            r, g, b, a = fcolor(r, g, b, a)
            texter.text(
                s, x + margin_x / over, y + margin_y / over,
                text_w / over,
                text_h / over,
                r, g, b, a,
            )
            texter.text(
                'L', x, y,
                text_w / over,
                text_h / 2 / over,
                r, g, b, a,
            )
        if not plot.hide_axes:
            text_w = 10 / media.width()  * view.w
            text_h = 15 / media.height() * view.h
            # draw x axis
            increment = 10 ** math.floor(math.log10(view.w))
            if view.w / increment < 2:
                increment /= 5
            elif view.w / increment < 5:
                increment /= 2
            i = view.x // increment * increment + increment
            while i < view.x + view.w:
                s = '{:.5}'.format(i)
                if view.x + view.w - i > increment:
                    if i == 0 and plot.epochs.get('x') != None:
                        texter.text(
                            plot.epochs['x']['min'].isoformat('\n'),
                            x=i + margin_x,
                            y=view.y + margin_y + 1.33 * text_h,
                            w=text_w * 0.66,
                            h=text_h * 0.66,
                        )
                    else:
                        texter.text(s, x=i+margin_x, y=view.y+margin_y, w=text_w, h=text_h)
                    texter.text('L', i, view.y, text_w * 2, text_h)
                i += increment
            # draw y axis
            increment = 10 ** math.floor(math.log10(view.h))
            if view.h / increment < 2:
                increment /= 5
            elif view.h / increment < 5:
                increment /= 2
            i = (view.y + text_h + 2*margin_y) // increment * increment + increment
            while i < view.y + view.h - (text_h + 2*margin_y):
                s = '{:.5}'.format(i)
                if i == 0 and plot.epochs.get('y') != None:
                    texter.text(
                        plot.epochs['y']['min'].isoformat('\n'),
                        x=view.x + margin_x,
                        y=i + margin_y + 1.33 * text_h,
                        w=text_w * 0.66,
                        h=text_h * 0.66,
                    )
                else:
                    texter.text(s, x=view.x+margin_x, y=i+margin_y, w=text_w, h=text_h)
                texter.text('L', view.x, i, text_w * 2, text_h)
                i += increment
        plot.buffer_text.data = texter.data
        plot.buffer_text.prep('dynamic')
        plot.buffer_text.draws = [('lines', 0, len(plot.buffer_text.data))]
        plot.buffer_text.draw()
    media.set_callbacks(
        mouse_drag=on_mouse_drag,
        mouse_scroll=on_mouse_scroll,
        key_press=on_key_press,
        draw=on_draw,
    )
    media.run()
