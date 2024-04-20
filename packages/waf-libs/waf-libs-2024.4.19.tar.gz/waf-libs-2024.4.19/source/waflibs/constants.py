"""
constants
"""

import os
import sys

PROGRAM_NAME = os.path.basename(sys.argv[0])

PERSONAL_DOMAINS = [
    "fawong.com",
    "hlx.tw",
    "waf.hk",
    "xilef.org",
    "xn--i8s3q.xn--j6w193g",
]
DEV_DOMAINS = [
    "gyx.io",
    "waf.sexy",
]
COMMUNITY_DOMAINS = [
    "fastandfungible.com",
    "kirinas.com",
    "seris-choice.com",
    "xn--ij2bx6jt8qgte.com",
    "xn--lckwg.net",
]
PUBLIC_DOMAINS = [
    "fantasticrealty.uk",
    "faw.gg",
    "orientelectronic.net",
    "waf.gg",
]
PROJECT_DOMAINS = [
    "mylists.cc",
    "mymovielist.org",
    "mytvlist.org",
]
ADMIN_DOMAINS = [
    "aatf.us",
]
ALL_DOMAINS = (
    PERSONAL_DOMAINS
    + DEV_DOMAINS
    + COMMUNITY_DOMAINS
    + PUBLIC_DOMAINS
    + ADMIN_DOMAINS
    + PROJECT_DOMAINS
)

IP_CIDRS = []
