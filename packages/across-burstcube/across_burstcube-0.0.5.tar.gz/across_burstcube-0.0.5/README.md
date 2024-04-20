# ACROSS API Python BurstCubeTOO Client

# Introduction
This is the Python API for the Astrophysics Cross-Observatory Science Support
(ACROSS), a NASA initiative to provide cross-observatory support for
time-domain and multi-messenger (TDAMM) coordination and observation planning.

The client provides support for accessing the BurstCube TOO interface that
ACROSS provides.

# Installation

To install the client, enter the command `pip install across-burstcube`.

The `across_client` module should now be available for use.

# Usage

The relevant classes are:

`BurstCubeTOO`

Main interface for submitting, updating, fetching and deleting BurstCube TOO
requests.

`BurstCubeTriggerInfo`

Class that provides extended information on the triggering event, this is an
parameter for `BurstCubeTOO`.

`BurstCubeTOORequests`

Allows to fetch multiple `BurstCubeTOO` entries using various filter criteria.

Note that submission of BurstCubeTOO requests requires an API Token, which will
be supplied by ACROSS.
