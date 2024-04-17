# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
import os, sys, site, re, yaml
from os.path import basename, relpath
from pathlib import Path
from textwrap import dedent
from typing import List, Tuple, Dict, Generator

from doit import get_var
from doit.action import BaseAction, CmdAction
from doit.tools import check_timestamp_unchanged, create_folder

import pdkmaster.technology, pdkmaster.design, pdkmaster.dispatch
import pdkmaster.io.spice, pdkmaster.io.klayout
import c4m, c4m.flexcell

### Config

DOIT_CONFIG = {
    "default_tasks": [
        "open_pdk", "gds", "spice", "klayout", "coriolis",
    ],
}


### support functions

def get_var_env(name, default=None):
    """Uses get_var to get a command line variable, also checks
    environment variables for default value

    If os.environ[name.upper()] exists that value will override the
    default value given.
    """
    try:
        default = os.environ[name.upper()]
    except:
        # Keep the specified default
        pass
    return get_var(name, default=default)


class AVTScriptAction(BaseAction):
    def __init__(self, avt_script, tmp=None):
        if tmp is None:
            tmp = tmp_dir
        self.script = avt_script
        self.tmp = tmp

        self.out = None
        self.err = None
        self.result = None
        self.values = {}

    def execute(self, out=None, err=None):
        # Create new action on every new call so we can always write
        # the script to the stdin of the subprocess.
        if avt_shell is None:
            action = CmdAction('echo "disabled because lack of avt_shell"')
        else:
            pr, pw = os.pipe()
            fpw = os.fdopen(pw, "w")
            fpw.write(self.script)
            fpw.close()

            action = CmdAction(avt_shell, stdin=pr, cwd=self.tmp)

        r = action.execute(out=out, err=err)
        self.values = action.values
        self.result = action.result
        self.out = action.out
        self.err = action.err
        return r


### globals

def _first(it):
    return next(iter(it))

top_dir = Path(__file__).parent
tmp_dir = top_dir.joinpath("tmp")
setup_file = top_dir.joinpath("setup.py")

dist_dir = top_dir.joinpath("dist")

open_pdk_dir = top_dir.joinpath("open_pdk")
open_pdk_gf180mcu_dir = open_pdk_dir.joinpath("C4M.gf180mcu")
open_pdk_tech_dir = open_pdk_gf180mcu_dir.joinpath("libs.tech")
open_pdk_ref_dir = open_pdk_gf180mcu_dir.joinpath("libs.ref")

override_dir = top_dir.joinpath("override")

c4m_local_dir = top_dir.joinpath("c4m")
gf180mcu_local_dir = c4m_local_dir.joinpath("pdk", "gf180mcu")
c4m_inst_dir = Path(site.getsitepackages()[0]).joinpath("c4m")
gf180mcu_inst_dir = c4m_inst_dir.joinpath("pdk", "gf180mcu")
flexcell_inst_dir = Path(c4m.flexcell.__file__).parent

c4m_pdk_gf180mcu_py_files = tuple(gf180mcu_local_dir.rglob("*.py"))
pdkmaster_deps = (
    *Path(_first(pdkmaster.technology.__path__)).rglob("*.py"),
    *Path(_first(pdkmaster.design.__path__)).rglob("*.py"),
    *Path(_first(pdkmaster.dispatch.__path__)).rglob("*.py"),
)
pdkmaster_io_spice_deps = (
    *Path(_first(pdkmaster.io.spice.__path__)).rglob("*.py"),
)
pdkmaster_io_klayout_deps = (
    *Path(_first(pdkmaster.io.klayout.__path__)).rglob("*.py"),
)
flexcell_deps = (
    *Path(_first(c4m.flexcell.__path__)).rglob("*.py"),
)

# variables
python = get_var_env("python", default="python3")
pip = get_var_env("pip", default="pip3")

gf180mcu_pdk = get_var_env("gf180mcu_pdk")
if gf180mcu_pdk is None:
    raise EnvironmentError(
        "gf180mcu_pdk variable or GF180MCU_PDK environment variable not given"
    )
os.environ["GF180MCU_PDK"] = gf180mcu_pdk
gf180mcu_pdk_dir = Path(gf180mcu_pdk)

avertec_top = get_var_env("avertec_top")
avt_shell = get_var_env(
    "avt_shell", default=(
        f"{avertec_top}/bin/avt_shell" if avertec_top is not None else None
    ),
)

### cell list

cell_list_file = top_dir.joinpath("cell_list.yml")

def task_cell_list():
    """Regenerate cell list.

    This task is not run by default. It needs to be run manually when the cell list
    has been changed and then the updated file has to be commit to git.
    """
    def write_list():
        import yaml

        from c4m.pdk import gf180mcu
        # from doitlib import libs

        cell_list = {
            lib.name: list(cell.name for cell in lib.cells)
            for lib in gf180mcu.__libs__
        }
        with cell_list_file.open("w") as f:
            yaml.dump(cell_list, f)

    return {
        "title": lambda _: "Creating cell list file",
        "targets": (
            cell_list_file,
        ),
        "actions": (
            write_list,
        ),
    }

