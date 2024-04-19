import numpy as np
from scipy.ndimage import zoom

from pathlib import Path
import json
import h5py

import txm_sandbox.utils.xanes_analysis as xa

cfg_fn = Path(__file__).parents[1] / "configs/txm_simple_gui_script_cfg.json"


def read_hdf5_group_to_dict(fp, group, is_file=False):
    if is_file:
        with h5py.File(fp, "r") as f:
            return recursively_load_dict(f[group])
    else:
        return recursively_load_dict(fp[group])


def recursively_load_dict(group):
    output = {}
    for key, val in group.items():
        if isinstance(val, h5py.Dataset):
            output[key] = val[...]
        elif isinstance(val, h5py.Group):
            output[key] = recursively_load_dict(val)
    return output


with open(cfg_fn, "r") as f:
    xanes2d_data_fn = json.load(f)["xanes2d_fit"]["cfg_file"]

print(f"{xanes2d_data_fn=}")
with h5py.File(xanes2d_data_fn, "a") as f:
    # if "/processed_XANES2D" in f:
    #     proc_xanes_path = "/processed_XANES2D"
    # else:
    proc_xanes_path = "/processed_XANES"

    bin_fact = f[f"/{proc_xanes_path}/proc_parameters/bin_fact"][()]
    if bin_fact == 1:
        imgs = f["/registration_results/reg_results/registered_xanes2D"][:]
    else:
        imgs = zoom(
            f["/registration_results/reg_results/registered_xanes2D"][:],
            (1, 1 / bin_fact, 1 / bin_fact),
        )
    xana_eng_list = f[f"/{proc_xanes_path}/proc_parameters/eng_list"][:]
    xana_edge_eng = f[f"/{proc_xanes_path}/proc_parameters/edge_eng"][()]
    xana_pre_edge_e = f[f"/{proc_xanes_path}/proc_parameters/pre_edge_e"][()]
    xana_post_edge_s = f[f"/{proc_xanes_path}/proc_parameters/post_edge_s"][()]
    xana_edge_jump_thres = f[f"/{proc_xanes_path}/proc_parameters/edge_jump_threshold"][
        ()
    ]
    xana_edge_offset_thres = f[
        "/processed_XANES/proc_parameters/edge_offset_threshold"
    ][()]
    # xana_use_mask = f[f"/{proc_xanes_path}/proc_parameters/use_mask"][()]
    xana_type = f[f"/{proc_xanes_path}/proc_parameters/analysis_type"][()].decode(
        "utf-8"
    )
    xana_data_shape = np.int32(
        np.round(f[f"/{proc_xanes_path}/proc_parameters/data_shape"][:] / bin_fact)
    )
    xana_edge50_fit_s = f[f"/{proc_xanes_path}/proc_parameters/edge50_fit_s"][()]
    xana_edge50_fit_e = f[f"/{proc_xanes_path}/proc_parameters/edge50_fit_e"][()]
    xana_wl_fit_eng_s = f[f"/{proc_xanes_path}/proc_parameters/wl_fit_eng_s"][()]
    xana_wl_fit_eng_e = f[f"/{proc_xanes_path}/proc_parameters/wl_fit_eng_e"][()]
    xana_edge_fit_order = f[
        f"/{proc_xanes_path}/proc_parameters/pre_post_edge_norm_fit_order"
    ][()]
    # xana_use_flt_spec = f[f"/{proc_xanes_path}/proc_parameters/flt_spec"][()]
    sav_items = list(f[f"/{proc_xanes_path}/proc_spectrum"].keys())
    xana = xa.xanes_analysis(
        imgs,
        xana_eng_list,
        xana_edge_eng,
        pre_ee=xana_pre_edge_e,
        post_es=xana_post_edge_s,
        edge_jump_threshold=xana_edge_jump_thres,
        pre_edge_threshold=xana_edge_offset_thres,
    )
    if f"/{proc_xanes_path}/proc_spectrum" in f:
        del f[f"/{proc_xanes_path}/proc_spectrum"]
        g12 = f.create_group(f"/{proc_xanes_path}/proc_spectrum")
    else:
        g12 = f.create_group(f"/{proc_xanes_path}/proc_spectrum")

    if xana_type == "wl":
        tem = read_hdf5_group_to_dict(
            f, f"/{proc_xanes_path}/proc_parameters/wl_fit method"
        )
        if isinstance(tem["optimizer"], np.ndarray):
            tem["optimizer"] = tem["optimizer"].item()
            if isinstance(tem["optimizer"], bytes):
                tem["optimizer"] = tem["optimizer"].decode("utf-8")
        if isinstance(tem["method"], np.ndarray):
            tem["method"] = tem["method"].item()
            if isinstance(tem["method"], bytes):
                tem["method"] = tem["method"].decode("utf-8")
        if isinstance(tem["params"]["spec"], np.ndarray):
            tem["params"]["spec"] = tem["params"]["spec"].item()
            if isinstance(tem["params"]["spec"], bytes):
                tem["params"]["spec"] = tem["params"]["spec"].decode("utf-8")
        if isinstance(tem["params"]["order"], np.ndarray):
            tem["params"]["order"] = int(tem["params"]["order"].item())
        if isinstance(tem["params"]["eng_offset"], np.ndarray):
            tem["params"]["eng_offset"] = float(tem["params"]["eng_offset"].item())
        print(f"{tem.items()=}")
        wl_fit_params = {
            "ftype": "wl",
            "optimizer": tem["optimizer"],
            "model": tem["method"],
            "on": tem["params"]["spec"],
            "order": tem["params"]["order"],
            "eoff": tem["params"]["eng_offset"],
        }
        _g12 = {}
        for jj in sav_items:
            _g12[jj] = g12.create_dataset(
                jj, shape=(xana_data_shape[1:]), dtype=np.float32
            )
        if bin_fact == 1:
            xana.spec[:] = f["/registration_results/reg_results/registered_xanes2D"][:]
            xana.smooth_spec()
            xana.fit_spec(xana_wl_fit_eng_s, xana_wl_fit_eng_e, **wl_fit_params)
            xana.find_wl(
                xana_wl_fit_eng_s, xana_wl_fit_eng_e, optimizer="model", ufac=50
            )
            xana.cal_wgt_eng(xana_wl_fit_eng_s, xana_wl_fit_eng_e)
            for jj in sav_items:
                if jj == "wl_pos_fit":
                    _g12[jj] = np.float32(xana.wl_pos_fit)[:]
                if jj == "wl_fit_err":
                    _g12[jj][:] = np.float32(
                        xana.model["wl"]["fit_rlt"][1].reshape(*xana.spec.shape[1:])
                    )[:]
                if jj == "weighted_attenuation":
                    _g12[jj] = np.float32(xana.weighted_atten)[:]
        else:
            xana.spec[:] = zoom(
                f["/registration_results/reg_results/registered_xanes2D"][:],
                (1, 1 / bin_fact, 1 / bin_fact),
            )
            xana.smooth_spec()
            xana.fit_spec(xana_wl_fit_eng_s, xana_wl_fit_eng_e, **wl_fit_params)
            xana.find_wl(
                xana_wl_fit_eng_s, xana_wl_fit_eng_e, optimizer="model", ufac=50
            )
            xana.cal_wgt_eng(xana_wl_fit_eng_s, xana_wl_fit_eng_e)
            for jj in sav_items:
                if jj == "wl_pos_fit":
                    _g12[jj] = np.float32(xana.wl_pos_fit)[:]
                if jj == "wl_fit_err":
                    _g12[jj][:] = np.float32(
                        xana.model["wl"]["fit_rlt"][1].reshape(*xana.spec.shape[1:])
                    )[:]
                if jj == "weighted_attenuation":
                    _g12[jj] = np.float32(xana.weighted_atten)[:]
    elif xana_type == "full":
        if "wl_pos_fit" in sav_items:
            tem = read_hdf5_group_to_dict(
                f, f"/{proc_xanes_path}/proc_parameters/wl_fit method"
            )
            if isinstance(tem["optimizer"], np.ndarray):
                tem["optimizer"] = tem["optimizer"].item()
                if isinstance(tem["optimizer"], bytes):
                    tem["optimizer"] = tem["optimizer"].decode("utf-8")
            if isinstance(tem["method"], np.ndarray):
                tem["method"] = tem["method"].item()
                if isinstance(tem["method"], bytes):
                    tem["method"] = tem["method"].decode("utf-8")
            if isinstance(tem["params"]["spec"], np.ndarray):
                tem["params"]["spec"] = tem["params"]["spec"].item()
                if isinstance(tem["params"]["spec"], bytes):
                    tem["params"]["spec"] = tem["params"]["spec"].decode("utf-8")
            if isinstance(tem["params"]["order"], np.ndarray):
                tem["params"]["order"] = int(tem["params"]["order"].item())
            if isinstance(tem["params"]["eng_offset"], np.ndarray):
                tem["params"]["eng_offset"] = float(tem["params"]["eng_offset"].item())
            wl_fit_params = {
                "ftype": "wl",
                "optimizer": tem["optimizer"],
                "model": tem["method"],
                "on": tem["params"]["spec"],
                "order": tem["params"]["order"],
                "eoff": tem["params"]["eng_offset"],
            }
        if np.any(
            np.array([ii in {"edge_pos_fit", "edge50_pos_fit"} for ii in sav_items])
        ):
            tem = read_hdf5_group_to_dict(
                f, f"/{proc_xanes_path}/proc_parameters/edge_fit method"
            )
            if isinstance(tem["optimizer"], np.ndarray):
                tem["optimizer"] = tem["optimizer"].item()
                if isinstance(tem["optimizer"], bytes):
                    tem["optimizer"] = tem["optimizer"].decode("utf-8")
            if isinstance(tem["method"], np.ndarray):
                tem["method"] = tem["method"].item()
                if isinstance(tem["method"], bytes):
                    tem["method"] = tem["method"].decode("utf-8")
            if isinstance(tem["params"]["spec"], np.ndarray):
                tem["params"]["spec"] = tem["params"]["spec"].item()
                if isinstance(tem["params"]["spec"], bytes):
                    tem["params"]["spec"] = tem["params"]["spec"].decode("utf-8")
            if isinstance(tem["params"]["order"], np.ndarray):
                tem["params"]["order"] = int(tem["params"]["order"].item())
            if isinstance(tem["params"]["eng_offset"], np.ndarray):
                tem["params"]["eng_offset"] = float(tem["params"]["eng_offset"].item())
            edge_fit_params = {
                "ftype": "edge",
                "optimizer": tem["optimizer"],
                "model": tem["method"],
                "on": tem["params"]["spec"],
                "order": tem["params"]["order"],
                "eoff": tem["params"]["eng_offset"],
            }
        _g12 = {}
        for jj in sav_items:
            _g12[jj] = g12.create_dataset(
                jj, shape=(xana_data_shape[1:]), dtype=np.float32
            )
        if bin_fact == 1:
            xana.spec[:] = f["/registration_results/reg_results/registered_xanes2D"][:]

            xana.smooth_spec()
            xana.cal_pre_edge_sd()
            xana.cal_post_edge_sd()
            xana.cal_pre_edge_mean()
            xana.cal_post_edge_mean()
            xana.full_spec_preprocess(
                xana_edge_eng, order=xana_edge_fit_order, save_pre_post=True
            )

            if np.any(
                np.array([ii in {"wl_pos_fit", "wl_fit_err"} for ii in sav_items])
            ):
                xana.fit_spec(xana_wl_fit_eng_s, xana_wl_fit_eng_e, **wl_fit_params)
                xana.find_wl(
                    xana_wl_fit_eng_s, xana_wl_fit_eng_e, optimizer="model", ufac=50
                )

            if np.any(
                np.array(
                    ii
                    in {
                        "edge_pos_fit",
                        "edge50_pos_fit",
                    }
                    for ii in sav_items
                )
            ):
                xana.fit_spec(xana_edge50_fit_s, xana_edge50_fit_e, **{})

            if "edge50_pos_fit" in sav_items:
                xana.find_edge_50(
                    xana_edge50_fit_s,
                    xana_edge50_fit_e,
                    xana_wl_fit_eng_s,
                    xana_wl_fit_eng_e,
                    optimizer="",
                    ufac=20,
                )

            if "edge_pos_fit" in sav_items:
                xana.find_edge_deriv(
                    xana_edge50_fit_s, xana_edge50_fit_e, optimizer="model", ufac=20
                )

            xana.cal_wgt_eng(xana_pre_edge_e + xana_edge_eng, xana_wl_fit_eng_e)
            for jj in sav_items:
                if jj == "wl_pos_fit":
                    _g12[jj] = np.float32(xana.wl_pos_fit)[:]
                if jj == "edge_pos_fit":
                    _g12[jj] = np.float32(xana.edge_pos_fit)[:]
                if jj == "edge50_pos_fit":
                    _g12[jj] = np.float32(xana.edge50_pos_fit)[:]
                if jj == "wl_fit_err":
                    _g12[jj] = np.float32(
                        xana.model["wl"]["fit_rlt"][1].reshape(*xana.spec.shape[1:])
                    )[:]
                if jj == "edge_fit_err":
                    _g12[jj] = np.float32(
                        xana.model["edge"]["fit_rlt"][1].reshape(*xana.spec.shape[1:])
                    )[:]
                if jj == "weighted_attenuation":
                    _g12[jj] = np.float32(xana.weighted_atten)[:]
        else:
            xana.spec[:] = zoom(
                f["/registration_results/reg_results/registered_xanes2D"][:],
                (1, 1 / bin_fact, 1 / bin_fact),
            )

            xana.smooth_spec()
            xana.cal_pre_edge_sd()
            xana.cal_post_edge_sd()
            xana.cal_pre_edge_mean()
            xana.cal_post_edge_mean()
            xana.full_spec_preprocess(
                xana_edge_eng, order=xana_edge_fit_order, save_pre_post=True
            )

            if np.any(
                np.array([ii in {"wl_pos_fit", "wl_fit_err"} for ii in sav_items])
            ):
                xana.fit_spec(xana_wl_fit_eng_s, xana_wl_fit_eng_e, **wl_fit_params)
                xana.find_wl(
                    xana_wl_fit_eng_s, xana_wl_fit_eng_e, optimizer="model", ufac=50
                )

            if np.any(
                np.array(
                    [
                        ii
                        in {
                            "edge_pos_fit",
                            "edge50_pos_fit",
                        }
                        for ii in sav_items
                    ]
                )
            ):
                xana.fit_spec(xana_edge50_fit_s, xana_edge50_fit_e, **{})

            if "edge_pos_fit" in sav_items:
                xana.find_edge_50(
                    xana_edge50_fit_s,
                    xana_edge50_fit_e,
                    xana_wl_fit_eng_s,
                    xana_wl_fit_eng_e,
                    optimizer="",
                    ufac=20,
                )

            if "edge50_pos_fit" in sav_items:
                xana.find_edge_deriv(
                    xana_edge50_fit_s, xana_edge50_fit_e, optimizer="model", ufac=20
                )

            xana.cal_wgt_eng(xana_pre_edge_e + xana_edge_eng, xana_wl_fit_eng_e)
            for jj in sav_items:
                if jj == "wl_pos_fit":
                    _g12[jj] = np.float32(xana.wl_pos_fit)[:]
                if jj == "edge_pos_fit":
                    _g12[jj] = np.float32(xana.edge_pos_fit)[:]
                if jj == "edge50_pos_fit":
                    _g12[jj] = np.float32(xana.edge50_pos_fit)[:]
                if jj == "wl_fit_err":
                    _g12[jj][:] = np.float32(
                        xana.model["wl"]["fit_rlt"][1].reshape(*xana.spec.shape[1:])
                    )[:]
                if jj == "edge_fit_err":
                    _g12[jj][:] = np.float32(
                        xana.model["edge"]["fit_rlt"][1].reshape(*xana.spec.shape[1:])
                    )[:]
                if jj == "weighted_attenuation":
                    _g12[jj] = np.float32(xana.weighted_atten)[:]
print("xanes2D analysis is done!")
