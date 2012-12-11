
class OutputFormat (object):
    
    def __init__ (self, service):
        self._service = service
    
    @property
    def service(self):
        return self._service
    
    def encode(self): pass
    def get_capabilities(self): pass
    def describe_feature_type(self): pass
