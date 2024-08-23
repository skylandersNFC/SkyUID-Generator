# Thanks to Nitrus#1839 for making this cool script.

import argparse
import binascii
import struct
import warnings
import libs.sklykeys as sklykeys
from libs.lerutils import *

blankPath = ''
skyPath = ''
outputFileName = 'defaultout.dump'

def calculate_bcc(bcc):
    return (bcc[0] ^ bcc[1] ^ bcc[2] ^ bcc[3])

def check_keys(a_or_b, data):
    blockOffset = 0
    if a_or_b == 'b':
        blockOffset = 10
    verified = True
    for sector in data:
        key = binascii.hexlify(sector[48+blockOffset:48+blockOffset+6]).decode("utf-8")
        verified = verified and (key == "000000000000" or key.upper() == "FFFFFFFFFFFF")
    return verified

def run(UID='00000000', skyPath=skyPath, outputName=None):

    skylanderDump = read_nfc_dump(skyPath)
    cleanTag = create_clear()
    uid = bytes.fromhex(UID)
    
    # Calculate BCC and convert directly to a byte
    bcc_value = calculate_bcc(uid)
    bcc = bytes([bcc_value])
    
    cleanTag[0] = b''.join((uid, bcc, bytes.fromhex("0804006263646566676869"), cleanTag[0][16:]))

    verifyKeysA = check_keys('a', cleanTag)
    verifyKeysB = check_keys('b', cleanTag)

    if not (verifyKeysA and verifyKeysB):
        warnings.warn("Some of the keys in the blank dump are not standard!")

    bytesUid = bytes(cleanTag[0][:4])
    writtenBcc = bytes(cleanTag[0][4:5])
    hexWrittenBcc = binascii.hexlify(writtenBcc)
    sak = bytes(cleanTag[0][5:6])
    atqa = bytearray(cleanTag[0][6:8])

    hexUid = binascii.hexlify(bytesUid)
    stringUid = hexUid.decode("utf-8")
    print("UID:",   "0x" + stringUid.upper())
    print("BCC:",   "0x" + hexWrittenBcc.decode("utf-8").upper())
    print("SAK:",   "0x" + binascii.hexlify(sak).decode("utf-8").upper())
    print("ATQA:",  "0x" + binascii.hexlify(struct.pack('<H', int.from_bytes(atqa, "big"))).decode("utf-8").upper())

    calculatedBcc = calculate_bcc(bytesUid)
    bccIsGood = calculatedBcc == int(hexWrittenBcc, 16)
    if not bccIsGood:
        warnings.warn("This Tag's BCC is incorrect! Possibly a 7 byte UID?")

    lockedZeroBlock = bytes(cleanTag[0][:16])
    newFile = skylanderDump.copy()
    newFile[0] = b''.join((lockedZeroBlock, newFile[0][16:]))
    skylanderInfo = skylanderDump[0][16:30]
    zeroChecksumData = (lockedZeroBlock + skylanderInfo)
    binaryCrc16 = int.to_bytes(struct.unpack("<H", struct.pack(">H", binascii.crc_hqx(zeroChecksumData, 0xFFFF)))[0], 2, "big")
    newFile[0] = b''.join((newFile[0][:30], binaryCrc16, newFile[0][32:]))

    keys = sklykeys.generate_keys(stringUid)

    print("New keys:", keys)
    
    for i, sector in enumerate(newFile):
        newFile[i] = b''.join((newFile[i][:48], binascii.unhexlify(keys[i]), newFile[i][54:]))
        pass
    newFile[0] = b''.join((newFile[0][:54], binascii.unhexlify("FF0780"), newFile[0][57:]))

    if not outputName:
        outputName = f'UID_{UID}_{skyPath[max(0, skyPath.rfind("/") + 1):]}'
    write_nfc_dump(outputName, newFile)

if __name__ == '__main__':
    run('07EB92D6', 'defaultInput.dump')
    pass
