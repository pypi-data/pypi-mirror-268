import re
import json
import numpy as np

from .geo import construction as geo
from manim import *
from .parsers.svg_parser import *
from .parsers import short_parser, ggb_parser

import xml.etree.ElementTree as ET

#--------------------------------------------------------------------------

#стилевик от Пандоры
style_pandora = {}

style_pandora['dot'] = {}
style_pandora['line'] = {}
style_pandora['angle'] = {}
style_pandora['strich'] = {}
style_pandora['color'] = {}

style_pandora['dot']['main'] = 7
style_pandora['dot']['bold'] = 9
style_pandora['dot']['aux'] = 5

style_pandora['line']['main'] = 2
style_pandora['line']['bold'] = 2.5
style_pandora['line']['aux'] = 1.5

style_pandora['angle']['line'] = 1
style_pandora['angle']['r_default'] = 12.5
style_pandora['angle']['r_shift'] = 1.5
style_pandora['angle']['r_right'] = 10

style_pandora['strich']['width'] = 2
style_pandora['strich']['len'] = 12
style_pandora['strich']['shift'] = 4

style_pandora['color']['black'] = '#000000'
style_pandora['color']['main'] = '#2581b5'
style_pandora['color']['light'] = '#bef3fc'
style_pandora['color']['aux'] = '#000000'
style_pandora['color']['acc'] = '#ef60ab'
style_pandora['color']['acc_light'] = '#ffd2ee'

def isnan(x):
    if isinstance(x, str):
        try:
            y = float(x)
            return False
        except:
            return True
    else:
        return not isinstance(x, (int, float))

def CorrectSVG(svg_path):
    #tree = ET.parse(svg_path)

    #for elem in tree.findall(f'.//{xmlns}text'):
    #    elem.set('font-style', 'italic')

    #tree.write(svg_path, encoding = "UTF-8", xml_declaration = False)
    return

class GeoStyle:
    def __init__(self, style_json_file = None, scheme = None, color = 'blue', theme = 'light', px_size = [1920, 1080], crop_padding = None):
        self.dot_size = 0.17   
        self.line_width = 6   
        self.ang_width = 0.75 * self.line_width
        self.strich_rshift = 0.14
        self.ang_rshift = 0.75 * self.strich_rshift
        self.strich_len = 0.45
        self.strich_width = 6
        self.ang_rdefault = 0.8
        self.ang_right = 0.65
        
        self.background = WHITE
        self.strong = BLACK
        
        if style_json_file is not None:
            style_json = json.loads(open(style_json_file, 'r').read())
            scheme = style_json['name']
            
            if scheme == 'pandora':
                global style_pandora
                style_pandora = style_json['style']
                #print(style_pandora)

        if scheme == 'pandora':            
            self.convert_pandora_to_manim()
            
        else:
            if theme == 'dark':
                self.background = BLACK
                self.strong = WHITE
                self.col_gray = '#282828'

                if color == 'white':
                    self.col = '#ffffff'
                    self.col_light = '#333333'
                    self.col_accent = '#db4251'
                    self.col_accent_light = '#68383f'
                elif color == 'purple':
                    self.background = '#151324'
                    self.col = '#9f9fdd'
                    self.col_light = '#3c3766'
                    self.col_accent = '#db4251'
                    self.col_accent_light = '#542f36'
                    self.col_gray = '#211f2f'

            else:
                self.background = WHITE
                self.strong = BLACK

                if color == 'green':
                    self.col = '#80be8c'
                    self.col_light = '#e3efdb'
                    self.col_accent = '#d05456'
                    self.col_accent_light = '#f6e0db'
                elif color == 'orange':
                    self.col = '#d97c2c'
                    self.col_light = '#fae7ca'
                    self.col_accent = '#72a6d9'
                    self.col_accent_light = '#d8edfb'
                elif color == 'purple':
                    self.col = '#8670ac'
                    self.col_light = '#e8e3f0'
                    self.col_accent = '#d05456'
                    self.col_accent_light = '#f6e0db'
                else: #blue
                    self.col = '#6688c2'
                    self.col_light = '#dee7f5'
                    self.col_accent = '#d05456'
                    self.col_accent_light = '#f6e0db'

                self.col_gray = '#eeeeee'
        
        #параметры окна отображения 
        # размеры width и height в px
        # положение начала координат xZero и yZero
        # масштаб scale в px для 0.5 unit
        self.view = {}
        if px_size is not None:
            self.view['width'], self.view['height'] = px_size[0], px_size[1]

    def convert_pandora_to_manim(self):
        self.dot_size = 0.02 * style_pandora['dot']['main']
        self.line_width = 2 * style_pandora['line']['main']
        self.ang_width = 2 * style_pandora['angle']['line']
        self.ang_rshift = 2 * style_pandora['angle']['r_shift']
        self.ang_rdefault = 0.02 * style_pandora['angle']['r_default']
        self.ang_right = 0.02 * style_pandora['angle']['r_right']
        self.strich_width = 2 * style_pandora['strich']['width']
        self.strich_len = 0.02 * style_pandora['strich']['len']
        self.strich_rshift = 0.02 * style_pandora['strich']['shift']
        
        self.background = '#ffffff'
        self.col = style_pandora['color']['main']
        self.col_light = style_pandora['color']['light']
        self.col_accent = style_pandora['color']['acc']
        self.col_accent_light = style_pandora['color']['acc_light']
        self.col_gray = '#eeeeee'

    def setViewByGeo(self, geoView):
        w0, h0 = self.view['width'], self.view['height']
        w, h = geoView['width'], geoView['height']
        if isnan(w0) & isnan(h0): 
            print("ERROR: width and heigth haven't been set")
        elif isnan(w0):
            #print(w0, h0, w, h)
            w0 = float(h0) * w / h
            self.view['width'] = w0
        elif isnan(h0):
            #print(w0, h0, w, h)
            h0 = float(w0) * h / w
            self.view['height'] = h0
            
        q = min(w0/w, h0/h)
        
        self.view['scale'] = geoView['scale'] * q
        self.view['xZero'] = geoView['xZero'] * q + (w0 - q * w) / 2
        self.view['yZero'] = geoView['yZero'] * q + (h0 - q * h) / 2

