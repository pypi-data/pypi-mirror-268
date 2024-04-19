# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.v1.domain.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput
from worldline.connect.sdk.v1.domain.card_essentials import CardEssentials
from worldline.connect.sdk.v1.domain.card_fraud_results import CardFraudResults
from worldline.connect.sdk.v1.domain.three_d_secure_results import ThreeDSecureResults


class CardPaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):
    """
    | Card payment specific response data
    """

    __authorisation_code: Optional[str] = None
    __card: Optional[CardEssentials] = None
    __fraud_results: Optional[CardFraudResults] = None
    __initial_scheme_transaction_id: Optional[str] = None
    __scheme_transaction_id: Optional[str] = None
    __three_d_secure_results: Optional[ThreeDSecureResults] = None
    __token: Optional[str] = None

    @property
    def authorisation_code(self) -> Optional[str]:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: Optional[str]) -> None:
        self.__authorisation_code = value

    @property
    def card(self) -> Optional[CardEssentials]:
        """
        | Object containing card details

        Type: :class:`worldline.connect.sdk.v1.domain.card_essentials.CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[CardEssentials]) -> None:
        self.__card = value

    @property
    def fraud_results(self) -> Optional[CardFraudResults]:
        """
        | Fraud results contained in the CardFraudResults object

        Type: :class:`worldline.connect.sdk.v1.domain.card_fraud_results.CardFraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value: Optional[CardFraudResults]) -> None:
        self.__fraud_results = value

    @property
    def initial_scheme_transaction_id(self) -> Optional[str]:
        """
        | The unique scheme transactionId of the initial transaction that was performed with SCA.
        | Should be stored by the merchant to allow it to be submitted in future transactions.

        Type: str
        """
        return self.__initial_scheme_transaction_id

    @initial_scheme_transaction_id.setter
    def initial_scheme_transaction_id(self, value: Optional[str]) -> None:
        self.__initial_scheme_transaction_id = value

    @property
    def scheme_transaction_id(self) -> Optional[str]:
        """
        | The unique scheme transactionId of this transaction.
        | Should be stored by the merchant to allow it to be submitted in future transactions. Use this value in case the initialSchemeTransactionId property is empty.

        Type: str
        """
        return self.__scheme_transaction_id

    @scheme_transaction_id.setter
    def scheme_transaction_id(self, value: Optional[str]) -> None:
        self.__scheme_transaction_id = value

    @property
    def three_d_secure_results(self) -> Optional[ThreeDSecureResults]:
        """
        | 3D Secure results object

        Type: :class:`worldline.connect.sdk.v1.domain.three_d_secure_results.ThreeDSecureResults`
        """
        return self.__three_d_secure_results

    @three_d_secure_results.setter
    def three_d_secure_results(self, value: Optional[ThreeDSecureResults]) -> None:
        self.__three_d_secure_results = value

    @property
    def token(self) -> Optional[str]:
        """
        | If a token was used for or created during the payment, then the ID of that token.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardPaymentMethodSpecificOutput, self).to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.initial_scheme_transaction_id is not None:
            dictionary['initialSchemeTransactionId'] = self.initial_scheme_transaction_id
        if self.scheme_transaction_id is not None:
            dictionary['schemeTransactionId'] = self.scheme_transaction_id
        if self.three_d_secure_results is not None:
            dictionary['threeDSecureResults'] = self.three_d_secure_results.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificOutput':
        super(CardPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardEssentials()
            self.card = value.from_dictionary(dictionary['card'])
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = CardFraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'initialSchemeTransactionId' in dictionary:
            self.initial_scheme_transaction_id = dictionary['initialSchemeTransactionId']
        if 'schemeTransactionId' in dictionary:
            self.scheme_transaction_id = dictionary['schemeTransactionId']
        if 'threeDSecureResults' in dictionary:
            if not isinstance(dictionary['threeDSecureResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureResults']))
            value = ThreeDSecureResults()
            self.three_d_secure_results = value.from_dictionary(dictionary['threeDSecureResults'])
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
