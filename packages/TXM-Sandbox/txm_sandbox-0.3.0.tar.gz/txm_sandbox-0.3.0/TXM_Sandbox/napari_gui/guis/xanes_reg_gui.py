import numpy as np
import os
import glob

import tifffile
import h5py
import json
import dask.array as da
import datetime
from pathlib import Path
from magicgui import widgets

from TXM_Sandbox.gui.gui_components import (
    check_file_availability,
)

from TXM_Sandbox.napari_gui.utils.misc import (
    set_data_widget,
    overlap_roi,
    update_layer_in_viewer,
    show_layers_in_viewer,
    rm_gui_viewers,
    disp_progress_info,
)
from TXM_Sandbox.napari_gui.dicts.data_struct_dict import ZFLY_CFG, FLY_CFG


cfg_fn = Path(__file__).parents[1] / "configs/txm_simple_gui_script_cfg.json"
xanes3d_auto_cen_reg_script_fn = (
    Path(__file__).parents[1] / "scripts/xanes3d_tomo_autocent_cmd.py"
)
xanes2d_img_auto_cen_script_fn = (
    Path(__file__).parents[1] / "scripts/xanes2d_image_autoreg_cmd.py"
)

with open(
    Path(__file__).parents[1] / "configs/xanes3d_tomo_autocent_cfg.json", "r"
) as f:
    xanes3d_tomo_autocent_cfg = json.load(f)

with open(
    Path(__file__).parents[1] / "configs/xanes2d_image_autoreg_cfg.json", "r"
) as f:
    xanes2d_image_autocent_cfg = json.load(f)

_TOMO_XANES3D_REC_ID_S_CHOICES = []
_TOMO_XANES3D_REC_ID_E_CHOICES = []


def get_tomo_xanes3d_rec_id_s_choices(ComboBox):
    global _TOMO_XANES3D_REC_ID_S_CHOICES
    return _TOMO_XANES3D_REC_ID_S_CHOICES


def get_tomo_xanes3d_rec_id_e_choices(ComboBox):
    global _TOMO_XANES3D_REC_ID_E_CHOICES
    return _TOMO_XANES3D_REC_ID_E_CHOICES


def check_cfg_type(json_cfg):
    with open(json_cfg, 'r') as f:
        tem = json.load(f)

    if "run_type" in tem.keys():
        return "xanes3d_autocen&reg"
    elif len(tem.keys()) == 1:
        key = tem[list(tem.keys())[0]]
        if np.all(item in tem[key].keys for item in ["file_params", "recon_config", "flt_params", "data_params", "alg_params"]):
            return "xanes3d_tomo_tplt"
    else:
        return None

