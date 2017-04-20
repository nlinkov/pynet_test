from pysnmp.hlapi import *

def snmp_get_oid_v3(snmp_user, auth_key, priv_key, snmp_device, snmp_port=161, auth_proto='sha', priv_proto='aes128', oid='.1.3.6.1.2.1.1.1.0'):

    auth_proto_map = {
        'sha':  usmHMACSHAAuthProtocol,
        'md5':  usmHMACMD5AuthProtocol,
        'none': usmNoAuthProtocol
    }

    if auth_proto in auth_proto_map.keys():
        auth_protocol = auth_proto_map[auth_proto]
    else:
        raise ValueError("Invalid authentication protocol specified: %s" % auth_proto)

    priv_proto_map = {
        'des':      usmDESPrivProtocol,
        '3des':     usm3DESEDEPrivProtocol,
        'aes128':   usmAesCfb128Protocol,
        'aes192':   usmAesCfb192Protocol,
        'aes256':   usmAesCfb256Protocol,
        'none':     usmNoPrivProtocol,
    }

    if priv_proto in priv_proto_map.keys():
        priv_protocol = priv_proto_map[priv_proto]
    else:
        raise ValueError("Invalid encryption protocol specified: %s" % priv_proto)

    get_oid = getCmd(
       SnmpEngine(),
       UsmUserData(snmp_user, auth_key, priv_key,
                   auth_protocol,
                   priv_protocol),
       UdpTransportTarget((snmp_device, snmp_port)),
       ContextData(),
       ObjectType(ObjectIdentity(oid))
    )

    (errorIndication, errorStatus, errorIndex, varBinds) = get_oid.next()

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


def snmp_get_oid_v2c(community_string, snmp_device, snmp_port=161, oid='.1.3.6.1.2.1.1.1.0'):

    get_oid = getCmd(
       SnmpEngine(),
       CommunityData(community_string),
       UdpTransportTarget((snmp_device, snmp_port)),
       ContextData(),
       ObjectType(ObjectIdentity(oid))
    )

    (errorIndication, errorStatus, errorIndex, varBinds) = get_oid.next()

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
