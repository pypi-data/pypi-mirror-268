from __future__ import annotations

import itertools as it
import tempfile
from contextlib import contextmanager
from pathlib import Path

import cairo
import numpy as np
from manim import VGroup, VMobject
from manim.utils.family import extract_mobject_family_members

CAIRO_LINE_WIDTH_MULTIPLE: float = 0.01

__all__ = ["create_svg_from_vmobject", "create_svg_from_vgroup"]


@contextmanager
def _get_cairo_context(
    file_name: str | Path
) -> cairo.Context:
    from manim import config
    
    view = config.ggb_view
    scale = view['scale']

    pw = int(view['width'])
    ph = int(view['height'])

    surface = cairo.SVGSurface(
        file_name,
        pw,
        ph,
    )
    ctx = cairo.Context(surface)
    ctx.scale(pw, ph)
    ctx.set_matrix(
        cairo.Matrix(
            scale,
            0,
            0,
            -scale,
            view['xZero'],
            view['yZero']
        ),
    )
    yield ctx
    surface.finish()

def _transform_points_pre_display(points: np.ndarray) -> np.ndarray:
    if not np.all(np.isfinite(points)):
        # TODO, print some kind of warning about
        # mobject having invalid points?
        points = np.zeros((1, 3))
    return points

def _get_stroke_rgbas(vmobject: VMobject, background: bool = False):
    return vmobject.get_stroke_rgbas(background)

def _set_cairo_context_color(
    ctx: cairo.Context,
    rgbas: np.ndarray,
    vmobject: VMobject,
):
    if len(rgbas) == 1:
        # Use reversed rgb because cairo surface is
        # encodes it in reverse order
        ctx.set_source_rgba(*rgbas[0])
    else:
        points = vmobject.get_gradient_start_and_end_points()
        points = _transform_points_pre_display(points)
        pat = cairo.LinearGradient(*it.chain(*(point[:2] for point in points)))
        step = 1.0 / (len(rgbas) - 1)
        offsets = np.arange(0, 1 + step, step)
        for rgba, offset in zip(rgbas, offsets):
            pat.add_color_stop_rgba(offset, *rgba)
        ctx.set_source(pat)

def _apply_stroke(ctx: cairo.Context, vmobject: VMobject, background: bool = False, technic = None):
    from manim import config

    width = vmobject.get_stroke_width(background)
    if width == 0:
        return
    _set_cairo_context_color(
        ctx,
        _get_stroke_rgbas(vmobject, background=background),
        vmobject,
    )
    ctx.set_line_width(
        width
        * CAIRO_LINE_WIDTH_MULTIPLE
        # This ensures lines have constant width as you zoom in on them.
        * (config.frame_width / config.frame_width),
    )
    if technic is not None:
        linecap = {
            "auto": cairo.LINE_CAP_BUTT,
            "butt": cairo.LINE_CAP_BUTT,
            "round": cairo.LINE_CAP_ROUND,
            "square": cairo.LINE_CAP_SQUARE
        }
        ctx.set_line_cap(linecap[technic['line_caps']])
    
    # if vmobject.joint_type != LineJointType.AUTO:
    #     ctx.set_line_join(LINE_JOIN_MAP[vmobject.joint_type])
    ctx.stroke_preserve()

def _apply_fill(ctx: cairo.Context, vmobject: VMobject, technic = None):
    """Fills the cairo context
    Parameters
    ----------
    ctx
        The cairo context
    vmobject
        The VMobject
    Returns
    -------
    Camera
        The camera object.
    """
    _set_cairo_context_color(
        ctx,
        vmobject.get_fill_rgbas(),
        vmobject,
    )
    ctx.fill_preserve()
    return

def _create_svg_from_vmobject_internal(vmobject: VMobject, ctx: cairo.Content, technic = None):
    # check if points are valid
    points = vmobject.points
    points = _transform_points_pre_display(points)
    if len(points) == 0:
        return
    ctx.new_path()
    subpaths = vmobject.gen_subpaths_from_points_2d(points)
    for subpath in subpaths:
        quads = vmobject.gen_cubic_bezier_tuples_from_points(subpath)
        ctx.new_sub_path()
        start = subpath[0]
        ctx.move_to(*start[:2])
        for _p0, p1, p2, p3 in quads:
            ctx.curve_to(*p1[:2], *p2[:2], *p3[:2])
        if vmobject.consider_points_equals_2d(subpath[0], subpath[-1]):
            ctx.close_path()

    _apply_stroke(ctx, vmobject, background=True, technic = technic)
    _apply_fill(ctx, vmobject, technic = technic)
    _apply_stroke(ctx, vmobject, technic = technic)

def create_svg_from_vmobject(
    vmobject: VMobject,
    file_name: str | Path = None,
    technic = None
) -> Path:
    """create_svg_from_vmobject creates an svg from a VMobject.

    Parameters
    ----------
    vmobject : VMobject
        The VMobject to create an svg from.
    file_name : str | Path, optional
        Path to the file to save the svg to, by default None
        which will create a temporary file and return the path.
    crop : bool, optional
        Whether to crop the svg, by default True
    padding : float, optional
        The padding around the svg, by default 0.05

    Returns
    -------
    Path
        The path to the svg file.
    """

    if file_name is None:
        file_name = tempfile.mktemp(suffix=".svg")
    file_name = Path(file_name).absolute()
    with _get_cairo_context(file_name) as ctx:
        for _vmobject in extract_mobject_family_members([vmobject], True, True):
            _create_svg_from_vmobject_internal(_vmobject, ctx, technic = technic)
    return file_name

def create_svg_from_vgroup(
    vgroup: VGroup,
    file_name: str | Path = None,
    technic = None
) -> Path:
    """create_svg_from_vgroup creates an svg from a VGroup.

    Parameters
    ----------
    vgroup : VGroup
        The VGroup to create the svg from.
    file_name : str | Path, optional
        Path to the file to save the svg to, by default None
        which will create a temporary file and return the path.
    crop : bool, optional
        Whether to crop the svg to the size of the VGroup, by default True
    padding : float, optional
        The padding to add to the svg if crop is ``True``, by default 0.05

    Returns
    -------
    Path
        The path to the svg file.
    """
    if file_name is None:
        file_name = tempfile.mktemp(suffix=".svg")
    file_name = Path(file_name).absolute()
    with _get_cairo_context(file_name) as ctx:
        # a vgroup is a list of VMobjects which may contain other VGroups
        # flatten the vgroup to get a list of VMobjects
        vgroup = extract_mobject_family_members(vgroup, True, True)
        for vmobject in vgroup:
            _create_svg_from_vmobject_internal(vmobject, ctx, technic = technic)
    return file_name