# We assume that the cell list is stored in git and is available in the top directory.
assert cell_list_file.exists()
with cell_list_file.open("r") as f:
    cell_list: Dict[str, List[str]]
    cell_list = yaml.safe_load(f)

lib_deps = {
    "StdCell3V3Lib": (*pdkmaster_deps, *flexcell_deps),
    "StdCell5V0Lib": (*pdkmaster_deps, *flexcell_deps),
}


### main tasks

#
# open_pdk
def task_open_pdk():
    """Create open_pdk dir"""
    # This is separate task so we can clean up full open_pdk directory

    return {
        "title": lambda _: "Creating open_pdk directory",
        "targets": (open_pdk_dir,),
        "actions": (
            (create_folder, (open_pdk_dir,)),
        ),
        "clean": (f"rm -fr {str(open_pdk_dir)}",),
    }


#
# gds
def task_gds():
    """Generate GDSII files"""

    gds_dirs = tuple(
        open_pdk_ref_dir.joinpath(lib, "gds") for lib in cell_list.keys()
    )
    gds_files: Dict[str, Tuple[Path, ...]] = {}
    for lib, cells in cell_list.items():
        gds_files[lib] = tuple(
            open_pdk_ref_dir.joinpath(lib, "gds", f"{cell}.gds")
            for cell in cells
        )

    def gen_gds(libname):
        from pdkmaster.io.klayout import export2db
        from c4m.pdk import gf180mcu
        # from doitlib import libs

        lib = None
        for lib2 in gf180mcu.__libs__:
            if lib2.name == libname:
                lib = lib2
                break
        assert lib is not None

        out_dir = open_pdk_ref_dir.joinpath(libname, "gds")
        layout = export2db(
            lib, gds_layers=gf180mcu.gds_layers, cell_name=None, merge=False,
            add_pin_label=True,
        )
        layout.write(str(out_dir.joinpath(f"{libname}.gds")))
        for cell in layout.each_cell():
            assert cell.name != libname
            cell.write(str(out_dir.joinpath(f"{cell.name}.gds")))

    for libname in cell_list.keys():
        yield {
            "name": libname,
            "doc": f"Creating gds files for {libname}",
            "file_dep": (*c4m_pdk_gf180mcu_py_files, *lib_deps[libname], *pdkmaster_io_klayout_deps),
            "targets": gds_files[libname],
            "actions": (
                *(
                    (create_folder, (dir_,)) for dir_ in gds_dirs
                ),
                (gen_gds, (libname,)),
            ),
        }


#
# spice_models
open_pdk_spice_dir = open_pdk_tech_dir.joinpath("ngspice")
spice_pdk_files = ("design.ngspice", "sm141064.ngspice")
spice_models_all_lib = open_pdk_spice_dir.joinpath("all.spice")
spice_models_tgts = (
    *(open_pdk_spice_dir.joinpath(file) for file in spice_pdk_files),
    spice_models_all_lib,
)
def task_spice_models():
    "Copy and generate C4M version of the models"
    gf180mcu_pdk_spice_dir = gf180mcu_pdk_dir.joinpath("libs.tech", "ngspice")

    def write_all():
        with spice_models_all_lib.open("w") as f:
            f.write(dedent("""
                * All corners file
                .lib init
                .include "design.ngspice"
                .endl

                .lib typical
                .lib "sm141064.ngspice" typical
                .endl

                .lib ff
                .lib "sm141064.ngspice" ff
                .endl

                .lib ss
                .lib "sm141064.ngspice" ss
                .endl

                .lib fs
                .lib "sm141064.ngspice" fs
                .endl

                .lib sf
                .lib "sm141064.ngspice" sf
                .endl
            """[1:]))

    return {
        "file_dep": tuple(
            gf180mcu_pdk_spice_dir.joinpath(file) for file in spice_pdk_files
        ),
        "targets": spice_models_tgts,
        "actions": (
            (create_folder, (open_pdk_spice_dir,)),
            *(
                f"cp {str(gf180mcu_pdk_spice_dir.joinpath(file))}"
                f" {str(open_pdk_spice_dir.joinpath(file))}"
                for file in spice_pdk_files
            ),
            write_all,
        )
    }


#
# spice_models_python (copy inside python module)
python_models_dir = gf180mcu_local_dir.joinpath("models")
def _repl_dir(p: Path) -> Path:
    b = basename(str(p))
    return python_models_dir.joinpath(b)
