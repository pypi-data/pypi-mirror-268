import numpy as np
import os
import glob
import functools

import tifffile
import h5py
import json
import napari
import skimage.data
import datetime
from enum import Enum
from pathlib import Path
import matplotlib.pyplot as plt
from magicgui import magicgui, widgets

from TXM_Sandbox.utils.io import data_reader, tomo_h5_reader, data_info, tomo_h5_info
from TXM_Sandbox.utils.tomo_recon_tools import rm_redundant
from TXM_Sandbox.gui.gui_components import (
    check_file_availability,
    determine_element,
    determine_fitting_energy_range,
    scale_eng_list,
    def_dflt_eng_rgn,
)
from TXM_Sandbox.utils.io import h5_lazy_reader

from utils.io import create_hdf5_from_json

plt.ion()

h5_reader = data_reader(tomo_h5_reader)
info_reader = data_info(tomo_h5_info)

cfg_fn = Path(__file__).parent / "configs/txm_simple_gui_script_cfg.json"
tomo_rec_script_fn = Path(__file__).parent / "scripts/tomo_recon_cmd.py"
xanes3d_auto_cen_reg_script_fn = (
    Path(__file__).parent / "scripts/xanes3d_tomo_autocent_cmd.py"
)
xanes3d_fit_script_fn = Path(__file__).parent / "scripts/xanes3D_fit_cmd.py"

with open(Path(__file__).parent / "configs/xanes3d_tomo_template_cfg.json") as f:
    xanes3d_tomo_template_dict = json.load(f)

with open(Path(__file__).parent / "configs/xanes3d_tomo_autocent_cfg.json") as f:
    xanes3d_tomo_autocent_cfg = json.load(f)

with open(Path(__file__).parent / "configs/xanes_proc_data_struct_cfg.json") as f:
    xanes_proc_data_struct = json.load(f)

ZFLY_CFG = {
    "io_data_structure_tomo": {
        "use_h5_reader": True,
        "structured_h5_reader": {
            "io_data_structure": {
                "data_path": "/Exchange/data",
                "flat_path": "/Exchange/flat",
                "dark_path": "/Exchange/dark",
                "theta_path": "/Exchange/angle",
            },
            "io_data_info": {
                "item00_path": "/Exchange/data",
                "item01_path": "/Exchange/angle",
                "item02_path": "/Experiment/Magnification",
                "item03_path": "/Experiment/Pixel Size",
                "item04_path": "/Experiment/X_eng (keV)",
                "item05_path": "/Experiment/note",
                "item06_path": "/Experiment/scan_time",
                "item07_path": "",
            },
        },
        "tomo_raw_fn_template": "tomo_zfly_id_{0}.h5",
        "customized_reader": {"user_tomo_reader": ""},
    },
    "io_data_structure_xanes2D": {
        "use_h5_reader": True,
        "structured_h5_reader": {
            "io_data_structure": {
                "data_path": "/img_xanes",
                "flat_path": "/img_bkg",
                "dark_path": "/img_dark",
                "eng_path": "/X_eng",
            },
            "io_data_info": {
                "item00_path": "/img_xanes",
                "item01_path": "/X_eng",
                "item02_path": "/Magnification",
                "item03_path": "/Pixel Size",
                "item04_path": "/note",
                "item05_path": "/scan_time",
                "item06_path": "",
                "item07_path": "",
            },
        },
        "xanes2D_raw_fn_template": "xanes_scan2_id_{0}.h5",
        "customized_reader": {"user_xanes2D_reader": ""},
    },
    "io_data_structure_xanes3D": {
        "use_h5_reader": True,
        "structured_h5_reader": {
            "io_data_structure": {
                "data_path": "/Exchange/data",
                "flat_path": "/Exchange/flat",
                "dark_path": "/Exchange/dark",
                "eng_path": "/Experiment/X_eng (keV)",
            },
            "io_data_info": {
                "item00_path": "/Exchange/data",
                "item01_path": "/Exchange/angle",
                "item02_path": "/Experiment/Magnification",
                "item03_path": "/Experiment/Pixel Size",
                "item04_path": "/Experiment/X_eng (keV)",
                "item05_path": "/Experiment/note",
                "item06_path": "/Experiment/scan_time",
                "item07_path": "",
            },
        },
        "tomo_raw_fn_template": "tomo_zfly_id_{0}.h5",
        "xanes3D_recon_dir_template": "recon_tomo_zfly_id_{0}",
        "xanes3D_recon_fn_template": "recon_tomo_zfly_id_{0}_{1}.tiff",
        "customized_reader": {"user_xanes3D_reader": ""},
    },
}

FLY_CFG = {
    "io_data_structure_tomo": {
        "use_h5_reader": True,
        "structured_h5_reader": {
            "io_data_structure": {
                "data_path": "/img_tomo",
                "flat_path": "/img_bkg",
                "dark_path": "/img_dark",
                "theta_path": "/angle",
            },
            "io_data_info": {
                "item00_path": "/img_tomo",
                "item01_path": "/angle",
                "item02_path": "/Magnification",
                "item03_path": "/Pixel Size",
                "item04_path": "/X_eng",
                "item05_path": "/note",
                "item06_path": "/scan_time",
                "item07_path": "",
            },
        },
        "tomo_raw_fn_template": "fly_scan_id_{0}.h5",
        "customized_reader": {"user_tomo_reader": ""},
    },
    "io_data_structure_xanes2D": {
        "use_h5_reader": True,
        "structured_h5_reader": {
            "io_data_structure": {
                "data_path": "/img_xanes",
                "flat_path": "/img_bkg",
                "dark_path": "/img_dark",
                "eng_path": "/X_eng",
            },
            "io_data_info": {
                "item00_path": "/img_xanes",
                "item01_path": "/X_eng",
                "item02_path": "/Magnification",
                "item03_path": "/Pixel Size",
                "item04_path": "/note",
                "item05_path": "/scan_time",
                "item06_path": "",
                "item07_path": "",
            },
        },
        "xanes2D_raw_fn_template": "xanes_scan2_id_{0}.h5",
        "customized_reader": {"user_xanes2D_reader": ""},
    },
    "io_data_structure_xanes3D": {
        "use_h5_reader": True,
        "structured_h5_reader": {
            "io_data_structure": {
                "data_path": "/img_tomo",
                "flat_path": "/img_bkg",
                "dark_path": "/img_dark",
                "eng_path": "/X_eng",
            },
            "io_data_info": {
                "item00_path": "/img_tomo",
                "item01_path": "/angle",
                "item02_path": "/Magnification",
                "item03_path": "/Pixel Size",
                "item04_path": "/X_eng",
                "item05_path": "/note",
                "item06_path": "/scan_time",
                "item07_path": "",
            },
        },
        "tomo_raw_fn_template": "fly_scan_id_{0}.h5",
        "xanes3D_recon_dir_template": "recon_fly_scan_id_{0}",
        "xanes3D_recon_fn_template": "recon_fly_scan_id_{0}_{1}.tiff",
        "customized_reader": {"user_xanes3D_reader": ""},
    },
}

_TOMO_TRL_SCN_ID_CHOICES = []
_TOMO_XANES3D_REC_ID_S_CHOICES = []
_TOMO_XANES3D_REC_ID_E_CHOICES = []
# _XANES_FIT_FIT_ITEMS_CHOICES = []
_XANES_FIT_SAVE_ITEMS_CHOICES = []


def get_tomo_trl_avail_scn_id_choices(ComboBox):
    global _TOMO_TRL_SCN_ID_CHOICES
    return _TOMO_TRL_SCN_ID_CHOICES


def get_tomo_xanes3d_rec_id_s_choices(ComboBox):
    global _TOMO_XANES3D_REC_ID_S_CHOICES
    return _TOMO_XANES3D_REC_ID_S_CHOICES


def get_tomo_xanes3d_rec_id_e_choices(ComboBox):
    global _TOMO_XANES3D_REC_ID_E_CHOICES
    return _TOMO_XANES3D_REC_ID_E_CHOICES


# def get_xanes_fit_fit_items_choices(ComboBox):
#     global _XANES_FIT_FIT_ITEMS_CHOICES
#     return _XANES_FIT_FIT_ITEMS_CHOICES


def get_xanes_fit_save_items_choices(ComboBox):
    global _XANES_FIT_SAVE_ITEMS_CHOICES
    return _XANES_FIT_SAVE_ITEMS_CHOICES


def set_data_widget(widget, new_min, new_val, new_max):
    widget.min = min(new_min, widget.min)
    widget.max = max(new_max, widget.max)
    widget.value = new_val
    widget.min = new_min
    widget.max = new_max


def overlap_roi(mode="auto_cen"):
    if mode == "auto_cen":
        if "auto_cen_roi" in viewer.layers:
            viewer.layers.remove("auto_cen_roi")
        if "recon_roi" in viewer.layers:
            viewer.layers["recon_roi"].visible = False
        if "xanes_roi" in viewer.layers:
            viewer.layers["xanes_roi"].visible = False
        if tomo_xanes3d_rec.auto_cen_dft_roi.value:
            dim = viewer.layers["tomo viewer"].data.shape
            ellipse_data = [
                [int(dim[0] * 0.5), int(dim[1] * 0.5)],
                [int(dim[0] * 0.45), int(dim[1] * 0.45)],
            ]
            viewer.add_shapes(
                ellipse_data,
                shape_type="ellipse",
                edge_color="green",
                edge_width=3,
                face_color="transparent",
                name="auto_cen_roi",
            )
        else:
            [xs, xe] = tomo_xanes3d_rec.auto_cen_roix.value
            [ys, ye] = tomo_xanes3d_rec.auto_cen_roiy.value
            roi_coor = [[ys, xs], [ys, xe], [ye, xe], [ye, xs]]
            viewer.add_shapes(
                roi_coor,
                shape_type="rectangle",
                edge_color="green",
                edge_width=3,
                face_color="transparent",
                name="auto_cen_roi",
            )
        viewer.layers["tomo viewer"].refresh()
    elif mode == "recon_roi":
        [xs, xe] = tomo_xanes3d_rec.rec_roix.value
        [ys, ye] = tomo_xanes3d_rec.rec_roiy.value
        roi_coor = [[ys, xs], [ys, xe], [ye, xe], [ye, xs]]
        if "recon_roi" in viewer.layers:
            viewer.layers.remove("recon_roi")
        if "auto_cen_roi" in viewer.layers:
            viewer.layers["auto_cen_roi"].visible = False
        if "xanes_roi" in viewer.layers:
            viewer.layers["xanes_roi"].visible = False
        viewer.add_shapes(
            roi_coor,
            shape_type="rectangle",
            edge_color="green",
            edge_width=3,
            face_color="transparent",
            name="recon_roi",
        )
        viewer.layers["tomo viewer"].refresh()
    elif mode == "xanes_roi":
        cx = xanes_reg_vis.roi_cen_x.value
        cy = xanes_reg_vis.roi_cen_y.value
        roi_coor = [
            [cy - 5, cx - 5],
            [cy - 5, cx + 5],
            [cy + 5, cx + 5],
            [cy + 5, cx - 5],
        ]
        if "recon_roi" in viewer.layers:
            viewer.layers["recon_roi"].visible = False
        if "auto_cen_roi" in viewer.layers:
            viewer.layers["auto_cen_roi"].visible = False
        if "xanes_roi" in viewer.layers:
            viewer.layers.remove("xanes_roi")
        viewer.add_shapes(
            roi_coor,
            shape_type="rectangle",
            edge_color="blue",
            edge_width=3,
            face_color="transparent",
            name="xanes_roi",
        )
        viewer.layers["xanes_data"].refresh()


