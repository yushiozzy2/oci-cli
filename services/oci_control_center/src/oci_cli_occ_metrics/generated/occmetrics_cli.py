# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230515

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('occ.occ_root_group.command_name', 'occ'), cls=CommandGroupWithAlias, help=cli_util.override('occ.occ_root_group.help', """OCI Control Center (OCC) service enables you to monitor the region-level cloud consumption and provides the region-level capacity data, in realms where OCC is available. Use the OCI Control Center (OCC) API to explore region-level capacity and utilization information about core services. For more information, see [OCI Control Center]."""), short_help=cli_util.override('occ.occ_root_group.short_help', """OCI Control Center API"""))
@cli_util.help_option_group
def occ_root_group():
    pass


@click.command(cli_util.override('occ.metric_property_collection_group.command_name', 'metric-property-collection'), cls=CommandGroupWithAlias, help="""A list of available metrics and their associated properties such as dimensions.""")
@cli_util.help_option_group
def metric_property_collection_group():
    pass


@click.command(cli_util.override('occ.namespace_collection_group.command_name', 'namespace-collection'), cls=CommandGroupWithAlias, help="""The list of source services called namespaces emitting metrics that you can explore using OCI Control Center.""")
@cli_util.help_option_group
def namespace_collection_group():
    pass


@click.command(cli_util.override('occ.summarized_metric_data_collection_group.command_name', 'summarized-metric-data-collection'), cls=CommandGroupWithAlias, help="""A list of aggregated metric data objects with properties.""")
@cli_util.help_option_group
def summarized_metric_data_collection_group():
    pass


occ_root_group.add_command(metric_property_collection_group)
occ_root_group.add_command(namespace_collection_group)
occ_root_group.add_command(summarized_metric_data_collection_group)


@metric_property_collection_group.command(name=cli_util.override('occ.list_metric_properties.command_name', 'list-metric-properties'), help=u"""Returns a list of available metrics for the given namespace. The results for metrics with dimensions includes list of all the associated dimensions. The results are sorted by the metricName and then by dimension in ascending alphabetical order. For a list of valid namespaces, see [List Namespaces API]. \n[Command Reference](listMetricProperties)""")
@cli_util.option('--namespace-name', required=True, help=u"""The name of the source service emitting the metric.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to use for authorization. To use the root compartment, provide the tenancyId.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see <a href=\"https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine\">List Pagination</a>.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oci_control_center', 'class': 'MetricPropertyCollection'})
@cli_util.wrap_exceptions
def list_metric_properties(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oci_control_center', 'occ_metrics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_metric_properties,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_metric_properties,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_metric_properties(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@namespace_collection_group.command(name=cli_util.override('occ.list_namespaces.command_name', 'list-namespaces'), help=u"""List all the available source services called namespaces emitting metrics for this region. The namespaces are sorted in ascending alphabetical order. \n[Command Reference](listNamespaces)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to use for authorization. To use the root compartment, provide the tenancyId.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see <a href=\"https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine\">List Pagination</a>.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oci_control_center', 'class': 'NamespaceCollection'})
@cli_util.wrap_exceptions
def list_namespaces(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oci_control_center', 'occ_metrics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_namespaces,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_namespaces,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_namespaces(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@summarized_metric_data_collection_group.command(name=cli_util.override('occ.request_summarized_metric_data.command_name', 'request-summarized-metric-data'), help=u"""Returns the summarized data for the given metric from the given namespace.  The aggregation method depends on the metric. The metric data can be filtered by providing the dimension, startTime or endTime.  The metric data in the response is sorted by dimension in ascending order and then by sampleTime in ascending chronological order. \n[Command Reference](requestSummarizedMetricData)""")
@cli_util.option('--namespace-name', required=True, help=u"""The source service or application to use when searching for metric data points to aggregate. For a list of valid namespaces, see [List Namespaces API].""")
@cli_util.option('--metric-name', required=True, help=u"""The name of a metric for retrieving aggregated data. For a list of valid metrics for a given namespace, see [List Metric Properties API].""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to use for authorization to read metrics. To use the root compartment, provide the tenancyId.""")
@cli_util.option('--dimensions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Qualifiers to use when searching for metric data. For a list of valid dimensions for a given metric, see [List Metric Properties API].

This option is a JSON dictionary of type dict(str, DimensionValue).  For documentation on DimensionValue please see our API reference: https://docs.cloud.oracle.com/api/#/en/occmetrics/20230515/datatypes/DimensionValue.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--start-time', type=custom_types.CLI_DATETIME, help=u"""The beginning of the sampled time range to use when searching for metric data points. Format is defined by <a href=\"https://www.rfc-editor.org/rfc/rfc3339\">RFC3339</a>. The response includes metric data points for the sampled time. Example 2019-02-01T02:02:29.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--end-time', type=custom_types.CLI_DATETIME, help=u"""The end of the sampled time range to use when searching for metric data points. Format is defined by <a href=\"https://www.rfc-editor.org/rfc/rfc3339\">RFC3339</a>. The response excludes metric data points for sampled time. Example 2019-02-01T02:02:29.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see <a href=\"https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine\">List Pagination</a>.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.""")
@json_skeleton_utils.get_cli_json_input_option({'dimensions': {'module': 'oci_control_center', 'class': 'dict(str, DimensionValue)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dimensions': {'module': 'oci_control_center', 'class': 'dict(str, DimensionValue)'}}, output_type={'module': 'oci_control_center', 'class': 'SummarizedMetricDataCollection'})
@cli_util.wrap_exceptions
def request_summarized_metric_data(ctx, from_json, namespace_name, metric_name, compartment_id, dimensions, start_time, end_time, page, limit):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['namespaceName'] = namespace_name
    _details['metricName'] = metric_name
    _details['compartmentId'] = compartment_id

    if dimensions is not None:
        _details['dimensions'] = cli_util.parse_json_parameter("dimensions", dimensions)

    if start_time is not None:
        _details['startTime'] = start_time

    if end_time is not None:
        _details['endTime'] = end_time

    client = cli_util.build_client('oci_control_center', 'occ_metrics', ctx)
    result = client.request_summarized_metric_data(
        request_summarized_metric_data_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
