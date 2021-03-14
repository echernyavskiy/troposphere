# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags
from .validators import boolean
from .validators import integer


class Destination(AWSObject):
    resource_type = "AWS::IoTWireless::Destination"

    props = {
        'Description': (basestring, False),
        'Expression': (basestring, True),
        'ExpressionType': (basestring, True),
        'Name': (basestring, True),
        'RoleArn': (basestring, True),
        'Tags': (Tags, False),
    }


class LoRaWANDeviceProfile(AWSProperty):
    props = {
        'ClassBTimeout': (integer, False),
        'ClassCTimeout': (integer, False),
        'MacVersion': (basestring, False),
        'MaxDutyCycle': (integer, False),
        'MaxEirp': (integer, False),
        'PingSlotDr': (integer, False),
        'PingSlotFreq': (integer, False),
        'PingSlotPeriod': (integer, False),
        'RegParamsRevision': (basestring, False),
        'RfRegion': (basestring, False),
        'Supports32BitFCnt': (boolean, False),
        'SupportsClassB': (boolean, False),
        'SupportsClassC': (boolean, False),
        'SupportsJoin': (boolean, False),
    }


class DeviceProfile(AWSObject):
    resource_type = "AWS::IoTWireless::DeviceProfile"

    props = {
        'LoRaWAN': (LoRaWANDeviceProfile, False),
        'Name': (basestring, False),
        'Tags': (Tags, False),
    }


class LoRaWANServiceProfile(AWSProperty):
    props = {
        'AddGwMetadata': (boolean, False),
        'ChannelMask': (basestring, False),
        'DevStatusReqFreq': (integer, False),
        'DlBucketSize': (integer, False),
        'DlRate': (integer, False),
        'DlRatePolicy': (basestring, False),
        'DrMax': (integer, False),
        'DrMin': (integer, False),
        'HrAllowed': (boolean, False),
        'MinGwDiversity': (integer, False),
        'NwkGeoLoc': (boolean, False),
        'PrAllowed': (boolean, False),
        'RaAllowed': (boolean, False),
        'ReportDevStatusBattery': (boolean, False),
        'ReportDevStatusMargin': (boolean, False),
        'TargetPer': (integer, False),
        'UlBucketSize': (integer, False),
        'UlRate': (integer, False),
        'UlRatePolicy': (basestring, False),
    }


class ServiceProfile(AWSObject):
    resource_type = "AWS::IoTWireless::ServiceProfile"

    props = {
        'LoRaWAN': (LoRaWANServiceProfile, False),
        'Name': (basestring, False),
        'Tags': (Tags, False),
    }


class SessionKeysAbpV10x(AWSProperty):
    props = {
        'AppSKey': (basestring, True),
        'NwkSKey': (basestring, True),
    }


class AbpV10x(AWSProperty):
    props = {
        'DevAddr': (basestring, True),
        'SessionKeys': (SessionKeysAbpV10x, True),
    }


class SessionKeysAbpV11(AWSProperty):
    props = {
        'AppSKey': (basestring, True),
        'FNwkSIntKey': (basestring, True),
        'NwkSEncKey': (basestring, True),
        'SNwkSIntKey': (basestring, True),
    }


class AbpV11(AWSProperty):
    props = {
        'DevAddr': (basestring, True),
        'SessionKeys': (SessionKeysAbpV11, True),
    }


class OtaaV10x(AWSProperty):
    props = {
        'AppEui': (basestring, True),
        'AppKey': (basestring, True),
    }


class OtaaV11(AWSProperty):
    props = {
        'AppKey': (basestring, True),
        'JoinEui': (basestring, True),
        'NwkKey': (basestring, True),
    }


class LoRaWANDevice(AWSProperty):
    props = {
        'AbpV10x': (AbpV10x, False),
        'AbpV11': (AbpV11, False),
        'DevEui': (basestring, False),
        'DeviceProfileId': (basestring, False),
        'OtaaV10x': (OtaaV10x, False),
        'OtaaV11': (OtaaV11, False),
        'ServiceProfileId': (basestring, False),
    }


class WirelessDevice(AWSObject):
    resource_type = "AWS::IoTWireless::WirelessDevice"

    props = {
        'Description': (basestring, False),
        'DestinationName': (basestring, True),
        'LastUplinkReceivedAt': (basestring, False),
        'LoRaWAN': (LoRaWANDevice, False),
        'Name': (basestring, False),
        'Tags': (Tags, False),
        'ThingArn': (basestring, False),
        'Type': (basestring, True),
    }


class LoRaWANGateway(AWSProperty):
    props = {
        'GatewayEui': (basestring, True),
        'RfRegion': (basestring, True),
    }


class WirelessGateway(AWSObject):
    resource_type = "AWS::IoTWireless::WirelessGateway"

    props = {
        'Description': (basestring, False),
        'LastUplinkReceivedAt': (basestring, False),
        'LoRaWAN': (LoRaWANGateway, True),
        'Name': (basestring, False),
        'Tags': (Tags, False),
        'ThingArn': (basestring, False),
    }