python_models_srctgts = tuple(
    (file, _repl_dir(file))
    for file in spice_models_tgts
)
python_models_deps = tuple(scr for (scr, _) in python_models_srctgts)
python_models_tgts = tuple(tgt for (_, tgt) in python_models_srctgts)
def task_spice_models_python():
    """Copy SPICE models inside pdk module

    This way they can be used by pyspicefactory without needing separate
    PDK install"""
    return {
        "file_dep": python_models_deps,
        "targets": python_models_tgts,
        "actions": (
            (create_folder, (python_models_dir,)),
            *(
                f"cp {str(python_models_deps[n])} {str(python_models_tgts[n])}"
                for n in range(len(python_models_tgts))
            )
        )
    }


#
# spice
def task_spice():
    """Generate SPICE files"""

    spice_dirs = tuple(
        open_pdk_ref_dir.joinpath(lib, "spice") for lib in cell_list.keys()
    )
    spice_files = {}
    for lib, cells in cell_list.items():
        lib_spice_files = []
        lib_spice_files.append(open_pdk_ref_dir.joinpath(lib, "spice", f"{lib}.spi"))
        for cell in cells:
            lib_spice_files.append(open_pdk_ref_dir.joinpath(lib, "spice", f"{cell}.spi"))
            lib_spice_files.append(open_pdk_ref_dir.joinpath(lib, "spice", f"{cell}_hier.spi"))
        spice_files[lib] = lib_spice_files

    def gen_spice(libname):
        from pdkmaster.design import circuit as _ckt
        from c4m.pdk import gf180mcu
        # from doitlib import libs

        lib = None
        # for lib2 in libs.__libs__:
        for lib2 in gf180mcu.__libs__:
            if lib2.name == libname:
                lib = lib2
                break
        assert lib is not None

        lib_spice_dir = open_pdk_ref_dir.joinpath(lib.name, "spice")
        with lib_spice_dir.joinpath(f"{lib.name}.spi").open("w") as f_lib:
            f_lib.write(f"* {lib.name}\n")
            for cell in lib.cells:
                if cell.name == "Gallery":
                    continue
                # Write cell only to spice file
                pyspicesubckt = gf180mcu.pyspicefab.new_pyspicesubcircuit(
                    circuit=cell.circuit
                )
                s = f"* {cell.name}\n" + str(pyspicesubckt)
                f_lib.write("\n" + s)
                with lib_spice_dir.joinpath(f"{cell.name}.spi").open("w") as f_cell:
                    f_cell.write(s)

                # Write cell hierarchy to file; make order so that each cell is in
                # the file before is is being used.
                with lib_spice_dir.joinpath(f"{cell.name}_hier.spi").open("w") as f_cell:
                    todo = [cell]
                    seen = {cell}

                    s_cell = ""
                    while todo:
                        subblock = todo.pop(0)

                        pyspicesubckt = gf180mcu.pyspicefab.new_pyspicesubcircuit(
                            circuit=subblock.circuit, lvs=True,
                        )
                        s = f"* {subblock.name}\n"
                        s_ckt = str(pyspicesubckt)
                        s_ckt = s_ckt.replace("Ohm", "")
                        # s_ckt = s_ckt.replace("(", "[").replace(")", "]")
                        s += s_ckt
                        s_cell = s + s_cell

                        for inst in subblock.circuit.instances.__iter_type__(_ckt._CellInstance):
                            if inst.cell not in seen:
                                todo.append(inst.cell)
                                seen.add(inst.cell)

                    f_cell.write(f"* {cell.name}\n{s_cell}")


    for lib in cell_list.keys():
        yield {
            "name": lib,
            "doc": f"Creating spice files for library {lib}",
            "file_dep": (*c4m_pdk_gf180mcu_py_files, *lib_deps[lib], *pdkmaster_io_spice_deps),
            "targets": spice_files[lib],
            "actions": (
                *(
                    (create_folder, (dir_,)) for dir_ in spice_dirs
                ),
                (gen_spice, (lib,)),
            ),
        }


