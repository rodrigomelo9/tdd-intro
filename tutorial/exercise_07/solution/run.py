# Import Python modules
from vunit import VUnit
from os.path import join, dirname

# Setup Python test runner project from command line arguments
prj = VUnit.from_argv()

# Set the root to the directory of this script file
root = dirname(__file__)

# Add VHDL libraries to project
common_lib = prj.add_library("common_lib")
tb_lib = prj.add_library("tb_lib")

# Add all VHDL files to libraries
common_lib.add_source_files(join(root, "..", "..", "common", "src", "*.vhd"))
tb_lib.add_source_files(join(root, "test", "*.vhd"))

# Add-ons
prj.add_verification_components()
prj.add_osvvm()

# Set simulator specific compile options
prj.set_compile_option("rivierapro.vcom_flags", ["-dbg"])

# Run VUnit
prj.main()