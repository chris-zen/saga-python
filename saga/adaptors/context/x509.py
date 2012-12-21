
import os

from   saga.utils.singleton import Singleton

import saga.cpi.base
import saga.cpi.context

SYNC  = saga.cpi.base.sync
ASYNC = saga.cpi.base.async


######################################################################
#
# adaptor meta data
#
_adaptor_schema   = 'X509'
_adaptor_name     = 'saga.adaptor.x509'
_adaptor_options  = []
_adaptor_info     = {
    'name'        : _adaptor_name,
    'cpis'        : [{ 
        'type'    : 'saga.Context',
        'class'   : 'ContextX509',
        'schemas' : [_adaptor_schema]
        }
    ]
}


###############################################################################
# The adaptor class

class Adaptor (saga.cpi.base.AdaptorBase):
    """ 
    This is the actual adaptor class, which gets loaded by SAGA (i.e. by the
    SAGA engine), and which registers the CPI implementation classes which
    provide the adaptor's functionality.

    We only need one instance of this adaptor per process (actually per engine,
    but engine is a singleton, too...) -- the engine will though create new CPI
    implementation instances as needed (one per SAGA API object).
    """

    __metaclass__ = Singleton


    def __init__ (self) :

        saga.cpi.base.AdaptorBase.__init__ (self, _adaptor_name, _adaptor_options)


    def register (self) :
        """ Adaptor registration function. The engine calls this during startup. 
    
            We usually do sanity checks here and throw and exception if we think
            the adaptor won't work in a given environment. In that case, the
            engine won't add it to it's internal list of adaptors. If everything
            is ok, we return the adaptor info.
        """
    
        return _adaptor_info


######################################################################
#
# job adaptor class
#
class ContextX509 (saga.cpi.Context) :

    def __init__ (self, api) :
        saga.cpi.Base.__init__ (self, api, _adaptor_name)


    @SYNC
    def init_instance (self, type) :

        if type.lower () != _adaptor_schema.lower () :
            raise saga.exceptions.BadParameter \
                    ("the x509 context adaptor only handles x509 contexts - duh!")

        self._api.type = type


    @SYNC
    def _initialize (self, session) :

        # make sure we have can access the proxy
        api = self._get_api ()

        if api.user_proxy :
            if not os.path.exists (api.user_proxy) or \
               not os.path.isfile (api.user_proxy)    :
                raise saga.exceptions.BadParameter ("X509 proxy does not exist: %s"
                                                 % api.user_proxy)

        try :
            fh = open (api.user_proxy)
        except Exception as e:
            raise saga.exceptions.PermissionDenied ("X509 proxy '%s' not readable: %s"
                                                 % (api.user_proxy, str(e)))
        else :
            fh.close ()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
