from model import ChienSiModel


def LayChienSiTuMa(Ma):
    try:
        chiensi = ChienSiModel.ChienSiModel.objects.get(Ma=Ma)
        return chiensi
    except:
        return None