def store_combobox():
    choices = []
    values = []
    choices.append(tomo_trl.scan_id.choices)
    choices.append(tomo_xanes3d_rec.scan_id_s.choices)
    choices.append(tomo_xanes3d_rec.scan_id_e.choices)
    values.append(tomo_trl.scan_id.value)
    values.append(tomo_xanes3d_rec.scan_id_s.value)
    values.append(tomo_xanes3d_rec.scan_id_e.value)
    return choices, values


def set_combobox(choices, values):
    tomo_trl.scan_id.choices = choices[0]
    tomo_xanes3d_rec.scan_id_s.choices = choices[1]
    tomo_xanes3d_rec.scan_id_e.choices = choices[2]
    if values[0] is not None:
        tomo_trl.scan_id.value = values[0]
    if values[1] is not None:
        tomo_xanes3d_rec.scan_id_s.value = values[1]
    if values[2] is not None:
        tomo_xanes3d_rec.scan_id_e.value = values[2]


def restore_combobox():
    def decorator_func(func):
        @functools.wraps(func)
        def inner_func(*args, **kwargs):
            choices, values = store_combobox()
            func(*args, **kwargs)
            set_combobox(choices, values)

        return inner_func

    return decorator_func


def show_layers_in_viewer(layers: list):
    for layer in viewer.layers:
        layer.visible = False
    for layer in layers:
        viewer.layers[layer].visible = True
    viewer.reset_view()


viewer = napari.Viewer()
viewer.add_image(
    skimage.data.astronaut().mean(-1).astype(np.float32), name="tomo viewer"
)


################################################################################
#             do trial recon for a single slice of a given scan                #
################################################################################
@magicgui(
    main_window=False,
    layout="vertical",
    call_button="Trial Recon",
    Step_1={
        "widget_type": "Label",
        "value": "--------------------     Trial Cen    --------------------",
    },
    top_dir={"widget_type": "FileEdit", "mode": "d", "value": Path.home()},
    file_type={
        "widget_type": "ComboBox",
        "choices": ["tomo_zfly", "fly_scan"],
        "value": "tomo_zfly",
    },
    # scan_id={"widget_type": "ComboBox", "choices": [], "enabled": False},
    scan_id={
        "widget_type": "ComboBox",
        "enabled": False,
        "choices": get_tomo_trl_avail_scn_id_choices,
    },
    cen_sch_s={
        "widget_type": "SpinBox",
        "min": 1,
        "max": 2500,
        "value": 600,
        "step": 1,
        "enabled": False,
    },
    ref_sli={
        "widget_type": "SpinBox",
        "min": 1,
        "max": 2560,
        "value": 540,
        "step": 1,
        "enabled": False,
    },
    is_wedge={
        "widget_type": "CheckBox",
        "value": False,
        "text": "is wedge",
        "enabled": False,
    },
    wedge_thsh={
        "widget_type": "FloatSpinBox",
        "min": 0,
        "max": 1,
        "step": 0.05,
        "value": 0.1,
        "enabled": False,
    },
    phase_retrieval={
        "widget_type": "CheckBox",
        "value": False,
        "text": "use phase retrieval filter",
        "enabled": False,
    },
    beta_gamma_ratio={
        "widget_type": "LineEdit",
        "value": "0.01",
        "label": "beta / gamma",
        "enabled": False,
    },
)
def tomo_trl(
    Step_1: str,
    top_dir: Path,
    file_type: str,
    scan_id: str,
    cen_sch_s: int,
    ref_sli: int,
    is_wedge: bool,
    wedge_thsh: float,
    phase_retrieval: bool,
    beta_gamma_ratio: str,
):
    _tomo_trl_run()


tomo_trl._tomo_cfg = ZFLY_CFG["io_data_structure_tomo"]
tomo_trl.scn_fn = None
tomo_trl._wedge_data_avg = 0


def __tomo_trl_check_avail_data():
    global _TOMO_TRL_SCN_ID_CHOICES
    ids = check_file_availability(
        str(tomo_trl.top_dir.value),
        scan_id=None,
        signature=tomo_trl._tomo_cfg["tomo_raw_fn_template"],
        return_idx=True,
    )
    if ids:
        _TOMO_TRL_SCN_ID_CHOICES = ids
    else:
        _TOMO_TRL_SCN_ID_CHOICES = []
    tomo_trl.scan_id.reset_choices()


def __comp_tomo_trl_fn():
    if tomo_trl.scan_id.value:
        tomo_trl.scn_fn = tomo_trl.top_dir.value / tomo_trl._tomo_cfg[
            "tomo_raw_fn_template"
        ].format(tomo_trl.scan_id.value)
    else:
        tomo_trl.scn_fn = None


def __disable_tomo_trl():
    if (tomo_trl.scn_fn is None) or (not tomo_trl.scn_fn.exists()):
        tomo_trl.scan_id.enabled = False
        tomo_trl.cen_sch_s.enabled = False
        tomo_trl.ref_sli.enabled = False
        tomo_trl.is_wedge.enabled = False
        tomo_trl.wedge_thsh.enabled = False
        tomo_trl.phase_retrieval.enabled = False
        tomo_trl.beta_gamma_ratio.enabled = False
        tomo_trl.call_button.enabled = False
    else:
        tomo_trl.scan_id.enabled = True
        tomo_trl.cen_sch_s.enabled = True
        tomo_trl.ref_sli.enabled = True
        tomo_trl.is_wedge.enabled = True
        if tomo_trl.is_wedge.value:
            tomo_trl.wedge_thsh.enabled = True
        else:
            tomo_trl.wedge_thsh.enabled = False
        tomo_trl.phase_retrieval.enabled = True
        if tomo_trl.phase_retrieval.value:
            tomo_trl.beta_gamma_ratio.enabled = True
        else:
            tomo_trl.beta_gamma_ratio.enabled = False
        tomo_trl.call_button.enabled = True
        __preset_tomo_trl()


def __preset_tomo_trl():
    tomo_trl._data_dim = info_reader(
        tomo_trl.scn_fn, dtype="data", cfg=tomo_trl._tomo_cfg
    )
    if (tomo_trl._data_dim[2] / 2 - tomo_trl.cen_sch_s.value) > (tomo_trl._data_dim[2] / 6):
        tomo_trl.cen_sch_s.value = int(tomo_trl._data_dim[2] / 2 - 40)
    if tomo_trl._data_dim[1] < tomo_trl.cen_sch_s.value:
        tomo_trl.ref_sli.value = int(tomo_trl._data_dim[1] / 2)


def _tomo_trl_sel_file_type():
    if tomo_trl.file_type.value == "tomo_zfly":
        tomo_trl._tomo_cfg = ZFLY_CFG["io_data_structure_tomo"]
    else:
        tomo_trl._tomo_cfg = FLY_CFG["io_data_structure_tomo"]
    __tomo_trl_check_avail_data()
    __comp_tomo_trl_fn()
    __disable_tomo_trl()
    tomo_vol_rec.enabled = False


def _tomo_trl_top_dir():
    __tomo_trl_check_avail_data()
    __comp_tomo_trl_fn()
    __disable_tomo_trl()
    tomo_trl._trial_cen_dir = tomo_trl.top_dir.value / "data_center"
    tomo_vol_rec.enabled = False


def _tomo_trl_sel_scn_id():
    __comp_tomo_trl_fn()
    __disable_tomo_trl()
    tomo_vol_rec.enabled = False


def _tomo_trl_is_wedge():
    if tomo_trl.is_wedge.value:
        tomo_trl.wedge_thsh.enabled = True

        theta = h5_reader(
            tomo_trl.scn_fn, dtype="theta", sli=[None], cfg=tomo_trl._tomo_cfg
        ).astype(np.float32)
        if tomo_trl.file_type.value == "tomo_zfly":
            idx = np.ones(tomo_trl._data_dim[0], dtype=bool)
        else:
            idx = rm_redundant(theta)
            theta = theta[idx]
            if tomo_trl._data_dim[0] > theta.shape[0]:
                idx = np.concatenate(
                    (idx, np.zeros(tomo_trl._data_dim[0] - theta.shape[0], dtype=bool))
                )
        data = h5_reader(
            tomo_trl.scn_fn,
            dtype="data",
            sli=[
                None,
                [tomo_trl.ref_sli.value, tomo_trl.ref_sli.value + 1],
                [0, tomo_trl._data_dim[2] - 1],
            ],
            cfg=tomo_trl._tomo_cfg,
        ).astype(np.float32)[idx]
        white = (
            h5_reader(
                tomo_trl.scn_fn,
                dtype="flat",
                sli=[
                    None,
                    [tomo_trl.ref_sli.value, tomo_trl.ref_sli.value + 1],
                    [0, tomo_trl._data_dim[2] - 1],
                ],
                cfg=tomo_trl._tomo_cfg,
            )
            .mean(axis=0)
            .astype(np.float32)
        )

        dark = (
            h5_reader(
                tomo_trl.scn_fn,
                dtype="dark",
                sli=[
                    None,
                    [tomo_trl.ref_sli.value, tomo_trl.ref_sli.value + 1],
                    [0, tomo_trl._data_dim[2] - 1],
                ],
                cfg=tomo_trl._tomo_cfg,
            )
            .mean(axis=0)
            .astype(np.float32)
        )

        data[:] = (data - dark[np.newaxis, :]) / (
            white[np.newaxis, :] - dark[np.newaxis, :]
        )[:]
        data[np.isinf(data)] = 0
        data[np.isnan(data)] = 0
        tomo_trl._wedge_data_avg = data.mean(axis=2).astype(np.float32)

        plt.close("all")
        plt.figure(0)
        plt.plot(tomo_trl._wedge_data_avg)
        plt.plot(
            np.ones(tomo_trl._wedge_data_avg.shape[0]) * tomo_trl.wedge_thsh.value,
        )
        plt.show()
    else:
        tomo_trl.wedge_thsh.enabled = False
        tomo_trl._wedge_data_avg = 0
    tomo_vol_rec.enabled = False


