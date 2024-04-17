# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
import os, sys, site, re, yaml
from os.path import basename, relpath
from pathlib import Path
from textwrap import dedent
from typing import List, Dict

from doit.action import CmdAction
from doit.tools import create_folder

import pdkmaster.technology, pdkmaster.design, pdkmaster.dispatch
import pdkmaster.io.spice, pdkmaster.io.klayout
import c4m, c4m.flexcell, c4m.flexio

### Config

default_tasks = [
    "gds", "spice", "liberty", "lef", "doc", "klayout", "coriolis",
]
DOIT_CONFIG = {
    "default_tasks": [
        "open_pdk", # added so 'doit clean' cleans up open_pdk directory
        *default_tasks,
    ],
}


### globals

def _first(it):
    return next(iter(it))

top_dir = Path(__file__).parent
os.environ["TOP_DIR"] = str(top_dir)

dist_dir = top_dir.joinpath("dist")

open_pdk_dir = top_dir.joinpath("open_pdk")
open_pdk_ihpsg13g2_dir = open_pdk_dir.joinpath("C4M.ihpsg13g2")
open_pdk_tech_dir = open_pdk_ihpsg13g2_dir.joinpath("libs.tech")
open_pdk_ref_dir = open_pdk_ihpsg13g2_dir.joinpath("libs.ref")
os.environ["OPEN_PDK_REF_DIR"] = str(open_pdk_ref_dir)
open_pdk_doc_dir = open_pdk_ihpsg13g2_dir.joinpath("libs.doc")

override_dir = top_dir.joinpath("override")

c4m_local_dir = top_dir.joinpath("c4m")
ihpsg13g2_local_dir = c4m_local_dir.joinpath("pdk", "ihpsg13g2")
c4m_inst_dir = Path(site.getsitepackages()[0]).joinpath("c4m")
ihpsg13g2_inst_dir = c4m_inst_dir.joinpath("pdk", "ihpsg13g2")
flexcell_inst_dir = Path(_first(c4m.flexcell.__path__))
flexio_inst_dir = Path(_first(c4m.flexio.__path__))

c4m_pdk_ihpsg13g2_deps = (
    *ihpsg13g2_local_dir.rglob("*.py"),
)
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
flexio_deps = (
    *Path(_first(c4m.flexio.__path__)).rglob("*.py"),
)

ihpsg13g2_pdk_dir = top_dir.joinpath("deps", "IHP-Open-PDK", "ihp-sg13g2")
os.environ["IHPSG13G2_PDK"] = str(ihpsg13g2_pdk_dir)

### cell list

cell_list_file = top_dir.joinpath("cell_list.yml")

