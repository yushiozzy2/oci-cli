# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
IGNORED_COMMANDS = [
    ['setup', 'autocomplete'],
    ['setup', 'bootstrap'],
    ['setup', 'config'],
    ['setup', 'instance-principal'],
    ['setup', 'keys'],
    ['setup', 'repair-file-permissions'],
    ['setup', 'oci-cli-rc'],
    ['raw-request'],
    ['session', 'authenticate'],
    ['session', 'export'],
    ['session', 'import'],
    ['session', 'refresh'],
    ['session', 'terminate'],
    ['session', 'validate'],
    ['artifacts', 'container', 'image-signature', 'sign-upload'],
    ['artifacts', 'container', 'image-signature', 'get-verify'],
    # Note this is being added b/c python sdk doesn't generate models
    # for top level enums.
    # This means that the --generate-full-command-json-input will not work
    # for these commands.
    ['cims', 'incident', 'create'],
    ['cims', 'incident', 'update'],
    # DTS commands
    ['dts', 'nfs-dataset', 'activate'],
    ['dts', 'nfs-dataset', 'create'],
    ['dts', 'nfs-dataset', 'deactivate'],
    ['dts', 'nfs-dataset', 'delete'],
    ['dts', 'nfs-dataset', 'get-seal-manifest'],
    ['dts', 'nfs-dataset', 'list'],
    ['dts', 'nfs-dataset', 'reopen'],
    ['dts', 'nfs-dataset', 'seal'],
    ['dts', 'nfs-dataset', 'seal-status'],
    ['dts', 'nfs-dataset', 'set-export'],
    ['dts', 'nfs-dataset', 'show'],
    ['dts', 'physical-appliance', 'list'],
    ['dts', 'physical-appliance', 'show'],
    ['dts', 'physical-appliance', 'unregister'],
    ['dts', 'physical-appliance', 'configure-encryption'],
    ['dts', 'physical-appliance', 'finalize'],
    ['dts', 'physical-appliance', 'initialize-authentication'],
    ['dts', 'physical-appliance', 'unlock'],
    ['dts', 'appliance', 'setup-notifications'],
    ['dts', 'job', 'verify-upload-user-credentials'],
    ['dts', 'job', 'setup-notifications'],
    ['dts', 'export', 'configure-physical-appliance'],
    ['dts', 'export', 'generate-manifest'],
    ['dts', 'export', 'request-appliance'],
    ['dts', 'export', 'create-policy'],
    ['dts', 'export', 'setup-notifications'],
    # TODO: fix this: (was commented out for DEXREQ-825)
    ['ce', 'node-pool', 'create'],
    ['ce', 'cluster', 'generate-token'],
    ['dts', 'appliance', 'show-entitlement'],
    ['os', 'replication', 'list-replication-sources'],
    ['os', 'replication', 'list-replication-policies'],
    ['os', 'replication', 'get-replication-policy'],
    ['os', 'replication', 'delete-replication-policy'],
    ['os', 'replication', 'create-replication-policy'],
    ['os', 'bucket', 'make-bucket-writable'],
    ['os', 'object', 'copy'],
    ['os', 'object', 'copy-part'],
    ['os', 'object', 'head'],
    ['os', 'object', 'merge-object-metadata'],
    ['os', 'object', 'replace-object-metadata'],
    ['os', 'retention-rule', 'update'],
    ['data-flow', 'application', 'create'],
    ['data-flow', 'application', 'update'],
    ['data-flow', 'run', 'create'],
    ['data-flow', 'run', 'submit'],
    # input requires a valid file to upload
    ['data-science', 'model', 'create-model-artifact'],
    ['data-science', 'job', 'create-job-artifact'],
    ['data-science', 'pipeline', 'create-step-artifact'],
    # this command expects either subnetId or vlanId optional param, therefore, cannot be tested here
    # removing it from here and adding coverage in test_compute_cli_extended.py
    ['compute', 'instance', 'attach-vnic'],
    # added to ignore as JSON can be produced
    ['ce', 'node-pool', 'update'],
    ['db', 'system', 'launch'],
    ['db', 'system', 'update'],
    ['db', 'pluggable-database', 'convert-to-regular'],
    ['db', 'pluggable-database', 'refresh'],
    ['lb', 'load-balancer', 'create'],
    ['network', 'private-endpoint', 'enable-reverse-connections'],
    ['os', 'object', 'reencrypt'],
    ['dns', 'resolver', 'update'],
    ['log-analytics', 'parser', 'list-parser-functions'],
    ['log-analytics', 'parser', 'list-parser-meta-plugins'],
    ['log-analytics', 'source', 'list-meta-source-types'],
    ['log-analytics', 'source', 'list-source-functions'],
    ['log-analytics', 'source', 'list-source-label-operators'],
    ['instance-agent', 'pluginconfig', 'plugin', 'list-instanceagent-available'],
    ['data-integration', 'task-validation', 'create-from-pipeline-task'],
    ['data-integration', 'task', 'update-pipeline-task'],
    ['data-integration', 'task', 'create-pipeline-task'],
    ['data-integration', 'task', 'create-task-from-rest-task'],
    ['dns', 'resolver', 'update'],
    # this command expects either src-dir or dest-dir as param, so this can't be tested here
    ['os', 'object', 'sync'],
    ['resource-manager', 'stack', 'copy'],
    ['log-analytics', 'upload', 'upload-log-file'],
    ['log-analytics', 'upload', 'upload-log-events-file'],
    ['database-migration', 'agent', 'update'],
    ['database-migration', 'connection', 'create'],
    ['database-migration', 'connection', 'update'],
    ['artifacts', 'generic', 'artifact', 'upload-by-path'],
    ['data-integration', 'task', 'update-task-from-rest-task'],
    ['os-management', 'work-request-summary'],
    ['resource-manager', 'job', 'create-plan-job'],
    ['resource-manager', 'job', 'create-apply-job'],
    ['resource-manager', 'job', 'create-destroy-job'],
    ['setup', 'find-installations'],
    ['iam', 'db-token', 'get'],
    ['data-connectivity', 'data-entity', 'create-entity-shape'],
    ['data-connectivity', 'endpoint', 'list'],
    ['data-connectivity', 'full-push-down-task-response', 'create-full-push-down-task'],
    ['data-connectivity', 'registry', 'list'],
    ['mysql', 'db-system', 'import'],
    ['devops', 'deploy-environment', 'update-oke-cluster-environment'],
    ['db', 'backup', 'list'],
    ['speech', 'transcription-job', 'create'],
    ['opsi', 'opsi-data-objects', 'query-data-templatized-query'],
    ['opsi', 'opsi-data-objects', 'get'],
    ['opsi', 'opsi-data-objects', 'list'],
    ['db', 'cloud-vm-cluster', 'create'],
    ['db', 'cloud-vm-cluster', 'update'],
    ['opsi', 'host-insights', 'list'],
    ['compute', 'instance', 'action'],
    ['oma', 'lockboxes', 'list'],
    ['media-services', 'media-asset-distribution-channel-attachment-collection'],
    ['media-services', 'media-workflow-configuration-collection'],
    ['db', 'autonomous-database', 'delete'],
    ['resource-manager', 'stack', 'create-from-template'],
    ['data-science', 'notebook-session', 'create'],
    ['data-science', 'notebook-session', 'update'],
    ['devops', 'build-pipeline-stage', 'create-build-stage'],
    ['devops', 'build-pipeline-stage', 'update-build-stage'],
    ['apm-synthetics', 'monitor', 'create-scripted-rest-monitor'],
    ['apm-synthetics', 'monitor', 'update-scripted-rest-monitor'],
    ['apm-synthetics', 'monitor', 'create-scripted-browser-monitor'],
    ['apm-synthetics', 'monitor', 'update-scripted-browser-monitor'],
    ['apm-synthetics', 'monitor', 'create-browser-monitor'],
    ['apm-synthetics', 'monitor', 'update-browser-monitor'],
    ['apm-synthetics', 'monitor', 'create-rest-monitor'],
    ['apm-synthetics', 'monitor', 'update-rest-monitor'],
    ['apm-synthetics', 'aggregated-network-data-result', 'aggregate-network-data'],
    ['dashboard-service', 'dashboard', 'change-dashboard-group'],
    ['dashboard-service', 'dashboard-group', 'change-compartment'],
    ['service-mesh', 'debug', 'report'],
    ['compute', 'compute-capacity-report', 'create'],
    ['db', 'autonomous-container-database', 'change-dataguard-role'],
    ['db', 'autonomous-container-database-version', 'list'],
    ['devops', 'deploy-artifact', 'create-helm-repository-artifact'],
    ['devops', 'deploy-artifact', 'update-helm-repository-artifact'],
    ['devops', 'deploy-stage', 'create-oke-helm-chart-stage'],
    ['devops', 'deploy-stage', 'update-oke-helm-chart-stage'],
    ['goldengate', 'deployment', 'export-wallet'],
    ['goldengate', 'deployment', 'import-wallet'],
    ['goldengate', 'deployment', 'wallet-exists'],
    ['goldengate', 'deployment-wallets-operation-summary', 'list-wallet-operations'],
    ['opsi', 'opsi-configurations', 'change'],
    ['opsi', 'opsi-configurations', 'create-opsi-ux-configuration-details'],
    ['opsi', 'opsi-configurations', 'delete'],
    ['opsi', 'opsi-configurations', 'get'],
    ['opsi', 'opsi-configurations', 'list'],
    ['opsi', 'opsi-configurations', 'summarize-configuration-items'],
    ['opsi', 'opsi-configurations', 'update-opsi-ux-configuration-details'],
    ['db', 'autonomous-database', 'update'],
    ['opsi', 'database-insights', 'change-autonomous-database-insight-advanced-features-credential-by-vault'],
    ['opsi', 'database-insights', 'enable-autonomous-database-insight-advanced-features-credential-by-vault'],
    ['identity-domains', 'dynamic-resource-group', 'create'],
    ['identity-domains', 'dynamic-resource-group', 'put'],
    ['identity-domains', 'me', 'create'],
    ['identity-domains', 'me', 'put'],
    ['identity-domains', 'group', 'create'],
    ['identity-domains', 'group', 'put'],
    ['identity-domains', 'authentication-factor-setting', 'put'],
    ['identity-domains', 'identity-provider', 'create'],
    ['identity-domains', 'identity-provider', 'put'],
    ['identity-domains', 'user', 'create'],
    ['identity-domains', 'user', 'put'],
    ['os-management-hub', 'managed-instance', 'update-packages'],
    ['os-management-hub', 'managed-instance-group', 'update-all-packages'],
    ['os-management-hub', 'software-source', 'list'],
    ['os-management-hub', 'update-all-packages-in-compartment'],
    ['os-management-hub', 'work-request', 'list'],
    ['os-management-hub', 'lifecycle-environment', 'list'],
    ['os-management-hub', 'lifecycle-stage', 'list'],
    ['os-management-hub', 'lifecycle-stage', 'list-installed-packages'],
    ['os-management-hub', 'managed-instance', 'get-analytic-content'],
    ['os-management-hub', 'managed-instance', 'list'],
    ['os-management-hub', 'managed-instance', 'list-available-packages'],
    ['os-management-hub', 'managed-instance', 'list-available-software-sources'],
    ['os-management-hub', 'managed-instance', 'list-installed-packages'],
    ['os-management-hub', 'managed-instance', 'list-updatable-packages'],
    ['os-management-hub', 'managed-instance', 'summarize-analytics'],
    ['os-management-hub', 'managed-instance-group', 'list'],
    ['os-management-hub', 'managed-instance-group', 'list-available-packages'],
    ['os-management-hub', 'managed-instance-group', 'list-available-software-sources'],
    ['os-management-hub', 'managed-instance-group', 'list-installed-packages'],
    ['os-management-hub', 'profile', 'list'],
    ['rover', 'device', 'diagnostics', 'bundle', 'cancel'],
    ['rover', 'device', 'diagnostics', 'bundle', 'create'],
    ['rover', 'device', 'diagnostics', 'bundle', 'get'],
    ['rover', 'device', 'diagnostics', 'bundle', 'list'],
    ['rover', 'device', 'diagnostics', 'bundle', 'view-summary'],
    ['rover', 'device', 'system-upgrade', 'import-bundle'],
    ['database-management', 'tablespace', 'drop-with-pwd'],
    ['database-management', 'tablespace', 'drop-with-secret'],
    ['database-management', 'tablespace', 'remove-datafile-with-pwd'],
    ['database-management', 'tablespace', 'remove-datafile-with-secret'],
    ['database-management', 'managed-database', 'change-plan-retention-with-password'],
    ['database-management', 'managed-database', 'change-plan-retention-with-secret'],
    ['database-management', 'managed-database', 'change-space-budget-with-password'],
    ['database-management', 'managed-database', 'change-space-budget-with-secret'],
    ['database-management', 'managed-database', 'change-spb-attr-with-password'],
    ['database-management', 'managed-database', 'change-spb-attr-with-secret'],
    ['database-management', 'managed-database', 'cfg-auto-capture-filters-with-password'],
    ['database-management', 'managed-database', 'cfg-auto-capture-filters-with-secret'],
    ['database-management', 'managed-database', 'cfg-auto-spm-evolve-task-with-password'],
    ['database-management', 'managed-database', 'cfg-auto-spm-evolve-task-with-secret'],
    ['database-management', 'managed-database', 'disable-auto-plan-capture-with-password'],
    ['database-management', 'managed-database', 'disable-auto-plan-capture-with-secret'],
    ['database-management', 'managed-database', 'disable-auto-spm-evolve-task-with-password'],
    ['database-management', 'managed-database', 'disable-auto-spm-evolve-task-with-secret'],
    ['database-management', 'managed-database', 'disable-hf-auto-spm-evolve-task-with-password'],
    ['database-management', 'managed-database', 'disable-hf-auto-spm-evolve-task-with-secret'],
    ['database-management', 'managed-database', 'disable-spb-usage-with-password'],
    ['database-management', 'managed-database', 'disable-spb-usage-with-secret'],
    ['database-management', 'managed-database', 'drop-sql-plan-baselines-with-password'],
    ['database-management', 'managed-database', 'drop-sql-plan-baselines-with-secret'],
    ['database-management', 'managed-database', 'enable-auto-plan-capture-with-password'],
    ['database-management', 'managed-database', 'enable-auto-plan-capture-with-secret'],
    ['database-management', 'managed-database', 'enable-auto-spm-evolve-task-with-password'],
    ['database-management', 'managed-database', 'enable-auto-spm-evolve-task-with-secret'],
    ['database-management', 'managed-database', 'enable-hf-auto-spm-evolve-task-with-password'],
    ['database-management', 'managed-database', 'enable-hf-auto-spm-evolve-task-with-secret'],
    ['database-management', 'managed-database', 'enable-spb-usage-with-password'],
    ['database-management', 'managed-database', 'enable-spb-usage-with-secret'],
    ['database-management', 'managed-database', 'load-spb-from-awr-with-password'],
    ['database-management', 'managed-database', 'load-spb-from-awr-with-secret'],
    ['database-management', 'managed-database', 'load-spb-from-cc-with-password'],
    ['database-management', 'managed-database', 'load-spb-from-cc-with-secret'],
]

IGNORED_COMMANDS_DOCS = [
    ['setup', 'autocomplete'],
    ['setup', 'bootstrap'],
    ['setup', 'config'],
    ['setup', 'instance-principal'],
    ['setup', 'keys'],
    ['setup', 'repair-file-permissions'],
    ['setup', 'oci-cli-rc'],
    ['raw-request'],
    ['session', 'authenticate'],
    ['session', 'export'],
    ['session', 'import'],
    ['session', 'refresh'],
    ['session', 'terminate'],
    ['session', 'validate'],
]
