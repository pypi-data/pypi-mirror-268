"""Command line API."""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import List

import perun
from perun.configuration import config, read_custom_config, read_environ, save_to_config
from perun.core import Perun
from perun.io.io import IOFormat
from perun.monitoring.application import Application
from perun.util import printableSensorConfiguration

log = logging.getLogger("perun")


def _get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="perun",
        description="Distributed performance and energy monitoring tool",
        allow_abbrev=False,
    )
    parser.add_argument("-c", "--configuration", default="./.perun.ini")
    parser.add_argument(
        "-l", "--log_lvl", choices=["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]
    )
    parser.add_argument(
        "--version", action="version", version=f"perun {perun.__version__}"
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    # showconf
    showconf_parser = subparsers.add_parser(
        "showconf", help="Print perun configuration in INI format."
    )
    showconf_parser.add_argument(
        "--default",
        action="store_true",
        help="Print the default configuration",
        dest="showconf_default",
    )
    showconf_parser.set_defaults(func=showconf)

    # sensors
    sensor_parser = subparsers.add_parser(
        "sensors", help="Print available sensors by host and rank."
    )
    sensor_parser.set_defaults(func=sensors)

    # metadata
    metadata_parser = subparsers.add_parser(
        "metadata", help="Print available metadata."
    )
    metadata_parser.set_defaults(func=metadata)

    # export
    export_parser = subparsers.add_parser(
        "export", help="Export existing output file to another format."
    )
    export_parser.add_argument(
        "-i", "--id", dest="run_id", help="Run id to export, last one by default"
    )
    export_parser.add_argument(
        "input_file",
        help="Existing perun output file. Should be hdf5, json or pickle.",
    )
    export_parser.add_argument(
        "format",
        help="Desired data output format.",
    )
    export_parser.set_defaults(func=export)

    # monitor
    monitor_parser = subparsers.add_parser(
        "monitor",
        help="""
    Gather power consumption from hardware devices while SCRIPT [SCRIPT_ARGS] is running.

    SCRIPT is a path to the python script to monitor, run with arguments SCRIPT_ARGS.
    """,
    )
    monitor_parser.add_argument(
        "-n",
        "--app_name",
        dest="app_name",
        help="Name o the monitored application. The name is used to distinguish between multiple application in the same directory. If left empty, the file name will be used.",
    )
    monitor_parser.add_argument(
        "-i",
        "--run_id",
        dest="run_id",
        help="Unique id of the latest run of the application. If left empty, perun will use the current date.",
    )
    monitor_parser.add_argument(
        "-f",
        "--format",
        help="Secondary report format.",
        choices=[format.value for format in IOFormat],
    )
    monitor_parser.add_argument(
        "--data_out",
        help="Directory where output files are saved. Defaults to ./perun_results",
    )
    monitor_parser.add_argument(
        "--sampling_rate",
        type=float,
        help="Sampling rate in seconds. Defaults to 1 second.",
    )
    monitor_parser.add_argument(
        "--power_overhead",
        type=float,
        help="Estimated power consumption of non-measured hardware components in Watts. Will be added to measured power consumption on the text report summary. Defaults to 0 Watts",
    )
    monitor_parser.add_argument(
        "--pue", type=float, help="Data center Power Usage Effectiveness. Defaults to 1"
    )
    monitor_parser.add_argument(
        "--price_factor",
        type=float,
        help="Electricity to Currency convertion factor in the form of Currency/kWh. Defaults to 0.3251 €/kWh",
    )
    monitor_parser.add_argument(
        "--price_unit",
        type=str,
        help="Currency character to use on the text report summary. Defaults to €",
    )
    monitor_parser.add_argument(
        "--emission_factor",
        type=float,
        help="Average carbon intensity of electricity (gCO2e/kWh). Defaults to 417.80 gC02e/kWh",
    )
    monitor_parser.add_argument(
        "--rounds", type=int, help="Number of warmup rounds to run app. Defaults to 1"
    )
    monitor_parser.add_argument(
        "--warmup_rounds",
        type=int,
        help="Number of warmup rounds to run the app. A warmup round is a full run of the application without gathering performance data. Defaults to 0",
    )
    monitor_parser.add_argument(
        "-b",
        "--binary",
        action="store_true",
        help="Indicate if the monitored application is a binary. Otherwise treat it as a python script.",
    )
    monitor_parser.add_argument("cmd", type=str)
    monitor_parser.add_argument("cmd_args", nargs=argparse.REMAINDER)
    monitor_parser.set_defaults(func=monitor)
    return parser


def cli():
    """Command line entrypoint."""
    parser = _get_arg_parser()

    # parse and read conf file and env
    args, remaining = parser.parse_known_args()

    if args.subcommand is None:
        parser.print_help()
        return

    # 1) Read custom configuration
    if args.configuration:
        read_custom_config(args.configuration)

    # 2) Read environment variables
    read_environ()

    # 3) Parse remaining arguments
    for key, value in vars(args).items():
        if value:
            save_to_config(key, value)

    # set logging
    log.setLevel(config.get("debug", "log_lvl"))

    # start function
    if hasattr(args, "func"):
        args.func(args)


def showconf(args: argparse.Namespace):
    """Print current perun configuration in INI format."""
    from perun.configuration import _default_config

    if args.showconf_default:
        config.read_dict(_default_config)
        config.write(sys.stdout)
    else:
        config.write(sys.stdout)


def sensors(args: argparse.Namespace):
    """Print sensors assigned to each rank by perun."""
    perun = Perun(config)
    log.debug(f"Rank {perun.comm.Get_rank()}: Sensors initialized perun object")
    sensor_config = perun.sensors_config
    host_rank = perun.host_rank
    log.debug(f"Rank {perun.comm.Get_rank()}: Sensors gather global configuration")
    if perun.comm.Get_rank() == 0:
        printableConfig = printableSensorConfiguration(sensor_config, host_rank)
        print(printableConfig)


def metadata(args: argparse.Namespace):
    """Print global metadata dictionaries in json format."""
    perun = Perun(config)

    hostMD = perun.l_host_metadata
    hostMD["backends"] = perun.l_backend_metadata
    allHostsMD = perun.comm.gather(hostMD, root=0)

    if perun.comm.Get_rank() == 0 and allHostsMD:
        metadataDict = {}
        for host, assignedRanks in perun.host_rank.items():
            metadataDict[host] = allHostsMD[assignedRanks[0]]

        json.dump(metadataDict, sys.stdout, indent=4)


def export(args: argparse.Namespace):
    """Export existing perun output file to another format."""
    in_file = Path(args.input_file)
    if not in_file.exists():
        log.error("File does not exist.")
        return -1

    perun = Perun(config)

    out_path = in_file.parent
    inputFormat = IOFormat.fromSuffix(in_file.suffix)
    out_format = IOFormat(args.format)

    dataNode = perun.import_from(in_file, inputFormat)
    if args.run_id:
        perun.export_to(out_path, dataNode, out_format, args.run_id)
    else:
        perun.export_to(out_path, dataNode, out_format)


def monitor(args: argparse.Namespace):
    """
    Gather power consumption from hardware devices while SCRIPT [SCRIPT_ARGS] is running.

    SCRIPT is a path to the python script to monitor, run with arguments SCRIPT_ARGS.
    """
    cmd: str = args.cmd
    log.debug(f"Cmd: {cmd}")
    argIndex = sys.argv.index(args.cmd)
    sys.argv = sys.argv[argIndex:]
    cmd_args: List[str] = sys.argv.copy()
    log.debug(f"Cmd args: { cmd_args }")
    if not args.binary:
        scriptPath = Path(cmd)
        assert scriptPath.exists()
        assert scriptPath.is_file()
        assert scriptPath.suffix == ".py"

        sys.path.insert(0, str(scriptPath.parent.absolute()))
        app = Application(scriptPath, config, args=tuple(sys.argv[1:]))
    else:
        app = Application(cmd, config, is_binary=True, args=tuple(sys.argv[1:]))

    perun = Perun(config)

    perun.monitor_application(app)