def _tomo_trl_wedge_thsh():
    if tomo_gui._wedge_autodet_fig is not None:
        plt.close(tomo_gui._wedge_autodet_fig)
    tomo_gui._wedge_autodet_fig, ax = plt.subplots()
    ax.plot(tomo_trl._wedge_data_avg)
    ax.set_title("spec in roi")
    ax.plot(
        np.ones(tomo_trl._wedge_data_avg.shape[0]) * tomo_trl.wedge_thsh.value,
    )
    ax.set_title("wedge detection")
    plt.show()
    tomo_vol_rec.enabled = False


def _tomo_trl_phase_retrieval():
    if tomo_trl.phase_retrieval.value:
        tomo_trl.beta_gamma_ratio.enabled = True
    else:
        tomo_trl.beta_gamma_ratio.enabled = False
    tomo_vol_rec.enabled = False


def _tomo_trl_run():
    with open(cfg_fn, "r") as f:
        tem = json.load(f)
        print(f"{tem=}")
        tem["tomo_recon"]["cfg_file"] = str(
            tomo_trl.top_dir.value
            / f"xanes3d_tomo_template_dict-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"
        )
    with open(cfg_fn, "w") as f:
        json.dump(tem, f, indent=4, separators=(",", ": "))

    xanes3d_tomo_template_dict["scan id"]["file_params"]["raw_data_top_dir"] = str(
        tomo_trl.top_dir.value
    )
    xanes3d_tomo_template_dict["scan id"]["file_params"]["data_center_dir"] = str(
        tomo_trl.top_dir.value / "data_center"
    )
    xanes3d_tomo_template_dict["scan id"]["file_params"]["recon_top_dir"] = str(
        tomo_trl.top_dir.value
    )
    xanes3d_tomo_template_dict["scan id"]["file_params"][
        "wedge_ang_auto_det_ref_fn"
    ] = str(
        tomo_trl.top_dir.value
        / f"{tomo_trl.file_type.value}_id_{tomo_trl.scan_id.value}.h5"
    )
    xanes3d_tomo_template_dict["scan id"]["file_params"][
        "io_confg"
    ] = tomo_trl._tomo_cfg
    xanes3d_tomo_template_dict["scan id"]["file_params"]["hardware_trig_type"] = (
        True if tomo_trl.file_type.value == "tomo_zfly" else False
    )

    xanes3d_tomo_template_dict["scan id"]["recon_config"]["recon_type"] = "Trial Cent"
    xanes3d_tomo_template_dict["scan id"]["recon_config"][
        "is_wedge"
    ] = tomo_trl.is_wedge.value

    xanes3d_tomo_template_dict["scan id"]["data_params"][
        "scan_id"
    ] = tomo_trl.scan_id.value
    xanes3d_tomo_template_dict["scan id"]["data_params"][
        "rot_cen"
    ] = tomo_trl.cen_sch_s.value
    xanes3d_tomo_template_dict["scan id"]["data_params"][
        "cen_win_s"
    ] = tomo_trl.cen_sch_s.value
    xanes3d_tomo_template_dict["scan id"]["data_params"]["sli_s"] = (
        tomo_trl.ref_sli.value - 10
    )
    xanes3d_tomo_template_dict["scan id"]["data_params"]["sli_e"] = (
        tomo_trl.ref_sli.value + 10
    )
    xanes3d_tomo_template_dict["scan id"]["data_params"]["col_s"] = 0
    xanes3d_tomo_template_dict["scan id"]["data_params"]["col_e"] = tomo_trl._data_dim[
        2
    ]
    xanes3d_tomo_template_dict["scan id"]["data_params"]["wedge_col_s"] = 0
    xanes3d_tomo_template_dict["scan id"]["data_params"]["wedge_col_e"] = (
        tomo_trl._data_dim[2]
    )
    xanes3d_tomo_template_dict["scan id"]["data_params"][
        "wedge_ang_auto_det_thres"
    ] = tomo_trl.wedge_thsh.value

    if tomo_trl.file_type.value == "tomo_zfly":
        xanes3d_tomo_template_dict["scan id"]["file_params"]["io_confg"][
            "structured_h5_reader"
        ]["io_data_structure"]["eng_path"] = ZFLY_CFG["io_data_structure_xanes3D"][
            "structured_h5_reader"
        ][
            "io_data_structure"
        ][
            "eng_path"
        ]
    else:
        xanes3d_tomo_template_dict["scan id"]["file_params"]["io_confg"][
            "structured_h5_reader"
        ]["io_data_structure"]["eng_path"] = FLY_CFG["io_data_structure_xanes3D"][
            "structured_h5_reader"
        ][
            "io_data_structure"
        ][
            "eng_path"
        ]

    if tomo_trl.phase_retrieval.value:
        xanes3d_tomo_template_dict["scan id"]["flt_params"]["2"] = {
            "filter_name": "phase retrieval",
            "params": {
                "filter": "paganin",
                "pad": "True",
                "pixel_size": 6.5e-05,
                "dist": 15.0,
                "energy": 35.0,
                "alpha": float(tomo_trl.beta_gamma_ratio.value),
            },
        }
    else:
        if "2" in xanes3d_tomo_template_dict["scan id"]["flt_params"].keys():
            del xanes3d_tomo_template_dict["scan id"]["flt_params"]["2"]

    xanes3d_tomo_cfg = {
        str(tomo_trl.scan_id.value): xanes3d_tomo_template_dict["scan id"]
    }

    with open(tem["tomo_recon"]["cfg_file"], "w") as f:
        json.dump(xanes3d_tomo_cfg, f, indent=4, separators=(",", ": "))

    sig = os.system(f"ipython {tomo_rec_script_fn}")
    if sig == 0:
        if "data_center" in viewer.layers:
            viewer.layers.remove("data_center")
        viewer.open(tomo_trl._trial_cen_dir)

        rng = float(viewer.layers["data_center"].data[0].max()) - float(
            viewer.layers["data_center"].data[0].min()
        )
        viewer.layers["data_center"].contrast_limits = [
            float(viewer.layers["data_center"].data[0].min()) + 0.1 * rng,
            float(viewer.layers["data_center"].data[0].max()) - 0.1 * rng,
        ]
        viewer.reset_view()
        tomo_vol_rec.enabled = True
        tomo_vol_rec.pick_cen.enabled = True
        tomo_vol_rec.call_button.enabled = False


def _tomo_trl_prv():
    pass


tomo_trl.file_type.changed.connect(_tomo_trl_sel_file_type)
tomo_trl.top_dir.changed.connect(_tomo_trl_top_dir)
tomo_trl.scan_id.changed.connect(_tomo_trl_sel_scn_id)
tomo_trl.is_wedge.changed.connect(_tomo_trl_is_wedge)
tomo_trl.wedge_thsh.changed.connect(_tomo_trl_wedge_thsh)
tomo_trl.phase_retrieval.changed.connect(_tomo_trl_phase_retrieval)


################################################################################
# full volume reconstruction of the scan defined in Step_1 with a given center #
################################################################################
@magicgui(
    main_window=False,
    layout="vertical",
    call_button="Vol Recon",
    Step_2={
        "widget_type": "Label",
        "value": "--------------------      Vol Rec     --------------------",
    },
    cen={"widget_type": "LineEdit", "value": 600, "enabled": False},
    pick_cen={"widget_type": "PushButton", "text": "Pick Center", "enabled": False},
)
def tomo_vol_rec(Step_2: str, cen: int, pick_cen):
    _tomo_vol_rec_recon()


tomo_vol_rec._cen = None
tomo_vol_rec.call_button.enabled = False


def __tomo_vol_rec_show_sli():
    try:
        viewer.layers["tomo viewer"].data = tifffile.imread(
            str(tomo_xanes3d_rec.rec_fntpl).format(
                tomo_xanes3d_rec.ref_scan_id.value,
                str(tomo_xanes3d_rec.ref_sli.value).zfill(5),
            )
        )
    except Exception as e:
        print(e)


def _tomo_vol_rec_cen():
    tomo_vol_rec.call_button.enabled = False


def _tomo_vol_rec_pick_cen():
    fns = glob.glob(str(Path(tomo_trl._trial_cen_dir) / "*.tiff"))
    tomo_vol_rec._trial_cens = sorted([float(Path(fn).stem) for fn in fns])
    tomo_vol_rec.cen.value = tomo_vol_rec._trial_cens[int(viewer.dims.point[0])]
    tomo_vol_rec._cen = float(tomo_vol_rec.cen.value)
    tomo_vol_rec.call_button.enabled = True


def _tomo_vol_rec_recon():
    if tomo_vol_rec._cen is None:
        print("Please pick the best center for volume reconstruction.")
    else:
        viewer.layers.remove("data_center")
        with open(cfg_fn, "r") as f:
            with open(json.load(f)["tomo_recon"]["cfg_file"], "r") as ft:
                tem = json.load(ft)

        tem[list(tem.keys())[0]]["data_params"]["rot_cen"] = tomo_vol_rec._cen
        tem[list(tem.keys())[0]]["data_params"]["sli_s"] = 0
        tem[list(tem.keys())[0]]["data_params"]["sli_e"] = tomo_trl._data_dim[1]
        tem[list(tem.keys())[0]]["recon_config"]["recon_type"] = "Vol Recon"

        with open(cfg_fn, "r") as f:
            with open(json.load(f)["tomo_recon"]["cfg_file"], "w") as ft:
                json.dump(tem, ft, indent=4, separators=(",", ": "))

        sig = os.system(f"ipython {tomo_rec_script_fn}")
        if sig == 0:
            rec_path = Path(
                tem[list(tem.keys())[0]]["file_params"]["recon_top_dir"]
            ) / (
                "recon_"
                + Path(
                    tem[list(tem.keys())[0]]["file_params"]["io_confg"][
                        "tomo_raw_fn_template"
                    ].format(list(tem.keys())[0])
                ).stem
            )
            try:
                if "tomo viewer" in viewer.layers:
                    viewer.layers.remove("tomo viewer")
                viewer.open(rec_path, name="tomo viewer")
                viewer.reset_view()
            except Exception as e:
                print(e)


