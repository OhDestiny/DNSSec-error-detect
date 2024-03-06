#!/bin/bash

python3 detect_dnssec_configuration_errors_Ecode.py "unsupportedDnskey.iwbtfy.top" "unsupportedDnskey"
echo "unsupportedDnskey finished!"

python3 detect_dnssec_configuration_errors_Ecode.py "unsupportedDs.iwbtfy.top" "unsupportedDs"
echo "unsupportedDs finished!"

python3 detect_dnssec_configuration_errors_Ecode.py "signatureNotValid.iwbtfy.top" "signatureNotValid"
echo "signatureNotValid finished!"

python3 detect_dnssec_configuration_errors_Ecode.py "signatureExpired.iwbtfy.top" "signatureExpired"
echo "signatureExpired finished!"

python3 detect_dnssec_configuration_errors_Ecode.py "rrsigMissing.iwbtfy.top" "rrsigMissing"
echo "rrsigMissing finished!"

python3 detect_dnssec_configuration_errors_Ecode.py "nsecMissing.iwbtfy.top" "nsecMissing"
echo "nsecMissing finished!"

python3 detect_dnssec_configuration_errors_Ecode.py "dnskeyMissing.iwbtfy.top" "dnskeyMissing"
echo "dnskeyMissing finished!"

python3 detect_dnssec_configuration_errors_Ecode.py "noZoneKey.iwbtfy.top" "noZoneKey"
echo "noZoneKey finished!"