#--------------------------------------------------------------------------

class GeoDynamic(MovingCameraScene):
    style_default = GeoStyle(color = 'blue', theme = 'light')

    def __init__(self):
        super().__init__()
        self.obj = {}                       #хранение объектов сцены mobjects obj[name] = MObject
        self.geo = geo.Construction()
        self.style = GeoStyle(color = 'blue')

        self._styles_back = {}
        self._gray_mobjects = {}

        self.cuts = 0

    def mobject(self, name):
        if name in self.obj: return self.obj[name]
        else: return None
        #result = list(filter(lambda obj: obj.name == name, self.mobjects))
        #return result[0] if result else None
    
    def element(self, name):
        return self.geo.element(name)
    
    def addGeoElement(self, elem, show = False):
        mobj = CreateMObject(elem, z_auto = True)
        self.obj[elem.name] = mobj
        if mobj is not None:
            self.add(mobj)
            #print('Visible', elem.name, elem.visible)
            if (not show) | (not elem.visible): mobj.set_opacity(0)

    def addAllGeometry(self, show = False):
        if not show:
            for el in self.geo.elements: el.visible = False
        element_types = [
            [geo.Polygon],
            [geo.Angle],
            [geo.Circle, geo.Arc, geo.Segment],
            [geo.Point]
        ]

        for el_types in element_types:
            for el in self.geo.elements: 
                if type(el.data) in el_types: self.addGeoElement(el, show) 
 
    def getAllGeometryBounds(self):
        bounds = [None,None,None,None]
        for elem in self.geo.elements: 
            if elem.visible:
                mobj = CreateMObject(elem, z_auto = True)
                if mobj is not None:
                    #!здесь нужно проверить границы элемента и расширить bounds по необходимости
                    x = 0
                    

    #пауза для обрезки видео + отображение ярлыка слева
    def waitCut(self, msg = None, **kwargs):
        self.cuts += 1

        rect = Rectangle(color = RED, fill_opacity = 1, height = self.camera.frame_height, width = self.camera.frame_width/4).move_to(self.camera.frame_center).shift( (3/8) * self.camera.frame_width * LEFT)
        txt = Text(str(msg) if msg is not None else str(self.cuts)).set_color(BLACK).scale(3).move_to(rect)
        
        self.add(rect, txt)
        self.wait(**kwargs)

        self.remove(rect)
        self.remove(txt)

    def updateAllGeometry(self):
        for el in self.geo.elements:
            #if not el.visible: continue
            mobj = self.mobject(el.name)
            mobj_new = CreateMObject(el)
            if mobj is not None: 
                mobj.become(mobj_new)
            elif mobj_new is not None:
                self.obj[el.name] = mobj_new
                self.add(mobj_new)
                mobj = mobj_new
            else: continue
            if not el.visible: 
                mobj.set_opacity(0)
    
    def updateGeoElements(self, updates):
        for el in self.geo.elements:
            if el.name not in updates: continue
            #if not el.visible: continue
            mobj = self.mobject(el.name)
            mobj_new = CreateMObject(el)
            if mobj_new is not None:
                if mobj is not None: 
                    mobj.become(mobj_new)
                else:
                    self.obj[el.name] = mobj_new
                    self.add(mobj_new)
                    mobj = mobj_new
            else: continue
            if not el.visible: 
                mobj.set_opacity(0)

    def loadGeometry(self, filepath, update = False, debug = False):
        short_parser.loadCode(self.geo, filepath, update = update, debug = debug)
        self.geo.rebuild(debug = debug)

    def loadGeoGebra(self, filepath, style_json_file = None, scheme = 'pandora', px_size = None, crop_padding = None, debug = False):
        self.geo = ggb_parser.load(filepath, debug = debug) 
        self.geo.rebuild(debug = debug)
        
        style = GeoStyle(style_json_file = style_json_file, scheme = scheme, px_size = px_size, crop_padding = crop_padding)
        
        if crop_padding is not None:
            print('This method is going to be realized soon.')    
        
        if px_size is not None:
            style.setViewByGeo(self.geo.style['view'])
        else:
            style.view = self.geo.style['view']

        view = style.view
        scale = view['scale']
        for key in ['dot_size', 'line_width', 'ang_width', 'ang_rdefault', 'ang_right', 'ang_rshift', 'strich_rshift', 'strich_len']:
            style.__setattr__(key, getattr(style, key) * 50 / scale)

        self.camera.frame.set(width = view['width'] / scale)
        dx = self.camera.frame.width / 2 - view['xZero'] / scale
        dy = view['height'] / (2 * scale) - view['yZero'] / scale      
        self.camera.frame.shift(dx * RIGHT + dy * DOWN)

        self.setStyle(style)
        self.addAllGeometry(show = True)

    def updateGeoVar(self, x, var_name):
        self.geo.update(var_name, float(x.get_value()))
        updates = self.geo.rebuild()
        #print(updates)
        #if np.isclose(self.geo.var(var_name).data, float(x.get_value())): return
        self.updateGeoElements(updates)

    def setStyle(self, style):
        self.style = style
        GeoDynamic.style_default = style
        self.camera.background_color = GeoDynamic.style_default.background
        Text.set_default(color = self.style.strong)
        MathTex.set_default(color = self.style.strong)

    def playShow(self, names, mode = None, **kwargs):
        self.play(*ShowObjs(self, names, mode, **kwargs))

    def playHide(self, names, mode = None, **kwargs):
        self.play(*HideObjs(self, names, mode, **kwargs))

    def playHide(self, names, mode = None, **kwargs):
        self.play(*HideObjs(self, names, mode, **kwargs))

    def playGrayStyle(self, names, mode = None, **kwargs):
        self.play(*GrayStyleObjs(self, names, mode, **kwargs))

    def playBackStyle(self, names, mode = None, **kwargs):
        self.play(*BackStyleObjs(self, names, mode, **kwargs))

    #----------------------------------

    def exportSVG(self, filepath):
        #config.frame_height = self.camera.frame.get_height()
        #config.frame_width = self.camera.frame.get_width()
        #scale = 2 * self.style['view']['scale']
        #config.frame_width, config.frame_height = self.style['view']['width'] / scale, self.style['view']['height'] / scale
        #config.__setattr__('frame_center', self.camera.frame.get_center())
        config.__setattr__('ggb_view', self.style.view)
        VGroup(*self.mobjects).to_svg(filepath)
    
    def addGrid(self, x_range=(-10, 10, 1), y_range=(-10, 10, 1)):
        grid = NumberPlane(
            x_range = x_range,
            y_range = y_range,
            x_length = x_range[1] - x_range[0],
            y_length = y_range[1] - y_range[0],
            background_line_style = {
                "stroke_color": BLACK,
                "stroke_width": self.style.ang_width,
                "stroke_opacity": 0.1
            },
            x_axis_config = {"stroke_opacity": 0},
            y_axis_config = {"stroke_opacity": 0}
        )

        self.add(grid.shift(-grid.get_origin()))

