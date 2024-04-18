from dig_ass_ocr_protos.DigitalAssistantOCR_pb2_grpc import DigitalAssistantOCRStub
from dig_ass_ocr_protos.DigitalAssistantOCR_pb2 import DigitalAssistantOCRRequest, DigitalAssistantOCRResponse

from .abstract_client import AbstractClient

class OCRClient(AbstractClient):
    def __init__(self, address) -> None:
        super().__init__(address)
        self._stub = DigitalAssistantOCRStub(self._channel)

    def __call__(self, image: bytearray, pdf: bytearray):
        request = DigitalAssistantOCRRequest(Image=image, PDF=pdf)
        response: DigitalAssistantOCRResponse = self._stub.GetTextResponse(request)
        return response.Text
