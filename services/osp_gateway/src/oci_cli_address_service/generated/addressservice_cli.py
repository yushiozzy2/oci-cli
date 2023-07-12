# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.osp_gateway.src.oci_cli_osp_gateway.generated import osp_gateway_service_cli


@click.command(cli_util.override('address_service.address_service_root_group.command_name', 'address-service'), cls=CommandGroupWithAlias, help=cli_util.override('address_service.address_service_root_group.help', """This site describes all the Rest endpoints of OSP Gateway."""), short_help=cli_util.override('address_service.address_service_root_group.short_help', """OSP Gateway API"""))
@cli_util.help_option_group
def address_service_root_group():
    pass


@click.command(cli_util.override('address_service.address_group.command_name', 'address'), cls=CommandGroupWithAlias, help="""Address details model.""")
@cli_util.help_option_group
def address_group():
    pass


osp_gateway_service_cli.osp_gateway_service_group.add_command(address_service_root_group)
address_service_root_group.add_command(address_group)


@address_group.command(name=cli_util.override('address_service.get_address.command_name', 'get'), help=u"""Get the address by id for the compartment \n[Command Reference](getAddress)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--address-id', required=True, help=u"""The identifier of the address.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'Address'})
@cli_util.wrap_exceptions
def get_address(ctx, from_json, osp_home_region, compartment_id, address_id):

    if isinstance(address_id, six.string_types) and len(address_id.strip()) == 0:
        raise click.UsageError('Parameter --address-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osp_gateway', 'address_service', ctx)
    result = client.get_address(
        osp_home_region=osp_home_region,
        compartment_id=compartment_id,
        address_id=address_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@address_group.command(name=cli_util.override('address_service.verify_address.command_name', 'verify'), help=u"""Verify address \n[Command Reference](verifyAddress)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--address-key', help=u"""Address identifier.""")
@cli_util.option('--line1', help=u"""Address line 1.""")
@cli_util.option('--line2', help=u"""Address line 2.""")
@cli_util.option('--line3', help=u"""Address line 3.""")
@cli_util.option('--line4', help=u"""Address line 4.""")
@cli_util.option('--street-name', help=u"""Street name of the address.""")
@cli_util.option('--street-number', help=u"""Street number of the address.""")
@cli_util.option('--city', help=u"""Name of the city.""")
@cli_util.option('--county', help=u"""County of the address.""")
@cli_util.option('--country', help=u"""Country of the address.""")
@cli_util.option('--province', help=u"""Province of the address.""")
@cli_util.option('--postal-code', help=u"""Post code of the address.""")
@cli_util.option('--state', help=u"""State of the address.""")
@cli_util.option('--email-address', help=u"""Contact person email address.""")
@cli_util.option('--company-name', help=u"""Name of the customer company.""")
@cli_util.option('--first-name', help=u"""First name of the contact person.""")
@cli_util.option('--middle-name', help=u"""Middle name of the contact person.""")
@cli_util.option('--last-name', help=u"""Last name of the contact person.""")
@cli_util.option('--phone-country-code', help=u"""Phone country code of the contact person.""")
@cli_util.option('--phone-number', help=u"""Phone number of the contact person.""")
@cli_util.option('--job-title', help=u"""Job title of the contact person.""")
@cli_util.option('--department-name', help=u"""Department name of the customer company.""")
@cli_util.option('--internal-number', help=u"""Internal number of the customer company.""")
@cli_util.option('--contributor-class', help=u"""Contributor class of the customer company.""")
@cli_util.option('--state-inscription', help=u"""State Inscription.""")
@cli_util.option('--municipal-inscription', help=u"""Municipal Inscription.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'VerifyAddressReceipt'})
@cli_util.wrap_exceptions
def verify_address(ctx, from_json, osp_home_region, compartment_id, address_key, line1, line2, line3, line4, street_name, street_number, city, county, country, province, postal_code, state, email_address, company_name, first_name, middle_name, last_name, phone_country_code, phone_number, job_title, department_name, internal_number, contributor_class, state_inscription, municipal_inscription, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if address_key is not None:
        _details['addressKey'] = address_key

    if line1 is not None:
        _details['line1'] = line1

    if line2 is not None:
        _details['line2'] = line2

    if line3 is not None:
        _details['line3'] = line3

    if line4 is not None:
        _details['line4'] = line4

    if street_name is not None:
        _details['streetName'] = street_name

    if street_number is not None:
        _details['streetNumber'] = street_number

    if city is not None:
        _details['city'] = city

    if county is not None:
        _details['county'] = county

    if country is not None:
        _details['country'] = country

    if province is not None:
        _details['province'] = province

    if postal_code is not None:
        _details['postalCode'] = postal_code

    if state is not None:
        _details['state'] = state

    if email_address is not None:
        _details['emailAddress'] = email_address

    if company_name is not None:
        _details['companyName'] = company_name

    if first_name is not None:
        _details['firstName'] = first_name

    if middle_name is not None:
        _details['middleName'] = middle_name

    if last_name is not None:
        _details['lastName'] = last_name

    if phone_country_code is not None:
        _details['phoneCountryCode'] = phone_country_code

    if phone_number is not None:
        _details['phoneNumber'] = phone_number

    if job_title is not None:
        _details['jobTitle'] = job_title

    if department_name is not None:
        _details['departmentName'] = department_name

    if internal_number is not None:
        _details['internalNumber'] = internal_number

    if contributor_class is not None:
        _details['contributorClass'] = contributor_class

    if state_inscription is not None:
        _details['stateInscription'] = state_inscription

    if municipal_inscription is not None:
        _details['municipalInscription'] = municipal_inscription

    client = cli_util.build_client('osp_gateway', 'address_service', ctx)
    result = client.verify_address(
        osp_home_region=osp_home_region,
        compartment_id=compartment_id,
        verify_address_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
