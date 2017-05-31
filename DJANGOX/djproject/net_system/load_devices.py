
from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    pynet_rtr1 = NetworkDevice(
        device_name='pynet-rtr1',
        device_type='cisco_ios',
        ip_address='184.105.247.70',
        port=22,
    )
    pynet_rtr1.save()

    pynet_rtr2 = NetworkDevice.objects.get_or_create(
        device_name='pynet-rtr2',
        device_type='cisco_ios',
        ip_address='184.105.247.71',
        port=22,
    )
    print pynet_rtr2

    pynet_sw1 = NetworkDevice.objects.get_or_create(
        device_name='pynet-sw1',
        device_type='arista_eos',
        ip_address='184.105.247.72',
        port=22,
    )
    print pynet_sw1

    pynet_sw2 = NetworkDevice.objects.get_or_create(
        device_name='pynet-sw2',
        device_type='arista_eos',
        ip_address='184.105.247.73',
        port=22,
    )
    print pynet_sw2

    pynet_sw3 = NetworkDevice.objects.get_or_create(
        device_name='pynet-sw3',
        device_type='arista_eos',
        ip_address='184.105.247.74',
        port=22,
    )
    print pynet_sw3

    pynet_sw4 = NetworkDevice.objects.get_or_create(
        device_name='pynet-sw4',
        device_type='arista_eos',
        ip_address='184.105.247.75',
        port=22,
    )
    print pynet_sw4

    juniper_srx = NetworkDevice.objects.get_or_create(
        device_name='juniper-srx',
        device_type='juniper',
        ip_address='184.105.247.76',
        port=22,
    )
    print juniper_srx

if __name__ == "__main__":
    main()