tomo_vol_rec.pick_cen.changed.connect(_tomo_vol_rec_pick_cen)
tomo_vol_rec.cen.changed.connect(_tomo_vol_rec_cen)


################################################################################
#             auto reconstruction and alignment for XANES3D                    #
################################################################################
@magicgui(
    main_window=False,
    layout="vertical",
    call_button="run",
    Step_3={
        "widget_type": "Label",
        "value": "-------------------- Auto Cen & Align --------------------",
    },
    # top_dir={"widget_type": "FileEdit", "mode": "d"},
    tomo_tplt_fn={"widget_type": "FileEdit", "mode": "r", "filter": "*.json"},
    ref_scan_id={
        "widget_type": "LineEdit",
        "enabled": False,
    },
    scan_id_s={
        "widget_type": "ComboBox",
        "choices": get_tomo_xanes3d_rec_id_s_choices,
        "enabled": False,
    },
    scan_id_e={
        "widget_type": "ComboBox",
        "choices": get_tomo_xanes3d_rec_id_e_choices,
        "enabled": False,
    },
    auto_cen_dft_roi={
        "widget_type": "CheckBox",
        "value": False,
        "text": "default roi x/y",
        "enabled": False,
    },
    auto_cen_roix={
        "widget_type": "RangeSlider",
        "min": 1,
        "max": 2560,
        "value": [540, 740],
        "enabled": False,
    },
    auto_cen_roiy={
        "widget_type": "RangeSlider",
        "min": 1,
        "max": 2560,
        "value": [540, 740],
        "enabled": False,
    },
    ref_sli={
        "widget_type": "Slider",
        "min": 1,
        "max": 2160,
        "value": 540,
        "enabled": False,
    },
    rec_roix={
        "widget_type": "RangeSlider",
        "min": 1,
        "max": 2560,
        "value": [540, 740],
        "enabled": False,
    },
    rec_roiy={
        "widget_type": "RangeSlider",
        "min": 1,
        "max": 2560,
        "value": [540, 740],
        "enabled": False,
    },
    rec_roiz={
        "widget_type": "RangeSlider",
        "min": 1,
        "max": 2160,
        "value": [440, 640],
        "enabled": False,
    },
    sli_srch_range={
        "widget_type": "SpinBox",
        "min": 0,
        "max": 30,
        "value": 10,
        "enabled": False,
    },
    cen_srch_range={
        "widget_type": "SpinBox",
        "min": 0,
        "max": 30,
        "value": 15,
        "enabled": False,
    },
    ang_corr={
        "widget_type": "CheckBox",
        "value": False,
        "text": "Ang Corr",
        "enabled": False,
    },
    ang_corr_range={
        "widget_type": "FloatSpinBox",
        "min": 0,
        "max": 5,
        "step": 0.5,
        "value": 3,
        "enabled": False,
        "enabled": False,
    },
    test_run={
        "widget_type": "PushButton",
        "tooltip": "run autocen for the first, middle, and the last scans to verify the autocen roi is correctly set",
        "enabled": False,
    },
    confirm_to_run={
        "widget_type": "RadioButtons",
        "choices": ["Yes", "No"],
        "orientation": "horizontal",
        "value": "No",
        "tooltip": "confirm if the autocen results are good",
        "enabled": False,
    },
)
def tomo_xanes3d_rec(
    Step_3: str,
    tomo_tplt_fn: Path,
    ref_scan_id: int,
    scan_id_s: str,
    scan_id_e: str,
    auto_cen_dft_roi: bool,
    auto_cen_roix: int,
    auto_cen_roiy: int,
    ref_sli: int,
    rec_roix: int,
    rec_roiy: int,
    rec_roiz: int,
    sli_srch_range: int,
    cen_srch_range: int,
    ang_corr: bool,
    ang_corr_range: float,
    test_run,
    confirm_to_run,
):
    _tomo_xanes3d_rec_run()


tomo_xanes3d_rec._tomo_cfg = ZFLY_CFG["io_data_structure_xanes3D"]
tomo_xanes3d_rec.scn_fntpl = None
tomo_xanes3d_rec._ref_rec_tplt = {"file_params": {"raw_data_top_dir": Path("")}}
tomo_xanes3d_rec._tomo_recon_tplt = None
tomo_xanes3d_rec.rec_roiz_lower_old_val = None
tomo_xanes3d_rec.rec_roiz_upper_old_val = None
tomo_xanes3d_rec._test_run_done = False
tomo_xanes3d_rec._continue_run_confirmed = False
tomo_xanes3d_rec._tomo_tplt_fn_old_val = ""
tomo_xanes3d_rec._scn_id_s_old_val = ""
tomo_xanes3d_rec._scn_id_e_old_val = ""


def __tomo_xanes3d_check_avail_id_s():
    global _TOMO_XANES3D_REC_ID_S_CHOICES
    ids = check_file_availability(
        tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"],
        scan_id=None,
        signature=tomo_xanes3d_rec._tomo_cfg["tomo_raw_fn_template"],
        return_idx=True,
    )
    if ids:
        _TOMO_XANES3D_REC_ID_S_CHOICES = ids
    else:
        _TOMO_XANES3D_REC_ID_S_CHOICES = []
    tomo_xanes3d_rec.scan_id_s.reset_choices()


def __tomo_xanes3d_check_avail_id_e():
    global _TOMO_XANES3D_REC_ID_E_CHOICES
    ids = check_file_availability(
        tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"],
        scan_id=None,
        signature=tomo_xanes3d_rec._tomo_cfg["tomo_raw_fn_template"],
        return_idx=True,
    )
    if ids:
        _TOMO_XANES3D_REC_ID_E_CHOICES = ids
    else:
        _TOMO_XANES3D_REC_ID_E_CHOICES = []
    tomo_xanes3d_rec.scan_id_e.reset_choices()


def __tomo_xanes3d_if_new_rec():
    if (
        (tomo_xanes3d_rec._tomo_tplt_fn_old_val != tomo_xanes3d_rec.tomo_tplt_fn.value)
        or (tomo_xanes3d_rec._scn_id_s_old_val != tomo_xanes3d_rec.scan_id_s.value)
        or (tomo_xanes3d_rec._scn_id_e_old_val != tomo_xanes3d_rec.scan_id_e.value)
    ):
        tomo_xanes3d_rec._new_rec_info = f"{xanes3d_tomo_autocent_cfg['aut_xns3d_pars']['scn_id_s']}-{xanes3d_tomo_autocent_cfg['aut_xns3d_pars']['scn_id_e']}_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


