import c2pa
@staticmethod
def checksign(file_path):
    try:
        authenticode = c2pa.Authenticode.from_file(file_path)
        return authenticode.is_signed()
    except Exception:
        return False