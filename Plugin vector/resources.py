from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xa0\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x04\x73\x42\x49\x54\x08\x08\x08\x08\x7c\x08\x64\x88\
\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd7\x00\x00\x0d\xd7\
\x01\x42\x28\x9b\x78\x00\x00\x00\x19\x74\x45\x58\x74\x53\x6f\x66\
\x74\x77\x61\x72\x65\x00\x77\x77\x77\x2e\x69\x6e\x6b\x73\x63\x61\
\x70\x65\x2e\x6f\x72\x67\x9b\xee\x3c\x1a\x00\x00\x00\x0b\x74\x45\
\x58\x74\x54\x69\x74\x6c\x65\x00\x74\x69\x6c\x65\x73\x26\x0b\xcd\
\xf6\x00\x00\x00\x18\x74\x45\x58\x74\x41\x75\x74\x68\x6f\x72\x00\
\x52\x6f\x62\x65\x72\x74\x20\x53\x7a\x63\x7a\x65\x70\x61\x6e\x65\
\x6b\x5f\x56\xb1\x08\x00\x00\x00\x18\x74\x45\x58\x74\x43\x72\x65\
\x61\x74\x69\x6f\x6e\x20\x54\x69\x6d\x65\x00\x32\x30\x31\x32\x2d\
\x30\x34\x2d\x32\x35\x9d\xb6\xd4\x63\x00\x00\x00\x52\x74\x45\x58\
\x74\x43\x6f\x70\x79\x72\x69\x67\x68\x74\x00\x43\x43\x20\x41\x74\
\x74\x72\x69\x62\x75\x74\x69\x6f\x6e\x2d\x53\x68\x61\x72\x65\x41\
\x6c\x69\x6b\x65\x20\x68\x74\x74\x70\x3a\x2f\x2f\x63\x72\x65\x61\
\x74\x69\x76\x65\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x6f\x72\x67\x2f\
\x6c\x69\x63\x65\x6e\x73\x65\x73\x2f\x62\x79\x2d\x73\x61\x2f\x33\
\x2e\x30\x2f\x5e\x83\x5a\xbc\x00\x00\x00\x60\x49\x44\x41\x54\x48\
\x89\x63\xac\x9c\xba\xe2\x3f\x03\x01\xd0\x96\x15\xce\xd8\xbc\x70\
\x2b\x41\x75\xb5\xf1\xde\x8c\xfd\xeb\x8f\xa2\xa8\x63\x22\xa4\x89\
\x52\x30\x6a\xc1\xa8\x05\x43\xc0\x02\xc6\xff\xff\x09\xe6\x1f\x8a\
\x00\x0b\xb9\x39\x14\x1b\x28\x0c\xb4\x66\x9c\xba\xfd\xec\x68\x4e\
\x1e\xb5\x60\xd4\x02\x34\x40\xfb\x9c\x4c\x6e\x0e\xc5\x06\xb2\x3d\
\x8d\x19\xd1\xc5\x86\x7e\x1c\xd0\xdc\x02\x00\x87\xdb\x24\x43\x2f\
\xf4\xcd\xa2\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x0d\
\x08\xbc\x6a\x22\
\x00\x50\
\x00\x6c\x00\x75\x00\x67\x00\x69\x00\x6e\x00\x5f\x00\x76\x00\x65\x00\x63\x00\x74\x00\x6f\x00\x72\
\x00\x0a\
\x0b\x6a\xc0\x07\
\x00\x76\
\x00\x65\x00\x63\x00\x74\x00\x6f\x00\x72\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x20\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x20\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x83\x19\x16\x5e\xc0\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()