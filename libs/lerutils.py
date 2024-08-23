def read_nfc_dump(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    sectors = [data[i:i + 64] for i in range(0, len(data), 64)]
    return sectors

def write_nfc_dump(file_path, sectors):
    with open(file_path, 'wb') as f:
        for sector in sectors:
            f.write(sector)

def zero_non_preserved_blocks(sectors):
    for sector_index, sector in enumerate(sectors):
        if sector_index == 0:
            continue

        blocks = [sector[i:i + 16] for i in range(0, len(sector), 16)]
        for block_index in range(4):
            if block_index != 3:
                blocks[block_index] = bytes(16)
        sectors[sector_index] = b''.join(blocks)
    return sectors

def sectors2blocks(sectors):
    sk = []
    for sector in sectors:
        sc = []
        for i in range(4):
            sc.append(sector[i*16:(i+1)*16])
        pass
        sk.append(sc)
    return sk
    pass

def blocks2sectors(blocks):
    sk = []
    for sector in blocks:
        sk.append(b''.join(sector))
    return sk
    pass

def create_clear():
    return [b'\x00' * 64 for i in range(16)]
    pass


def calculate_bcc(uid_bytes):
    if len(uid_bytes) != 4:
        raise ValueError("UID must be exactly 4 bytes long.")

    bcc = 0
    for byte in uid_bytes:
        bcc ^= byte

    return bcc