def __comp_tomo_xanes3d_fntpl():
    tomo_xanes3d_rec.scn_fntpl = (
        Path(tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"])
        / tomo_xanes3d_rec._tomo_cfg["tomo_raw_fn_template"]
    )
    tomo_xanes3d_rec.rec_fntpl = (
        Path(tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"])
        / tomo_xanes3d_rec._tomo_cfg["xanes3D_recon_dir_template"]
        / tomo_xanes3d_rec._tomo_cfg["xanes3D_recon_fn_template"]
    )


def __set_scan_id_lims():
    # ids = check_file_availability(
    #     tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"],
    #     scan_id=None,
    #     signature=tomo_xanes3d_rec._tomo_cfg["tomo_raw_fn_template"],
    #     return_idx=True,
    # )
    # print(f"{ids=}")
    # if ids:
    #     tomo_xanes3d_rec.scan_id_s.choices = ids
    #     if int(tomo_xanes3d_rec.ref_scan_id.value) - 1 >= int(ids[0]):
    #         tomo_xanes3d_rec.scan_id_s.value = ids[
    #             ids.index(tomo_xanes3d_rec.ref_scan_id.value) - 1
    #         ]
    #     else:
    #         tomo_xanes3d_rec.scan_id_s.value = ids[0]

    #     tomo_xanes3d_rec.scan_id_e.choices = ids
    #     if int(tomo_xanes3d_rec.ref_scan_id.value) + 1 <= int(ids[-1]):
    #         tomo_xanes3d_rec.scan_id_e.value = ids[
    #             ids.index(tomo_xanes3d_rec.ref_scan_id.value) + 1
    #         ]
    #     else:
    #         tomo_xanes3d_rec.scan_id_e.value = ids[-1]
    try:
        if int(tomo_xanes3d_rec.ref_scan_id.value) - 1 >= int(
            tomo_xanes3d_rec.scan_id_s.choices[0]
        ):
            tomo_xanes3d_rec.scan_id_s.value = tomo_xanes3d_rec.scan_id_s.choices[
                tomo_xanes3d_rec.scan_id_s.choices.index(
                    tomo_xanes3d_rec.ref_scan_id.value
                )
                - 1
            ]
        else:
            tomo_xanes3d_rec.scan_id_s.value = tomo_xanes3d_rec.scan_id_s.choices[0]

        if int(tomo_xanes3d_rec.ref_scan_id.value) + 1 <= int(
            tomo_xanes3d_rec.scan_id_s.choices[-1]
        ):
            tomo_xanes3d_rec.scan_id_e.value = tomo_xanes3d_rec.scan_id_s.choices[
                tomo_xanes3d_rec.scan_id_s.choices.index(
                    tomo_xanes3d_rec.ref_scan_id.value
                )
                + 1
            ]
        else:
            tomo_xanes3d_rec.scan_id_e.value = tomo_xanes3d_rec.scan_id_s.choices[-1]
    except:
        print("There is no valid scan series available for XANES3D autocent operation!")


def __set_roi_lims():
    b = glob.glob(
        str(
            (
                Path(tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"])
                / tomo_xanes3d_rec._tomo_cfg["xanes3D_recon_dir_template"].format(
                    tomo_xanes3d_rec.ref_scan_id.value
                )
            ).joinpath("*.tiff")
        )
    )
    ref_rec_ids = sorted([int(str(Path(fn).stem).split("_")[-1]) for fn in b])

    if ref_rec_ids:
        set_data_widget(
            tomo_xanes3d_rec.ref_sli,
            ref_rec_ids[0],
            ref_rec_ids[int(len(ref_rec_ids) / 2)],
            ref_rec_ids[-1],
        )
        set_data_widget(
            tomo_xanes3d_rec.rec_roiz,
            ref_rec_ids[0],
            [
                ref_rec_ids[int(len(ref_rec_ids) / 4)],
                ref_rec_ids[int(len(ref_rec_ids) * 3 / 4)],
            ],
            ref_rec_ids[-1],
        )
        tomo_xanes3d_rec.rec_roiz_lower_old_val = tomo_xanes3d_rec.rec_roiz.value[0]
        tomo_xanes3d_rec.rec_roiz_upper_old_val = tomo_xanes3d_rec.rec_roiz.value[1]

        dim = tifffile.imread(
            str(tomo_xanes3d_rec.rec_fntpl).format(
                tomo_xanes3d_rec.ref_scan_id.value,
                str(tomo_xanes3d_rec.ref_sli.value).zfill(5),
            )
        ).shape
        set_data_widget(
            tomo_xanes3d_rec.auto_cen_roix,
            0,
            [
                int(dim[1] / 4),
                int(dim[1] * 3 / 4),
            ],
            dim[1] - 1,
        )
        set_data_widget(
            tomo_xanes3d_rec.auto_cen_roiy,
            0,
            [
                int(dim[0] / 4),
                int(dim[0] * 3 / 4),
            ],
            dim[0] - 1,
        )
        set_data_widget(
            tomo_xanes3d_rec.rec_roix,
            0,
            [
                int(dim[1] / 4),
                int(dim[1] * 3 / 4),
            ],
            dim[1] - 1,
        )
        set_data_widget(
            tomo_xanes3d_rec.rec_roiy,
            0,
            [
                int(dim[0] / 4),
                int(dim[0] * 3 / 4),
            ],
            dim[0] - 1,
        )


def __disable_tomo_xanes3d_rec():
    if (tomo_xanes3d_rec.rec_fntpl is None) or (
        not Path(
            str(tomo_xanes3d_rec.rec_fntpl).format(
                tomo_xanes3d_rec.ref_scan_id.value,
                str(tomo_xanes3d_rec.ref_sli.value).zfill(5),
            )
        ).exists()
    ):
        tomo_xanes3d_rec.scan_id_s.enabled = False
        tomo_xanes3d_rec.scan_id_e.enabled = False
        tomo_xanes3d_rec.auto_cen_dft_roi.enabled = False
        tomo_xanes3d_rec.auto_cen_roix.enabled = False
        tomo_xanes3d_rec.auto_cen_roiy.enabled = False
        tomo_xanes3d_rec.ref_sli.enabled = False
        tomo_xanes3d_rec.rec_roix.enabled = False
        tomo_xanes3d_rec.rec_roiy.enabled = False
        tomo_xanes3d_rec.rec_roiz.enabled = False
        tomo_xanes3d_rec.sli_srch_range.enabled = False
        tomo_xanes3d_rec.cen_srch_range.enabled = False
        tomo_xanes3d_rec.ang_corr.enabled = False
        tomo_xanes3d_rec.ang_corr_range.enabled = False
        tomo_xanes3d_rec.test_run.enabled = False
        tomo_xanes3d_rec.confirm_to_run.enabled = False
        tomo_xanes3d_rec.call_button.enabled = False
    else:
        tomo_xanes3d_rec.scan_id_s.enabled = True
        tomo_xanes3d_rec.scan_id_e.enabled = True
        tomo_xanes3d_rec.auto_cen_dft_roi.enabled = True
        if tomo_xanes3d_rec.auto_cen_dft_roi.value:
            tomo_xanes3d_rec.auto_cen_roix.enabled = False
            tomo_xanes3d_rec.auto_cen_roiy.enabled = False
        else:
            tomo_xanes3d_rec.auto_cen_roix.enabled = True
            tomo_xanes3d_rec.auto_cen_roiy.enabled = True
        tomo_xanes3d_rec.ref_sli.enabled = True
        tomo_xanes3d_rec.rec_roix.enabled = True
        tomo_xanes3d_rec.rec_roiy.enabled = True
        tomo_xanes3d_rec.rec_roiz.enabled = True
        tomo_xanes3d_rec.sli_srch_range.enabled = True
        tomo_xanes3d_rec.cen_srch_range.enabled = True
        tomo_xanes3d_rec.ang_corr.enabled = True
        if tomo_xanes3d_rec.ang_corr.value:
            tomo_xanes3d_rec.ang_corr_range.enabled = True
        else:
            tomo_xanes3d_rec.ang_corr_range.enabled = False
        tomo_xanes3d_rec.test_run.enabled = True
        # __tomo_xanes3d_reset_rec_buttons()
        # __set_roi_lims()
        # try:
        #     __tomo_xanes3d_show_sli()
        # except:
        #     pass


def __tomo_xanes3d_show_sli(mode="auto_cen"):
    if mode == "auto_cen":
        try:
            viewer.layers["tomo viewer"].data = tifffile.imread(
                str(tomo_xanes3d_rec.rec_fntpl).format(
                    tomo_xanes3d_rec.ref_scan_id.value,
                    str(tomo_xanes3d_rec.ref_sli.value).zfill(5),
                )
            )
        except Exception as e:
            print(e)
    elif mode == "recon_roi":
        if (
            tomo_xanes3d_rec.rec_roiz_lower_old_val
            != tomo_xanes3d_rec.rec_roiz.value[0]
        ):
            try:
                viewer.layers["tomo viewer"].data = tifffile.imread(
                    str(tomo_xanes3d_rec.rec_fntpl).format(
                        tomo_xanes3d_rec.ref_scan_id.value,
                        str(tomo_xanes3d_rec.rec_roiz.value[0]).zfill(5),
                    )
                )
            except Exception as e:
                print(e)
        elif (
            tomo_xanes3d_rec.rec_roiz_upper_old_val
            != tomo_xanes3d_rec.rec_roiz.value[1]
        ):
            try:
                viewer.layers["tomo viewer"].data = tifffile.imread(
                    str(tomo_xanes3d_rec.rec_fntpl).format(
                        tomo_xanes3d_rec.ref_scan_id.value,
                        str(tomo_xanes3d_rec.rec_roiz.value[1]).zfill(5),
                    )
                )
            except Exception as e:
                print(e)
    rng = (
        viewer.layers["tomo viewer"].data.max()
        - viewer.layers["tomo viewer"].data.min()
    )
    viewer.layers["tomo viewer"].contrast_limits = [
        viewer.layers["tomo viewer"].data.min() + 0.1 * rng,
        viewer.layers["tomo viewer"].data.max() - 0.1 * rng,
    ]
    tomo_xanes3d_rec.rec_roiz_lower_old_val = tomo_xanes3d_rec.rec_roiz.value[0]
    tomo_xanes3d_rec.rec_roiz_upper_old_val = tomo_xanes3d_rec.rec_roiz.value[1]
    viewer.reset_view()


def __tomo_xnaes3d_def_autocent_cfg():
    with open(cfg_fn, "r") as f:
        tem = json.load(f)
        print(f"{tem=}")
        tem["xanes3d_auto_cen"]["cfg_file"] = str(
            Path(tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"])
            / f"xanes3d_tomo_autocent-{tomo_xanes3d_rec._new_rec_info}.json"
        )
    with open(cfg_fn, "w") as f:
        json.dump(tem, f, indent=4, separators=(",", ": "))

    xanes3d_tomo_autocent_cfg["template_file"] = str(
        tomo_xanes3d_rec.tomo_tplt_fn.value
    )
    if tomo_xanes3d_rec._continue_run_confirmed:
        xanes3d_tomo_autocent_cfg["run_type"] = "autocen&rec&reg"
    else:
        xanes3d_tomo_autocent_cfg["run_type"] = "autocen"
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["rec_dir_tplt"] = str(
        Path(tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"])
        / tomo_xanes3d_rec._tomo_cfg["xanes3D_recon_dir_template"]
    )
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["rec_fn_tplt"] = str(
        tomo_xanes3d_rec.rec_fntpl
    )
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["ref_scn_cen"] = (
        tomo_xanes3d_rec._ref_rec_tplt["data_params"]["rot_cen"]
    )
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "use_dflt_ref_reg_roi"
    ] = tomo_xanes3d_rec.auto_cen_dft_roi.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["ref_cen_roi"] = [
        tomo_xanes3d_rec.auto_cen_roiy.value[0],
        tomo_xanes3d_rec.auto_cen_roiy.value[1],
        tomo_xanes3d_rec.auto_cen_roix.value[0],
        tomo_xanes3d_rec.auto_cen_roix.value[1],
    ]
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "ref_cen_sli"
    ] = tomo_xanes3d_rec.ref_sli.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["rec_roi"] = [
        tomo_xanes3d_rec.rec_roiy.value[0],
        tomo_xanes3d_rec.rec_roiy.value[1],
        tomo_xanes3d_rec.rec_roix.value[0],
        tomo_xanes3d_rec.rec_roix.value[1],
        tomo_xanes3d_rec.rec_roiz.value[0],
        (tomo_xanes3d_rec.rec_roiz.value[1]),
    ]
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "ref_sli_srch_half_wz"
    ] = tomo_xanes3d_rec.sli_srch_range.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "ref_cen_srch_half_wz"
    ] = tomo_xanes3d_rec.cen_srch_range.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "ref_scn_id"
    ] = tomo_xanes3d_rec.ref_scan_id.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "scn_id_s"
    ] = tomo_xanes3d_rec.scan_id_s.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "scn_id_e"
    ] = tomo_xanes3d_rec.scan_id_e.value

    ids = tomo_xanes3d_rec.scan_id_e.choices.index(tomo_xanes3d_rec.scan_id_s.value)
    ide = tomo_xanes3d_rec.scan_id_e.choices.index(tomo_xanes3d_rec.scan_id_e.value)
    if tomo_xanes3d_rec._continue_run_confirmed:
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_lst"] = (
            tomo_xanes3d_rec.scan_id_e.choices[ids : ide + 1]
        )
    else:
        if len(tomo_xanes3d_rec.scan_id_e.choices[ids : ide + 1]) >= 3:
            xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_lst"] = [
                tomo_xanes3d_rec.scan_id_e.choices[ids],
                tomo_xanes3d_rec.ref_scan_id.value,
                tomo_xanes3d_rec.scan_id_e.choices[ide],
            ]
        else:
            xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_lst"] = [
                tomo_xanes3d_rec.scan_id_e.choices[ids],
                tomo_xanes3d_rec.scan_id_e.choices[ide],
            ]

    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "ang_corr"
    ] = tomo_xanes3d_rec.ang_corr.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
        "ang_corr_rgn"
    ] = tomo_xanes3d_rec.ang_corr_range.value
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["xanes3d_sav_trl_reg_fn"] = str(
        Path(tomo_xanes3d_rec._ref_rec_tplt["file_params"]["raw_data_top_dir"])
        / f"3D_trial_reg_scan_id_{tomo_xanes3d_rec._new_rec_info}.h5"
    )
    xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["XANES_tmp_fn"] = ""

    print(xanes3d_tomo_autocent_cfg)

    with open(tem["xanes3d_auto_cen"]["cfg_file"], "w") as f:
        json.dump(xanes3d_tomo_autocent_cfg, f, indent=4, separators=(",", ": "))