#--------------------------------------------------------------------------

def getParamFromDict(dict, key, paramDefault = None, check = True):
    if not check: return paramDefault
    if key not in dict: return paramDefault
    if dict[key] is None: 
        return paramDefault
    else: 
        return dict[key]

def hasParam(dict, key):
    if key not in dict: return False
    if not dict[key]: return False
    return True

def ShowObjs(scene, names, mode = None, **kwargs):
    plays = []
    for name in names:
        elem = scene.geo.element(name)
        if not elem: continue
        elem.visible = True
        mobj = scene.mobject(name)
        if mobj is None: continue
        mobj.set_opacity(1)

        op_s = getParamFromDict(elem.style, 'stroke_opacity', 1)
        op_f = getParamFromDict(elem.style, 'fill_opacity', 0 if (type(elem.data) != geo.Point) else 1)
        
        hasLabel = hasParam(elem.style, 'show_label')

        if type(elem.data) == geo.Segment:
            if hasLabel: 
                for m in mobj[:-1]:
                    m.set_stroke(opacity = op_s)
            else: mobj.set_stroke(opacity = op_s)

            plays.append(Create(mobj, **kwargs) if mode == 'Create' else FadeIn(mobj, **kwargs))

        elif type(elem.data) == geo.Angle:
            mobj[0].set_fill(opacity = op_f)

            if hasLabel:
                for m in mobj[1:-1]: 
                    m.set_fill(opacity = 0).set_stroke(opacity = op_s)
            else:
                for m in mobj[1:]: 
                    m.set_fill(opacity = 0).set_stroke(opacity = op_s)

            plays.append(FadeIn(mobj[0], **kwargs))
            plays.append(Create(mobj[1:], **kwargs) if mode == 'Create' else FadeIn(mobj[1:], **kwargs))

        else:
            if (type(elem.data) == geo.Polygon) | (type(elem.data) == geo.Circle) | (type(elem.data) == geo.Arc):
                mobj[0].set_stroke(opacity = 0).set_fill(opacity = op_f)  
                mobj[1].set_stroke(opacity = op_s).set_fill(opacity = 0)
            else:
                mobj[0].set_stroke(opacity = op_s).set_fill(opacity = op_f)  
        
            plays.append(Create(mobj, **kwargs) if mode == 'Create' else FadeIn(mobj, **kwargs))

    if len(plays) == 0:
        print('ShowObjs: NO OBJECTS found from ', names)

    return plays