#
# VHDL/Verilog
def task_rtl():
    """Generate VHDL/verilog files"""
    langs = ("vhdl", "verilog")

    spice_init_file = tmp_dir.joinpath("rtl_init.spi")
    def rtl_spice_files():
        spice_file = "sm141064.ngspice"
        with spice_init_file.open("w") as f:
            f.write(dedent(f"""
                # RTL spice init
                .include "design.ngspice"
                .lib "{spice_file}" typical
            """[1:]))

        with open_pdk_spice_dir.joinpath(spice_file).open() as fin:
            with tmp_dir.joinpath(spice_file).open("w") as fout:
                for line in fin:
                    pat = "v\([^\)]*\)"
                    s = re.search(pat, line)
                    while s:
                        line = line[:s.start()] + "0.0" + line[s.end():]
                        s = re.search(pat, line)
                    fout.write(line)

    def rtl_targets(lib, lang):
        suffix = {
            "vhdl": "vhdl",
            "verilog": "v",
        }[lang]

        tgts = []
        cells = cell_list[lib]
        for cell in cells:
            if (lib == "IOLib") and not cell.startswith("IOPad"):
                continue
            tgts.append(open_pdk_ref_dir.joinpath(lib, lang, f"{cell}.{suffix}"))
        return tuple(tgts)

    def rtl_dirs(lang):
        return (tmp_dir, *(
            open_pdk_ref_dir.joinpath(lib, lang)
            for lib in cell_list.keys()
        ))

    def rtl_title(task):
        return (
            f"Creating {task.name[4:]} files" if avt_shell is not None
            else f"missing avt_shell; no {task.name[4:]} files created"
        )

    def rtl_script(lib, lang):
        avt_shell_script = dedent(f"""
            avt_config simToolModel hspice
            avt_config avtLibraryDirs "{tmp_dir}"
            avt_LoadFile "{str(spice_init_file)}" spice
            avt_config avtVddName "vdd:iovdd"
            avt_config avtVssName "vss:iovss"
            avt_config yagNoSupply "yes"
        """[1:])

        if lang == "verilog":
            avt_shell_script += dedent("""
                avt_config avtOutputBehaviorFormat "vlg"
                set map {spice verilog _hier.spi .v}
                set suffix v
                set comment "//"
            """[1:])
        elif lang == "vhdl":
            avt_shell_script += dedent("""
                avt_config avtOutputBehaviorFormat "vhd"
                set map {spice vhdl _hier.spi .vhdl}
                set suffix vhd
                set comment "--"
            """[1:])
        else:
            raise NotImplementedError(f"rtl lang {lang}")

        avt_shell_script += "foreach spice_file {\n"
        cells = cell_list[lib]
        for cell in cells:
            if cell == "Gallery":
                continue
            if (lib == "IOLib") and not cell.startswith("IOPad"):
                continue
            avt_shell_script += (
                f'    "{str(open_pdk_ref_dir.joinpath(lib, "spice", f"{cell}_hier.spi"))}"'
            ) + "\n"
        avt_shell_script += dedent("""
            } {
                avt_LoadFile $spice_file spice
                set rtl_file [string map $map $spice_file]
                set cell [string map {_hier.spi ""} [file tail $spice_file]]
                if {[string match "dff*" $cell]} {
                    inf_SetFigureName $cell
                    inf_MarkSignal dff_m "FLIPFLOP+MASTER"
                    inf_MarkSignal dff_s SLAVE
                }
                set out_file "$cell.$suffix"
                yagle $cell
                if [file exists $out_file] {
                    file copy -force $out_file $rtl_file
                } else {
                    set f [open $rtl_file w]
                    puts $f "$comment no model for $cell"
                }
            }
        """[1:])

        return avt_shell_script

    def rtl_override(lib, lang):
        """Override some of the verilog file with some hard coded ones.

        Needed as Yagle does not seem to understand the zero/one cell.
        """
        override_lang_dir = override_dir.joinpath(lib, lang)
        if override_lang_dir.exists():
            rtl_lang_dir = open_pdk_ref_dir.joinpath(lib, lang)
            os.system(f"cp {str(override_lang_dir)}/* {str(rtl_lang_dir)}")

    rtl_libs = tuple(filter(lambda l: l not in ("ExampleSRAMs", "MacroLib"), cell_list.keys()))
    yield {
        "name": "init",
        "doc": "initialize spice for RTL file generation",
        "task_dep": ("spice_models",),
        "targets": (spice_init_file,),
        "actions": (
            (create_folder, (tmp_dir,)),
            f"cp {open_pdk_spice_dir.joinpath('design.ngspice')} {tmp_dir}",
            rtl_spice_files,
        )
    }
    for lib in rtl_libs:
        docstrings = {
            "vhdl": f"Generate VHDL files for lib {lib}",
            "verilog": f"Generate Verilog files for lib {lib}",
        }
        for lang in langs:
            yield {
                "name": f"{lib}:{lang}",
                "doc": docstrings[lang],
                "title": rtl_title,
                "file_dep": (*c4m_pdk_gf180mcu_py_files, *lib_deps[lib], spice_init_file),
                "task_dep": (f"spice:{lib}", "spice_models"),
                "targets": rtl_targets(lib, lang),
                "actions": (
                    *(
                        (create_folder, (dir_,)) for dir_ in rtl_dirs(lang)
                    ),
                    AVTScriptAction(rtl_script(lib, lang)),
                    (rtl_override, (lib, lang))
                )
            }
        yield {
            "name": lib,
            "doc": f"Generate RTL files for lib {lib}",
            "task_dep": tuple(f"rtl:{lib}:{lang}" for lang in langs),
            "actions": None,
        }
    docstrings = {
        "vhdl": f"Generate VHDL files for all libs",
        "verilog": f"Generate Verilog files for all libs",
    }
    for lang in langs:
        yield {
            "name": lang,
            "doc": docstrings[lang],
            "task_dep": tuple(f"rtl:{lib}:{lang}" for lib in rtl_libs),
            "actions": None,
        }