def __tomo_xanes3d_set_rec_status():
    tomo_xanes3d_rec._test_run_done = False
    tomo_xanes3d_rec.confirm_to_run.value == "No"
    tomo_xanes3d_rec._continue_run_confirmed = False


def __tomo_xanes3d_reset_rec_buttons():
    if tomo_xanes3d_rec._test_run_done:
        tomo_xanes3d_rec.confirm_to_run.enabled = True
    else:
        tomo_xanes3d_rec.confirm_to_run.enabled = False
        tomo_xanes3d_rec.confirm_to_run.value == "No"
        tomo_xanes3d_rec._continue_run_confirmed = False
    if tomo_xanes3d_rec._continue_run_confirmed:
        tomo_xanes3d_rec.call_button.enabled = True
    else:
        tomo_xanes3d_rec.call_button.enabled = False


def _tomo_xanes3d_set_cfg_fn():
    tomo_xanes3d_rec._tomo_tplt_fn = tomo_xanes3d_rec.tomo_tplt_fn.value
    with open(tomo_xanes3d_rec._tomo_tplt_fn, "r") as f:
        tem = json.load(f)
        tomo_xanes3d_rec.ref_scan_id.value = list(tem.keys())[0]
        tomo_xanes3d_rec._ref_rec_tplt = tem[list(tem.keys())[0]]
    __comp_tomo_xanes3d_fntpl()
    __tomo_xanes3d_check_avail_id_s()
    __tomo_xanes3d_check_avail_id_e()
    __set_scan_id_lims()
    __tomo_xanes3d_set_rec_status()
    __disable_tomo_xanes3d_rec()
    __tomo_xanes3d_reset_rec_buttons()
    __set_roi_lims()
    __tomo_xanes3d_show_sli(mode="auto_cen")


def _check_scan_id_s():
    if int(tomo_xanes3d_rec.scan_id_s.value) > int(tomo_xanes3d_rec.ref_scan_id.value):
        tomo_xanes3d_rec.scan_id_s.value = tomo_xanes3d_rec.ref_scan_id.value
    __tomo_xanes3d_set_rec_status()
    __tomo_xanes3d_reset_rec_buttons()


def _check_scan_id_e():
    if int(tomo_xanes3d_rec.scan_id_e.value) < int(tomo_xanes3d_rec.ref_scan_id.value):
        tomo_xanes3d_rec.scan_id_e.value = tomo_xanes3d_rec.ref_scan_id.value
    __tomo_xanes3d_set_rec_status()
    __tomo_xanes3d_reset_rec_buttons()


def _tomo_xanes3d_auto_cen_dft_roi():
    if tomo_xanes3d_rec.auto_cen_dft_roi.value:
        tomo_xanes3d_rec.auto_cen_roix.enabled = False
        tomo_xanes3d_rec.auto_cen_roiy.enabled = False
    else:
        tomo_xanes3d_rec.auto_cen_roix.enabled = True
        tomo_xanes3d_rec.auto_cen_roiy.enabled = True
    overlap_roi(mode="auto_cen")
    __tomo_xanes3d_set_rec_status()
    __tomo_xanes3d_reset_rec_buttons()


def _tomo_xanes3d_auto_cen_roix():
    overlap_roi(mode="auto_cen")
    show_layers_in_viewer(["tomo viewer", "auto_cen_roi"])
    __tomo_xanes3d_set_rec_status()
    __tomo_xanes3d_reset_rec_buttons()


def _tomo_xanes3d_auto_cen_roiy():
    overlap_roi(mode="auto_cen")
    show_layers_in_viewer(["tomo viewer", "auto_cen_roi"])
    __tomo_xanes3d_set_rec_status()
    __tomo_xanes3d_reset_rec_buttons()


def _tomo_xanes3d_auto_cen_ref_sli():
    __tomo_xanes3d_show_sli(mode="auto_cen")
    overlap_roi(mode="auto_cen")
    show_layers_in_viewer(["tomo viewer", "auto_cen_roi"])
    __tomo_xanes3d_set_rec_status()
    __tomo_xanes3d_reset_rec_buttons()


def _tomo_xanes3d_rec_roix():
    overlap_roi(mode="recon_roi")
    show_layers_in_viewer(["tomo viewer", "recon_roi"])


def _tomo_xanes3d_rec_roiy():
    overlap_roi(mode="recon_roi")
    show_layers_in_viewer(["tomo viewer", "recon_roi"])


def _tomo_xanes3d_rec_roiz():
    __tomo_xanes3d_show_sli(mode="recon_roi")
    overlap_roi(mode="recon_roi")
    show_layers_in_viewer(["tomo viewer", "recon_roi"])


def _tomo_xanes3d_test_run():
    # choices, values = store_combobox()
    __tomo_xanes3d_if_new_rec()
    __tomo_xnaes3d_def_autocent_cfg()

    sig = os.system(f"ipython {xanes3d_auto_cen_reg_script_fn}")
    print(f"{sig=}")

    if sig == 0:
        with open(cfg_fn, "r") as f:
            tem = json.load(f)
        with open(tem["xanes3d_auto_cen"]["cfg_file"], "r") as f:
            tem = json.load(f)
        trial_imgs = []
        with h5py.File(tem["aut_xns3d_pars"]["xanes3d_sav_trl_reg_fn"], "r") as f:
            for key in f["/auto_centering/"].keys():
                trial_imgs.append(
                    f[f"/auto_centering/{key}/optimization itr 1/trial_rec"][:]
                )
        viewer.add_image(np.array(trial_imgs), name="autocent_check")
        show_layers_in_viewer(["autocent_check"])
    if sig == 0:
        tomo_xanes3d_rec._test_run_done = True
    else:
        tomo_xanes3d_rec._test_run_done = False
        print("auto centering fails")
    tomo_xanes3d_rec.confirm_to_run.value == "No"
    tomo_xanes3d_rec._continue_run_confirmed = False
    __tomo_xanes3d_reset_rec_buttons()


def _tomo_xanes3d_confirm_to_run():
    if tomo_xanes3d_rec.confirm_to_run.value == "Yes":
        tomo_xanes3d_rec._continue_run_confirmed = True
        tomo_xanes3d_rec.call_button.enabled = True
    else:
        tomo_xanes3d_rec._continue_run_confirmed = False
        tomo_xanes3d_rec.call_button.enabled = False


def _tomo_xanes3d_rec_run():
    __tomo_xanes3d_if_new_rec()
    __tomo_xnaes3d_def_autocent_cfg()

    sig = os.system(f"ipython {xanes3d_auto_cen_reg_script_fn}")
    if sig == 0:
        print(
            "autocen and registration are finished. please check the results in 'XANES Analysis'."
        )
    else:
        print("something went wrong during autocen or registration processes.")
        tomo_xanes3d_rec.call_button.enabled = False


tomo_xanes3d_rec.tomo_tplt_fn.changed.connect(_tomo_xanes3d_set_cfg_fn)
tomo_xanes3d_rec.scan_id_s.changed.connect(_check_scan_id_s)
tomo_xanes3d_rec.scan_id_e.changed.connect(_check_scan_id_e)
tomo_xanes3d_rec.auto_cen_dft_roi.changed.connect(_tomo_xanes3d_auto_cen_dft_roi)
tomo_xanes3d_rec.auto_cen_roix.changed.connect(_tomo_xanes3d_auto_cen_roix)
tomo_xanes3d_rec.auto_cen_roiy.changed.connect(_tomo_xanes3d_auto_cen_roiy)
tomo_xanes3d_rec.ref_sli.changed.connect(_tomo_xanes3d_auto_cen_ref_sli)
tomo_xanes3d_rec.rec_roix.changed.connect(_tomo_xanes3d_rec_roix)
tomo_xanes3d_rec.rec_roiy.changed.connect(_tomo_xanes3d_rec_roiy)
tomo_xanes3d_rec.rec_roiz.changed.connect(_tomo_xanes3d_rec_roiz)
tomo_xanes3d_rec.test_run.changed.connect(_tomo_xanes3d_test_run)
tomo_xanes3d_rec.confirm_to_run.changed.connect(_tomo_xanes3d_confirm_to_run)


__comp_tomo_xanes3d_fntpl()
tomo_gui = widgets.Container()
tomo_gui.append(tomo_trl)
tomo_gui.append(tomo_vol_rec)
tomo_gui.append(tomo_xanes3d_rec)
tomo_gui._wedge_autodet_fig = None


################################################################################
#                               XANES Data Type                                #
################################################################################
@magicgui(
    main_window=False,
    call_button=False,
    layout="vertical",
    result_widget=False,
    Step_1={
        "widget_type": "Label",
        "value": "-----------------     XANES Data Type    -----------------",
    },
    data_type={
        "widget_type": "ComboBox",
        "choices": ["xanes2D", "xanes3D"],
        "value": "xanes3D",
        "enabled": True,
    },
)
def xanes_data_type(
    Step_1: str,
    data_type: str,
):
    print("place holder")


