#!/usr/bin/env python3
# import fake_gracedb
from gwtc.gwtc_gracedb import GWTCGraceDB

# import sqlite3
import logging
import json
import requests

from typing import Dict, Tuple

# setup verbose logs
logging.basicConfig(level=logging.INFO)

#
# Utility functions to define catalogs directly from useful gracedb queries. These are mostly for demos
#


def update_far_and_pastro_in_smap(gdb: GWTCGraceDB, smap: Dict) -> Dict:
    """
    Parameters
    ==========
    gdb : `gwtc.gwtc_gracedb.GWTCGraceDB`
        A rest API GraceDB instance modified for GWTC support
    smap : dict
        e.g.,

        "S230824d": {
            "pipelines": {
                "gstlal": "G651775"
            },
            "far": null,
            "pastro": null
        },
        "S230522a": {
            "pipelines": {
                "gstlal": "G651776"
            },
            "far": null,
            "pastro": null
        },
        "S230513ar": {
            "pipelines": {
                "gstlal": "G651774"
            },
            "far": null,
            "pastro": null
        }

    Returns
    =======
    dict :
        updated smap with fars and pastros computed from min FAR and min P
        terrestrial across pipelines, e.g.,

        "S230824d": {
            "pipelines": {
                "gstlal": "G651775"
            },
            "far": 1.611950746698324e-13,
            "pastro": null
        },
        "S230522a": {
            "pipelines": {
                "gstlal": "G651776"
            },
            "far": 3.171756306943489e-16,
            "pastro": {
                "BBH": 1.0,
                "BNS": 0.0,
                "NSBH": 0.0,
                "Terrestrial": 0.0
            }
        },
        "S230513ar": {
            "pipelines": {
                "gstlal": "G651774"
            },
            "far": 2.016192919429939e-07,
            "pastro": null
        }
    """
    smap = smap.copy()
    for se, d in smap.items():
        fars = []
        pastros = []
        for p, g in d["pipelines"].items():
            fars.append(gdb.event(g).json()["far"])
            pastro_files = [
                k for k, f in gdb.files(g).json().items() if k.endswith("p_astro.json")
            ]
            if len(pastro_files) > 0:
                assert len(pastro_files) == 1
                r = gdb.files(g, pastro_files[0])
                pastros.append(r.json())
        if len(fars) > 0:
            d["far"] = min(fars)
        if len(pastros) > 0:
            d["pastro"] = sorted(pastros, key=lambda d: d["Terrestrial"])[0]
    return smap


def smap_from_gracedb_query(
    gdb: GWTCGraceDB,
    query: str,
) -> Dict:
    """For each superevent satisfying query conditions,
    produce a map from s-name to g-event data for online pipeline preferred events

    Parameters
    ==========
    gdb : `gwtc.gwtc_gracedb.GWTCGraceDB`
        A rest API GraceDB instance modified for GWTC support
    query : string, required
        Gracedb query to extract super events

    Returns
    =======
    dict :
        A dictionary with s-events as keys,
        and values of dictionaries, e.g.,

        "S230824d": {
            "pipelines": {
                "gstlal": "G651775"
            },
            "far": 1.611950746698324e-13,
            "pastro": null
        },
        "S230522a": {
            "pipelines": {
                "gstlal": "G651776"
            },
            "far": 3.171756306943489e-16,
            "pastro": {
                "BBH": 1.0,
                "BNS": 0.0,
                "NSBH": 0.0,
                "Terrestrial": 0.0
            }
        },
        "S230513ar": {
            "pipelines": {
                "gstlal": "G651774"
            },
            "far": 2.016192919429939e-07,
            "pastro": null
        }
    """
    logging.info(f"Querying gracedb with query: {query}")
    smap = {}
    for se in gdb.superevents(query=query):
        smap[se["superevent_id"]] = {
            "pipelines": {
                pipeline: data["graceid"]
                for pipeline, data in se["pipeline_preferred_events"].items()
            },
            "far": None,
            "pastro": None,
        }
    logging.info("found the following event map:\n" + json.dumps(smap, indent=4))
    smap = update_far_and_pastro_in_smap(gdb, smap)
    return smap


def _diff(smap1, smap2):
    # calculate the differences and similarities in super event ids
    newsid = set(smap2) - set(smap1)
    delsid = set(smap1) - set(smap2)
    sameid = set(smap2) & set(smap1)
    changedsid = set()
    for sid in sameid:
        assert set(smap2[sid]) == set(smap1[sid])
        g1 = set(smap1[sid]["pipelines"].values()) | set((smap1[sid]["far"],))
        if smap1[sid]["pastro"]:
            g1 |= set(smap1[sid]["pastro"].items())
        g2 = set(smap2[sid]["pipelines"].values()) | set((smap2[sid]["far"],))
        if smap2[sid]["pastro"]:
            g2 |= set(smap2[sid]["pastro"].items())
        if g1 != g2:
            changedsid.add(sid)
    return newsid, delsid, sameid, changedsid