#
# liberty
def task_liberty():
    """Generate liberty files"""

    liberty_libs = ("StdCell3V3Lib", "StdCell5V0Lib")
    liberty_spice_corners = {
        "nom": "typical", "fast": "ff", "slow": "ss",
    }

    spice_files = tuple(
        tmp_dir.joinpath(f"liberty_{corner}.spi")
        for corner in liberty_spice_corners.keys()
    )
    def liberty_spice_files():
        for libcorner, proccorner in liberty_spice_corners.items():
            with tmp_dir.joinpath(f"liberty_{libcorner}.spi").open("w") as f:
                f.write(dedent(f"""
                    * liberty init for {libcorner}
                    .include "design.ngspice"
                    .lib "sm141064.ngspice" {proccorner}
                """[1:]))

    def liberty_target(lib, corner):
        return open_pdk_ref_dir.joinpath(lib, "liberty", f"{lib}_{corner}.lib")

    def liberty_dir(lib):
        return open_pdk_ref_dir.joinpath(lib, "liberty")

    def liberty_title(task):
        lib, corner = task.name[8:].split("_")
        return (
            f"Creating liberty files for library {lib}, corner {corner}" if avt_shell is not None
            else "missing avt_shell; no liberty files created for library {lib}, corner {corner}"
        )

    def liberty_script(lib, corner):
        assert lib in liberty_libs, "Unsupported lib"

        avt_script = dedent("""
            avt_config simToolModel hspice
            avt_config avtVddName "vdd:iovdd"
            avt_config avtVssName "vss:iovss"
            avt_config tasBefig yes
            avt_config tmaDriveCapaout yes
            avt_config avtPowerCalculation yes
            avt_config simSlope 20e-12
        """[1:])

        if lib == "StdCell3V3Lib":
            if corner == "nom":
                avt_script += dedent(f"""
                    avt_config simPowerSupply 3.3
                    avt_config simTemperature 25
                """[1:])
            elif corner == "fast":
                avt_script += dedent(f"""
                    avt_config simPowerSupply 3.63
                    avt_config simTemperature -20
                """[1:])
            elif corner == "slow":
                avt_script += dedent(f"""
                    avt_config simPowerSupply 2.97
                    avt_config simTemperature 85
                """[1:])
            else:
                raise NotImplementedError(f"corner {corner}")
        elif lib == "StdCell5V0Lib":
            if corner == "nom":
                avt_script += dedent(f"""
                    avt_config simPowerSupply 5.0
                    avt_config simTemperature 25
                """[1:])
            elif corner == "fast":
                avt_script += dedent(f"""
                    avt_config simPowerSupply 5.5
                    avt_config simTemperature -20
                """[1:])
            elif corner == "slow":
                avt_script += dedent(f"""
                    avt_config simPowerSupply 4.5
                    avt_config simTemperature 85
                """[1:])
            else:
                raise NotImplementedError(f"corner {corner}")
        else:
            raise RuntimeError("Unsupport lib '{lib}'")

        init_spice_file = tmp_dir.joinpath(f"liberty_{corner}.spi")
        spice_file = open_pdk_ref_dir.joinpath(lib, "spice", f"{lib}.spi")
        avt_script += dedent(f"""
            avt_config avtLibraryDirs "{tmp_dir}"
            avt_LoadFile "{init_spice_file}" spice
            avt_config tmaLibraryName {lib}_{corner}
            avt_LoadFile {spice_file} spice

            foreach cell {{
        """[1:])
        avt_script += "".join(
            f"    {cell}\n"
            for cell in filter(
                lambda s: s != "Gallery",
                cell_list[lib],
            )
        )
        verilog_dir = open_pdk_ref_dir.joinpath(lib, "verilog")
        liberty_file_raw = open_pdk_ref_dir.joinpath(
            lib, "liberty", f"{lib}_{corner}_raw.lib",
        )
        avt_script += dedent(f"""
            }} {{
                set verilogfile {verilog_dir}/$cell.v

                if {{[string match "dff*" $cell]}} {{
                    # TODO: make these settings configurable
                    set beh_fig NULL
                    inf_SetFigureName $cell
                    inf_MarkSignal dff_m "MASTER"
                    inf_MarkSignal dff_s "FLIPFLOP+SLAVE"
                    create_clock -period 3000 clk
                }} elseif {{[string match "*latch*" $cell]}} {{
                    set beh_fig NULL
                }} else {{
                    set beh_fig [avt_LoadBehavior $verilogfile verilog]
                }}
                set tma_fig [tma_abstract [hitas $cell] $beh_fig]

                lappend tma_list $tma_fig
                lappend beh_list $beh_fig
            }}

            lib_drivefile $tma_list $beh_list "{liberty_file_raw}" max
        """[1:])

        return avt_script

    def fix_lib(lib, corner):
        import re

        cell_pattern = re.compile(r'\s*cell\s*\((?P<cell>\w+)\)\s*\{')
        # area_pattern = re.compile(r'(?P<area>\s*area\s*:\s*)\d+.\d+\s*;')
        qpin_pattern = re.compile(r'\s*pin\s*\(q\)\s*\{')
        clkpin_pattern = re.compile(r'\s*pin\s*\(clk\)\s*\{')

        liberty_file_raw = open_pdk_ref_dir.joinpath(
            lib, "liberty", f"{lib}_{corner}_raw.lib",
        )
        tgt = liberty_target(lib, corner)
        with liberty_file_raw.open("r") as fin:
            with tgt.open("w") as fout:
                is_flipflop = False
                for line in fin:

                    # In current one/zero cells output pins are wrongly seen as inout
                    # TODO: Check if we can fix that during HiTAS/Yagle run
                    line = line.replace("direction : inout", "direction : output")

                    m = cell_pattern.match(line)
                    if m:
                        cell = m.group("cell")
                        is_flipflop = cell.startswith("dff")
                        has_reset = cell.startswith("dffnr")
                        if is_flipflop:
                            fout.write(line)
                            fout.write('        ff (IQ,IQN) {\n')
                            fout.write('            next_state : "i" ;\n')
                            fout.write('            clocked_on : "clk" ;\n')
                            if has_reset:
                                fout.write('            clear : "nrst\'" ;\n')
                            fout.write('        }\n')
                            continue
                    elif is_flipflop:
                        m = qpin_pattern.match(line)
                        if m:
                            fout.write(line)
                            fout.write('            function : "IQ" ;\n')
                            continue

                        m = clkpin_pattern.match(line)
                        if m:
                            fout.write(line)
                            fout.write('            clock : true ;\n')
                            continue

                    fout.write(line)

    yield {
        "name": "init",
        "doc": "Initialize spice files for liberty generation",
        "task_dep": ("rtl:init",),
        "targets": spice_files,
        "actions": (
            liberty_spice_files,
        )
    }
    for lib in liberty_libs:
        for corner in ("nom", "fast", "slow"):
            spice_corner = liberty_spice_corners[corner]
            tmp = tmp_dir.joinpath(f"{lib}_{corner}")
            yield {
                "name": f"{lib}_{corner}",
                "doc": f"Generate liberty file for {lib}; {corner} corner",
                "title": liberty_title,
                "file_dep": (*c4m_pdk_gf180mcu_py_files, *lib_deps[lib]),
                "task_dep": (
                    f"spice:{lib}", f"rtl:{lib}:verilog",
                    "liberty:init",
                    # f"spice_models:logic_{spice_corner}",
                    # f"spice_models:io_{spice_corner}",
                    # f"spice_models:diode_{spice_corner}",
                ),
                "targets": (liberty_target(lib, corner),),
                "actions": (
                    (create_folder, (liberty_dir(lib),)),
                    (create_folder, (tmp,)),
                    AVTScriptAction(liberty_script(lib, corner), tmp=tmp),
                    (fix_lib, (lib, corner)),
                ),
            }


