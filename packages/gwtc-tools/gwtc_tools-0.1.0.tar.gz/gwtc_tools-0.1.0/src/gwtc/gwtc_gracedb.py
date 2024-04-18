#!/usr/bin/env python3
from ligo.gracedb.rest import GraceDb
import json
import logging

# setup verbose logs
logging.basicConfig(level=logging.INFO)


class GWTCGraceDB(GraceDb):
    """
    This candidate GraceDb client adds:
      1) a method for creating a new catalog
      2) a method for listing existing catalogs and versions
    """

    def gwtc_create(self, smap, number, comment=None):
        """Create a new GWTC entry.

        User must be a member of the catalog_managers group to create
        a gwtc entry.

        Args:
           smap (str | dict): path to a json-formatted file containing a catalog
               entry or a dictionary. An example of the format is below:
                   {
                     "S231002i": {
                         "pipelines": {
                             "MBTA": "G419572",
                             "spiir": "G419571",
                             "pycbc": "G419570",
                             "gstlal": "G419569"
                         },
                         "far": null,
                         "pastro": null
                     },
                     "S231002h": {
                         "pipelines": {
                             "MBTA": "G419568",
                             "spiir": "G419567",
                             "pycbc": "G419566",
                             "gstlal": "G419565"
                         },
                         "far": 1.8432234e-10,
                         "pastro": {
                             "BBH": 2.5953132292424023e-28,
                             "BNS": 0.9922100906247882,
                             "NSBH": 4.260287692039069e-29,
                             "Terrestrial": 0.007789909375211845
                         }
                     },
                     "S231002g": {
                         "pipelines": {
                             "MBTA": "G419564",
                             "spiir": "G419563",
                             "pycbc": "G419562",
                             "gstlal": "G419561"
                         },
                         "far": 3.23421e-23,
                         "pastro": null
                      }
                   }
               Note that superevent_id's and graceid's in the smap file must
               correspond to superevents and events on the live server.

               far values can be a number, or null

               pastro values must be a valid dict, or null

           number (str): identifying number of the catalog. Currently a slug.
               Example: number={'4', '4a', '4a'-1', etc}.

           comment (str, optional): an analyst comment to accompany the smap upload

        Returns:
            :class:`requests.models.Response`

        Raises:
            ligo.gracedb.exceptions.HTTPError: if the response has a status
                code >= 400.

        """

        # First open the smap file:

        if isinstance(smap, str):
            json_file = open(smap)
            smap_json = json.load(json_file)
            json_file.close()
        elif isinstance(smap, dict):
            smap_json = smap
        else:
            raise ValueError(
                "smap must be a string indicating a json filename or a dictionary"
            )

        # Verify that the number is a string. The server will verify that it's a
        # valid slug.
        if not isinstance(number, str):
            raise ValueError(f'"number" must be a str, not {type(number)}')

        # Construct the request uri:
        try:
            uri = str(self.links["gwtc"])
        except KeyError:
            raise NotImplementedError(
                f"gwtc functionality is not yet live on {self._service_url}"
            )

        json_request = {"number": number, "smap": smap_json, "comment": comment}

        return self.post(uri, json=json_request)

    def gwtc_get(self, number=None, version=None):
        """
        Retrieve a specific gwtc catalog based on number and version

        Args:
            number (str): identifying number of the catalog.

            version (int or str('latest')): positive integer version number of the
                catalog to retrieve. Entering 'latest' will pull the most recently
                uploaded version.

        Returns:
            :class:`requests.models.Response`

            A HTTPresponse with an individual catalog entry, if a specific version
            was specified.


        Note: version cannot be specified without specifying number.
        """

        # Try and construct the request URL to determine if gwtc is active
        # on the server.
        try:
            uri = str(self.templates["gwtc-version-detail"])
        except KeyError:
            raise NotImplementedError(
                f"gwtc functionality is not yet live on {self._service_url}"
            )

        # Verify 'number' and construct request URL.
        if number:
            if not isinstance(number, str):
                raise ValueError(f"number must be a str, not {type(number)}")
            elif version or version == 0:  # if the user has specified 'version'
                if (
                    (isinstance(version, int) and version <= 0)
                    or (isinstance(version, str) and version.lower() != "latest")
                    or (not isinstance(version, int) and not isinstance(version, str))
                ):
                    raise ValueError("version must be a positive integer or 'latest'")
                else:
                    uri = str(self.templates["gwtc-version-detail"]).format(
                        number=number, version=version
                    )
                    r = self.get(uri)
                    return r
            else:
                raise ValueError(
                    "both a number and a version must be supplied to " "gwtc_get"
                )

    def gwtc_list(self, number=None):
        """
        Retrieve an iterator of gwtc catalog dictionaries

        Args:
            number (str): identifying number of the catalog.

        Returns:
            :obj:`Iterator[dict]`

            An iterator which yields individual catalog dictionaries

        Note: not specifying a catalog number will retrieve an iterator with all
              available catalogs.

        """

        if number:
            if not isinstance(number, str):
                raise ValueError(f"number must be a str, not {type(number)}")
            else:
                uri = str(self.templates["gwtc-number-list"]).format(number=number)
        else:
            uri = str(self.links["gwtc"])

        # iterate over the results:
        while uri:
            response = self.get(uri).json()
            catalogs = response.get("results")
            uri = response.get("next")

            for catalog in catalogs:
                yield catalog

    def gwtc_numbers(self):
        """Return the unique catalog numbers

        Returns
        =======
        list
            The list of all unique catalog numbers (e.g. 4 for GWTC-4, etc)"""

        # Construct the request uri:
        try:
            uri = str(self.links["gwtc"])
        except KeyError:
            raise NotImplementedError(
                f"gwtc functionality is not yet live on {self._service_url}"
            )

        # Get the dictionary of catalog entries:
        catalog_dict = self.get(uri).json()

        # Construct a list of catalog numbers:
        catalog_numbers = [cat["number"] for cat in catalog_dict["results"]]

        # Return a unique list:
        return list(set(catalog_numbers))

    def gwtc_versions(self, number="4"):
        """Return the unique catalog versions

        Parameters
        ==========
        number : int, optional
            The GWTC number to act on, 4 for now

        Returns
        =======
        list
            The list of unique catalog versions for this catalog number
        """

        # Verify that the number is a string. The server will verify that it's a
        # valid slug.
        if not isinstance(number, str):
            raise ValueError(f'"number" must be a str, not {type(number)}')

        # Construct the request uri:
        try:
            uri = str(self.templates["gwtc-number-list"])
        except KeyError:
            raise NotImplementedError(
                f"gwtc functionality is not yet live on {self._service_url}"
            )

        # Get the dictionary of catalog number versions:
        versions_dict = self.get(uri.format(number=number)).json()

        # Construct and return a list of version numbers:
        return [cat["version"] for cat in versions_dict["results"]]
