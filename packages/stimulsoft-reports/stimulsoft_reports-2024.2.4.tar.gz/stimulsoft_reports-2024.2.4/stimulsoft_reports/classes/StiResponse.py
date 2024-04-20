from stimulsoft_data_adapters.classes.StiBaseResponse import StiBaseResponse

from ..classes.StiFileResult import StiFileResult
from ..enums.StiDataType import StiDataType


class StiResponse(StiBaseResponse):
    
### Properties

    @property
    def mimetype(self) -> str:
        """Returns the mime-type for the handler response."""

        if (isinstance(self.result, StiFileResult)):
            if (self.result.dataType == StiDataType.JAVASCRIPT):
                return 'text/javascript'
            if (self.result.dataType == StiDataType.HTML):
                return 'text/html'
        
        return super().mimetype
    
    @property
    def data(self) -> bytes:
        """Returns the handler response as a byte array. When using encryption, the response will be encrypted and encoded into a Base64 string."""
        
        if (isinstance(self.result, StiFileResult)):
            return self.result.data
        
        return super().data