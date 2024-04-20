import ctypes

from . import evp

CIPHER_ALGORITHMS = ("DES", "DES-EDE3", "BF", "AES-128", "AES-192", "AES-256")
CIPHER_MODES = ("CBC", "CFB", "OFB", "ECB")


class CipherError(Exception):
    pass


class CipherType(ctypes.Structure):
    _fields_ = evp._cipher_fields

    @classmethod
    def from_name(cls, *cipher_name):
        """
        Create a CipherType from a cipher name.

        Takes one or two parameters. If one is supplied, it should be
        a dash-separated string of algorithm-mode.
        If two are supplied, they should be the algorithm and mode.
        """
        cipher_name = "-".join(cipher_name)
        algorithm, mode = cipher_name.rsplit("-", 1)
        assert algorithm in CIPHER_ALGORITHMS, f"Unknown algorithm {algorithm}"
        assert mode in CIPHER_MODES, f"Unknown mode {mode}"
        res = evp.get_cipherbyname(cipher_name.encode("ascii"))
        if not res:
            raise CipherError(f"Unknown cipher: {cipher_name}")
        res.contents.algorithm, res.contents.mode = algorithm, mode
        return res.contents


class Cipher(ctypes.Structure):
    _fields_ = evp._cipher_context_fields
    finalized = False

    def __new__(cls, *a, **kw):
        return evp.lib.EVP_CIPHER_CTX_new().contents

    def __del__(self):
        evp.lib.EVP_CIPHER_CTX_free(self)

    def __init__(self, type, key, iv, encrypt=True):
        key = key.encode("ascii")
        iv = iv.encode("ascii")
        engine = None
        type = self.interpret_type(type)
        res = evp.CipherInit_ex(self, type, engine, key, iv, encrypt)
        if res == 0:
            raise CipherError(f"Unable to initialize cipher: {evp.get_error()}")
        self.out_data = []

    @staticmethod
    def interpret_type(type):
        if not isinstance(type, CipherType):
            if not hasattr(type, "__iter__"):
                type = [type]
            type = CipherType.from_name(*type)
        return type

    def set_padding(self, padding=True):
        evp.CIPHER_CTX_set_padding(self, padding)

    def update(self, data):
        """
        From docs:
        EVP_EncryptUpdate() encrypts inl bytes from the
        buffer in and writes the encrypted version to out.
        This function can be called multiple times to
        encrypt successive blocks of data. The amount of
        data written depends on the block alignment of the
        encrypted data: as a result the amount of data
        written may be anything from zero bytes to
        (inl + cipher_block_size - 1) so outl should
        contain sufficient room. The actual number of
        bytes written is placed in outl.
        """
        if self.finalized:
            raise CipherError("No updates allowed")
        if isinstance(data, str):
            data = data.encode()
        out = ctypes.create_string_buffer(len(data) + evp.MAX_BLOCK_LENGTH - 1)
        out_len = ctypes.c_int()

        res = evp.CipherUpdate(self, out, out_len, data, len(data))
        if res != 1:
            raise CipherError(f"Error updating cipher: {evp.get_error()}")
        self.out_data.append(out.raw[: out_len.value])

    def finalize(self, data=None):
        if data is not None:
            self.update(data)
        self.finalized = True
        out = ctypes.create_string_buffer(evp.MAX_BLOCK_LENGTH)
        out_len = ctypes.c_int()
        res = evp.CipherFinal_ex(self, out, out_len)
        if res != 1:
            raise CipherError(f"Error finalizing cipher: {evp.get_error()}")
        self.out_data.append(out.raw[: out_len.value])
        self.finalize = lambda: "".join(self.out_data)
        return b"".join(self.out_data)


evp.get_cipherbyname.argtypes = (ctypes.c_char_p,)  # type: ignore
evp.get_cipherbyname.restype = ctypes.POINTER(CipherType)  # type: ignore


# https://www.openssl.org/docs/man3.1/man3/EVP_CipherInit_ex.html

_init_args = (
    ctypes.POINTER(Cipher),  # ctx
    ctypes.POINTER(CipherType),  # type
    ctypes.c_void_p,  # impl
    ctypes.c_char_p,  # key
    ctypes.c_char_p,  # iv
    ctypes.c_int,  # enc
)
_update_args = (
    ctypes.POINTER(Cipher),  # ctx
    ctypes.c_char_p,  # out
    ctypes.POINTER(ctypes.c_int),  # outl
    ctypes.c_char_p,  # in
    ctypes.c_int,  # inl
)
_final_args = (
    ctypes.POINTER(Cipher),  # ctx
    ctypes.c_char_p,  # out[m]
    ctypes.POINTER(ctypes.c_int),  # outl
)
evp.EncryptInit_ex.argtypes = (  # type: ignore
    evp.DecryptInit_ex.argtypes  # type: ignore
) = _init_args[:2] + _init_args[3:5]
evp.CipherInit_ex.argtypes = _init_args  # type: ignore
evp.EncryptUpdate.argtypes = (  # type: ignore
    evp.DecryptUpdate.argtypes  # type: ignore
) = evp.CipherUpdate.argtypes = _update_args  # type: ignore
evp.EncryptFinal_ex.argtypes = (  # type: ignore
    evp.DecryptFinal_ex.argtypes  # type: ignore
) = evp.CipherFinal_ex.argtypes = _final_args  # type: ignore

evp.lib.EVP_CIPHER_CTX_new.argtypes = None
evp.lib.EVP_CIPHER_CTX_new.restype = ctypes.POINTER(Cipher)

evp.lib.EVP_CIPHER_CTX_free.argtypes = (ctypes.POINTER(Cipher),)
evp.lib.EVP_CIPHER_CTX_free.restype = None
