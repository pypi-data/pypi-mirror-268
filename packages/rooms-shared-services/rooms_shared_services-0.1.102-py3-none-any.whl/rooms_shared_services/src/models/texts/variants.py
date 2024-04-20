from enum import Enum


class TextVariant(Enum):
    PRODUCT_NAME = "PRODUCT_NAME"
    PRODUCT_FULL_DESCRIPTION = "PRODUCT_FULL_DESCRIPTION"
    PRODUCT_SHORT_DESCRIPTION = "PRODUCT_SHORT_DESCRIPTION"
    PRODUCT_ATTRIBUTE_NAME = "PRODUCT_ATTRIBUTE_NAME"
    PRODUCT_ATTRIBUTE_TERM = "PRODUCT_ATTRIBUTE_TERM"

    @property
    def readable(self):
        return self.value.lower().replace("_", " ")
