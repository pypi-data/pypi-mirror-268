from stimulsoft_data_adapters.events.StiEvent import StiEvent
from stimulsoft_data_adapters.events.StiEventArgs import StiEventArgs

from ..classes.StiComponent import StiComponent


class StiComponentEvent(StiEvent):
    
### Private

    __component: StiComponent = None
    __isHtmlRendered: bool = False

    
### Protected

    def _applyFields(self, *args, **keywargs) -> StiEventArgs:
        eventArgs = super()._applyFields(*args, **keywargs)
        if isinstance(eventArgs, StiEventArgs):
            eventArgs.sender = self.component


### Properties

    @property
    def handler(self):
        return self.component.handler if self.component.handler != None else super().handler
    
    @property
    def component(self):
        return self.__component

### Public

    def getHtml(self, callback: bool = False, prevent: bool = False, process: bool = True, internal: bool = False) -> str:
        if (len(self) == 0 or self.__isHtmlRendered):
            return ''

        argsName = 'args';
        if internal:
            argsName += self.name[2:]
        
        eventValue = ''
        callbacksJS = [eventCallback for eventCallback in self.callbacks if type(eventCallback) == str]
        for eventCallback in callbacksJS:
            eventValue += f'if (typeof {eventCallback} === "function") {eventCallback}({argsName}); ' if eventCallback.isalnum() else eventCallback

        if internal:
            eventArgs = f'let {argsName} = {{ event: "{self.name[2:]}", sender: "{self.component.componentType}", report: {self.component.id} }}'
            return f'{eventArgs}\n{eventValue}\n'
        
        callbackValue = ', callback' if callback else ''
        preventValue = 'args.preventDefault = true; ' if prevent else ''
        processValue = f'Stimulsoft.handler.process(args{callbackValue}); ' if process else ('callback(); ' if callback else '')
        result = f'{self.component.id}.{self.name} = function (args{callbackValue}) {{ {preventValue}{eventValue}{processValue}}}\n'
        
        self.__isHtmlRendered = True
        return result
    

### Constructor

    def __init__(self, component: StiComponent, name: str):
        super().__init__(component.handler, name)
        self.__component = component