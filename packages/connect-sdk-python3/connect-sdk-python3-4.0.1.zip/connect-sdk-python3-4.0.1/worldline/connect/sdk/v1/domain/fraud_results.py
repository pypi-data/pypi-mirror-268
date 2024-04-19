# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.in_auth import InAuth
from worldline.connect.sdk.v1.domain.microsoft_fraud_results import MicrosoftFraudResults


class FraudResults(DataObject):

    __fraud_service_result: Optional[str] = None
    __in_auth: Optional[InAuth] = None
    __microsoft_fraud_protection: Optional[MicrosoftFraudResults] = None

    @property
    def fraud_service_result(self) -> Optional[str]:
        """
        | Results from the fraud prevention check. Possible values are:
        
        * accepted - Based on the checks performed the transaction can be accepted
        * challenged - Based on the checks performed the transaction should be manually reviewed
        * denied - Based on the checks performed the transaction should be rejected
        * no-advice - No fraud check was requested/performed
        * error - The fraud check resulted in an error and the fraud check was thus not performed

        Type: str
        """
        return self.__fraud_service_result

    @fraud_service_result.setter
    def fraud_service_result(self, value: Optional[str]) -> None:
        self.__fraud_service_result = value

    @property
    def in_auth(self) -> Optional[InAuth]:
        """
        | Object containing device fingerprinting details from InAuth

        Type: :class:`worldline.connect.sdk.v1.domain.in_auth.InAuth`
        """
        return self.__in_auth

    @in_auth.setter
    def in_auth(self, value: Optional[InAuth]) -> None:
        self.__in_auth = value

    @property
    def microsoft_fraud_protection(self) -> Optional[MicrosoftFraudResults]:
        """
        | This object contains the results of Microsoft Fraud Protection risk assessment. Microsoft collects transaction data points and uses Adaptive AI that continuously learns to protect you against payment fraud, and the device fingerprinting details from the Microsoft Device Fingerprinting service.

        Type: :class:`worldline.connect.sdk.v1.domain.microsoft_fraud_results.MicrosoftFraudResults`
        """
        return self.__microsoft_fraud_protection

    @microsoft_fraud_protection.setter
    def microsoft_fraud_protection(self, value: Optional[MicrosoftFraudResults]) -> None:
        self.__microsoft_fraud_protection = value

    def to_dictionary(self) -> dict:
        dictionary = super(FraudResults, self).to_dictionary()
        if self.fraud_service_result is not None:
            dictionary['fraudServiceResult'] = self.fraud_service_result
        if self.in_auth is not None:
            dictionary['inAuth'] = self.in_auth.to_dictionary()
        if self.microsoft_fraud_protection is not None:
            dictionary['microsoftFraudProtection'] = self.microsoft_fraud_protection.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'FraudResults':
        super(FraudResults, self).from_dictionary(dictionary)
        if 'fraudServiceResult' in dictionary:
            self.fraud_service_result = dictionary['fraudServiceResult']
        if 'inAuth' in dictionary:
            if not isinstance(dictionary['inAuth'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['inAuth']))
            value = InAuth()
            self.in_auth = value.from_dictionary(dictionary['inAuth'])
        if 'microsoftFraudProtection' in dictionary:
            if not isinstance(dictionary['microsoftFraudProtection'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['microsoftFraudProtection']))
            value = MicrosoftFraudResults()
            self.microsoft_fraud_protection = value.from_dictionary(dictionary['microsoftFraudProtection'])
        return self
