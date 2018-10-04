# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.audit import AuditClient

MODULE_TO_TYPE_MAPPINGS["audit"] = oci.audit.models.audit_type_mapping
CLIENT_MAP["audit"] = AuditClient