
class TestData:

    def __init__(self) -> None:
        self._test_name = ""
        self._feature_name = ""
        self._device = ""

    @property
    def test_name(self):
        return self._test_name
    
    @test_name.setter
    def test_name(self, name):
        self._test_name = name

    @property
    def feature_name(self):
        return self._feature_name
    
    @feature_name.setter
    def feature_name(self, name):
        self._feature_name = name

    @property
    def device(self):
        return self._device
    
    @device.setter
    def feature_name(self, device):
        self._device = device
