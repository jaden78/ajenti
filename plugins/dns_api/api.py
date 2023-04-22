from jadi import interface


@interface
class ApiDnsManager():
    """
    Abstract interface to manage all DNS API providers.
    """

    id = None
    name = None

    def get_domains(self):
        raise NotImplementedError

    def get_records(self, _id):
        raise NotImplementedError