#
# klayout
klayout_dir = open_pdk_tech_dir.joinpath("klayout")
klayout_tech_dir = klayout_dir.joinpath("tech", "C4M.gf180mcu")
klayout_bin_dir = klayout_dir.joinpath("bin")
klayout_lvs_script = klayout_bin_dir.joinpath("lvs_gf180mcu")
klayout_drc_script = klayout_bin_dir.joinpath("drc_gf180mcu")
def task_klayout():
    """Generate klayout files"""

    klayout_drc_dir = klayout_tech_dir.joinpath("drc")
    klayout_lvs_dir = klayout_tech_dir.joinpath("lvs")
    klayout_share_dir = klayout_dir.joinpath("share")

    klayout_lyt_file = klayout_tech_dir.joinpath("C4M.gf180mcu.lyt")
    klayout_drc_lydrc_file = klayout_drc_dir.joinpath("DRC.lydrc")
    klayout_extract_lylvs_file = klayout_lvs_dir.joinpath("Extract.lylvs")
    klayout_drc_file = klayout_share_dir.joinpath("gf180mcu.drc")
    klayout_extract_file = klayout_share_dir.joinpath("gf180mcu_extract.lvs")
    klayout_extract_script = klayout_bin_dir.joinpath("extract_gf180mcu")
    klayout_lvs_file = klayout_share_dir.joinpath("gf180mcu.lvs")

    def gen_klayout():
        from pdkmaster.io.klayout import FileExporter
        from c4m.pdk import gf180mcu
        from xml.etree.ElementTree import ElementTree

        expo = FileExporter(
            tech=gf180mcu.tech, gds_layers=gf180mcu.gds_layers,
            export_name=f"C4M.{gf180mcu.tech.name}",
            prims_spiceparams=gf180mcu.prims_spiceparams,
        )()

        # DRC
        with klayout_drc_file.open("w") as f:
            f.write(expo["drc"])
        with klayout_drc_script.open("w") as f:
            relfile = relpath(klayout_drc_file, klayout_bin_dir)
            f.write(dedent(f"""
                #!/bin/sh
                d=`dirname $0`
                deck=`realpath $d/{relfile}`

                if [ $# -ne 2 ]
                then
                    echo "Usage `basename $0` input report"
                    exit 20
                fi

                export SOURCE_FILE=$1 REPORT_FILE=$2
                klayout -b -r ${{deck}}
            """[1:]))
        klayout_drc_script.chmod(0o755)

        # Extract
        with klayout_extract_file.open("w") as f:
            f.write(expo["extract"])
        with klayout_extract_script.open("w") as f:
            relfile = relpath(klayout_extract_file, klayout_bin_dir)
            f.write(dedent(f"""
                #!/bin/sh
                d=`dirname $0`
                deck=`realpath $d/{relfile}`

                if [ $# -ne 2 ]
                then
                    echo "Usage `basename $0` input spice_out"
                    exit 20
                fi

                export SOURCE_FILE=$1 SPICE_FILE=$2
                klayout -b -r ${{deck}}
            """[1:]))
        klayout_extract_script.chmod(0o755)

        # LVS
        with klayout_lvs_file.open("w") as f:
            f.write(expo["lvs"])
        with klayout_lvs_script.open("w") as f:
            relfile = relpath(klayout_lvs_file, klayout_bin_dir)
            f.write(dedent(f"""
                #!/bin/sh
                d=`dirname $0`
                deck=`realpath $d/{relfile}`

                if [ $# -ne 3 ]
                then
                    echo "Usage `basename $0` gds spice report"
                    exit 20
                fi

                export SOURCE_FILE=`realpath $1` SPICE_FILE=`realpath $2` REPORT_FILE=$3
                klayout -b -r ${{deck}}
            """[1:]))
        klayout_lvs_script.chmod(0o755)

        # klayout technology
        et = ElementTree(expo["ly_drc"])
        et.write(klayout_drc_lydrc_file, encoding="utf-8", xml_declaration=True)
        et = ElementTree(expo["ly_extract"])
        et.write(klayout_extract_lylvs_file, encoding="utf-8", xml_declaration=True)
        et = ElementTree(expo["ly_tech"])
        et.write(klayout_lyt_file, encoding="utf-8", xml_declaration=True)

    return {
        "title": lambda _: "Creating klayout files",
        "file_dep": (*c4m_pdk_gf180mcu_py_files, *pdkmaster_deps),
        "targets": (
            klayout_lyt_file, klayout_drc_lydrc_file, klayout_extract_lylvs_file,
            klayout_drc_file, klayout_drc_script, klayout_extract_file,
            klayout_extract_script, klayout_lvs_file, klayout_lvs_script,
        ),
        "actions": (
            (create_folder, (klayout_share_dir,)),
            (create_folder, (klayout_bin_dir,)),
            (create_folder, (klayout_drc_dir,)),
            (create_folder, (klayout_lvs_dir,)),
            gen_klayout,
        ),
    }


