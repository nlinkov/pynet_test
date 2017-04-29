from pysnmp.hlapi import *

def snmp_get_oid(snmp_credentials = (), snmp_socket = (), oid='1.3.6.1.2.1.1.1.0', snmp_security_level = ('sha', 'aes128'), snmp_version = '2c'):
    '''
    snmp_version string or integer:       snmp_version = '2c' or '3';
        ***

        Default is '2c', wroks for version '1' as well
        ***

    snmp_credentials tuple:
        - for version '2c':    snmp_credentials = ('community_string');
        - for version '3':     snmp_credentials_v3 = ('snmp_username', 'auth_key', 'priv_key');

    snmp_socket tuple:              snmp_socket = ('snmp_device_ip', 'snmp_port');
        ***

        Default SNMP port is '161'
        ***

    oid string or tuple:       oid = 'OID';
        ***

        Default is '1.3.6.1.2.1.1.1.0'
        ***

    snmp_security_level tuple: snmp_security_level = ('auth_proto', 'priv_proto'); For version '3' only;
        ***

        Defaults to SHA1-AES128 for authentication + encryption

        auth_proto can be 'sha' or 'md5' or 'none'
        encrypt_proto can be 'aes128', 'aes192', 'aes256', '3des', 'des', or 'none'


        From PySNMP manuals:  http://pysnmp.sourceforge.net/docs/current/security-configuration.html

        Optional authProtocol parameter may be used to specify non-default hash function algorithm.
        Possible values include:
        usmHMACMD5AuthProtocol -- MD5-based authentication protocol
        usmHMACSHAAuthProtocol -- SHA-based authentication protocol
        usmNoAuthProtocol -- no authentication to use (default)

        Optional privProtocol parameter may be used to specify non-default ciphering algorithm.
        Possible values include:
        usmDESPrivProtocol -- DES-based encryption protocol
        usmAesCfb128Protocol -- AES128-based encryption protocol (RFC3826)
        usm3DESEDEPrivProtocol -- triple DES-based encryption protocol (Extended Security Options)
        usmAesCfb192Protocol -- AES192-based encryption protocol (Extended Security Options)
        usmAesCfb256Protocol -- AES256-based encryption protocol (Extended Security Options)
        usmNoPrivProtocol -- no encryption to use (default)

        ***

    '''

    if (type(snmp_credentials) is str):
        print '1-st if'
        if (snmp_version != 3):
            community_string = snmp_credentials
            snmp_version = '2c'
            print 'community_string: '
            print community_string

        elif (snmp_version == 3):
            (snmp_user, auth_key, priv_key) = (snmp_credentials, '', '')
            (auth_proto, priv_proto) = ('none', 'none')
            print 'auth_proto, priv_proto: '
            print auth_proto ', ' priv_proto

    elif (type(snmp_credentials) is tuple):
        print '2-nd elif'
        if (len(snmp_credentials) < 2):
            print '2-nd elif, 1-st if'
            snmp_version = '2c'
        elif (len(snmp_credentials) == 3):
            print '2-nd elif, 2-nd elif'
            snmp_version = 3
            print snmp_version
            (snmp_user, auth_key, priv_key) = snmp_credentials
            (auth_proto, priv_proto) = snmp_security_level
            print 'auth_proto, priv_proto: '
            print auth_proto ', ' priv_proto
        elif (len(snmp_credentials) == 2):
            print '2-nd elif, 3-d elif'
            snmp_version = 3
            print snmp_version
            (snmp_user, auth_key) = snmp_credentials
            (auth_proto) = snmp_security_level[0]
            print 'auth_proto: '
            print auth_proto


    print 'snmp_version: '
    print snmp_version
    print 'snmp_credentials: '
    print snmp_credentials
    if true:
        print 'snmp_security_level: '
        print snmp_security_level

    if (type(snmp_socket) is str):
        snmp_device = snmp_socket
        snmp_port = 161

    elif (type(snmp_socket) is tuple):
        if (len(snmp_socket) < 2):
            snmp_device = snmp_socket[0]
            snmp_port = 161
        elif (len(snmp_socket) == 2):
            (snmp_device, snmp_port) = snmp_socket

    print 'snmp_device: '
    print snmp_device
    print 'snmp_port: '
    print snmp_port

    if snmp_version == 3:

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

        return get_oid

    elif (snmp_version == '2c' or snmp_version == 1):

        if (type(snmp_credentials) is str):
            community_string = snmp_credentials

        elif (type(snmp_credentials) is tuple):
            community_string = snmp_credentials[0]

        get_oid = getCmd(
           SnmpEngine(),
           CommunityData(community_string),
           UdpTransportTarget((snmp_device, snmp_port)),
           ContextData(),
           ObjectType(ObjectIdentity(oid))
        )

        return get_oid

def print_or_error(get_oid):
    (errorIndication, errorStatus, errorIndex, varBinds) = get_oid.next()

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
