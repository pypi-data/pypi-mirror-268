# -*- coding: utf-8 -*-

"""
postnl

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnl.api_helper import APIHelper
from postnl.configuration import Server
from postnl.http.api_response import ApiResponse
from postnl.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from postnl.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from postnl.models.labelling_response import LabellingResponse
from postnl.exceptions.labelling_response_invalid_exception import LabellingResponseInvalidException
from postnl.exceptions.barcode_method_not_allowed_exception import BarcodeMethodNotAllowedException
from postnl.exceptions.barcode_response_error_exception import BarcodeResponseErrorException


class LabellingController(BaseController):

    """A Controller to access Endpoints in the postnl API."""
    def __init__(self, config):
        super(LabellingController, self).__init__(config)

    def generate_a_label_and_confirmation(self,
                                          body,
                                          confirm=True):
        """Does a POST request to /shipment/v2_2/label.

        TODO: type endpoint description here.

        Args:
            body (LabellingRequest): TODO: type description here.
            confirm (bool, optional): With the Confirm boolean in the request,
                you can determine if you want to confirm the shipment in the
                same call or not. If the Boolean variable is true the shipment
                will be preannounced. If this is set to false, then an
                additional Confirming API request needs to be made.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A Label

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2_2/label')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .query_param(Parameter()
                         .key('confirm')
                         .value(confirm))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LabellingResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error payload', LabellingResponseInvalidException)
            .local_error('401', 'Invalid apikey', BarcodeMethodNotAllowedException)
            .local_error('405', 'Method not allowed', BarcodeMethodNotAllowedException)
            .local_error('429', 'Too many requests', BarcodeMethodNotAllowedException)
            .local_error('500', 'Internal server error', BarcodeResponseErrorException)
        ).execute()
