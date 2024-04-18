#!/usr/bin/env python3



import os
import sys
import argparse
import subprocess
from sys import argv as SYS_ARGV
from dataclasses import dataclass



@dataclass
class Validated_Arguments:
	starting_directory: str
	extensions_list: list[str]
	include_list: list[str]
	ignore_list: list[str]
	do_print_structure: bool
	do_protect_privacy: bool
	do_print: bool
	do_use_bat: bool
	do_use_color: bool
	script: str



if os.name == "nt":
	SPLITTER = "\\"
else:
	SPLITTER = "/"



def display_error(err_msg:"str"):

	if os.name != "nt":
		err_msg = f"\033[31m{err_msg}\033[0m"

	print(err_msg)
	exit(1)

	return None

	f"END {display_error}"



def parse_bracket_list(s:"str"):

	return s[1:-1].replace(" ", "").split(",") if s.startswith("[") and s.endswith("]") else []

	f"END {parse_bracket_list}"



def print_structure(directory:"str"):
	indent_level = 0
	for root, _, _ in os.walk(directory):

		indent_level = root[len(directory):].count(os.sep)
		indent = "\t" * indent_level

		print(f"{indent}+-- {os.path.basename(root)}/", flush=True)

	return None

	f"END {print_structure}"



def find_children_of_dir(s_dir:"str", extensions:"list[str]", includes:"list[str]", ignores:"list[str]") -> "list[str]":
	"""
	Find all the files in the starting_directory that have the extensions in the extensions_list or are in the
	include_list, while excluding those in the ignore_list.
	"""
	# Convert lists to sets for faster checks
	ignore_set = set(ignores)
	include_set = set(includes)
	extensions_tuple = tuple(extensions)  # Prepare a tuple of extensions
	found_items = []
	for root, dirs, files in os.walk(s_dir, topdown=True):

		# Modify dirs in-place to prevent os.walk from walking ignored directories
		dirs[:] = [d for d in dirs if os.path.join(root, d) not in ignore_set]

		for file in files:
			full_path = os.path.join(root, file)
			if full_path in ignore_set:
				continue
			if file.endswith(extensions_tuple) or full_path in include_set:
				found_items.append(full_path)

	return found_items
	f"END {find_children_of_dir}"



def use_bat_to_print(starting_directory, file_path, i, do_protect_privacy):
	# TODO: Add support for `do_protect_privacy` in this function.
	try:

		subprocess.run(["bat", "--paging=never", file_path])

	except Exception as e:

		display_error(f"Could not use bat: {e}")

	return None
	f"END {use_bat_to_print}"



def normal_print(starting_directory, item_path, i, do_protect_privacy):

	if os.path.isdir(item_path):
		return
	
	with open(item_path, "r") as f:
		if do_protect_privacy:
			item_path = item_path[len(starting_directory):]
		print(f"[{i}] '{item_path}': ```\n")
		print(f.read())
		print("\n```")
	
	return None
	f"END {normal_print}"



def just_print_paths(item_path:"str", i:"int", args:"Validated_Arguments") -> None:

	path = item_path

	if args.do_protect_privacy:
		path = "." + path[len(args.starting_directory):]
		assert os.path.exists(path)

	print(f"[{i}] '{path}'")

	f"END {just_print_paths}"



def validate_args(args):

	if not os.path.exists(args.starting_directory):
		err_msg = ""
		err_msg += f"[[routput.py]]: Invalid `starting_directory`: [{args.starting_directory}]\n"
		err_msg += "Directory does not exist."
		display_error(err_msg)

	starting_dir = os.path.abspath(args.starting_directory)
	extensions_list = [ext if ext.startswith('.') else f".{ext}" for ext in parse_bracket_list(args.extensions)]
	include_list = parse_bracket_list(args.also_include)
	ignore_list = parse_bracket_list(args.ignore)

	for i, item in enumerate(ignore_list):
		if item == "":
			ignore_list.pop(i)
			continue
		if not os.path.exists(item):
			display_error(f"[[routput.py]]: Invalid `ignore_list` item: [{item}]\nItem does not exist.")
		ignore_list[i] = os.path.abspath(item)

	for i, item in enumerate(include_list):
		if item == "":
			include_list.pop(i)
			continue
		if not os.path.exists(item):
			display_error(f"[[routput.py]]: Invalid `also_include` item: [{item}]\nItem does not exist.")
		include_list[i] = os.path.abspath(item)

	if args.script != "":
		file = args.script
		if not os.path.exists(file):
			display_error(f"[[routput.py]]: Invalid `script` item: [{file}]\nItem does not exist.")
		if not os.path.isabs(file):
			args.script = os.path.abspath(file)

	return Validated_Arguments(
		starting_directory= 	starting_dir,
		extensions_list= 	extensions_list,
		include_list= 		include_list,
		ignore_list= 		ignore_list,
		do_print_structure= 	args.do_print_structure,
		do_protect_privacy= 	args.do_protect_privacy,
		do_print= 		not args.no_print,
		do_use_bat= 		args.do_use_bat,
		do_use_color= 		args.do_colors,
		script= 		args.script 
	)

	f"END {validate_args}"



