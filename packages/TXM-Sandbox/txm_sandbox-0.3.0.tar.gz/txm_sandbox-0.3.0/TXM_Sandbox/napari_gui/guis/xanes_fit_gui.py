import numpy as np
import os

import dask.array as da
import h5py
import json
from pathlib import Path
import matplotlib.pyplot as plt
from magicgui import widgets

from TXM_Sandbox.gui.gui_components import (
    determine_element,
    determine_fitting_energy_range,
    scale_eng_list,
    def_dflt_eng_rgn,
)
from TXM_Sandbox.napari_gui.utils.io import create_hdf5_from_json
from TXM_Sandbox.napari_gui.utils.misc import (
    set_data_widget,
    overlap_roi,
    update_layer_in_viewer,
    show_layers_in_viewer,
    rm_gui_viewers,
    disp_progress_info,
)


cfg_fn = Path(__file__).parents[1] / "configs/txm_simple_gui_script_cfg.json"
xanes3d_fit_script_fn = Path(__file__).parents[1] / "scripts/xanes3D_fit_cmd.py"
xanes2d_fit_script_fn = Path(__file__).parents[1] / "scripts/xanes2D_fit_cmd.py"

with open(Path(__file__).parents[1] / "configs/xanes_proc_data_struct_cfg.json") as f:
    xanes_proc_data_struct = json.load(f)


_XANES_FIT_SAVE_ITEMS_CHOICES = []


def get_xanes_fit_save_items_choices(ComboBox):
    global _XANES_FIT_SAVE_ITEMS_CHOICES
    return _XANES_FIT_SAVE_ITEMS_CHOICES


