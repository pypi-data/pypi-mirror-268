# vim: ts=8 sw=8 noexpandtab
#
#   CRC code generator
#
#   Copyright (c) 2019-2023 Michael Büsch <m@bues.ch>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from libcrcgen import CrcGen, CrcGenError, CRC_PARAMETERS, poly2int, int2poly

import sys
import argparse

__all__ = [
	"main",
]

def poly_convert(p, nr_crc_bits, shift_right):
	if nr_crc_bits is None:
		raise CrcGenError("-B|--nr-crc-bits is required for -T|--polynomial-convert")
	p = p.strip()
	try:
		# Hex format
		if not p.startswith("0x"):
			raise ValueError
		p = int(p[2:], 16)
		p = int2poly(p, nr_crc_bits, shift_right)
		print(p)
		return 0
	except ValueError:
		pass
	try:
		# Decimal format
		p = int(p, 10)
		p = int2poly(p, nr_crc_bits, shift_right)
		print(p)
		return 0
	except ValueError:
		pass
	try:
		# Polynomial coefficient format
		p = poly2int(p, nr_crc_bits, shift_right)
		print(f"0x{p:X}")
		return 0
	except ValueError:
		pass
	raise CrcGenError("-T|--polynomial-convert: Invalid polynomial")

def main():
	try:
		def argInt(string):
			if string.startswith("0x"):
				return int(string[2:], 16)
			return int(string)
		p = argparse.ArgumentParser(
			description="CRC algorithm HDL code generator (VHDL, Verilog, MyHDL)"
		)
		g = p.add_mutually_exclusive_group(required=True)
		g.add_argument("-v", "--verilog-function", action="store_true",
			       help="Generate Verilog function")
		g.add_argument("-m", "--verilog-module", action="store_true",
			       help="Generate Verilog module")
		g.add_argument("-V", "--vhdl", action="store_true",
			       help="Generate VHDL module")
		g.add_argument("-M", "--myhdl", action="store_true",
			       help="Generate MyHDL block")
		g.add_argument("-p", "--python", action="store_true",
			       help="Generate Python code (mainly useful for testing purposes)")
		g.add_argument("-c", "--c", action="store_true",
			       help="Generate C code (mainly useful for testing purposes)")
		g.add_argument("-T", "--polynomial-convert", metavar="POLYNOMIAL", type=str,
			       help="Convert a polynomial from string to int or vice versa and then exit.")
		g.add_argument("--test", action="store_true",
			       help=argparse.SUPPRESS)
		p.add_argument("-a", "--algorithm", type=str,
			       choices=CRC_PARAMETERS.keys(), default="CRC-32",
			       help="Select the CRC algorithm. "
				    "Individual algorithm parameters (e.g. polynomial) can be overridden with the options below.")
		p.add_argument("-P", "--polynomial", type=str,
			       help="Use this CRC polynomial for code generation")
		p.add_argument("-B", "--nr-crc-bits", type=argInt,
			       help="Number of CRC bits.")
		p.add_argument("-b", "--nr-data-bits", type=argInt, default="8",
			       help="Number of input data word bits.")
		g = p.add_mutually_exclusive_group()
		g.add_argument("-R", "--shift-right", action="store_true",
			       help="CRC algorithm shift direction: right shift")
		g.add_argument("-L", "--shift-left", action="store_true",
			       help="CRC algorithm shift direction: left shift")
		p.add_argument("-n", "--name", type=str, default="crc",
			       help="Generated function/module name")
		p.add_argument("-D", "--data-param", type=str, default="data",
			       help="Generated function/module data parameter name")
		p.add_argument("-C", "--crc-in-param", type=str, default="crcIn",
			       help="Generated function/module crc input parameter name")
		p.add_argument("-o", "--crc-out-param", type=str, default="crcOut",
			       help="Generated module crc output parameter name")
		p.add_argument("-S", "--static", action="store_true",
			       help="Generate static C function. (only if -c)")
		p.add_argument("-I", "--inline", action="store_true",
			       help="Generate inline C function. (only if -c)")
		p.add_argument("-O", "--optimize", type=argInt, default=CrcGen.OPT_ALL,
			       help=f"Select individual algorithm optimizer steps. "
				    f"The argument to the -O option can be any sum of the following integers: "
				    f"-O{CrcGen.OPT_FLATTEN} (Flatten the bit operation tree), "
				    f"-O{CrcGen.OPT_ELIMINATE} (Eliminate redundant operations), "
				    f"-O{CrcGen.OPT_LEX} (Sort the operands in lexicographical order where possible). "
				    f"-O{CrcGen.OPT_NONE} disables all optimizer steps. "
				    f"If this option is not given, then by default all optimizer steps are enabled (-O{CrcGen.OPT_ALL}).")
		args = p.parse_args()

		if (args.nr_crc_bits is not None and
		    args.nr_crc_bits < 1):
			raise CrcGenError("Invalid -B|--nr-crc-bits argument.")
		if args.nr_data_bits < 1:
			raise CrcGenError("Invalid -b|--nr-data-bits argument.")

		if args.polynomial_convert is not None:
			return poly_convert(args.polynomial_convert,
					    args.nr_crc_bits,
					    args.shift_right)

		crcParameters = CRC_PARAMETERS[args.algorithm].copy()
		if args.nr_crc_bits is not None:
			crcParameters["nrBits"] = args.nr_crc_bits
		if args.shift_right:
			crcParameters["shiftRight"] = True
		if args.shift_left:
			crcParameters["shiftRight"] = False
		if args.polynomial is not None:
			crcParameters["polynomial"] = poly2int(
				args.polynomial,
				crcParameters["nrBits"],
				crcParameters["shiftRight"])

		polynomial = crcParameters["polynomial"]
		nrCrcBits = crcParameters["nrBits"]
		shiftRight = crcParameters["shiftRight"]

		if polynomial > ((1 << nrCrcBits) - 1):
			raise CrcGenError(f"Invalid polynomial. "
					  f"It is bigger than the CRC width "
					  f"of (2**{nrCrcBits})-1.")

		if args.test:
			from libcrcgen.generator_test import CrcGenTest
			CrcGenClass = CrcGenTest
		else:
			CrcGenClass = CrcGen

		gen = CrcGenClass(P=polynomial,
				  nrCrcBits=nrCrcBits,
				  nrDataBits=args.nr_data_bits,
				  shiftRight=shiftRight,
				  optimize=args.optimize)
		if args.test:
			gen.runTests()
		else:
			if args.python:
				print(gen.genPython(funcName=args.name,
						    crcVarName=args.crc_in_param,
						    dataVarName=args.data_param))
			elif args.verilog_function:
				print(gen.genVerilog(genFunction=True,
						     name=args.name,
						     inDataName=args.data_param,
						     inCrcName=args.crc_in_param,
						     outCrcName=args.crc_out_param))
			elif args.verilog_module:
				print(gen.genVerilog(genFunction=False,
						     name=args.name,
						     inDataName=args.data_param,
						     inCrcName=args.crc_in_param,
						     outCrcName=args.crc_out_param))
			elif args.vhdl:
				print(gen.genVHDL(name=args.name,
						  inDataName=args.data_param,
						  inCrcName=args.crc_in_param,
						  outCrcName=args.crc_out_param))
			elif args.myhdl:
				print(gen.genMyHDL(blockName=args.name,
						   inDataName=args.data_param,
						   inCrcName=args.crc_in_param,
						   outCrcName=args.crc_out_param))
			elif args.c:
				print(gen.genC(funcName=args.name,
					       crcVarName=args.crc_in_param,
					       dataVarName=args.data_param,
					       static=args.static,
					       inline=args.inline))
			else:
				assert False
		return 0
	except CrcGenError as e:
		print("ERROR: " + str(e), file=sys.stderr)
	return 1
