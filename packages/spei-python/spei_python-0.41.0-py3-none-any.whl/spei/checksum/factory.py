from spei.checksum.generator import (
    ChecksumGenerator,
    ChecksumGeneratorBeneficiary,
    ChecksumGeneratorBeneficiaryAndAdditionalBeneficiary,
    ChecksumGeneratorDefault,
    ChecksumGeneratorEveryField,
    ChecksumGeneratorOrigin,
    ChecksumGeneratorOriginAndBeneficiary,
)
from spei.checksum.types import (
    PAYMENT_TYPES_WITH_BENEFICIARY_ACCOUNT,
    PAYMENT_TYPES_WITH_BENEFICIARY_AND_ADDITIONAL_BENEFICIARY_ACCOUNT,
    PAYMENT_TYPES_WITH_DEFAULT_FIELDS,
    PAYMENT_TYPES_WITH_ORIGIN_ACCOUNT,
    PAYMENT_TYPES_WITH_ORIGIN_AND_BENEFICIARY_ACCOUNT,
    PAYMENT_TYPES_WITH_ORIGIN_BENEFICIARY_AND_ADDITIONAL_BENEFICIARY_ACCOUNT,
)
from spei.types import TipoPagoOrdenPago


def get_checksum_generator(payment_type: TipoPagoOrdenPago) -> ChecksumGenerator:  # noqa: C901, WPS212, E501
    if payment_type in PAYMENT_TYPES_WITH_DEFAULT_FIELDS:
        return ChecksumGeneratorDefault()

    if payment_type in PAYMENT_TYPES_WITH_ORIGIN_ACCOUNT:
        return ChecksumGeneratorOrigin()

    if payment_type in PAYMENT_TYPES_WITH_BENEFICIARY_ACCOUNT:
        return ChecksumGeneratorBeneficiary()

    if payment_type in PAYMENT_TYPES_WITH_ORIGIN_AND_BENEFICIARY_ACCOUNT:
        return ChecksumGeneratorOriginAndBeneficiary()

    if payment_type in PAYMENT_TYPES_WITH_BENEFICIARY_AND_ADDITIONAL_BENEFICIARY_ACCOUNT:  # noqa: E501
        return ChecksumGeneratorBeneficiaryAndAdditionalBeneficiary()

    if payment_type in PAYMENT_TYPES_WITH_ORIGIN_BENEFICIARY_AND_ADDITIONAL_BENEFICIARY_ACCOUNT:  # noqa: E501
        return ChecksumGeneratorEveryField()

    raise NotImplementedError
