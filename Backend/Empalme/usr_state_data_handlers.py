from yangson.instance import InstanceRoute
from jetconf.handler_base import StateDataContainerHandler
from jetconf.data import BaseDatastore

class EnpalmeGetCosto(StateDataContainerHandler):
    def generate_node(self, node_ii: InstanceRoute, username: str, staging: bool):
        info ("Backend: Se accedió al recurso {}".format(node_ii))
        return 0


def register_state_handlers(ds: BaseDatastore):
    ietf_route = '/ietf-routing:routing/control-plane-protocols/' + \
                 'control-plane-protocol'
    handlers = [ EnpalmeGetCosto(ds, ietf_route + '/rpl'),]
    for handler in handlers:
        ds.handlers.state.register(handler)