def HideObjs(scene, names, **kwargs):
    plays = []

    for name in names:
        mobj = scene.mobject(name)
        if not mobj: continue
        elem = scene.geo.element(name)
        if not elem: continue

        elem.visible = False
        plays.append(FadeOut(mobj, **kwargs))
        #mobj.set_opacity(0)

    return plays

def UpdateObjs(scene, names, mode = 'Fade', **kwargs):
    plays = []

    for name in names:
        elem = scene.geo.element(name)
        if not elem: continue      
        mobj = scene.mobject(name)
        if not mobj:
            mobj = CreateMObject(elem)
            scene.obj[name] = mobj
            scene.add(mobj)  

        mobj_new = CreateMObject(elem)
        if mobj_new: 
            if mode == 'Fade':
                plays.append(FadeOut(mobj), **kwargs)
                plays.append(FadeIn(mobj_new), **kwargs)
            else:
                plays.append(mobj.animate(**kwargs).become(mobj_new))
                
            scene.obj[name] = mobj_new
        else:
            plays.append(FadeOut(mobj), **kwargs)

    return plays

def PlayHideObjs(scene, names, **kwargs):
    plays = []
    for name in names:
        mobj = scene.mobject(name)
        if not mobj: continue
        elem = scene.geo.element(name)
        if not elem: continue

        plays.append(FadeOut(mobj, **kwargs))

    scene.play(*plays)

    for name in names:
        mobj = scene.mobject(name)
        if not mobj: continue
        elem = scene.geo.element(name)
        if not elem: continue

        elem.visible = False
        mobj.set_opacity(0)

