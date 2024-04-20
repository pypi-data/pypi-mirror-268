import pefile

from . import utils


def get_packed_status_and_reasons(file_path):
    packed = False
    reasons = []
    try:
        if not file_path.is_file():
            utils.warn(f"Not a valid file: {file_path}")
            return None, None
    except OSError as e:
        utils.warn(f"{e}")
        return None, None
    try:
        pe = pefile.PE(file_path, fast_load=True)
    except pefile.PEFormatError as e:
        if str(e) != "'The file is empty'":
            utils.warn(f"{e}: {file_path}")
        return None, None

    upx_type = is_upx_type(pe)
    if upx_type is True:
        packed = None
        reasons.append('UPX-type exe; packing status unknown')
    else:
        if packed_section_flags(pe) is True:
            packed = True
            reasons.extend(pe.get_warnings())
        if packed_mismatched_data_sizes(pe) is True:
            packed = True
            reasons.append('Reported size is less than actual size.')

    return packed, reasons


# def packed_peutils(pe): # incorrect result often given for installer EXEs.
#     return peutils.is_probably_packed(pe)


def packed_section_flags(pe):
    for s in pe.sections:
        if s.IMAGE_SCN_MEM_WRITE and s.IMAGE_SCN_MEM_EXECUTE:
            return True
    return False


def packed_mismatched_data_sizes(pe):
    rep_idata_size = pe.OPTIONAL_HEADER.SizeOfInitializedData
    rep_udata_size = pe.OPTIONAL_HEADER.SizeOfUninitializedData
    idata_sum, udata_sum = sum_pe_data_types(pe)
    if idata_sum is None and udata_sum is None:
        return False
    if not (rep_idata_size >= idata_sum and rep_udata_size >= udata_sum):
        # print(f"{rep_idata_size = }; {idata_sum = }")
        # print(f"{rep_udata_size = }; {udata_sum = }")
        return True
    return False


def is_upx_type(pe):
    return pe.sections[0].Name[:3] == b'UPX'


def sum_pe_data_types(pe):
    idata_size = 0
    udata_size = 0
    for s in pe.sections:
        if s.IMAGE_SCN_CNT_INITIALIZED_DATA:
            idata_size += s.SizeOfRawData
        elif s.IMAGE_SCN_CNT_UNINITIALIZED_DATA:
            udata_size += s.SizeOfRawData
    return idata_size, udata_size
