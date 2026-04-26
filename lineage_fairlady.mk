#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from fairlady device
$(call inherit-product, device/oneplus/fairlady/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_fairlady
PRODUCT_DEVICE := fairlady
PRODUCT_MANUFACTURER := OnePlus
PRODUCT_BRAND := OnePlus
PRODUCT_MODEL := PLZ110

PRODUCT_GMS_CLIENTID_BASE := android-oneplus

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="qssi-user 16 BP2A.250605.015 1785335374439 release-keys" \
    BuildFingerprint=OnePlus/PLZ110/OP64DDL1:16/BP2A.250605.015/B.40e10d0-1bdc90a-1c00f52:user/release-keys \
    DeviceName=OP64DDL1 \
    DeviceProduct=PLZ110 \
    SystemDevice=OP64DDL1 \
    SystemName=PLZ110