def GrayStyleObjs(scene, names, **kwargs):
    plays = []
    for name in names:
        mobj = scene.mobject(name)
        if not mobj: continue
        elem = scene.geo.element(name)
        if not elem: continue

        scene._styles_back[name] = {}

        if getParamFromDict(elem.style, 'z_index'): 
            scene._styles_back[name]['z_index'] = elem.style['z_index']
            elem.style['z_index'] = 0

        if getParamFromDict(elem.style, 'stroke'): 
            scene._styles_back[name]['stroke'] = elem.style['stroke']
            elem.style['stroke'] = GeoDynamic.style_default.col_gray

        if getParamFromDict(elem.style, 'fill'):
            scene._styles_back[name]['fill'] = elem.style['fill']
            elem.style['fill'] = GeoDynamic.style_default.col_gray

        if getParamFromDict(elem.style, 'show_label'):
            scene._styles_back[name]['label_color'] = elem.style['label_color'] if ('label_color' in elem.style) else GeoDynamic.style_default.strong
            elem.style['label_color'] = GeoDynamic.style_default.col_gray

        if type(elem.data) == geo.Point:
            scene._styles_back[name]['fill_opacity'] = elem.style['fill_opacity'] if ('fill_opacity' in elem.style) else 1
            elem.style['fill_opacity'] = 0

        scene._gray_mobjects['_gray_' + name] = CreateMObject(elem, debug = True)
        #plays.append(mobj.animate.become(CreateMObject(elem)))
        plays.extend(HideObjs(scene, [name], **kwargs))
        plays.append(FadeIn(scene._gray_mobjects['_gray_' + name], **kwargs))

    return plays

def BackStyleObjs(scene, names, **kwargs):
    plays = []
    for name in names:
        mobj = scene.mobject(name)
        if not mobj: continue
        if name not in scene._styles_back: continue
        elem = scene.geo.element(name)
        style_back = scene._styles_back[name]
        if (not elem) or (not style_back): continue

        for key in style_back: elem.style[key] = style_back[key]

        #plays.append(mobj.animate.become(CreateMObject(elem)))
        plays.extend(ShowObjs(scene, [name], **kwargs))
        plays.append(FadeOut(scene._gray_mobjects['_gray_' + name], **kwargs))
        del scene._gray_mobjects['_gray_' + name]

    return plays

#--------------------------------------------------------------------------

