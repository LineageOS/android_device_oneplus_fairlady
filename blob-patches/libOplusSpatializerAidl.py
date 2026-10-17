#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import re

from extract_utils.fixups_blob import (
    BlobFixupCtx,
    File,
)
from extract_utils.tools import (
    llvm_objdump_path,
)
from extract_utils.utils import (
    run_cmd,
)


def blob_fixup(
    ctx: BlobFixupCtx,
    file: File,
    file_path: str,
    *args,
    **kwargs,
):
    # mov w8, #2
    from_instruction = bytes.fromhex('48 00 80 52')[::-1].hex()

    # mov w8, #0
    to_instruction = bytes.fromhex('08 00 80 52')

    segments = [
        (int(vaddr, 16), int(off, 16), int(filesz, 16))
        for off, vaddr, filesz in re.findall(
            r'LOAD off\s+(0x[0-9a-f]+) vaddr (0x[0-9a-f]+).*\n'
            r'\s+filesz (0x[0-9a-f]+)',
            run_cmd([llvm_objdump_path, '-p', file_path]),
        )
    ]

    for line in run_cmd(
        [
            llvm_objdump_path,
            f'--disassemble-symbols=_ZN4aidl7android8hardware5audio6effect20OplusSpatializerImplC2Ev',
            file_path,
        ]
    ).splitlines():
        line = line.split(maxsplit=3)

        if len(line) != 4:
            continue

        offset, instruction, _, _ = line

        if instruction != from_instruction:
            continue

        offset = int(offset[:-1], 16)
        offset = next(
            offset - vaddr + off
            for vaddr, off, filesz in segments
            if vaddr <= offset < vaddr + filesz
        )

        with open(file_path, 'rb+') as f:
            f.seek(offset)
            f.write(to_instruction)

        break