################################################################################
#             auto reconstruction and alignment for XANES3D                    #
################################################################################
class xanes_reg_gui:
    def __init__(self, viewer):
        self.viewer = viewer
        self._tomo_cfg = None
        self.scn_fntpl = None
        self._ref_rec_tplt = {"file_params": {"raw_data_top_dir": Path("")}}
        self._tomo_recon_tplt = None
        self._test_run_done = False
        self._continue_run_confirmed = False
        self._tomo_tplt_fn_old_val = ""
        self._3dxanes_new_rec_info = ""
        self._3dxanes_rec_roix_old_val = [0, 1]
        self._3dxanes_rec_roiy_old_val = [0, 1]
        self._3dxanes_rec_roiz_old_val = [0, 1]
        self._scn_id_s_old_val = ""
        self._scn_id_e_old_val = ""
        self._2dxanes_if_new_reg = True
        self._2dxanes_data = None
        self._2dxanes_eng_lst = None
        self._2dxanes_fn_p = None
        self._2dxanes_data_ready = False
        self._2dxanes_new_reg_info = ""
        self._2dxanes_reg_fn_p = None
        self._2dxanes_reg_roix_old_val = [0, 1]
        self._2dxanes_reg_roiy_old_val = [0, 1]
        self._2dxanes_reg_roiz_old_val = [0, 1]
        self._2dxanes_reg_ref_im_old_val = 0
        self._2dxanes_if_new_align = False
        self._2dxanes_align_roix_old_val = [0, 1]
        self._2dxanes_align_roiy_old_val = [0, 1]
        self._2dxanes_align_roiz_old_val = [0, 1]
        self._viewers = [
            "autocent_check",
            "autoreg_check",
            "xanes_raw_viewer",
            "auto_cen_roi",
            "recon_roi",
        ]

        self.label1 = widgets.Label(
            value="-------------------- Auto Cen & Align --------------------",
        )
        self.data_type = widgets.ComboBox(
            name="data type",
            choices=["2D XANES", "3D XANES"],
            value="3D XANES",
            enabled=True,
        )
        self.tomo_tplt_fn = widgets.FileEdit(
            mode="r",
            filter="*.json",
            name="xanes file",
        )
        self.ref_scan_id = widgets.LineEdit(name="ref scan id", enabled=False)
        self.scan_id_s = widgets.ComboBox(
            choices=get_tomo_xanes3d_rec_id_s_choices, name="scan id s", enabled=False
        )
        self.scan_id_e = widgets.ComboBox(
            choices=get_tomo_xanes3d_rec_id_e_choices, name="scan id e", enabled=False
        )
        self.auto_cen_dft_roi = widgets.CheckBox(
            value=False, text="default roi x/y", enabled=False
        )
        self.auto_cen_roix = widgets.RangeSlider(
            min=1, max=2560, name="reg roi x", value=[540, 740], enabled=False
        )
        self.auto_cen_roiy = widgets.RangeSlider(
            min=1, max=2560, name="reg roi y", value=[540, 740], enabled=False
        )
        self.ref_sli = widgets.Slider(
            min=1, max=2160, name="reg ref sli", value=540, enabled=False
        )
        self.rec_roix = widgets.RangeSlider(
            min=1, max=2560, name="rec roi x", value=[540, 740], enabled=False
        )
        self.rec_roiy = widgets.RangeSlider(
            min=1, max=2560, name="rec roi y", value=[540, 740], enabled=False
        )
        self.rec_roiz = widgets.RangeSlider(
            min=1, max=2160, name="rec roi z", value=[440, 640], enabled=False
        )
        self.sli_srch_range = widgets.SpinBox(
            min=0, max=30, name="sli srch rgn", value=10, enabled=False
        )
        self.cen_srch_range = widgets.SpinBox(
            min=0, max=30, name="cen srch rgn", value=15, enabled=False
        )
        self.ang_corr = widgets.CheckBox(value=False, text="Ang Corr", enabled=False)
        self.ang_corr_range = widgets.FloatSpinBox(
            min=0, max=5, step=0.5, name="ang rgn", value=2, enabled=False
        )
        self.test_run = widgets.PushButton(
            text="test run",
            tooltip="run autocen for the first, middle, and the last scans to verify the autocen roi is correctly set",
            enabled=False,
        )
        self.confirm_test_run = widgets.RadioButtons(
            name="confirm test run",
            choices=["Yes", "No"],
            orientation="horizontal",
            value="No",
            tooltip="confirm if the autocen results are good",
            enabled=False,
        )
        self.reg_run = widgets.PushButton(text="run")
        self.close_file = widgets.PushButton(text="close file", enabled=False)
        self.op_status = widgets.LineEdit(name="operation status", enabled=False)

        self.data_type.changed.connect(self._xanes_data_type)
        self.tomo_tplt_fn.changed.connect(self._xanes_set_fn)
        self.scan_id_s.changed.connect(self._3dxanes_check_scan_id_s)
        self.scan_id_e.changed.connect(self._3dxanes_check_scan_id_e)
        self.auto_cen_dft_roi.changed.connect(self._3dxanes_tomo_auto_cen_dft_roi)
        self.auto_cen_roix.changed.connect(self._xanes_tomo_auto_cen_roix)
        self.auto_cen_roiy.changed.connect(self._xanes_tomo_auto_cen_roiy)
        self.ref_sli.changed.connect(self._xanes_tomo_auto_cen_ref_sli)
        self.rec_roix.changed.connect(self._xanes_tomo_rec_roix)
        self.rec_roiy.changed.connect(self._xanes_tomo_rec_roiy)
        self.rec_roiz.changed.connect(self._xanes_tomo_rec_roiz)
        self.test_run.changed.connect(self._xanes_test_run)
        self.confirm_test_run.changed.connect(self._xanes_confirm_to_run)
        self.reg_run.changed.connect(self._xanes_reg_run)
        self.close_file.changed.connect(self._close_file)

        self.gui_layout = widgets.VBox(
            widgets=[
                self.label1,
                self.data_type,
                self.tomo_tplt_fn,
                self.ref_scan_id,
                self.scan_id_s,
                self.scan_id_e,
                self.auto_cen_dft_roi,
                self.auto_cen_roix,
                self.auto_cen_roiy,
                self.ref_sli,
                self.rec_roix,
                self.rec_roiy,
                self.rec_roiz,
                self.sli_srch_range,
                self.cen_srch_range,
                self.ang_corr,
                self.ang_corr_range,
                self.test_run,
                self.confirm_test_run,
                self.reg_run,
                self.close_file,
                self.op_status,
            ]
        )

    def __3dxanes_tomo_check_avail_id_s(self):
        global _TOMO_XANES3D_REC_ID_S_CHOICES
        ids = check_file_availability(
            self._ref_rec_tplt["file_params"]["raw_data_top_dir"],
            scan_id=None,
            signature=self._tomo_cfg["tomo_raw_fn_template"],
            return_idx=True,
        )
        if ids:
            _TOMO_XANES3D_REC_ID_S_CHOICES = ids
        else:
            _TOMO_XANES3D_REC_ID_S_CHOICES = []
        self.scan_id_s.reset_choices()

    def __3dxanes_tomo_check_avail_id_e(self):
        global _TOMO_XANES3D_REC_ID_E_CHOICES
        ids = check_file_availability(
            self._ref_rec_tplt["file_params"]["raw_data_top_dir"],
            scan_id=None,
            signature=self._tomo_cfg["tomo_raw_fn_template"],
            return_idx=True,
        )
        if ids:
            _TOMO_XANES3D_REC_ID_E_CHOICES = ids
        else:
            _TOMO_XANES3D_REC_ID_E_CHOICES = []
        self.scan_id_e.reset_choices()

    def __3dxanes_tomo_if_new_rec(self):
        if (
            (self._tomo_tplt_fn_old_val != self.tomo_tplt_fn.value)
            or (self._scn_id_s_old_val != self.scan_id_s.value)
            or (self._scn_id_e_old_val != self.scan_id_e.value)
        ):
            self._3dxanes_new_rec_info = f"{xanes3d_tomo_autocent_cfg['aut_xns3d_pars']['scn_id_s']}-{xanes3d_tomo_autocent_cfg['aut_xns3d_pars']['scn_id_e']}_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
            self._tomo_tplt_fn_old_val = self.tomo_tplt_fn.value
            self._scn_id_s_old_val = self.scan_id_s.value
            self._scn_id_e_old_val = self.scan_id_e.value
            self._3dxanes_rec_roix_old_val = self.rec_roix.value
            self._3dxanes_rec_roiy_old_val = self.rec_roiy.value
            self._3dxanes_rec_roiz_old_val = self.rec_roiz.value

    def __3dxanes_comp_tomo_fntpl(self):
        self.scn_fntpl = (
            Path(self._ref_rec_tplt["file_params"]["raw_data_top_dir"])
            / self._tomo_cfg["tomo_raw_fn_template"]
        )
        self.rec_fntpl = (
            Path(self._ref_rec_tplt["file_params"]["raw_data_top_dir"])
            / self._tomo_cfg["xanes3D_recon_dir_template"]
            / self._tomo_cfg["xanes3D_recon_fn_template"]
        )

    def __3dxanes_set_scan_id_lims(self):
        try:
            if int(self.ref_scan_id.value) - 1 >= int(self.scan_id_s.choices[0]):
                self.scan_id_s.value = self.scan_id_s.choices[
                    self.scan_id_s.choices.index(self.ref_scan_id.value) - 1
                ]
            else:
                self.scan_id_s.value = self.scan_id_s.choices[0]

            if int(self.ref_scan_id.value) + 1 <= int(self.scan_id_s.choices[-1]):
                self.scan_id_e.value = self.scan_id_s.choices[
                    self.scan_id_s.choices.index(self.ref_scan_id.value) + 1
                ]
            else:
                self.scan_id_e.value = self.scan_id_s.choices[-1]
        except:
            self.op_status.value = "There is no valid scan series available for XANES3D autocent operation!"
            print(
                "There is no valid scan series available for XANES3D autocent operation!"
            )

    def __3dxanes_set_widget(self):
        if (self.rec_fntpl is None) or (
            not Path(
                str(self.rec_fntpl).format(
                    self.ref_scan_id.value,
                    str(self.ref_sli.value).zfill(5),
                )
            ).exists()
        ):
            self.scan_id_s.enabled = False
            self.scan_id_e.enabled = False
            self.auto_cen_dft_roi.enabled = False
            self.auto_cen_roix.enabled = False
            self.auto_cen_roiy.enabled = False
            self.ref_sli.enabled = False
            self.rec_roix.enabled = False
            self.rec_roiy.enabled = False
            self.rec_roiz.enabled = False
            self.sli_srch_range.enabled = False
            self.cen_srch_range.enabled = False
            self.ang_corr.enabled = False
            self.ang_corr_range.enabled = False
            self.test_run.enabled = False
            self.confirm_test_run.enabled = False
            self.reg_run.enabled = False
            self.close_file.enabled = False
        else:
            self.scan_id_s.enabled = True
            self.scan_id_e.enabled = True
            self.auto_cen_dft_roi.enabled = True
            if self.auto_cen_dft_roi.value:
                self.auto_cen_roix.enabled = False
                self.auto_cen_roiy.enabled = False
            else:
                self.auto_cen_roix.enabled = True
                self.auto_cen_roiy.enabled = True
            self.ref_sli.enabled = True
            self.rec_roix.enabled = True
            self.rec_roiy.enabled = True
            self.rec_roiz.enabled = True
            self.sli_srch_range.enabled = True
            self.cen_srch_range.enabled = True
            self.ang_corr.enabled = True
            if self.ang_corr.value:
                self.ang_corr_range.enabled = True
            else:
                self.ang_corr_range.enabled = False
            self.test_run.enabled = True
            self.close_file.enabled = True

    def __3dxanes_tomo_show_sli(self, mode="auto_cen"):
        if mode == "auto_cen":
            try:
                update_layer_in_viewer(self.viewer, tifffile.imread(
                    str(self.rec_fntpl).format(
                        self.ref_scan_id.value,
                        str(self.ref_sli.value).zfill(5),
                    )
                ), "xanes_raw_viewer")
            except Exception as e:
                self.op_status.value = (
                    "Something is wrong. Please check terminal for more information."
                )
                print(f"{str(e)=}")
        elif mode == "recon_roi":
            if self._3dxanes_rec_roiz_old_val[0] != self.rec_roiz.value[0]:
                try:
                    update_layer_in_viewer(self.viewer, tifffile.imread(
                        str(self.rec_fntpl).format(
                            self.ref_scan_id.value,
                            str(self.rec_roiz.value[0]).zfill(5),
                        )
                    ), "xanes_raw_viewer")
                except Exception as e:
                    self.op_status.value = "Something is wrong. Please check terminal for more information."
                    print(str(e))
            elif self._3dxanes_rec_roiz_old_val[1] != self.rec_roiz.value[1]:
                try:
                    update_layer_in_viewer(self.viewer, tifffile.imread(
                        str(self.rec_fntpl).format(
                            self.ref_scan_id.value,
                            str(self.rec_roiz.value[1]).zfill(5),
                        )
                    ), "xanes_raw_viewer")                   
                except Exception as e:
                    self.op_status.value = "Something is wrong. Please check terminal for more information."
                    print(str(e))
        rng = (
            self.viewer.layers["xanes_raw_viewer"].data.max()
            - self.viewer.layers["xanes_raw_viewer"].data.min()
        )
        self.viewer.layers["xanes_raw_viewer"].contrast_limits = [
            self.viewer.layers["xanes_raw_viewer"].data.min() + 0.1 * rng,
            self.viewer.layers["xanes_raw_viewer"].data.max() - 0.1 * rng,
        ]
        self._3dxanes_rec_roiz_old_val = self.rec_roiz.value
        self.viewer.reset_view()

    def __3dxnaes_tomo_def_autocent_cfg(self):
        with open(cfg_fn, "r") as f:
            tem = json.load(f)
            tem["xanes3d_auto_cen"]["cfg_file"] = str(
                Path(self._ref_rec_tplt["file_params"]["raw_data_top_dir"])
                / f"xanes3d_autocen&reg-{self._3dxanes_new_rec_info}.json"
            )
        with open(cfg_fn, "w") as f:
            json.dump(tem, f, indent=4, separators=(",", ": "))

        xanes3d_tomo_autocent_cfg["template_file"] = str(self.tomo_tplt_fn.value)
        if self._continue_run_confirmed:
            xanes3d_tomo_autocent_cfg["run_type"] = "autocen&rec&reg"
        else:
            xanes3d_tomo_autocent_cfg["run_type"] = "autocen"
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["rec_dir_tplt"] = str(
            Path(self._ref_rec_tplt["file_params"]["raw_data_top_dir"])
            / self._tomo_cfg["xanes3D_recon_dir_template"]
        )
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["rec_fn_tplt"] = str(self.rec_fntpl)
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["ref_scn_cen"] = self._ref_rec_tplt[
            "data_params"
        ]["rot_cen"]
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
            "use_dflt_ref_reg_roi"
        ] = self.auto_cen_dft_roi.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["ref_cen_roi"] = [
            self.auto_cen_roiy.value[0],
            self.auto_cen_roiy.value[1],
            self.auto_cen_roix.value[0],
            self.auto_cen_roix.value[1],
        ]
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["ref_cen_sli"] = self.ref_sli.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["rec_roi"] = [
            self.rec_roiy.value[0],
            self.rec_roiy.value[1],
            self.rec_roix.value[0],
            self.rec_roix.value[1],
            self.rec_roiz.value[0],
            (self.rec_roiz.value[1]),
        ]
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
            "ref_sli_srch_half_wz"
        ] = self.sli_srch_range.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
            "ref_cen_srch_half_wz"
        ] = self.cen_srch_range.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
            "ref_scn_id"
        ] = self.ref_scan_id.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_s"] = self.scan_id_s.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_e"] = self.scan_id_e.value

        ids = self.scan_id_e.choices.index(self.scan_id_s.value)
        ide = self.scan_id_e.choices.index(self.scan_id_e.value)
        if self._continue_run_confirmed:
            xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_lst"] = (
                self.scan_id_e.choices[ids : ide + 1]
            )
        else:
            if len(self.scan_id_e.choices[ids : ide + 1]) >= 3:
                xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_lst"] = list(
                    set(
                        [
                            self.scan_id_e.choices[ids],
                            self.ref_scan_id.value,
                            self.scan_id_e.choices[ide],
                        ]
                    )
                )
            else:
                xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["scn_id_lst"] = [
                    self.scan_id_e.choices[ids],
                    self.scan_id_e.choices[ide],
                ]

        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["ang_corr"] = self.ang_corr.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"][
            "ang_corr_rgn"
        ] = self.ang_corr_range.value
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["xanes3d_sav_trl_reg_fn"] = str(
            Path(self._ref_rec_tplt["file_params"]["raw_data_top_dir"])
            / f"3D_trial_reg_scan_id_{self._3dxanes_new_rec_info}.h5"
        )
        xanes3d_tomo_autocent_cfg["aut_xns3d_pars"]["XANES_tmp_fn"] = ""

        with open(tem["xanes3d_auto_cen"]["cfg_file"], "w") as f:
            json.dump(xanes3d_tomo_autocent_cfg, f, indent=4, separators=(",", ": "))

    def __3dxanes_set_roi_lims(self):
        b = glob.glob(
            str(
                (
                    Path(self._ref_rec_tplt["file_params"]["raw_data_top_dir"])
                    / self._tomo_cfg["xanes3D_recon_dir_template"].format(
                        self.ref_scan_id.value
                    )
                ).joinpath("*.tiff")
            )
        )
        ref_rec_ids = sorted([int(str(Path(fn).stem).split("_")[-1]) for fn in b])

        if ref_rec_ids:
            set_data_widget(
                self.ref_sli,
                ref_rec_ids[0],
                ref_rec_ids[int(len(ref_rec_ids) / 2)],
                ref_rec_ids[-1],
            )
            set_data_widget(
                self.rec_roiz,
                ref_rec_ids[0],
                [
                    ref_rec_ids[int(len(ref_rec_ids) / 4)],
                    ref_rec_ids[int(len(ref_rec_ids) * 3 / 4)],
                ],
                ref_rec_ids[-1],
            )
            self._3dxanes_rec_roiz_old_val = self.rec_roiz.value

            dim = tifffile.imread(
                str(self.rec_fntpl).format(
                    self.ref_scan_id.value,
                    str(self.ref_sli.value).zfill(5),
                )
            ).shape
            set_data_widget(
                self.auto_cen_roix,
                0,
                [
                    int(dim[1] / 4),
                    int(dim[1] * 3 / 4),
                ],
                dim[1] - 1,
            )
            set_data_widget(
                self.auto_cen_roiy,
                0,
                [
                    int(dim[0] / 4),
                    int(dim[0] * 3 / 4),
                ],
                dim[0] - 1,
            )
            set_data_widget(
                self.rec_roix,
                0,
                [
                    int(dim[1] / 4),
                    int(dim[1] * 3 / 4),
                ],
                dim[1] - 1,
            )
            set_data_widget(
                self.rec_roiy,
                0,
                [
                    int(dim[0] / 4),
                    int(dim[0] * 3 / 4),
                ],
                dim[0] - 1,
            )

    @disp_progress_info("data directory info read")
    def _3dxanes_check_scan_id_s(self):
        if int(self.scan_id_s.value) > int(self.ref_scan_id.value):
            self.scan_id_s.value = self.ref_scan_id.value
        self.__xanes_reset_run_status()
        self.__xanes_reset_run_buttons()

    @disp_progress_info("data directory info read")
    def _3dxanes_check_scan_id_e(self):
        if int(self.scan_id_e.value) < int(self.ref_scan_id.value):
            self.scan_id_e.value = self.ref_scan_id.value
        self.__xanes_reset_run_status()
        self.__xanes_reset_run_buttons()

    def _3dxanes_tomo_auto_cen_dft_roi(self):
        if self.auto_cen_dft_roi.value:
            self.auto_cen_roix.enabled = False
            self.auto_cen_roiy.enabled = False
        else:
            self.auto_cen_roix.enabled = True
            self.auto_cen_roiy.enabled = True
        overlap_roi(self.viewer, self, mode="auto_cen")
        self.__xanes_reset_run_status()
        self.__xanes_reset_run_buttons()

    @disp_progress_info("xanes2d data loading")
    def __2dxanes_check_in_file(self):
        self._2dxanes_fn = self.tomo_tplt_fn.value
        if self._2dxanes_fn_p is None:
            self._2dxanes_fn_p = h5py.File(self._2dxanes_fn, "r")
        else:
            self._2dxanes_fn_p.close()
            self._2dxanes_fn_p = h5py.File(self._2dxanes_fn, "r")
        if (
            (self._2dxanes_fn_p["X_eng"].shape[0] > 1)
            and len(self._2dxanes_fn_p["img_xanes"].shape) == 3
            and self._2dxanes_fn_p["X_eng"].shape[0]
            == self._2dxanes_fn_p["img_xanes"].shape[0]
        ):
            try:
                self._2dxanes_eng_lst = self._2dxanes_fn_p["X_eng"][:]
                dark = self._2dxanes_fn_p["img_dark"][:].squeeze()
                flat = self._2dxanes_fn_p["img_bkg"][:].squeeze()
                tem = -np.log(
                    (da.from_array(self._2dxanes_fn_p["img_xanes"]) - dark)
                    / (flat - dark)
                )
                tem[np.isinf(tem)] = 0
                tem[np.isnan(tem)] = 0
                self._2dxanes_data = tem.compute()
                self.viewer.layers["xanes_raw_viewer"].data = self._2dxanes_data
                self.viewer.layers["xanes_raw_viewer"].refresh()
                self.viewer.reset_view()
                self._2dxanes_data_ready = True
            except Exception as e:
                self.op_status.value = (
                    "Something is wrong. Please check terminal for more information."
                )
                print(str(e))
                self._2dxanes_fn_p.close()
                self._2dxanes_fn_p = None
                self._2dxanes_data = None
                self._2dxanes_eng_lst = None
                self._2dxanes_fn = None
                self._2dxanes_data_ready = False
        self._test_run_done = False
        self._continue_run_confirmed = False

    def __2dxanes_set_widget(self):
        if self._2dxanes_data_ready:
            self.scan_id_s.enabled = False
            self.scan_id_e.enabled = False
            self.auto_cen_dft_roi.enabled = False
            self.auto_cen_dft_roi.value = False
            self.auto_cen_roix.enabled = True
            self.auto_cen_roiy.enabled = True
            self.ref_sli.enabled = True
            self.rec_roix.enabled = True
            self.rec_roiy.enabled = True
            self.rec_roiz.enabled = True
            self.sli_srch_range.enabled = False
            self.cen_srch_range.enabled = False
            self.ang_corr.enabled = False
            self.ang_corr_range.enabled = False
            self.test_run.enabled = True
            if self._test_run_done:
                self.confirm_test_run.enabled = True
            else:
                self.confirm_test_run.enabled = False
            if self._continue_run_confirmed:
                self.reg_run.enabled = True
            else:
                self.reg_run.enabled = False
            self.close_file.enabled = True
        else:
            self.scan_id_s.enabled = False
            self.scan_id_e.enabled = False
            self.auto_cen_dft_roi.enabled = False
            self.auto_cen_dft_roi.value = False
            self.auto_cen_roix.enabled = False
            self.auto_cen_roiy.enabled = False
            self.ref_sli.enabled = False
            self.rec_roix.enabled = False
            self.rec_roiy.enabled = False
            self.rec_roiz.enabled = False
            self.sli_srch_range.enabled = False
            self.cen_srch_range.enabled = False
            self.ang_corr.enabled = False
            self.ang_corr_range.enabled = False
            self.test_run.enabled = False
            self.confirm_test_run.enabled = False
            self.reg_run.enabled = False
            self.close_file.enabled = False

    def __2dxanes_show_sli(self, mode="auto_reg"):
        if mode == "auto_reg":
            if self.ref_sli.value < self.rec_roiz.value[0]:
                if self.rec_roiz.value[0] < len(self._2dxanes_eng_lst):
                    self.ref_sli.value = self.rec_roiz.value[0]
            if self.ref_sli.value > self.rec_roiz.value[1]:
                if self.rec_roiz.value[1] < len(self._2dxanes_eng_lst):
                    self.ref_sli.value = self.rec_roiz.value[1]

            tem = self.viewer.dims.current_step
            try:
                self.viewer.dims.current_step = [
                    self.ref_sli.value,
                    int(tem[1]),
                    int(tem[2]),
                ]
            except Exception as e:
                self.op_status.value = (
                    "Something is wrong. Please check terminal for more information."
                )
                print(str(e))

            self.ref_scan_id.value = (
                f"{float(self._2dxanes_eng_lst[self.ref_sli.value]) * 1000}eV"
            )
        elif mode == "auto_algn":
            if self._2dxanes_reg_roiz_old_val[0] != self.rec_roiz.value[0]:
                if self.rec_roiz.value[0] > self.ref_sli.value:
                    self.rec_roiz.value = [self.ref_sli.value, self.rec_roiz.value[1]]
                tem = self.viewer.dims.current_step
                try:
                    self.viewer.dims.current_step = [
                        self.rec_roiz.value[0],
                        int(tem[1]),
                        int(tem[2]),
                    ]
                    self.ref_scan_id.value = f"{float(self._2dxanes_eng_lst[self.rec_roiz.value[0]]) * 1000}eV"
                except Exception as e:
                    self.op_status.value = "Something is wrong. Please check terminal for more information."
                    print(str(e))
            elif self._2dxanes_reg_roiz_old_val[1] != self.rec_roiz.value[1]:
                if self.rec_roiz.value[1] < self.ref_sli.value:
                    self.rec_roiz.value = [self.rec_roiz.value[0], self.ref_sli.value]
                tem = self.viewer.dims.current_step
                try:
                    self.viewer.dims.current_step = [
                        self.rec_roiz.value[1],
                        int(tem[1]),
                        int(tem[2]),
                    ]
                    self.ref_scan_id.value = f"{float(self._2dxanes_eng_lst[self.rec_roiz.value[1]]) * 1000}eV"
                except Exception as e:
                    self.op_status.value = "Something is wrong. Please check terminal for more information."
                    print(str(e))
            self._2dxanes_reg_roiz_old_val = self.rec_roiz.value
        self.viewer.reset_view()

    def __2dxanes_set_roi_lims(self):
        dim = self._2dxanes_data.shape
        set_data_widget(
            self.ref_sli,
            0,
            int(dim[0] / 2),
            dim[0] - 1,
        )
        set_data_widget(
            self.auto_cen_roix,
            0,
            [
                int(dim[2] / 4),
                int(dim[2] * 3 / 4),
            ],
            dim[2] - 1,
        )
        set_data_widget(
            self.auto_cen_roiy,
            0,
            [
                int(dim[1] / 4),
                int(dim[1] * 3 / 4),
            ],
            dim[1] - 1,
        )
        set_data_widget(
            self.rec_roix,
            0,
            [
                int(dim[2] / 4),
                int(dim[2] * 3 / 4),
            ],
            dim[2] - 1,
        )
        set_data_widget(
            self.rec_roiy,
            0,
            [
                int(dim[1] / 4),
                int(dim[1] * 3 / 4),
            ],
            dim[1] - 1,
        )
        set_data_widget(
            self.rec_roiz,
            0,
            [
                0,
                dim[0] - 1,
            ],
            dim[0] - 1,
        )
        self._2dxanes_reg_roiz_old_val = self.rec_roiz.value

    def __2dxanes_check_if_new_reg(self):
        if (
            (self._tomo_tplt_fn_old_val != self.tomo_tplt_fn.value)
            or (self._2dxanes_reg_roix_old_val != self.auto_cen_roix.value)
            or (self._2dxanes_reg_roiy_old_val != self.auto_cen_roiy.value)
            or (self._2dxanes_reg_ref_im_old_val != self.ref_sli.value)
        ):
            self._2dxanes_if_new_reg = True
            self._2dxanes_new_reg_info = (
                f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
            )
            self._tomo_tplt_fn_old_val = self.tomo_tplt_fn.value
            self._2dxanes_reg_roix_old_val = self.auto_cen_roix.value
            self._2dxanes_reg_roiy_old_val = self.auto_cen_roiy.value
            self._2dxanes_reg_ref_im_old_val = self.ref_sli.value
        else:
            self._2dxanes_if_new_reg = False

    def __2dxanes_check_if_new_align(self):
        if (
            (self._2dxanes_align_roix_old_val != self.rec_roix.value)
            or (self._2dxanes_align_roiy_old_val != self.rec_roiy.value)
            or (self._2dxanes_align_roiz_old_val != self.rec_roiz.value)
        ):
            self._2dxanes_if_new_align = True
            self._2dxanes_align_roix_old_val = self.rec_roix.value
            self._2dxanes_align_roiy_old_val = self.rec_roiy.value
            self._2dxanes_align_roiz_old_val = self.rec_roiz.value
        else:
            self._2dxanes_if_new_reg = False

    def __2dxanes_def_img_autoreg_cfg(self):
        with open(cfg_fn, "r") as f:
            tem = json.load(f)
            tem["xanes2d_reg"]["cfg_file"] = str(
                Path(self._2dxanes_fn).parent
                / (
                    "2D_trial_reg_cfg_"
                    + Path(self._2dxanes_fn).stem
                    + "_"
                    + self._2dxanes_new_reg_info
                    + ".json"
                )
            )
        with open(cfg_fn, "w") as f:
            json.dump(tem, f, indent=4, separators=(",", ": "))

        xanes2d_image_autocent_cfg["data"]["im_id_s"] = self.rec_roiz.value[0]
        xanes2d_image_autocent_cfg["data"]["im_id_e"] = self.rec_roiz.value[1]
        xanes2d_image_autocent_cfg["data"]["im_id_fixed"] = self.ref_sli.value
        if self._continue_run_confirmed:
            xanes2d_image_autocent_cfg["reg_type"] = "align"
            xanes2d_image_autocent_cfg["data"]["roi"] = [
                self.rec_roiy.value[0],
                self.rec_roiy.value[1],
                self.rec_roix.value[0],
                self.rec_roix.value[1],
            ]
        else:
            xanes2d_image_autocent_cfg["reg_type"] = "auto_reg"
            xanes2d_image_autocent_cfg["data"]["roi"] = [
                self.auto_cen_roiy.value[0],
                self.auto_cen_roiy.value[1],
                self.auto_cen_roix.value[0],
                self.auto_cen_roix.value[1],
            ]

        xanes2d_image_autocent_cfg["file"]["XANES2D_raw_fn"] = str(
            Path(self._2dxanes_fn).resolve()
        )
        xanes2d_image_autocent_cfg["file"]["sav_fn"] = str(
            Path(self._2dxanes_fn).parent
            / (
                "2D_trial_reg_"
                + Path(self._2dxanes_fn).stem
                + "_"
                + self._2dxanes_new_reg_info
                + ".h5"
            )
        )
        xanes2d_image_autocent_cfg["meta"]["eng_list"] = list(
            self._2dxanes_eng_lst[self.rec_roiz.value[0] : self.rec_roiz.value[1]]
        )

        with open(tem["xanes2d_reg"]["cfg_file"], "w") as f:
            json.dump(xanes2d_image_autocent_cfg, f, indent=4, separators=(",", ": "))

    def __xanes_reset_run_status(self):
        self._test_run_done = False
        self.confirm_test_run.value == "No"
        self._continue_run_confirmed = False

    def __xanes_reset_run_buttons(self):
        if self._test_run_done:
            self.confirm_test_run.enabled = True
        else:
            self.confirm_test_run.enabled = False
            self.confirm_test_run.value == "No"
            self._continue_run_confirmed = False
        if self._continue_run_confirmed:
            self.reg_run.enabled = True
        else:
            self.reg_run.enabled = False

    def _xanes_data_type(self):
        self.tomo_tplt_fn.value = ""
        self.ref_scan_id.value = ""
        global _TOMO_XANES3D_REC_ID_S_CHOICES
        _TOMO_XANES3D_REC_ID_S_CHOICES = []
        self.scan_id_s.reset_choices()
        global _TOMO_XANES3D_REC_ID_E_CHOICES
        _TOMO_XANES3D_REC_ID_E_CHOICES = []
        self.scan_id_e.reset_choices()
        self.auto_cen_dft_roi.value = False
        self.auto_cen_roix.value = [540, 740]
        self.auto_cen_roiy.value = [540, 740]
        self.ref_sli.value = 540
        self.rec_roix.value = [540, 740]
        self.rec_roiy.value = [540, 740]
        self.rec_roiz.value = [440, 640]
        self.sli_srch_range.value = 10
        self.cen_srch_range.value = 15
        self.ang_corr.value = False
        self.ang_corr_range.value = 2.0
        self.confirm_test_run.value = "No"
        self.op_status.value = ""
        self.rec_fntpl = None
        self._test_run_done = False
        self._continue_run_confirmed = False
        if self.data_type.value == "3D XANES":
            self.tomo_tplt_fn.filter = "*.json"
            self.__3dxanes_set_widget()
        else:
            self.tomo_tplt_fn.filter = "*.h5"
            self.__2dxanes_set_widget()
        self.__xanes_reset_run_buttons()

    def _xanes_set_fn(self):
        if self.data_type.value == "3D XANES":
            self._tomo_tplt_fn = self.tomo_tplt_fn.value
            cfg_type = check_cfg_type(self._tomo_tplt_fn)
            if cfg_type == "xanes3d_tomo_tplt":
                with open(self._tomo_tplt_fn, "r") as f:
                    tem = json.load(f)
                    self.ref_scan_id.value = list(tem.keys())[0]
                    self._ref_rec_tplt = tem[list(tem.keys())[0]]
                if (
                    "tomo_zfly"
                    in self._ref_rec_tplt["file_params"]["io_confg"]["tomo_raw_fn_template"]
                ):
                    self._tomo_cfg = ZFLY_CFG["io_data_structure_xanes3D"]
                elif (
                    "fly_scan"
                    in self._ref_rec_tplt["file_params"]["io_confg"]["tomo_raw_fn_template"]
                ):
                    self._tomo_cfg = FLY_CFG["io_data_structure_xanes3D"]
                self.__3dxanes_comp_tomo_fntpl()
                self.__3dxanes_tomo_check_avail_id_s()
                self.__3dxanes_tomo_check_avail_id_e()
                self.__3dxanes_set_scan_id_lims()
                self.__3dxanes_set_widget()
                self.__3dxanes_set_roi_lims()
                self.__3dxanes_tomo_show_sli(mode="auto_cen")
                self.__xanes_reset_run_status()
                self.__xanes_reset_run_buttons()
            else:
                self.op_status.value = "wrong type of json cfg file. check error message in terminal"
                print("The required json file should have file name starting with 'xanes3d_tomo_tplt_cfg'.")
        else:
            self.__2dxanes_check_in_file()
            self.__2dxanes_set_widget()
            self.__2dxanes_set_roi_lims()
            self.__2dxanes_show_sli(mode="auto_reg")
            _min = self.viewer.layers["xanes_raw_viewer"].data[self.ref_sli.value].min()
            _max = self.viewer.layers["xanes_raw_viewer"].data[self.ref_sli.value].max()
            rng = _max - _min
            self.viewer.layers["xanes_raw_viewer"].contrast_limits = [
                _min + 0.1 * rng,
                _max - 0.1 * rng,
            ]
            self.__xanes_reset_run_status()
            self.__xanes_reset_run_buttons()

    def _xanes_tomo_auto_cen_roix(self):
        overlap_roi(self.viewer, self, mode="auto_cen")
        show_layers_in_viewer(self.viewer, ["xanes_raw_viewer", "auto_cen_roi"])
        self.__xanes_reset_run_status()
        self.__xanes_reset_run_buttons()

    def _xanes_tomo_auto_cen_roiy(self):
        overlap_roi(self.viewer, self, mode="auto_cen")
        show_layers_in_viewer(self.viewer, ["xanes_raw_viewer", "auto_cen_roi"])
        self.__xanes_reset_run_status()
        self.__xanes_reset_run_buttons()

    def _xanes_tomo_auto_cen_ref_sli(self):
        if self.data_type.value == "3D XANES":
            self.__3dxanes_tomo_show_sli(mode="auto_cen")
        else:
            self.__2dxanes_show_sli(mode="auto_reg")
        overlap_roi(self.viewer, self, mode="auto_cen")
        show_layers_in_viewer(self.viewer, ["xanes_raw_viewer", "auto_cen_roi"])
        self.__xanes_reset_run_status()
        self.__xanes_reset_run_buttons()

    def _xanes_tomo_rec_roix(self):
        overlap_roi(self.viewer, self, mode="recon_roi")
        show_layers_in_viewer(self.viewer, ["xanes_raw_viewer", "recon_roi"])
        if self.data_type.value == "2D XANES":
            self.confirm_test_run.value = "No"

    def _xanes_tomo_rec_roiy(self):
        overlap_roi(self.viewer, self, mode="recon_roi")
        show_layers_in_viewer(self.viewer, ["xanes_raw_viewer", "recon_roi"])
        if self.data_type.value == "2D XANES":
            self.confirm_test_run.value = "No"

    def _xanes_tomo_rec_roiz(self):
        if self.data_type.value == "3D XANES":
            self.__3dxanes_tomo_show_sli(mode="recon_roi")
        else:
            self.__2dxanes_show_sli(mode="auto_algn")
            self.confirm_test_run.value = "No"
        overlap_roi(self.viewer, self, mode="recon_roi")
        show_layers_in_viewer(self.viewer, ["xanes_raw_viewer", "recon_roi"])

    @disp_progress_info("xanes auto registration test run")
    def _xanes_test_run(self):
        if self.data_type.value == "3D XANES":
            self.__3dxanes_tomo_if_new_rec()
            self.__3dxnaes_tomo_def_autocent_cfg()

            sig = os.system(f"ipython {xanes3d_auto_cen_reg_script_fn}")
            print(f"{sig=}")

            if sig == 0:
                with open(cfg_fn, "r") as f:
                    tem = json.load(f)
                with open(tem["xanes3d_auto_cen"]["cfg_file"], "r") as f:
                    tem = json.load(f)
                trial_imgs = []
                with h5py.File(
                    tem["aut_xns3d_pars"]["xanes3d_sav_trl_reg_fn"], "r"
                ) as f:
                    for key in f["/auto_centering/"].keys():
                        trial_imgs.append(
                            f[f"/auto_centering/{key}/optimization itr 1/trial_rec"][:]
                        )
                update_layer_in_viewer(self.viewer, np.array(trial_imgs), "autocent_check")
                show_layers_in_viewer(self.viewer, ["autocent_check"])
            if sig == 0:
                self._test_run_done = True
            else:
                self._test_run_done = False
                self.op_status.value = "auto centering fails"
                print("auto centering fails")
            self.confirm_test_run.value == "No"
            self._continue_run_confirmed = False
            self.__xanes_reset_run_buttons()
        else:
            self.__2dxanes_check_if_new_reg()
            self.__2dxanes_def_img_autoreg_cfg()

            if self._2dxanes_if_new_reg:
                sig = os.system(f"ipython {xanes2d_img_auto_cen_script_fn}")

                if sig == 0:
                    with open(cfg_fn, "r") as f:
                        tem = json.load(f)
                    with open(tem["xanes2d_reg"]["cfg_file"], "r") as f:
                        tem = json.load(f)
                    if self._2dxanes_reg_fn_p is None:
                        self._2dxanes_reg_fn_p = h5py.File(tem["file"]["sav_fn"], "r")
                    else:
                        self._2dxanes_reg_fn_p.close()
                        self._2dxanes_reg_fn_p = h5py.File(tem["file"]["sav_fn"], "r")

                    reg_rlt = da.from_array(
                        self._2dxanes_reg_fn_p[
                            "/registration_results/reg_results/registered_xanes2D"
                        ]
                    )
                    update_layer_in_viewer(self.viewer, reg_rlt, "autoreg_check")
                    show_layers_in_viewer(self.viewer, ["autoreg_check"])
                    self._test_run_done = True
                else:
                    self._test_run_done = False
                    self.op_status.value = "auto alignment fails"
                    print("auto alignment fails")
                self.confirm_test_run.value == "No"
                self._continue_run_confirmed = False
                self.__xanes_reset_run_buttons()
            else:
                self.op_status.value = "Nothing is changed from last auto-registration."
                print("Nothing is changed from last auto-registration.")

    def _xanes_confirm_to_run(self):
        if self.confirm_test_run.value == "Yes":
            self._continue_run_confirmed = True
            if self.data_type.value == "3D XANES":
                self.reg_run.enabled = True
            else:
                if (self.auto_cen_roix.value == self.rec_roix.value) and (
                    self.auto_cen_roiy.value == self.rec_roiy.value
                ):
                    self.reg_run.enabled = False
                    self.op_status.value = (
                        "2D XANES registration is done! Nothing is left in this page."
                    )
                    print(
                        "2D XANES registration is done! Nothing is left in this page."
                    )
                else:
                    self.reg_run.enabled = True
        else:
            self._continue_run_confirmed = False
            self.reg_run.enabled = False

    @disp_progress_info("xanes auto registration")
    def _xanes_reg_run(self):
        if self.data_type.value == "3D XANES":
            self.__3dxanes_tomo_if_new_rec()
            self.__3dxnaes_tomo_def_autocent_cfg()

            sig = os.system(f"ipython {xanes3d_auto_cen_reg_script_fn}")
            if sig == 0:
                self.op_status.value = "autocen and registration are finished. please check the results in 'XANES Analysis'."
                print(
                    "autocen and registration are finished. please check the results in 'XANES Analysis'."
                )
            else:
                self.op_status.value = (
                    "something went wrong during autocen or registration processes."
                )
                print("something went wrong during autocen or registration processes.")
                self.reg_run.enabled = False
        else:
            self.__2dxanes_check_if_new_reg()
            self.__2dxanes_def_img_autoreg_cfg()
            self.__2dxanes_check_if_new_align()

            if self._2dxanes_if_new_align:
                rm_gui_viewers(self.viewer, ["autocent_check"])
                if self._2dxanes_reg_fn_p is not None:
                    self._2dxanes_reg_fn_p.close()

                sig = os.system(f"ipython {xanes2d_img_auto_cen_script_fn}")

                if sig == 0:
                    with open(cfg_fn, "r") as f:
                        tem = json.load(f)
                    with open(tem["xanes2d_reg"]["cfg_file"], "r") as f:
                        tem = json.load(f)
                    if self._2dxanes_reg_fn_p is None:
                        self._2dxanes_reg_fn_p = h5py.File(tem["file"]["sav_fn"], "r")
                    else:
                        self._2dxanes_reg_fn_p.close()
                        self._2dxanes_reg_fn_p = h5py.File(tem["file"]["sav_fn"], "r")

                    reg_rlt = da.from_array(
                        self._2dxanes_reg_fn_p[
                            "/registration_results/reg_results/registered_xanes2D"
                        ]
                    )
                    update_layer_in_viewer(self.viewer, reg_rlt, "autocent_check")
                    show_layers_in_viewer(self.viewer, ["autocent_check"])
                else:
                    self._test_run_done = False
                    self.op_status.value = "Alignment fails"
                    print("Alignment fails")
            else:
                self.op_status.value = "Nothing is changed from last alignment."
                print("Nothing is changed from last alignment.")

    def _close_file(self):
        if self._2dxanes_reg_fn is not None:
            self._2dxanes_reg_fn.close()
            self._2dxanes_reg_fn = None
        if self._2dxanes_fn_p is not None:
            self._2dxanes_fn_p.close()
            self._2dxanes_fn_p = None
        rm_gui_viewers(self.viewer, self._viewers)