def task_cell_list():
    """Regenerate cell list.

    This task is not run by default. It needs to be run manually when the cell list
    has been changed and then the updated file has to be commit to git.
    """
    def write_list():
        import yaml

        from c4m.pdk import ihpsg13g2
        # from doitlib import libs

        # Generate layout for all cells so that possible extra cell are generated
        for lib in ihpsg13g2.__libs__:
            print(lib.name)
            for cell in lib.cells:
                print(f"  {cell.name}")
                cell.layout

        cell_list = {
            lib.name: list(cell.name for cell in lib.cells)
            for lib in ihpsg13g2.__libs__
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

iolib_name = "sg13g2_io"
os.environ["IOLIB_NAME"] = iolib_name
lib_deps = {
    "StdCell1V2Lib": (*pdkmaster_deps, *flexcell_deps),
    "StdCell3V3Lib": (*pdkmaster_deps, *flexcell_deps),
    "StdCell1V2LambdaLib": (*pdkmaster_deps, *flexcell_deps),
    "StdCell3V3LambdaLib": (*pdkmaster_deps, *flexcell_deps),
    iolib_name: (*pdkmaster_deps, *flexcell_deps, *flexio_deps),
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

    script = top_dir.joinpath("scripts", "gen_gds.py")

    for libname in cell_list.keys():
        gds_file = open_pdk_ref_dir.joinpath(libname, "gds", f"{libname}.gds")
        yield {
            "name": libname,
            "doc": f"Creating gds files for {libname}",
            "file_dep": (
                *c4m_pdk_ihpsg13g2_deps, *lib_deps[libname], *pdkmaster_io_klayout_deps,
                script,
            ),
            "targets": (
                gds_file,
            ),
            "actions": (
                f'{script} "{libname}"',
                f'gzip -kf "{gds_file}"'
            ),
        }


#
# spice_models
open_pdk_spice_dir = open_pdk_tech_dir.joinpath("ngspice")
spice_pdk_files = (
    "sg13g2_moslv_mod.lib", "sg13g2_moslv_parm.lib", "sg13g2_moslv_stat.lib", "cornerMOSlv.lib",
    "sg13g2_moshv_mod.lib", "sg13g2_moshv_parm.lib", "sg13g2_moshv_stat.lib", "cornerMOShv.lib",
    "resistors_mod.lib", "resistors_parm.lib", "resistors_stat.lib", "cornerRES.lib",
    "diodes.lib",
)
spice_models_all_lib = open_pdk_spice_dir.joinpath("all.spice")
spice_models_tgts = (
    *(open_pdk_spice_dir.joinpath(file) for file in spice_pdk_files),
    spice_models_all_lib,
)
def task_spice_models():
    "Copy and generate C4M version of the models"
    ihpsg13g2_pdk_spice_dir = ihpsg13g2_pdk_dir.joinpath("libs.tech", "ngspice", "models")

    def write_all():
        with spice_models_all_lib.open("w") as f:
            f.write(dedent("""
                * All corners file

                * lvmos
                .lib lvmos_tt
                .lib "cornerMOSlv.lib" mos_tt
                .endl

                .lib lvmos_ff
                .lib "cornerMOSlv.lib" mos_ff
                .endl

                .lib lvmos_ss
                .lib "cornerMOSlv.lib" mos_ss
                .endl

                .lib lvmos_fs
                .lib "cornerMOSlv.lib" mos_fs
                .endl

                .lib lvmos_sf
                .lib "cornerMOSlv.lib" mos_sf
                .endl

                * hvmos
                .lib hvmos_tt
                .lib "cornerMOShv.lib" mos_tt
                .endl

                .lib hvmos_ff
                .lib "cornerMOShv.lib" mos_ff
                .endl

                .lib hvmos_ss
                .lib "cornerMOShv.lib" mos_ss
                .endl

                .lib hvmos_fs
                .lib "cornerMOShv.lib" mos_fs
                .endl

                .lib hvmos_sf
                .lib "cornerMOShv.lib" mos_sf
                .endl

                * resistors
                .lib res_typ
                .lib "cornerRES.lib" res_typ
                .endl

                * resistors
                .lib res_bcs
                .lib "cornerRES.lib" res_bcs
                .endl

                * resistors
                .lib res_wcs
                .lib "cornerRES.lib" res_wcs
                .endl

                * diodes
                .lib dio
                .include "diodes.lib"
                .endl
            """[1:]))

    return {
        "file_dep": tuple(
            ihpsg13g2_pdk_spice_dir.joinpath(file) for file in spice_pdk_files
        ),
        "targets": spice_models_tgts,
        "actions": (
            (create_folder, (open_pdk_spice_dir,)),
            *(
                f"cp {str(ihpsg13g2_pdk_spice_dir.joinpath(file))}"
                f" {str(open_pdk_spice_dir.joinpath(file))}"
                for file in spice_pdk_files
            ),
            write_all,
        )
    }


#
# spice_models_python (copy inside python module)
python_models_dir = ihpsg13g2_local_dir.joinpath("models")
def _repl_dir(p: Path) -> Path:
    b = basename(str(p))
    return python_models_dir.joinpath(b)
python_models_srctgts = tuple(
    (file, _repl_dir(file))
    for file in spice_models_tgts
)
python_models_init_file = python_models_dir.joinpath("__init__.py")
python_models_deps = tuple(scr for (scr, _) in python_models_srctgts)
python_models_tgts = tuple(tgt for (_, tgt) in python_models_srctgts)
def task_spice_models_python():
    """Copy SPICE models inside pdk module

    This way they can be used by pyspicefactory without needing separate
    PDK install"""
    def write_init():
        with python_models_init_file.open("w") as f:
            f.write(dedent("""
                # Autogenerated module
            """[1:]))

    return {
        "file_dep": python_models_deps,
        "targets": (*python_models_tgts, python_models_init_file),
        "actions": (
            (create_folder, (python_models_dir,)),
            write_init,
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

    script = top_dir.joinpath("scripts", "gen_spice.py")

    for libname in cell_list.keys():
        spice_file = open_pdk_ref_dir.joinpath(libname, "spice", f"{libname}.spi")
        yield {
            "name": libname,
            "doc": f"Creating spice files for library {libname}",
            "file_dep": (
                *c4m_pdk_ihpsg13g2_deps, *lib_deps[libname], *pdkmaster_io_spice_deps,
                script,
            ),
            "targets": (
                spice_file,
            ),
            "actions": (
                f"{script} {libname}",
            ),
        }


#
# liberty
def task_liberty():
    liberty_io_dir = open_pdk_ref_dir.joinpath(iolib_name, "liberty")
    liberty_io_file = liberty_io_dir.joinpath(f"{iolib_name}_dummy.lib")

    script = top_dir.joinpath("scripts", "gen_liberty.py")

    yield {
        "name": iolib_name,
        "doc": f"Creating liberty file for {iolib_name}",
        "file_dep": (*c4m_pdk_ihpsg13g2_deps, *lib_deps[iolib_name], script),
        "targets": (liberty_io_file,),
        "actions": (
            f"{script} {iolib_name}",
        )
    }


#
# LEF
def task_lef():
    """Generate LEF files"""
    # Currenlty only implemented ad-hoc for IO library

    lef_io_dir = open_pdk_ref_dir.joinpath(iolib_name, "lef")
    lef_io_file = lef_io_dir.joinpath(f"{iolib_name}.lef")
    lef_ionotrack_file = lef_io_dir.joinpath(f"{iolib_name}_notracks.lef")

    script = top_dir.joinpath("scripts", "gen_lef.py")

    yield {
        "name": iolib_name,
        "doc": f"Creating lef file for {iolib_name}",
        "file_dep": (*c4m_pdk_ihpsg13g2_deps, *lib_deps[iolib_name], script),
        "targets": (lef_io_file, lef_ionotrack_file),
        "actions": (
            f"{script} sg13g2_io",
        )
    }


#
# klayout
klayout_dir = open_pdk_tech_dir.joinpath("klayout")
klayout_tech_dir = klayout_dir.joinpath("tech", "C4M.ihpsg13g2")
klayout_bin_dir = klayout_dir.joinpath("bin")
klayout_lvs_script = klayout_bin_dir.joinpath("lvs_ihpsg13g2")
klayout_drc_script = klayout_bin_dir.joinpath("drc_ihpsg13g2")
def task_klayout():
    """Generate klayout files"""

    klayout_drc_dir = klayout_tech_dir.joinpath("drc")
    klayout_lvs_dir = klayout_tech_dir.joinpath("lvs")
    klayout_share_dir = klayout_dir.joinpath("share")

    klayout_lyt_file = klayout_tech_dir.joinpath("C4M.ihpsg13g2.lyt")
    klayout_drc_lydrc_file = klayout_drc_dir.joinpath("DRC.lydrc")
    klayout_extract_lylvs_file = klayout_lvs_dir.joinpath("Extract.lylvs")
    klayout_drc_file = klayout_share_dir.joinpath("ihpsg13g2.drc")
    klayout_extract_file = klayout_share_dir.joinpath("ihpsg13g2_extract.lvs")
    klayout_extract_script = klayout_bin_dir.joinpath("extract_ihpsg13g2")
    klayout_lvs_file = klayout_share_dir.joinpath("ihpsg13g2.lvs")

    def gen_klayout():
        from pdkmaster.io.klayout import FileExporter
        from c4m.pdk import ihpsg13g2
        from xml.etree.ElementTree import ElementTree

        expo = FileExporter(
            tech=ihpsg13g2.tech, gds_layers=ihpsg13g2.gds_layers,
            export_name=f"C4M.{ihpsg13g2.tech.name}",
            prims_spiceparams=ihpsg13g2.prims_spiceparams,
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
        "file_dep": (*c4m_pdk_ihpsg13g2_deps, *pdkmaster_deps),
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
    corio_node130_dir = corio_dir.joinpath("node130")
    corio_ihpsg13g2_dir = corio_node130_dir.joinpath("ihpsg13g2")

    corio_nda_init_file = corio_dir.joinpath("__init__.py")
    corio_node130_init_file = corio_node130_dir.joinpath("__init__.py")
    corio_ihpsg13g2_init_file = corio_ihpsg13g2_dir.joinpath("__init__.py")
    corio_ihpsg13g2_techno_file = corio_ihpsg13g2_dir.joinpath("techno.py")
    corio_ihpsg13g2_lib_files = tuple(
        corio_ihpsg13g2_dir.joinpath(f"{lib}.py") for lib in cell_list.keys()
    )

    def gen_init():
        from c4m.pdk import ihpsg13g2
        # from doitlib import libs

        with corio_ihpsg13g2_init_file.open("w") as f:
            print("from .techno import *", file=f)
            # for lib in libs.__libs__:
            for lib in ihpsg13g2.__libs__:
                print(f"from .{lib.name} import setup as {lib.name}_setup", file=f)

            print(
                "\n__lib_setups__ = [{}]".format(
                    # ",".join(f"{lib.name}.setup" for lib in libs.__libs__)
                    ",".join(f"{lib.name}.setup" for lib in ihpsg13g2.__libs__)
                ),
                file=f,
            )

    def gen_coriolis():
        from pdkmaster.io import coriolis as _iocorio
        from c4m.flexcell import coriolis_export_spec
        from c4m.pdk import ihpsg13g2
        # from doitlib import libs

        expo = _iocorio.FileExporter(
            tech=ihpsg13g2.tech, gds_layers=ihpsg13g2.gds_layers, spec=coriolis_export_spec,
        )

        with corio_ihpsg13g2_techno_file.open("w") as f:
            f.write(dedent("""
                # Autogenerated file
                # SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
            """))
            f.write(expo())

        # for lib in libs.__libs__:
        for lib in ihpsg13g2.__libs__:
            with corio_ihpsg13g2_dir.joinpath(f"{lib.name}.py").open("w") as f:
                f.write(expo(lib))

    return {
        "title": lambda _: "Creating coriolis files",
        "file_dep": (
            *c4m_pdk_ihpsg13g2_deps,
            *pdkmaster_deps, *flexcell_deps, *flexio_deps, #*flexmem_deps,
        ),
        "targets": (
            corio_nda_init_file, corio_node130_init_file, corio_ihpsg13g2_init_file,
            corio_ihpsg13g2_techno_file, *corio_ihpsg13g2_lib_files,
        ),
        "actions": (
            (create_folder, (corio_ihpsg13g2_dir,)),
            corio_nda_init_file.touch, corio_node130_init_file.touch,
            gen_init, gen_coriolis,
        ),
    }


#
# docs
sim_dir = top_dir.joinpath("sim")
iolib_doc_dir = open_pdk_ref_dir.joinpath(iolib_name, "doc")
def task_doc():
    """Generate the docs"""

    script = top_dir.joinpath("scripts", "gen_readme_iolib.py")
    readme_file = iolib_doc_dir.joinpath("README.md")

    yield {
        "name": "README",
        "doc": "Create README file",
        "file_dep": (script,),
        "targets": (
            readme_file,
        ),
        "actions": (
            f"{script} {readme_file}",
        )
    }

    drivestrength_sim_notebook = sim_dir.joinpath("SimOutDriveStrength.ipynb")
    drivestrength_sim_out_file = sim_dir.joinpath("SimOutDriveStrength.html")
    drivestrength_doc_file = iolib_doc_dir.joinpath("DriveStrengthSim.html")
    yield {
        "name": "DriveStrength",
        "doc": "Simulate and document output drive strength",
        "file_dep": (
            *c4m_pdk_ihpsg13g2_deps,
            drivestrength_sim_notebook,
        ),
        "targets": (
            drivestrength_doc_file,
        ),
        "actions": (
            (create_folder, (iolib_doc_dir,)),
            f"cd {str(sim_dir)}; jupyter nbconvert --to html --execute {str(drivestrength_sim_notebook)}",
            f"cp {str(drivestrength_sim_out_file)} {str(drivestrength_doc_file)}",
        ),
    }

    input_sim_notebook = sim_dir.joinpath("SimInputPerformance.ipynb")
    input_sim_out_file = sim_dir.joinpath("SimInputPerformance.html")
    input_doc_file = iolib_doc_dir.joinpath("InputPerformance.html")
    yield {
        "name": "InputPerformance",
        "doc": "Simulate and document input performance",
        "file_dep": (
            *c4m_pdk_ihpsg13g2_deps,
            input_sim_notebook,
        ),
        "targets": (
            input_doc_file,
        ),
        "actions": (
            (create_folder, (iolib_doc_dir,)),
            f"cd {str(sim_dir)}; jupyter nbconvert --to html --execute {str(input_sim_notebook)}",
            f"cp {str(input_sim_out_file)} {str(input_doc_file)}",
        ),
    }


#
# release
def task_tarball():
    """Create a tarball"""
    from datetime import datetime

    tarballs_dir = top_dir.joinpath("tarballs")
    t = datetime.now()
    tarball = tarballs_dir.joinpath(f'{t.strftime("%Y%m%d_%H%M")}_openpdk_c4m_ihpsg13g2.tgz')

    return {
        "title": lambda _: "Create release tarball",
        "task_dep": (
            *default_tasks,
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
    tarball = tarballs_dir.joinpath(f'{t.strftime("%Y%m%d_%H%M")}_nd_openpdk_c4m_ihpsg13g2.tgz')

    return {
        "title": lambda _: "Create release tarball",
        "targets": (tarball,),
        "actions": (
            (create_folder, (tarballs_dir,)),
            f"cd {str(top_dir)}; tar czf {str(tarball)} open_pdk",
        )
    }


#
# patch for upstream PDK
def task_patch4upstream():
    """Create a patch for the upstream PDK"""
    script = top_dir.joinpath("upstream", "mkpatch.sh")
    return {
        "title": lambda _: "Create patch for upstream",
        "file_dep": (
            script,
        ),
        "uptodate": [False], # Always rerun
        "task_dep": (
            *default_tasks,
        ),
        "actions": (
            str(script),
        )
    }
def task_patch4upstream_nodep():
    """Create a patch for the upstream PDK"""
    script = top_dir.joinpath("upstream", "mkpatch.sh")
    return {
        "title": lambda _: "Create patch for upstream",
        "file_dep": (
            script,
        ),
        "uptodate": [False], # Always rerun
        "actions": (
            str(script),
        )
    }


#
# drc
def task_drc():
    "Run drc checks"
    drc_dir = top_dir.joinpath("drc")

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

    def lib_rep(lib, cells):
        with drc_dir.joinpath(f"{lib}.rep").open("w") as librep:
            for cell in cells:
                drcrep = drc_dir.joinpath(lib, f"{cell}.rep")
                with drcrep.open("r") as f:
                    # Each DRC error has an <item> section in the output XML
                    ok = not any(("<item>" in line for line in f))

                print(f"{cell}: {'OK' if ok else 'NOK'}", file=librep)

    for lib, cells in cell_list.items():
        drc_lib_dir = drc_dir.joinpath(lib)
        for cell in cells:
            yield {
                "name": f"{lib}:{cell}",
                "doc": f"Running DRC check for lib {lib} cell {cell}",
                "task_dep": (f"gds:{lib}", "klayout"),
                "targets": (drc_dir.joinpath(lib, f"{cell}.rep"),),
                "actions": (
                    (create_folder, (drc_lib_dir,)),
                    (run_drc, (lib, cell)),
                ),
            }

        # If there exist a Gallery cell then do only DRC on that cell by default
        if "Gallery" in cells:
            cells = ("Gallery",)

        yield {
            "name": f"{lib}",
            "doc": f"Assembling DRC results for lib",
            "task_dep": (
                *(f"drc:{lib}:{cell}" for cell in cells),
                "klayout",
            ),
            "targets": (drc_dir.joinpath(f"{lib}.rep"),),
            "actions": (
                (lib_rep, (lib, cells)),
            ),
            "clean": (f"rm -fr {str(drc_lib_dir)}",),
        }