#
# coriolis
def task_coriolis():
    """Generate coriolis support files"""

    coriolis_dir = open_pdk_tech_dir.joinpath("coriolis")
    corio_dir = coriolis_dir.joinpath("techno", "etc", "coriolis2")
    corio_node180_dir = corio_dir.joinpath("node180")
    corio_gf180mcu_dir = corio_node180_dir.joinpath("gf180mcu")

    corio_nda_init_file = corio_dir.joinpath("__init__.py")
    corio_node130_init_file = corio_node180_dir.joinpath("__init__.py")
    corio_gf180mcu_init_file = corio_gf180mcu_dir.joinpath("__init__.py")
    corio_gf180mcu_techno_file = corio_gf180mcu_dir.joinpath("techno.py")
    corio_gf180mcu_lib_files = tuple(
        corio_gf180mcu_dir.joinpath(f"{lib}.py") for lib in cell_list.keys()
    )

    def gen_init():
        from c4m.pdk import gf180mcu
        # from doitlib import libs

        with corio_gf180mcu_init_file.open("w") as f:
            print("from .techno import *", file=f)
            # for lib in libs.__libs__:
            for lib in gf180mcu.__libs__:
                print(f"from .{lib.name} import setup as {lib.name}_setup", file=f)

            print(
                "\n__lib_setups__ = [{}]".format(
                    # ",".join(f"{lib.name}.setup" for lib in libs.__libs__)
                    ",".join(f"{lib.name}.setup" for lib in gf180mcu.__libs__)
                ),
                file=f,
            )

    def gen_coriolis():
        from pdkmaster.io import coriolis as _iocorio
        from c4m.flexcell import coriolis_export_spec
        from c4m.pdk import gf180mcu
        # from doitlib import libs

        expo = _iocorio.FileExporter(
            tech=gf180mcu.tech, gds_layers=gf180mcu.gds_layers, spec=coriolis_export_spec,
        )

        with corio_gf180mcu_techno_file.open("w") as f:
            f.write(dedent("""
                # Autogenerated file
                # SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
            """))
            f.write(expo())

        # for lib in libs.__libs__:
        for lib in gf180mcu.__libs__:
            with corio_gf180mcu_dir.joinpath(f"{lib.name}.py").open("w") as f:
                f.write(expo(lib))

    return {
        "title": lambda _: "Creating coriolis files",
        "file_dep": (
            *c4m_pdk_gf180mcu_py_files,
            *pdkmaster_deps, *flexcell_deps, #*flexio_deps, *flexmem_deps,
        ),
        "targets": (
            corio_nda_init_file, corio_node130_init_file, corio_gf180mcu_init_file,
            corio_gf180mcu_techno_file, *corio_gf180mcu_lib_files,
        ),
        "actions": (
            (create_folder, (corio_gf180mcu_dir,)),
            corio_nda_init_file.touch, corio_node130_init_file.touch,
            gen_init, gen_coriolis,
        ),
    }


