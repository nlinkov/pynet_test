from snmp_helper import snmp_get_oid_v3,snmp_extract
import time
import pygal

snmp_device = ('192.168.20.113', 161)
a_user = 'test1'
auth_key = 'test1111'
encrypt_key = 'test1111'
snmp_user = (a_user, auth_key, encrypt_key)

snmp_oids = (
  ('sysName', '1.3.6.1.2.1.1.5.0', 'None'),
  ('sysUpTimeInstance', '1.3.6.1.2.1.1.3.0', 'Counter'),
  ('ifDescr', '1.3.6.1.2.1.2.2.1.2.8', 'None'),
  ('ifInOctets', '1.3.6.1.2.1.2.2.1.10.8', 'Counter'),
  ('ifInUcastPkts', '1.3.6.1.2.1.2.2.1.11.8', 'Counter'),
  ('ifOutOctets', '1.3.6.1.2.1.2.2.1.16.8', 'Counter'),
  ('ifOutUcastPkts', '1.3.6.1.2.1.2.2.1.17.8', 'Counter')        
)

hash_counters = {}
hash_counters['timed_counter'] = []
hash_counters['sysUpTimeInstance'] = []
hash_counters['ifInOctets'] = []
hash_counters['ifInUcastPkts'] = []
hash_counters['ifOutOctets'] = []
hash_counters['ifOutUcastPkts'] = []

hash_counters_growth = {}
hash_counters_growth['timed_counter'] = []
hash_counters_growth['sysUpTimeInstance'] = []
hash_counters_growth['ifInOctets'] = []
hash_counters_growth['ifInUcastPkts'] = []
hash_counters_growth['ifOutOctets'] = []
hash_counters_growth['ifOutUcastPkts'] = []

repeat = range(10)

for i in repeat:
  print i
  local_time = time.strftime("%H:%M:%S", time.localtime())
  hash_counters['timed_counter'].append(local_time)

  if i is not 0:
    hash_counters_growth['timed_counter'].append(local_time)

  for OID_descr, OID_numbers, is_counter in snmp_oids:
    snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=OID_numbers)
    output = snmp_extract(snmp_data)
    print "%s %s" % (OID_descr, output)
    if is_counter == 'Counter':
      hash_counters[OID_descr].append(int(output))
      if i is not 0:
        hash_counters_growth[OID_descr].append(int(output) - hash_counters[OID_descr][-2])

  time.sleep(5)

line_chart = pygal.Line()
line_chart.title = 'Input/Output Packets and Bytes'
line_chart.x_labels = hash_counters_growth['timed_counter']
line_chart.add('InPacktes', hash_counters_growth['ifInUcastPkts'])
line_chart.add('OutPacktes', hash_counters_growth['ifOutUcastPkts'])
line_chart.add('InBytes', hash_counters_growth['ifInOctets'])
line_chart.add('OutBytes', hash_counters_growth['ifOutOctets'])
line_chart.render_to_file('test.svg')