def correctedLabel(label):
    texsymb = {
        '\\cdot': '·', '\\times':  '×', '\\neq': '≠', '\\approx': '≈', '\\sim': '~', '\\leqslant': '⩽', '\\geqslant': '⩾',
        '\\degree': '°', '\\Rightarrow': '⇒', '\\Leftarrow': '⇐', '\\rightarrow': '→', '\\to': '→', '\\gets': '←',
        '\mathbf': '∠', '\\triangle': '△', '\\perp': '⊥', '\\parallel': '∥', '\\nparralel': '∦',
        '\\in': '∈', '\\notin': '∉', '\\cap': '∩', '\\cup': '∪', '\\subset': '⊂', '\\supset': '⊃', '\\subseteq': '⊆', '\\supseteq': '⊇', '\\forall': '∀', '\\exists': '∃',
        '\\Longleftrightarrow': '⟺', '\\Leftrightarrow': '⟺', '\\pm': '±', '\\varnothing': '∅', '\\infty': '∞',
        '\\mathrm A': 'Α', '\\alpha': 'α',
        '\\mathrm B': 'Β', '\\beta': 'β',
        '\\Gamma': 'Γ', '\\gamma': 'γ',
        '\\Delta': 'Δ', '\\delta': 'δ',
        '\\mathrm E': 'Ε', '\\varepsilon': 'ε',
        '\\mathrm Z': 'Ζ', '\\zeta': 'ζ',
        '\\mathrm H': 'Η', '\\eta': 'η',
        '\\Theta': 'Θ', '\\theta': 'ϑ', '\\vartheta': 'ϑ',
        '\\mathrm I': 'Ι', '\\iota': 'ι',
        '\\mathrm K': 'Κ', '\\kappa': 'κ',
        '\\Lambda': 'Λ', '\\lambda': 'λ',
        '\\mathrm M': 'Μ', '\\mu': 'μ',
        '\\mathrm N': 'Ν', '\\nu': 'ν',
        '\\Xi': 'Ξ', '\\xi': 'ξ',
        '\\mathrm O': 'Ο', '\\mathrm o': 'ο',
        '\\Pi': 'Π', '\\pi': 'π', '\\varpi': 'ϖ',
        '\\mathrm P': 'Ρ', '\\rho': 'ρ',
        '\\Sigma': 'Σ', '\\sigma': 'σ', '\\varsigma': 'ς',
        '\\mathrm T': 'Τ', '\\tau': 'τ',
        '\\Upsilon': 'Υ', '\\upsilon': 'υ',
        '\\Phi': 'Φ', '\\varphi': 'φ',
        '\\mathrm X': 'Χ', '\\chi': 'χ',
        '\\Psi': 'Ψ', '\\psi': 'ψ',
        '\\Omega': 'Ω', '\\omega': 'ω'
    }

    #print('BEFORE: ', label)
    for tex in texsymb:
        label = re.sub(texsymb[tex], re.sub(r'\\', r'\\\\', tex), label)

    #print('AFTER: ', label)

    return label

def getAngRadius(ang: geo.Angle, style = None):
    if style is None: style = GeoDynamic.style_default
    r = style.ang_rdefault
    max_r = min(np.linalg.norm(ang.v1), np.linalg.norm(ang.v2))*0.65
    if ang.angle > 0.01:
        return min(max_r, r / ang.angle**0.25)
    else:
        return min(max_r, r / 0.01**0.25)
        
def getRightAngSize(ang: geo.Angle, style = None):
    if style is None: style = GeoDynamic.style_default
    r = style.ang_right
    max_r = min(np.linalg.norm(ang.v1), np.linalg.norm(ang.v2))*0.65
    return min(max_r, r)

