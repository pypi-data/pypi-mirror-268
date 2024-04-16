from ...interface import IData
from ...packer.trade.read_exc_product_param_data_packer import ReadExcProductParamDataPacker


class ReadExcProductParamData(IData):
    def __init__(self, exchange_id: str = '', product_id: str = ''):
        super().__init__(ReadExcProductParamDataPacker(self))
        self._ExchangeID: str = exchange_id
        self._ProductID: str = product_id
        self._DataList = []

    @property
    def ExchangeID(self):
        return self._ExchangeID

    @ExchangeID.setter
    def ExchangeID(self, value: str):
        self._ExchangeID = value

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, value: str):
        self._ProductID = value

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, value):
        self._DataList = value
