#!/usr/bin/env python3
from gwtc.gwtc_gracedb import GWTCGraceDB
from .gwtc import catalog_delta
import logging
from optparse import OptionParser


def parse_command_line():
    parser = OptionParser(usage="usage: %prog [options] version1 version2")
    parser.add_option(
        "--number",
        type="string",
        default="4",
        help='Set the catalog number: default "4"',
    )
    parser.add_option(
        "--proxy-path", type="string", help="Set the path to find the proxy file"
    )
    parser.add_option(
        "--service-url",
        type="string",
        default="https://gracedb-test.ligo.org/api/",
        help="Set the gracedb service url. Default: https://gracedb-test.ligo.org/api/",
    )
    options, versions = parser.parse_args()
    if len(versions) == 2:
        return options, int(versions[0]), int(versions[1])
    elif len(versions) == 0:
        return options, None, None
    else:
        raise ValueError(
            "Either provide two versions to compare or nothing to show the latest difference"
        )


def main():
    options, v1, v2 = parse_command_line()

    # setup verbose logs
    logging.basicConfig(level=logging.INFO)

    client = GWTCGraceDB(service_url=options.service_url, cred=options.proxy_path)

    logging.info(f"Calculating catalog diff from versions {v1} to {v2}")
    newsid, delsid, changedsid, diffstr = catalog_delta(
        client, v1, v2, number=options.number
    )
    logging.info(diffstr)