def catalog_delta(
    gdb: GWTCGraceDB, v1: int = None, v2: int = None, number: str = "4"
) -> Tuple[set, set, set, str]:
    """Highlight changes between v2 and v1 of catalog

    Parameters
    ==========
    gdb : `gwtc.gwtc_gracedb.GWTCGraceDB`
        A rest API GraceDB instance modified for GWTC support
    v1 : int
        The version number of the base catalog for comparison
    v2 : int
        The version number of the updated catalog for comparison
    number : str, optional
        The GWTC number ("4" for the time being)

    Returns
    =======
    set
        The set of newly added superevents sids
    set
        The set of removed superevent sids
    set
        The set of superevent sids which have had their contents updated
    str
        The human readable summary of the changes
    """
    if v1 is not None and v2 is not None:
        smap1 = gdb.gwtc_get(number, v1).json()["gwtc_superevents"]
        smap2 = gdb.gwtc_get(number, v2).json()["gwtc_superevents"]
    elif v1 is None and v2 is None:
        smap2 = gdb.gwtc_get(number, "latest").json()
        v2 = smap2["version"]
        smap2 = smap2["gwtc_superevents"]
        v1 = v2 - 1
        smap1 = gdb.gwtc_get(number, v1).json()["gwtc_superevents"]
    else:
        raise ValueError("v1 and v2 must both be integers or both be None")
    newsid, delsid, sameid, changedsid = _diff(smap1, smap2)

    outstr = """
- new s events in version %d: %s
- deleted s events in version %d: %s
- changed s events in version %d:
""" % (
        v2,
        sorted(newsid),
        v2,
        sorted(delsid),
        v2,
    )
    for sid in changedsid:
        outstr += f"\n\t{sid}:\n"
        for pipeline in set(smap1[sid]) | set(smap2[sid]):
            g1 = None if pipeline not in smap1[sid] else smap1[sid][pipeline]
            g2 = None if pipeline not in smap2[sid] else smap2[sid][pipeline]
            if g1 != g2:
                outstr += f"\t\t{pipeline}: {g1} -> {g2}\n"
    return newsid, delsid, changedsid, outstr


def gwtc_update_pipeline_events(
    gdb: GWTCGraceDB, pmap: dict, pipeline: str, number: str = "4", reset: bool = False
) -> requests.models.Response:
    """Update GWTC "number" for "pipeline" with provided changes

    Parameters
    ==========
    gdb : `gwtc.gwtc_gracedb.GWTCGraceDB`
        A rest API GraceDB instance modified for GWTC support
    pmap : dict
        The pipeline map to perform the update with, of the form, e.g.,

        "S230824d": {
            "pipelines": {
                "gstlal": "G651775"
            },
            "far": 1.611950746698324e-13,
            "pastro": null
        },
        "S230522a": {
            "pipelines": {
                "gstlal": "G651776"
            },
            "far": 3.171756306943489e-16,
            "pastro": {
                "BBH": 1.0,
                "BNS": 0.0,
                "NSBH": 0.0,
                "Terrestrial": 0.0
            }
        },
        "S230513ar": {
            "pipelines": {
                "gstlal": "G651774"
            },
            "far": 2.016192919429939e-07,
            "pastro": null
        }

    pipeline : str
        The pipeline for which to perform the update
    number : int, optional
        The GWTC number (4 for the time being)
    reset : bool
        If "reset" is provided, superevents
        that exist in the catalog but not in the pmap provided will have their gevents
        for "pipeline" removed. If a superevent has no pipelines left, it is deleted.

    Returns
    =======
    :class:`requests.models.Response`
    """
    # Sanity check that only pipeline events are provided and that they exist in
    # gracedb with the correct pipeline
    for s, d in pmap.items():
        assert set(d["pipelines"]) == set((pipeline,))
        gid = d["pipelines"][pipeline]
        assert gdb.event(gid).json()["pipeline"] == pipeline

    # get the current catalog
    try:
        smap = gdb.gwtc_get(number, "latest")
        smap = smap.json()["gwtc_superevents"]
    except requests.exceptions.HTTPError as e:
        logging.warn(
            "Couldn't retrieve previous version of catalog. Setting to empty dictionary. %s"
            % e
        )
        smap = {}

    new_sids, delete_sids, _, update_sids = _diff(smap, pmap)

    # add new super events that were not there previously
    for sid in new_sids:
        smap[sid] = pmap[sid]
    # update sids that are in both
    for sid in update_sids:
        smap[sid]["pipelines"].update(pmap[sid]["pipelines"])
    if reset:
        # delete pipeline gevents from superevents not in the provided map
        for sid in delete_sids:
            if pipeline in smap[sid]["pipelines"]:
                del smap[sid]["pipelines"][pipeline]
            # delete super events that no longer have any pipelines
            if len(smap[sid]["pipelines"]) == 0:
                del smap[sid]

    update_far_and_pastro_in_smap(gdb, smap)
    return gdb.gwtc_create(smap, number=number)