################################################################################
#                             XANES Analysis GUI                               #
################################################################################
class xanes_fit_gui:
    def __init__(self, viewer):
        self.viewer = viewer
        self._reg_done = False
        self._spec_in_roi_fig = None
        self._elem = None
        self._xanes_data = None
        self._xanes_data_fn_p = None
        self._viewers = ["xanes_data", "xanes_spec_roi"]

        self._anal_type_dict = {"2D XANES": "xanes2D", "3D XANES": "xanes3D"}

        self.label0 = widgets.Label(
            value="------------------     XANES Fitting    ------------------",
        )
        self.label1 = widgets.Label(
            name="Step 1",
            value="-----------------     XANES Data Type    -----------------",
        )
        self.data_type = widgets.ComboBox(
            choices=["2D XANES", "3D XANES"],
            value="3D XANES",
            enabled=True,
            name="data type",
        )
        self.label2 = widgets.Label(
            name="Step 2",
            value="---------------     Visualize XANES Reg    ---------------",
        )
        self.xanes_file = widgets.FileEdit(mode="r", filter="*.h5", name="xanes file")
        self.reload = widgets.PushButton(
            text="reload registered xanes data", enabled=False
        )
        self.eng_eV = widgets.LineEdit(value="", enabled=False, label="eng (eV)")
        self.sli = widgets.Slider(enabled=False, name="sli")
        self.E = widgets.Slider(enabled=False, name="E")
        self.spec_in_roi = widgets.CheckBox(
            value=False, text="spec in roi", enabled=False
        )
        self.roi_cen_x = widgets.Slider(enabled=False, tracking=False, name="roi cen x")
        self.roi_cen_y = widgets.Slider(enabled=False, tracking=False, name="roi cen y")
        self.def_fit_range = widgets.PushButton(
            text="def fit energy range", enabled=False
        )
        self.label3 = widgets.Label(
            name="Step 3",
            value="------------------     XANES Fitting    ------------------",
        )
        self.element = widgets.Label(value="")
        self.analysis_type = widgets.ComboBox(
            choices=["full", "wl"], value="wl", enabled=False, name="fit type"
        )
        self.edge_eng = widgets.LineEdit(enabled=False, label="edge eng")
        self.wl_s = widgets.LineEdit(enabled=False, label="wl s eng")
        self.wl_e = widgets.LineEdit(enabled=False, label="wl e eng")
        self.edge_s = widgets.LineEdit(enabled=False, label="edge eng s")
        self.edge_e = widgets.LineEdit(enabled=False, label="edge eng e")
        self.downsample_factor = widgets.SpinBox(
            min=1, max=10, value=1, enabled=False, name="ds fac"
        )
        self.save_items = widgets.Select(
            choices=get_xanes_fit_save_items_choices, name="save items"
        )
        self.fit = widgets.PushButton(text="fit", enabled=False)
        self.close_file = widgets.PushButton(text="close file", enabled=False)
        self.op_status = widgets.LineEdit(name="operation status", enabled=False)

        self.data_type.changed.connect(self._data_type)
        self.xanes_file.changed.connect(self._sel_xanes_file)
        self.reload.changed.connect(self._reload_xanes_data)
        self.sli.changed.connect(self._vis_sli_chgd)
        self.E.changed.connect(self._vis_E_chgd)
        self.spec_in_roi.changed.connect(self._spec_in_roi_chkd)
        self.roi_cen_x.changed.connect(self._spec_roi_cen_x_chgd)
        self.roi_cen_y.changed.connect(self._spec_roi_cen_y_chgd)
        self.def_fit_range.changed.connect(self._def_fit_eng_rgn)
        self.analysis_type.changed.connect(self._xanes_fit_type_chgd)
        self.fit.changed.connect(self._xanes_fit)
        self.close_file.changed.connect(self._close_file)

        self.gui_layout = widgets.VBox(
            widgets=[
                self.label0,
                self.label1,
                self.data_type,
                self.label2,
                self.xanes_file,
                self.reload,
                self.eng_eV,
                self.sli,
                self.E,
                self.spec_in_roi,
                self.roi_cen_x,
                self.roi_cen_y,
                self.def_fit_range,
                self.label3,
                self.element,
                self.analysis_type,
                self.edge_eng,
                self.wl_s,
                self.wl_e,
                self.edge_s,
                self.edge_e,
                self.downsample_factor,
                self.save_items,
                self.fit,
                self.close_file,
                self.op_status,
            ]
        )

    def _data_type(self):
        self.xanes_file.value = ""
        self.eng_eV.value = ""
        self.sli.value = 0
        self.E.value = 0
        self.spec_in_roi.value = False
        self.roi_cen_x.value = 0
        self.roi_cen_y.value = 0
        self.element.value = ""
        self.analysis_type = "wl"
        self.edge_eng = ""
        self.wl_s.value = ""
        self.wl_e.value = ""
        self.edge_s.value = ""
        self.edge_e.value = ""
        self.downsample_factor.value = 1
        global _XANES_FIT_SAVE_ITEMS_CHOICES
        _XANES_FIT_SAVE_ITEMS_CHOICES = []
        self.save_items.reset_choices()
        self.op_status.value = ""
        self._reg_done = False
        self.__lock_xanes_gui_widgets()

    def __lock_xanes_gui_widgets(self):
        if self._reg_done:
            self.E.enabled = True
            if self._elem is not None:
                self.spec_in_roi.enabled = True
                if self.spec_in_roi.value:
                    self.roi_cen_x.enabled = True
                    self.roi_cen_y.enabled = True
                else:
                    self.roi_cen_x.enabled = False
                    self.roi_cen_y.enabled = False
                self.def_fit_range.enabled = True

                if self.analysis_type.value == "wl":
                    self.edge_eng.enabled = False
                    self.edge_s.enabled = False
                    self.edge_e.enabled = False
                else:
                    self.edge_eng.enabled = True
                    self.edge_s.enabled = True
                    self.edge_e.enabled = True
                self.analysis_type.enabled = True
                self.wl_s.enabled = True
                self.wl_e.enabled = True
                self.fit.enabled = True
                self.enabled = True
            else:
                self.enabled = False
                self.spec_in_roi.enabled = False
                self.roi_cen_x.enabled = False
                self.roi_cen_y.enabled = False
                self.def_fit_range.enabled = False
                self.data_type.enabled = True
            self.xanes_file.enabled = True
            if self._xanes_type == "2D XANES":
                self.sli.enabled = False
            else:
                self.sli.enabled = True
            self.close_file.enabled = True
        else:
            self.enabled = False
            self.reload.enabled = False
            self.sli.enabled = False
            self.E.enabled = False
            self.spec_in_roi.enabled = False
            self.roi_cen_x.enabled = False
            self.roi_cen_y.enabled = False
            self.def_fit_range.enabled = False
            self.close_file.enabled = False
        self.data_type.enabled = True
        self.xanes_file.enabled = True

    def __set_xanes_gui_widgets(self):
        if self._reg_done:
            if self._xanes_type == "2D XANES":
                self.sli.enabled = False
                set_data_widget(self.E, 0, 0, self._xanes_data_dim[0] - 1)
                set_data_widget(self.sli, 0, 0, 0)
                set_data_widget(
                    self.roi_cen_x,
                    10,
                    int(self._xanes_data_dim[2] / 2),
                    self._xanes_data_dim[2] - 10,
                )
                set_data_widget(
                    self.roi_cen_y,
                    10,
                    int(self._xanes_data_dim[1] / 2),
                    self._xanes_data_dim[1] - 10,
                )
            elif self._xanes_type == "3D XANES":
                self.sli.enabled = False
                set_data_widget(self.E, 0, 0, self._xanes_data_dim[0] - 1)
                set_data_widget(self.sli, 0, 0, self._xanes_data_dim[1] - 1)
                set_data_widget(
                    self.roi_cen_x,
                    10,
                    int(self._xanes_data_dim[3] / 2),
                    self._xanes_data_dim[3] - 10,
                )
                set_data_widget(
                    self.roi_cen_y,
                    10,
                    int(self._xanes_data_dim[2] / 2),
                    self._xanes_data_dim[2] - 10,
                )

            self._elem = determine_element(self._eng_lst)

            if self._elem is not None:
                self.element.value = self._elem
                (
                    edge_eng,
                    wl_fit_eng_s,
                    wl_fit_eng_e,
                    _,
                    _,
                    edge_0p5_fit_s,
                    edge_0p5_fit_e,
                ) = determine_fitting_energy_range(self.element.value)
                self.edge_eng.value = edge_eng
                self.wl_s.value = wl_fit_eng_s
                self.wl_e.value = wl_fit_eng_e
                self.edge_s.value = edge_0p5_fit_s
                self.edge_e.value = edge_0p5_fit_e
                self.analysis_type.value = "full"
                self.analysis_type.value = "wl"
                self.enabled = True
                self.spec_in_roi.enabled = True
                self.roi_cen_x.enabled = True
                self.roi_cen_y.enabled = True
                self.def_fit_range.enabled = True
            else:
                self.enabled = False
                self.spec_in_roi.enabled = False
                self.roi_cen_x.enabled = False
                self.roi_cen_y.enabled = False
                self.def_fit_range.enabled = False

    def __vis_xanes_data(self):
        if self._reg_done:
            if self.data_type.value == "2D XANES":
                self.viewer.dims.set_point(
                    axis=[
                        0,
                    ],
                    value=[
                        self.E.value,
                    ],
                )
            else:
                self.viewer.dims.set_point(
                    axis=[0, 1], value=[self.E.value, self.sli.value]
                )

    def __plot_spec_in_roi(self):
        if self.data_type.value == "2D XANES":
            self._spec_in_roi = self._xanes_data[
                :,
                self.roi_cen_y.value - 5 : self.roi_cen_y.value + 5,
                self.roi_cen_x.value - 5 : self.roi_cen_x.value + 5,
            ].mean(axis=(1, 2))
        else:
            self._spec_in_roi = self._xanes_data[
                :,
                self.sli.value,
                self.roi_cen_y.value - 5 : self.roi_cen_y.value + 5,
                self.roi_cen_x.value - 5 : self.roi_cen_x.value + 5,
            ].mean(axis=(1, 2))
        if self._spec_in_roi_fig is not None:
            plt.close(self._spec_in_roi_fig)
        self._spec_in_roi_fig, ax = plt.subplots()
        ax.plot(self._eng_lst, self._spec_in_roi)
        ax.set_title("spec in roi")
        plt.show()

    @disp_progress_info("xanes data loading")
    def _sel_xanes_file(self):
        with h5py.File(self.xanes_file.value, "r") as f:
            if (
                f"/registration_results/reg_results/registered_{self._anal_type_dict[self.data_type.value]}"
                in f
            ):
                self._reg_done = True
                self._xanes_type = self.data_type.value
                self._xanes_data_fn = self.xanes_file.value
                self._xanes_data_dim = f[
                    f"/registration_results/reg_results/registered_{self._anal_type_dict[self.data_type.value]}"
                ].shape
                self._eng_lst = scale_eng_list(
                    f["/registration_results/reg_results/eng_list"][:]
                )
            else:
                self._reg_done = False
                self._xanes_type = None
                self._xanes_data_fn = None
                self._xanes_data = None
                self._xanes_data_dim = None
                self._eng_lst = None
        if self._reg_done:
            rm_gui_viewers(self.viewer, ["xanes_data"])
            try:
                self._xanes_data_fn_p = h5py.File(self._xanes_data_fn, "r")
                self._xanes_data = da.from_array(
                    self._xanes_data_fn_p[
                        f"/registration_results/reg_results/registered_{self._anal_type_dict[self.data_type.value]}"
                    ]
                )
                update_layer_in_viewer(self.viewer, self._xanes_data, "xanes_data")
                show_layers_in_viewer(self.viewer, ["xanes_data"])
            except Exception as e:
                self.viewer.status = (
                    "Something is wrong. Please check terminal for more information."
                )
                print(str(e))
                self._xanes_data_fn_p = None
                self._xanes_data = None

        self._spec_in_roi = None
        self.__set_xanes_gui_widgets()
        self.__lock_xanes_gui_widgets()
        self.__vis_xanes_data()

    @disp_progress_info("xanes data reloading")
    def _reload_xanes_data(self):
        if self._xanes_data_fn_p is None:
            self._sel_xanes_file()

    def _vis_sli_chgd(self):
        self.__vis_xanes_data()

    def _vis_E_chgd(self):
        self.eng_eV.value = str(self._eng_lst[self.E.value])
        self.__vis_xanes_data()

    def _spec_in_roi_chkd(self):
        if self.spec_in_roi.value:
            self.roi_cen_x.enabled = True
            self.roi_cen_y.enabled = True
            self.def_fit_range.enabled = True
        else:
            self.roi_cen_x.enabled = False
            self.roi_cen_y.enabled = False
            self.def_fit_range.enabled = False

    def _spec_roi_cen_x_chgd(self):
        overlap_roi(self.viewer, self, mode="xanes_spec_roi")
        self.__plot_spec_in_roi()

    def _spec_roi_cen_y_chgd(self):
        overlap_roi(self.viewer, self, mode="xanes_spec_roi")
        self.__plot_spec_in_roi()

    def _def_fit_eng_rgn(self):
        (_, wl_fit_s, wl_fit_e, edge_fit_s, edge_fit_e, edge_eng, fit_type) = (
            def_dflt_eng_rgn(self._spec_in_roi, self._eng_lst)
        )
        self.analysis_type.value = fit_type
        if fit_type == "wl":
            self.wl_s.value = wl_fit_s
            self.wl_e.value = wl_fit_e
        else:
            self.edge_eng.value = edge_eng
            self.wl_s.value = wl_fit_s
            self.wl_e.value = wl_fit_e
            self.edge_s.value = edge_fit_s
            self.edge_e.value = edge_fit_e

    def __set_analysis_type(self):
        if (self._eng_lst.min() > (float(self.edge_eng.value) - 50)) and (
            self._eng_lst.max() < (float(self.edge_eng.value) + 50)
        ):
            self.analysis_type.value = "wl"

    def _xanes_fit_type_chgd(self):
        self.__set_analysis_type()
        self.wl_s.enabled = True
        self.wl_e.enabled = True
        global _XANES_FIT_SAVE_ITEMS_CHOICES
        if self.analysis_type.value == "wl":
            self.edge_eng.enabled = False
            self.edge_s.enabled = False
            self.edge_e.enabled = False
            _XANES_FIT_SAVE_ITEMS_CHOICES = [
                "wl_pos_fit",
                "weighted_attenuation",
                "wl_fit_err",
            ]
            self.save_items.reset_choices()
            self.save_items.value = [
                "wl_pos_fit",
                "weighted_attenuation",
            ]
        else:
            self.edge_eng.enabled = True
            self.edge_s.enabled = True
            self.edge_e.enabled = True
            _XANES_FIT_SAVE_ITEMS_CHOICES = [
                "wl_pos_fit",
                "edge_pos_fit",
                "edge50_pos_fit",
                "weighted_attenuation",
                "wl_fit_err",
                "edge_fit_err",
            ]
            self.save_items.reset_choices()
            self.save_items.value = [
                "wl_pos_fit",
                "edge_pos_fit",
                "edge50_pos_fit",
                "weighted_attenuation",
            ]

    @disp_progress_info("xanes data fitting")
    def _xanes_fit(self):
        self._close_file()

        with open(cfg_fn, "r") as f:
            tem = json.load(f)
            if self.data_type.value == "3D XANES":
                tem["xanes3d_fit"]["cfg_file"] = str(self._xanes_data_fn)
            elif self.data_type.value == "2D XANES":
                tem["xanes2d_fit"]["cfg_file"] = str(self._xanes_data_fn)
        with open(cfg_fn, "w") as f:
            json.dump(tem, f, indent=4, separators=(",", ": "))

        create_hdf5_from_json(xanes_proc_data_struct, self._xanes_data_fn)
        with h5py.File(self._xanes_data_fn, "r+") as f:
            del f["/processed_XANES/proc_parameters/analysis_type"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "analysis_type", data=self.analysis_type.value
            )
            del f["/processed_XANES/proc_parameters/bin_fact"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "bin_fact", data=int(self.downsample_factor.value)
            )
            del f["/processed_XANES/proc_parameters/element"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "element", data=self.element.value
            )
            del f["/processed_XANES/proc_parameters/eng_list"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "eng_list", data=np.float32(self._eng_lst)
            )
            del f["/processed_XANES/proc_parameters/data_shape"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "data_shape", data=self._xanes_data_dim
            )
            del f["/processed_XANES/proc_parameters/wl_fit_eng_s"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "wl_fit_eng_s", data=float(self.wl_s.value)
            )
            del f["/processed_XANES/proc_parameters/wl_fit_eng_e"]
            f["/processed_XANES/proc_parameters"].create_dataset(
                "wl_fit_eng_e", data=float(self.wl_e.value)
            )

            if self.analysis_type.value == "full":
                del f["/processed_XANES/proc_parameters/edge_eng"]
                f["/processed_XANES/proc_parameters"].create_dataset(
                    "edge_eng", data=float(self.edge_eng.value)
                )
                del f["/processed_XANES/proc_parameters/edge50_fit_s"]
                f["/processed_XANES/proc_parameters"].create_dataset(
                    "edge50_fit_s", data=float(self.edge_s.value)
                )
                del f["/processed_XANES/proc_parameters/edge50_fit_e"]
                f["/processed_XANES/proc_parameters"].create_dataset(
                    "edge50_fit_e", data=float(self.edge_e.value)
                )
                del f["/processed_XANES/proc_parameters/edge_fit method/params/spec"]
                f[
                    "/processed_XANES/proc_parameters/edge_fit method/params"
                ].create_dataset("spec", data="norm")
                del f[
                    "/processed_XANES/proc_parameters/edge_fit method/params/eng_offset"
                ]
                f[
                    "/processed_XANES/proc_parameters/edge_fit method/params"
                ].create_dataset("eng_offset", data=float(self.edge_eng.value))
                del f["/processed_XANES/proc_parameters/wl_fit method/params/spec"]
                f[
                    "/processed_XANES/proc_parameters/wl_fit method/params"
                ].create_dataset("spec", data="norm")
                del f[
                    "/processed_XANES/proc_parameters/wl_fit method/params/eng_offset"
                ]
                f[
                    "/processed_XANES/proc_parameters/wl_fit method/params"
                ].create_dataset(
                    "eng_offset",
                    data=(float(self.wl_s.value) + float(self.wl_e.value)) / 2.0,
                )
            else:
                del f["/processed_XANES/proc_parameters/wl_fit method/params/spec"]
                f[
                    "/processed_XANES/proc_parameters/wl_fit method/params"
                ].create_dataset("spec", data="raw")
                del f[
                    "/processed_XANES/proc_parameters/wl_fit method/params/eng_offset"
                ]
                f[
                    "/processed_XANES/proc_parameters/wl_fit method/params"
                ].create_dataset(
                    "eng_offset",
                    data=(float(self.wl_s.value) + float(self.wl_e.value)) / 2.0,
                )

            for item in self.save_items.value:
                f["/processed_XANES/proc_spectrum"].create_dataset(item, data=False)

        if self.data_type.value == "3D XANES":
            sig = os.system(f"ipython {xanes3d_fit_script_fn}")
        elif self.data_type.value == "2D XANES":
            sig = os.system(f"ipython {xanes2d_fit_script_fn}")

    def _close_file(self):
        if self._spec_in_roi_fig is not None:
            plt.close(self._spec_in_roi_fig)
        rm_gui_viewers(self.viewer, self._viewers)
        if self._xanes_data_fn_p is not None:
            self._xanes_data_fn_p.close()
            self._xanes_data_fn_p = None
            self._xanes_data = None