def main():

	desc = ""
	desc += "Find files based on their extensions, recursively from a starting directory.\n"
	appendix_a = ""
	appendix_a += "Appendix A: Three arguments are passed to your script: "
	appendix_a += "1) The path to the starting directory. "
	appendix_a += "2) The path to the file. "
	appendix_a += "3) The index of the file in the list of found files. "
	appendix_a += "Also note that if `-p` is used: "
	appendix_a += "1) the 2nd argument will be the relative path, and "
	appendix_a += "2) the 1st argument will be the exact string, `HIDDEN`. "
	appendix_a += "This means it is important to check the 1st argument to determine if the path is hidden. "
	parser = argparse.ArgumentParser(description=desc, epilog=" | ".join([
		appendix_a
	]))
	
	parser.add_argument(
		"-d",
		"--starting-directory", 
		type=str, 
		default=".",
		help="Directory to start the search from."
	)
	parser.add_argument(
		"-s",
		"--do-print-structure", 
		action="store_true",
		default=False,
		help="Print the directory structure."
	)
	parser.add_argument(
		"-e",
		"--extensions", 
		type=str,
		required=True,
		help="List of file extensions to search for, in the format [ext1,ext2,...]."
	)
	parser.add_argument(
		"-p",
		"--do-protect-privacy", 
		action="store_true",
		default=False,
		help="Anonymize the file paths to be relative to the starting directory."
	)
	parser.add_argument(
		"-a",
		"--also-include",
		type=str,
		default="[]",
		help="List of additional filenames to include, in the format [file1,file2,...]."
	)
	parser.add_argument(
		"-i",
		"--ignore",
		type=str,
		default="[]",
		help="List of filenames to ignore, in the format [file1,file2,dir1,dir2...]."
	)
	parser.add_argument(
		"-n",
		"--no-print",
		action="store_true",
		default=False,
		help="Don't print the files, just return them."
	)
	parser.add_argument(
		"-b",
		"--do-use-bat",
		action="store_true",
		default=False,
		help="Use `bat` utility for syntax highlighting."
	)
	parser.add_argument(
		"-c",
		"--do-colors",
		action="store_true",
		default=False,
		help="Use a different color for each file."
	)
	parser.add_argument(
		"--script",
		type=str,
		default="",
		help="Script to run on each file. SEE Appendix A."
	)
	
	if not len(SYS_ARGV) > 1:
		parser.print_help()
		exit(0)

	args = parser.parse_args()
	args = validate_args(args)

	if args.do_print_structure:
		print("Directory Structure:")
		print_structure(args.starting_directory)
	
	found_items = find_children_of_dir(
		args.starting_directory,
		args.extensions_list,
		args.include_list,
		args.ignore_list
	)
	
	for i, item_path in enumerate(found_items):
		if args.script != "":
			if args.do_protect_privacy:
				item_path = item_path[len(args.starting_directory):]
				args.starting_directory = "HIDDEN"
			subprocess.run([sys.executable, args.script,
				args.starting_directory, item_path, str(i)
			])
		else:
			if args.do_print:
				if args.do_use_bat:
					use_bat_to_print(args.starting_directory, item_path, i, args.do_protect_privacy)
				else:
					normal_print(args.starting_directory, item_path, i, args.do_protect_privacy)
			else:
				just_print_paths(item_path, i, args)

	return None
	f"END {main}"