#
# release
def task_tarball():
    """Create a tarball"""
    from datetime import datetime

    tarballs_dir = top_dir.joinpath("tarballs")
    t = datetime.now()
    tarball = tarballs_dir.joinpath(f'{t.strftime("%Y%m%d_%H%M")}_c4m_pdk_gf180mcu.tgz')

    return {
        "title": lambda _: "Create release tarball",
        "task_dep": (
            "coriolis", "klayout", "spice_models", "spice", "gds", "rtl", "liberty",
        ),
        "targets": (tarball,),
        "actions": (
            (create_folder, (tarballs_dir,)),
            f"cd {str(top_dir)}; tar czf {str(tarball)} open_pdk",
        )
    }
def task_tarball_nodep():
    """Create a tarball from existing open_pdk"""
    from datetime import datetime

    tarballs_dir = top_dir.joinpath("tarballs")
    t = datetime.now()
    tarball = tarballs_dir.joinpath(f'{t.strftime("%Y%m%d_%H%M")}_nd_c4m_pdk_gf180mcu.tgz')

    return {
        "title": lambda _: "Create release tarball",
        "targets": (tarball,),
        "actions": (
            (create_folder, (tarballs_dir,)),
            f"cd {str(top_dir)}; tar czf {str(tarball)} open_pdk",
        )
    }


#
# drc
drc_dir = top_dir.joinpath("drc")
def task_drc():
    "Run drc checks"

    def lib_rep(lib, cells):
        with drc_dir.joinpath(f"{lib}.rep").open("w") as librep:
            for cell in cells:
                drcrep = drc_dir.joinpath(lib, f"{cell}.rep")
                with drcrep.open("r") as f:
                    # Each DRC error has an <item> section in the output XML
                    ok = not any(("<item>" in line for line in f))

                print(f"{cell}: {'OK' if ok else 'NOK'}", file=librep)

    for lib, cells in cell_list.items():
        # If there exist a Gallery cell then do only DRC on that cell by default
        if "Gallery" in cells:
            cells = ("Gallery",)

        yield {
            "name": f"{lib}",
            "doc": f"Assembling DRC results for lib",
            "file_dep": (*c4m_pdk_gf180mcu_py_files, *lib_deps[lib]),
            "task_dep": (
                *(f"drccells:{lib}:{cell}" for cell in cells),
                "klayout",
            ),
            "targets": (drc_dir.joinpath(f"{lib}.rep"),),
            "actions": (
                (lib_rep, (lib, cells)),
            )
        }
# suppor DRC for each separate cell if wanted
def task_drccells():
    """DRC check for each cell in each library"""
    def run_drc(lib, cell):
        gds_dir = open_pdk_ref_dir.joinpath(lib, "gds")

        drcrep = drc_dir.joinpath(lib, f"{cell}.rep")
        gdsfile = gds_dir.joinpath(f"{cell}.gds")

        try:
            CmdAction(
                f"{str(klayout_drc_script)} {str(gdsfile)} {str(drcrep)}",
            ).execute()
            with drcrep.open("r") as f:
                # Each DRC error has an <item> section in the output XML
                ok = not any(("<item>" in line for line in f))
        except:
            ok = False
        if not ok:
            print(f"DRC of {lib}/{cell} failed!", file=sys.stderr)

    for lib, cells in cell_list.items():
        for cell in cells:
            yield {
                "name": f"{lib}:{cell}",
                "doc": f"Running DRC check for lib {lib} cell {cell}",
                "file_dep": (*c4m_pdk_gf180mcu_py_files, *lib_deps[lib]),
                "task_dep": (f"gds:{lib}", "klayout"),
                "targets": (drc_dir.joinpath(lib, f"{cell}.rep"),),
                "actions": (
                    (create_folder, (drc_dir.joinpath(lib),)),
                    (run_drc, (lib, cell)),
                )
            }