def CreateMObject(elem, z_auto = False, style = None, debug = False):
    try:
        if style is None: style = GeoDynamic.style_default

        dash = getParamFromDict(elem.style, 'stroke_dash', None)

        col_s = getParamFromDict(elem.style, 'stroke', style.strong)
        col_f = getParamFromDict(elem.style, 'fill', style.background if type(elem.data) != geo.Point else style.strong)
        op_s = getParamFromDict(elem.style, 'stroke_opacity', 1)
        op_f = getParamFromDict(elem.style, 'fill_opacity', 1)
        lw = getParamFromDict(elem.style, 'stroke_width', style.line_width, type(elem.data) == geo.Arc)
        col_label = getParamFromDict(elem.style, 'label_color', style.strong)

        zz = getParamFromDict(elem.style, 'z_index')
        zz_fill = 0.01
        zz_stroke = 5
        zz_label = 50

        if (zz is None) & z_auto:
            if type(elem.data) == geo.Polygon: zz = 0.01
            elif type(elem.data) == geo.Angle: zz = 3
            elif type(elem.data) == geo.Segment: zz = 5
            elif type(elem.data) == geo.Circle: zz = 5
            elif type(elem.data) == geo.Arc: zz = 5
            elif type(elem.data) == geo.Point: zz = 50

        if zz is None: zz = 0.01
        if zz == 0.01: zz_label = 0.1

        if type(elem.data) == geo.Polygon:
            pp = [[p[0], p[1], 0] for p in elem.data.points]
            poly_fill = Polygon(*pp, color = col_s, fill_color = col_f, fill_opacity = op_f, stroke_width = 0, stroke_opacity = 0).set_z_index(zz)
            poly_stroke = Polygon(*pp, joint_type = LineJointType.ROUND, color = col_s, fill_opacity = 0, stroke_width = lw, stroke_opacity = op_s).set_z_index(max(zz_stroke, zz + 0.1))
            
            return VGroup(poly_fill, poly_stroke, name = elem.name)
            
        if type(elem.data) == geo.Angle: 
            arr = []
            r = getAngRadius(elem.data, style) + elem.style['r_offset'] + (elem.style['lines'] - 1) * style.ang_rshift
            p = [elem.data.p[0], elem.data.p[1], 0]
            line1 = Line([p[0], p[1], 0], [p[0] + elem.data.v1[0], p[1] + elem.data.v1[1], 0])
            line2 = Line([p[0], p[1], 0], [p[0] + elem.data.v2[0], p[1] + elem.data.v2[1], 0])    

            right_mark = np.isclose(elem.data.angle, PI/2) if 'right_mark' not in elem.style else elem.style['right_mark']

            if right_mark:
                r = getRightAngSize(elem.data, style)
                n1 = elem.data.v1 * (r / np.linalg.norm(elem.data.v1))
                n2 = elem.data.v2 * (r / np.linalg.norm(elem.data.v2))
                p1 = [p[0] + n1[0], p[1] + n1[1], 0]
                p2 = [p1[0] + n2[0], p1[1] + n2[1], 0]
                p3 = [p[0] + n2[0], p[1] + n2[1], 0]
                arr.append(Polygon(p, p1, p2, p3, 
                                    color = col_f, stroke_width = 0, fill_opacity = op_f).set_z_index(zz))
                arr.append(RightAngle(line1, line2, length = r,
                                color = col_s, fill_opacity = 0, stroke_width = style.ang_width, stroke_opacity = op_s).set_z_index(zz + 0.1))
            else:
                arr.append(AnnularSector(inner_radius = 0, outer_radius = r, angle = elem.data.angle, 
                                color = col_f, fill_opacity = op_f).set_z_index(zz)
                                .rotate(elem.data.start_angle, about_point=ORIGIN).shift ([p[0], p[1], 0]))
                for i in range(elem.style['lines']):
                    arr.append(Angle(line1, line2, radius = r - i * style.ang_rshift, other_angle = False, 
                                color = col_s, fill_opacity = 0, stroke_width = style.ang_width, stroke_opacity = op_s).set_z_index(zz + 0.1))

            if hasParam(elem.style, 'show_label'):
                if hasParam(elem.style, 'label_r_offset'): r += elem.style['label_r_offset']
                label = elem.style['label'] if hasParam(elem.style, 'label') else '$' + elem.name + '$'
                tex = Tex(correctedLabel(label), color = col_label).set_z_index(zz_label)
                tex.move_to(Angle(line1, line2, radius = r).point_from_proportion(0.5))
                arr.append(tex)
                if hasParam(elem.style, 'offset'):
                    tex.shift([elem.style['offset'][0], elem.style['offset'][1], 0])

            return VGroup(*arr, name = elem.name)

        if type(elem.data) == geo.Segment:
            p1, p2 = elem.data.end_points
            m = (p1 + p2) / 2
            arr = []

            if dash: arr.append(DashedLine([p1[0], p1[1], 0], [p2[0], p2[1], 0], 
                            color = col_s, stroke_opacity = op_s, stroke_width = lw, dash_length = 0.17, dashed_ratio = dash).set_z_index(zz))
            else: arr.append(Line([p1[0], p1[1], 0], [p2[0], p2[1], 0], 
                            color = col_s, stroke_opacity = op_s, stroke_width = lw).set_z_index(zz))

            if 'lines' in elem.style:
                num = elem.style['lines']
                dn = elem.data.n * style.strich_len / 2
                v = (p2 - p1) / np.linalg.norm(p2 - p1)
                line = Line([m[0] + dn[0], m[1] + dn[1], 0], [m[0] - dn[0], m[1] - dn[1], 0],
                            color = col_s, stroke_width = style.strich_width, stroke_opacity = op_s).set_z_index(zz)

                for i in range(num):
                    d = style.strich_rshift * ((1 - num) * 0.5 + i)
                    arr.append(line.copy().shift([v[0] * d, v[1] * d, 0]))       

            if hasParam(elem.style, 'show_label'):
                label = elem.style['label'] if hasParam(elem.style, 'label') else '$' + elem.name + '$'
                tex = Tex(correctedLabel(label), color = col_label).set_z_index(zz_label)
                tex.move_to([m[0], m[1], 0])
                arr.append(tex)
                if hasParam(elem.style, 'offset'):
                    tex.shift([elem.style['offset'][0], elem.style['offset'][1], 0])
            
            return VGroup(*arr, name = elem.name)

        if type(elem.data) == geo.Circle: 
            circ_fill = Circle(name = elem.name, arc_center = [elem.data.c[0], elem.data.c[1], 0], radius = elem.data.r, 
                        fill_color = col_f, fill_opacity = op_f, stroke_opacity = 0, stroke_width = 0).set_z_index(zz_fill)
            circ_stroke = Circle(name = elem.name, arc_center = [elem.data.c[0], elem.data.c[1], 0], radius = elem.data.r, 
                        color = col_s, fill_opacity = 0, stroke_opacity = op_s, stroke_width = lw).set_z_index(zz)
            
            if dash:
                circ_stroke = DashedVMobject(
                    circ_stroke, num_dashes=int(2 * np.pi * elem.data.r / 0.17), dashed_ratio=dash
                )
            
            return VGroup(circ_fill, circ_stroke, name = elem.name)

        if type(elem.data) == geo.Arc:  
            c = [elem.data.c[0], elem.data.c[1], 0]
            a1, a2 = elem.data.angles 
            arr = [
                Arc(arc_center = c, radius = elem.data.r, start_angle = a1, angle = (a2 - a1) % (2*np.pi),
                        fill_color = col_f, fill_opacity = op_f, stroke_width = 0).set_z_index(zz_fill),
                Arc(arc_center = c, radius = elem.data.r, start_angle = a1, angle = (a2 - a1) % (2*np.pi),
                        color = col_s, fill_opacity = 0, stroke_opacity = op_s, stroke_width = lw).set_z_index(zz)
            ]
            if hasParam(elem.style, 'show_label'):
                label = elem.style['label'] if hasParam(elem.style, 'label') else '$' + elem.name + '$'
                tex = Tex(correctedLabel(label), color = col_label).set_z_index(zz_label)
                tex.move_to(Arc(arc_center = c, radius = elem.data.r + 0.7, start_angle = a1, angle = a2 - a1).point_from_proportion(0.5))
                arr.append(tex)
                if hasParam(elem.style, 'offset'):
                    tex.shift([elem.style['offset'][0], elem.style['offset'][1], 0])

            return VGroup(*arr, name = elem.name)

        if type(elem.data) == geo.Point:  
            arr = [Dot([elem.data.a[0], elem.data.a[1], 0], radius = style.dot_size / 2,
                    color = col_f, fill_opacity = op_f).set_z_index(zz)]
            if hasParam(elem.style, 'show_label'):
                label = elem.style['label'] if hasParam(elem.style, 'label') else '$' + elem.name + '$'
                tex = Tex(correctedLabel(label), color = col_label).set_z_index(zz_label).scale(1.12).move_to(arr[0])
                arr.append(tex)
                if hasParam(elem.style, 'offset'):
                    tex.shift([elem.style['offset'][0], elem.style['offset'][1], 0])

            return VGroup(*arr, name = elem.name)
    except:
        print(f'MObject for element "{elem.name}" is NONE')
        return None
    
    return None