################################################################################
#                         XANES3D Reg Visualization                            #
################################################################################
@magicgui(
    main_window=False,
    call_button=False,
    layout="vertical",
    result_widget=False,
    Step_2={
        "widget_type": "Label",
        "value": "--------------     Visualize XANES3D Reg    --------------",
    },
    xanes_file={"widget_type": "FileEdit", "mode": "r", "filter": "*.h5"},
    eng_eV={
        "widget_type": "LineEdit",
        "value": "",
        "enabled": False,
        "label": "eng (eV)",
    },
    sli={
        "widget_type": "Slider",
        "enabled": False,
    },
    E={
        "widget_type": "Slider",
        "enabled": False,
    },
    spec_in_roi={
        "widget_type": "CheckBox",
        "value": False,
        "enabled": False,
    },
    roi_cen_x={"widget_type": "Slider", "enabled": False, "tracking": False},
    roi_cen_y={"widget_type": "Slider", "enabled": False, "tracking": False},
    def_fit_range={
        "widget_type": "PushButton",
        "text": "def fit energy range",
        "enabled": False,
    },
)
def xanes_reg_vis(
    Step_2: str,
    xanes_file: Path,
    eng_eV: str,
    sli: int,
    E: int,
    spec_in_roi: bool,
    roi_cen_x: int,
    roi_cen_y: int,
    def_fit_range: widgets.PushButton,
):
    pass


def __lock_xanes_gui_widgets():
    if xanes_gui._reg_done:
        xanes_reg_vis.sli.enabled = True
        xanes_reg_vis.E.enabled = True
        print(f"2: {xanes_gui._elem=}")
        if xanes_gui._elem is not None:
            xanes_reg_vis.spec_in_roi.enabled = True
            if xanes_reg_vis.spec_in_roi.value:
                xanes_reg_vis.roi_cen_x.enabled = True
                xanes_reg_vis.roi_cen_y.enabled = True
            else:
                xanes_reg_vis.roi_cen_x.enabled = False
                xanes_reg_vis.roi_cen_y.enabled = False
            xanes_reg_vis.def_fit_range.enabled = True

            if xanes_fit.analysis_type.value == "wl":
                xanes_fit.edge_eng.enabled = False
                xanes_fit.edge_s.enabled = False
                xanes_fit.edge_e.enabled = False
            else:
                xanes_fit.edge_eng.enabled = True
                xanes_fit.edge_s.enabled = True
                xanes_fit.edge_e.enabled = True
            xanes_fit.analysis_type.enabled = True
            xanes_fit.wl_s.enabled = True
            xanes_fit.wl_e.enabled = True
            xanes_fit.fit.enabled = True
            xanes_fit.enabled = True
        else:
            xanes_fit.enabled = False
            xanes_reg_vis.spec_in_roi.enabled = False
            xanes_reg_vis.roi_cen_x.enabled = False
            xanes_reg_vis.roi_cen_y.enabled = False
            xanes_reg_vis.def_fit_range.enabled = False
    else:
        xanes_reg_vis.sli.enabled = False
        xanes_reg_vis.E.enabled = False
        xanes_reg_vis.spec_in_roi.enabled = False
        xanes_reg_vis.roi_cen_x.enabled = False
        xanes_reg_vis.roi_cen_y.enabled = False
        xanes_reg_vis.def_fit_range.enabled = False
        xanes_fit.enabled = False


def __set_xanes_gui_widgets():
    if xanes_gui._reg_done:
        if xanes_gui._xanes_type == "xanes2D":
            xanes_reg_vis.sli.enabled = False
            set_data_widget(xanes_reg_vis.E, 0, 0, xanes_gui._xanes_data_dim[0] - 1)
            set_data_widget(
                xanes_reg_vis.roi_cen_x,
                10,
                int(xanes_gui._xanes_data_dim[2] / 2),
                xanes_gui._xanes_data_dim[2] - 10,
            )
            set_data_widget(
                xanes_reg_vis.roi_cen_y,
                10,
                int(xanes_gui._xanes_data_dim[1] / 2),
                xanes_gui._xanes_data_dim[1] - 10,
            )
        elif xanes_gui._xanes_type == "xanes3D":
            xanes_reg_vis.sli.enabled = False
            set_data_widget(xanes_reg_vis.E, 0, 0, xanes_gui._xanes_data_dim[0] - 1)
            set_data_widget(xanes_reg_vis.sli, 0, 0, xanes_gui._xanes_data_dim[1] - 1)
            set_data_widget(
                xanes_reg_vis.roi_cen_x,
                10,
                int(xanes_gui._xanes_data_dim[3] / 2),
                xanes_gui._xanes_data_dim[3] - 10,
            )
            set_data_widget(
                xanes_reg_vis.roi_cen_y,
                10,
                int(xanes_gui._xanes_data_dim[2] / 2),
                xanes_gui._xanes_data_dim[2] - 10,
            )

        xanes_gui._elem = determine_element(xanes_gui._eng_lst)
        print(f"1: {xanes_gui._elem=}")
        if xanes_gui._elem is not None:
            xanes_fit.element.value = xanes_gui._elem
            (
                edge_eng,
                wl_fit_eng_s,
                wl_fit_eng_e,
                _,
                _,
                edge_0p5_fit_s,
                edge_0p5_fit_e,
            ) = determine_fitting_energy_range(xanes_fit.element.value)
            xanes_fit.edge_eng.value = edge_eng
            xanes_fit.wl_s.value = wl_fit_eng_s
            xanes_fit.wl_e.value = wl_fit_eng_e
            xanes_fit.edge_s.value = edge_0p5_fit_s
            xanes_fit.edge_e.value = edge_0p5_fit_e
            xanes_fit.analysis_type.value = "full"
            xanes_fit.analysis_type.value = "wl"
            xanes_fit.enabled = True
            xanes_reg_vis.spec_in_roi.enabled = True
            xanes_reg_vis.roi_cen_x.enabled = True
            xanes_reg_vis.roi_cen_y.enabled = True
            xanes_reg_vis.def_fit_range.enabled = True
        else:
            xanes_fit.enabled = False
            xanes_reg_vis.spec_in_roi.enabled = False
            xanes_reg_vis.roi_cen_x.enabled = False
            xanes_reg_vis.roi_cen_y.enabled = False
            xanes_reg_vis.def_fit_range.enabled = False


def __vis_xanes_data():
    if xanes_gui._reg_done:
        if xanes_data_type.data_type.value == "xanes 2D":
            viewer.dims.set_point(
                axis=[
                    0,
                ],
                value=[
                    xanes_reg_vis.E.value,
                ],
            )
        else:
            viewer.dims.set_point(
                axis=[0, 1], value=[xanes_reg_vis.E.value, xanes_reg_vis.sli.value]
            )


def __plot_spec_in_roi():
    if xanes_data_type.data_type.value == "xanes 2D":
        xanes_gui._spec_in_roi = xanes_gui._xanes_data[
            :,
            xanes_reg_vis.roi_cen_y.value - 5 : xanes_reg_vis.roi_cen_y.value + 5,
            xanes_reg_vis.roi_cen_x.value - 5 : xanes_reg_vis.roi_cen_x.value + 5,
        ].mean(axis=(1, 2))
    else:
        xanes_gui._spec_in_roi = xanes_gui._xanes_data[
            :,
            xanes_reg_vis.sli.value,
            xanes_reg_vis.roi_cen_y.value - 5 : xanes_reg_vis.roi_cen_y.value + 5,
            xanes_reg_vis.roi_cen_x.value - 5 : xanes_reg_vis.roi_cen_x.value + 5,
        ].mean(axis=(1, 2))
    if xanes_gui._spec_in_roi_fig is not None:
        plt.close(xanes_gui._spec_in_roi_fig)
    xanes_gui._spec_in_roi_fig, ax = plt.subplots()
    ax.plot(xanes_gui._eng_lst, xanes_gui._spec_in_roi)
    ax.set_title("spec in roi")
    plt.show()


def _xanes_reg_vis_sel_xanes_file():
    with h5py.File(xanes_reg_vis.xanes_file.value, "r") as f:
        if (
            f"/registration_results/reg_results/registered_{xanes_data_type.data_type.value}"
            in f
        ):
            xanes_gui._reg_done = True
            xanes_gui._xanes_type = xanes_data_type.data_type.value
            xanes_gui._xanes_data_fn = xanes_reg_vis.xanes_file.value
            xanes_gui._xanes_data_dim = f[
                f"/registration_results/reg_results/registered_{xanes_data_type.data_type.value}"
            ].shape
            xanes_gui._eng_lst = scale_eng_list(
                f["/registration_results/reg_results/eng_list"][:]
            )
            if "xanes_data" in viewer.layers:
                viewer.layers.remove("xanes_data")
        else:
            xanes_gui._reg_done = False
            xanes_gui._xanes_type = None
            xanes_gui._xanes_data_fn = None
            xanes_gui._xanes_data = None
            xanes_gui._xanes_data_dim = None
            xanes_gui._eng_lst = None
    if xanes_gui._reg_done:
        xanes_gui._xanes_data = h5_lazy_reader(
            xanes_gui._xanes_data_fn,
            f"/registration_results/reg_results/registered_{xanes_data_type.data_type.value}",
            np.s_[:],
        )
        viewer.add_image(xanes_gui._xanes_data, name="xanes_data")
        viewer.reset_view()

    xanes_gui._spec_in_roi = None
    __set_xanes_gui_widgets()
    __lock_xanes_gui_widgets()
    __vis_xanes_data()
    show_layers_in_viewer(["xanes_data", "xanes_roi"])


def _xanes_reg_vis_sli_changed():
    __vis_xanes_data()


def _xanes_reg_vis_E_changed():
    xanes_reg_vis.eng_eV.value = str(xanes_gui._eng_lst[xanes_reg_vis.E.value])
    __vis_xanes_data()


def _xanes_reg_vis_spec_in_roi_changed():
    if xanes_reg_vis.spec_in_roi.value:
        xanes_reg_vis.roi_cen_x.enabled = True
        xanes_reg_vis.roi_cen_y.enabled = True
        xanes_reg_vis.def_fit_range.enabled = True
    else:
        xanes_reg_vis.roi_cen_x.enabled = False
        xanes_reg_vis.roi_cen_y.enabled = False
        xanes_reg_vis.def_fit_range.enabled = False


def _xanes_reg_vis_roi_cen_x_changed():
    overlap_roi(mode="xanes_roi")
    __plot_spec_in_roi()


def _xanes_reg_vis_roi_cen_y_changed():
    overlap_roi(mode="xanes_roi")
    __plot_spec_in_roi()


