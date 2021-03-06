# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device t0lte
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy Note 2

%define installable_zip 1

%define enable_kernel_update 1

%define straggler_files \
/selinux_version\
/service_contexts\
/bugreports\
/cache\
/d\
/file_contexts.bin\
/property_contexts\
/sdcard\
/vendor\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

