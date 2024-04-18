
import segmentools.utils.metrics as M


def _available_metrics():
    """Return list of avalilabel metric classes.

    Returns:
        _type_: _description_
    """
    return [F1score, IoU, Accuracy]


class F1score(M.SegmentationMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(func = M.f1_score, name = "f1score", *args, **kwargs)

class Accuracy(M.SegmentationMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(func = M.accuracy, name = "accuracy", *args, **kwargs)
        
class IoU(M.SegmentationMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(func = M.iou, name = "iou", *args, **kwargs)