def _xanes_reg_vis_def_fit_range_changed():
    (_, wl_fit_s, wl_fit_e, edge_fit_s, edge_fit_e, edge_eng, fit_type) = (
        def_dflt_eng_rgn(xanes_gui._spec_in_roi, xanes_gui._eng_lst)
    )
    xanes_fit.analysis_type.value = fit_type
    if fit_type == "wl":
        xanes_fit.wl_s.value = wl_fit_s
        xanes_fit.wl_e.value = wl_fit_e
        print(f"set {wl_fit_s=}, {wl_fit_e=}")
    else:
        xanes_fit.edge_eng.value = edge_eng
        xanes_fit.wl_s.value = wl_fit_s
        xanes_fit.wl_e.value = wl_fit_e
        xanes_fit.edge_s.value = edge_fit_s
        xanes_fit.edge_e.value = edge_fit_e
        print(
            f"set {edge_eng=}, {wl_fit_s=}, {wl_fit_e=}, {edge_fit_s=}, {edge_fit_e=}"
        )


xanes_reg_vis.xanes_file.changed.connect(_xanes_reg_vis_sel_xanes_file)
xanes_reg_vis.sli.changed.connect(_xanes_reg_vis_sli_changed)
xanes_reg_vis.E.changed.connect(_xanes_reg_vis_E_changed)
xanes_reg_vis.spec_in_roi.changed.connect(_xanes_reg_vis_spec_in_roi_changed)
xanes_reg_vis.roi_cen_x.changed.connect(_xanes_reg_vis_roi_cen_x_changed)
xanes_reg_vis.roi_cen_y.changed.connect(_xanes_reg_vis_roi_cen_y_changed)
xanes_reg_vis.def_fit_range.changed.connect(_xanes_reg_vis_def_fit_range_changed)


################################################################################
#                              XANES3D Fitting                                 #
################################################################################
@magicgui(
    main_window=False,
    call_button=False,
    layout="vertical",
    result_widget=False,
    Step_3={
        "widget_type": "Label",
        "value": "-----------------     XANES3D Fitting    -----------------",
    },
    element={
        "widget_type": "Label",
        "value": "",
    },
    analysis_type={
        "widget_type": "ComboBox",
        "choices": ["full", "wl"],
        "value": "wl",
        "enabled": False,
    },
    edge_eng={
        "widget_type": "LineEdit",
        "enabled": False,
    },
    wl_s={
        "widget_type": "LineEdit",
        "enabled": False,
    },
    wl_e={
        "widget_type": "LineEdit",
        "enabled": False,
    },
    edge_s={
        "widget_type": "LineEdit",
        "enabled": False,
    },
    edge_e={
        "widget_type": "LineEdit",
        "enabled": False,
    },
    downsample_factor={
        "widget_type": "SpinBox",
        "min": 1,
        "max": 10,
        "value": 1,
        "enabled": False,
    },
    save_items={
        "widget_type": "Select",
        "choices": get_xanes_fit_save_items_choices,
    },
    fit={"widget_type": "PushButton", "text": "Fit", "enabled": False},
)
def xanes_fit(
    Step_3: str,
    element: str,
    analysis_type: str,
    edge_eng: str,
    wl_s: str,
    wl_e: str,
    edge_s: str,
    edge_e: str,
    downsample_factor: int,
    # fit_items: list,
    save_items: list,
    fit: widgets.PushButton,
):
    pass


def __set_analysis_type():
    if (xanes_gui._eng_lst.min() > (float(xanes_fit.edge_eng.value) - 50)) and (
        xanes_gui._eng_lst.max() < (float(xanes_fit.edge_eng.value) + 50)
    ):
        xanes_fit.analysis_type.value = "wl"
    else:
        xanes_fit.analysis_type.value = "full"


def _xanes_fit_analysis_type_changed():
    __set_analysis_type()
    xanes_fit.wl_s.enabled = True
    xanes_fit.wl_e.enabled = True
    global _XANES_FIT_SAVE_ITEMS_CHOICES
    if xanes_fit.analysis_type.value == "wl":
        xanes_fit.edge_eng.enabled = False
        xanes_fit.edge_s.enabled = False
        xanes_fit.edge_e.enabled = False
        _XANES_FIT_SAVE_ITEMS_CHOICES = [
            "wl_pos_fit",
            "weighted_attenuation",
            "wl_fit_err",
        ]
        xanes_fit.save_items.reset_choices()
        xanes_fit.save_items.value = [
            "wl_pos_fit",
            "weighted_attenuation",
        ]
    else:
        xanes_fit.edge_eng.enabled = True
        xanes_fit.edge_s.enabled = True
        xanes_fit.edge_e.enabled = True
        _XANES_FIT_SAVE_ITEMS_CHOICES = [
            "wl_pos_fit",
            "edge_pos_fit",
            "edge50_pos_fit",
            "weighted_attenuation",
            "wl_fit_err",
            "edge_fit_err",
        ]
        xanes_fit.save_items.reset_choices()
        xanes_fit.save_items.value = [
            "wl_pos_fit",
            "edge_pos_fit",
            "edge50_pos_fit",
            "weighted_attenuation",
        ]


def _xanes_fit_fit():
    with open(cfg_fn, "r") as f:
        tem = json.load(f)
        tem["xanes3d_fit"]["cfg_file"] = str(xanes_gui._xanes_data_fn)
    with open(cfg_fn, "w") as f:
        json.dump(tem, f, indent=4, separators=(",", ": "))

    with open(tem["xanes3d_fit"]["cfg_file"], "r+") as f:
        pass

    create_hdf5_from_json(xanes_proc_data_struct, xanes_gui._xanes_data_fn)
    with h5py.File(xanes_gui._xanes_data_fn, "r+") as f:
        del f["/processed_XANES/proc_parameters/analysis_type"]
        f["/processed_XANES/proc_parameters"].create_dataset(
            "analysis_type", data=xanes_fit.analysis_type.value
        )
        del f["/processed_XANES/proc_parameters/bin_fact"]
        f["/processed_XANES/proc_parameters"].create_dataset(
            "bin_fact", data=int(xanes_fit.downsample_factor.value)
        )
        del f["/processed_XANES/proc_parameters/element"]
        f["/processed_XANES/proc_parameters"].create_dataset(
            "element", data=xanes_fit.element.value
        )
        del f["/processed_XANES/proc_parameters/eng_list"]
        f["/processed_XANES/proc_parameters"].create_dataset(
            "eng_list", data=np.float32(xanes_gui._eng_lst)
        )
        del f["/processed_XANES/proc_parameters/data_shape"]
        f["/processed_XANES/proc_parameters"].create_dataset(
            "data_shape", data=xanes_gui._xanes_data_dim
        )
        del f["/processed_XANES/proc_parameters/wl_fit_eng_s"]
        f["/processed_XANES/proc_parameters"].create_dataset(
            "wl_fit_eng_s", data=float(xanes_fit.wl_s.value)
        )
        del f["/processed_XANES/proc_parameters/wl_fit_eng_e"]
        f["/processed_XANES/proc_parameters"].create_dataset(
            "wl_fit_eng_e", data=float(xanes_fit.wl_e.value)
        )

        if xanes_fit.analysis_type.value == "full":
            del f["/processed_XANES/proc_parameters/edge_eng"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "edge_eng", data=float(xanes_fit.edge_eng.value)
            )
            del f["/processed_XANES/proc_parameters/edge50_fit_s"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "edge50_fit_s", data=float(xanes_fit.edge_s.value)
            )
            del f["/processed_XANES/proc_parameters/edge50_fit_e"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "edge50_fit_e", data=float(xanes_fit.edge_e.value)
            )
            del f["/processed_XANES/proc_parameters/edge_fit method/params/spec"]
            f["/processed_XANES/proc_parameters/edge_fit method/params"].create_dataset(
                "spec", data="norm"
            )
            del f["/processed_XANES/proc_parameters/edge_fit method/params/eng_offset"]
            f["/processed_XANES/proc_parameters/edge_fit method/params"].create_dataset(
                "eng_offset", data=float(xanes_fit.edge_eng.value)
            )
            del f["/processed_XANES/proc_parameters/wl_fit method/params/spec"]
            f["/processed_XANES/proc_parameters/wl_fit method/params"].create_dataset(
                "spec", data="norm"
            )
            del f["/processed_XANES/proc_parameters/wl_fit method/params/eng_offset"]
            f["/processed_XANES/proc_parameters/wl_fit method/params"].create_dataset(
                "eng_offset",
                data=(float(xanes_fit.wl_s.value) + float(xanes_fit.wl_e.value)) / 2.0,
            )
        else:
            del f["/processed_XANES/proc_parameters/wl_fit method/params/spec"]
            f["/processed_XANES/proc_parameters/wl_fit method/params"].create_dataset(
                "spec", data="raw"
            )
            del f["/processed_XANES/proc_parameters/wl_fit method/params/eng_offset"]
            f["/processed_XANES/proc_parameters/wl_fit method/params"].create_dataset(
                "eng_offset",
                data=(float(xanes_fit.wl_s.value) + float(xanes_fit.wl_e.value)) / 2.0,
            )

        for item in xanes_fit.save_items.value:
            f["/processed_XANES/proc_spectrum"].create_dataset(item, data=False)

    sig = os.system(f"ipython {xanes3d_fit_script_fn}")


xanes_fit.analysis_type.changed.connect(_xanes_fit_analysis_type_changed)
xanes_fit.fit.changed.connect(_xanes_fit_fit)

xanes_gui = widgets.Container()
xanes_gui.append(xanes_data_type)
xanes_gui.append(xanes_reg_vis)
xanes_gui.append(xanes_fit)

xanes_gui._spec_in_roi_fig = None
xanes_gui._elem = None

# Add it to the napari viewer
viewer.window.add_dock_widget(tomo_gui, name="Tomo Recon", area="right", tabify=True)
viewer.window.add_dock_widget(
    xanes_gui, name="XANES Analysis", area="right", tabify=True
)
# viewer.window.add_dock_widget(config, name="Config", area="right", tabify=True)

# update the layer dropdown menu when the layer list changes
viewer.layers.events.changed.connect(tomo_gui.reset_choices)

tomo_trl.call_button.enabled = False
tomo_xanes3d_rec.call_button.enabled = False
__comp_tomo_trl_fn()

# tomo_gui.enabled = False
# xanes3D_gui.enabled = False

napari.run()
