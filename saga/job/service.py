# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Andre Merzky"
__copyright__ = "Copyright 2012, The SAGA Project"
__license__   = "MIT"

""" SAGA job service interface
"""


from saga.engine.logger   import getLogger
from saga.engine.engine   import getEngine, ANY_ADAPTOR
from saga.task            import SYNC, ASYNC, TASK
from saga.url             import Url
from saga.job.description import Description



# class Service (Object, Async) :
class Service (object) :
    """ The job.Service represents a resource management backend, and as 
        such allows the creation, submision and management of jobs.

        :param rm_url:  resource manager URL
        :type  rm_url:  string or :class:`saga.Url`
        :param session: an optional session object with security contexts
        :type  session: :class:`saga.Session`
        :rtype:         :class:`saga.job.Service`


    """
    def __init__ (self, rm_url=None, session=None) : 
        """ Create a new job.Service instance.
        """

        rm = Url (rm_url)

        self._engine  = getEngine ()
        self._logger  = getLogger ('saga.job.Service')
        self._logger.debug ("saga.job.Service.__init__ (%s, %s)"  \
                         % (str(rm), str(session)))

        self._adaptor = self._engine.get_adaptor (self, 'saga.job.Service', rm.scheme, \
                                                  None, ANY_ADAPTOR, rm, session)


    @classmethod
    def create (self, rm_url=None, session=None, ttype=None) :
        """ Create a new job.Service intance asynchronously.

            :param rm_url:  resource manager URL
            :type  rm_url:  string or :class:`saga.Url`
            :param session: an optional session object with security contexts
            :type  session: :class:`saga.Session`
            :rtype:         :class:`saga.Task`
        """
    
        rm = Url (rm_url)

        engine = getEngine ()
        logger = getLogger ('saga.job.Service')
        logger.debug ("saga.job.Service.create(%s, %s, %s)"  \
                   % (str(rm), str(session), str(ttype)))
    
        # attempt to find a suitable adaptor, which will call 
        # init_instance_async(), which returns a task as expected.
        return engine.get_adaptor (self, 'saga.job.Service', rm.scheme, \
                                   ttype, ANY_ADAPTOR, rm, session)


    def create_job (self, job_desc, ttype=None) :
        """ Create a new job.Job instance from a 
            :class:`~saga.job.Description`. The resulting job instance
            is in :data:`~saga.job.NEW` state. 

            :param job_desc: job description to create the job from
            :type job_desc:  :data:`saga.job.Description`
            :param ttype: |param_ttype|
            :rtype:       :class:`saga.job.Job` or |rtype_ttype|
        """
        jd_copy = Description()
        job_desc._attributes_deep_copy (jd_copy)

        return self._adaptor.create_job (jd_copy, ttype=ttype)


    def run_job (self, cmd, host="", ttype=None) :
        '''
        ** NOT IMPLEMENTED**

        cmd:       string
        host:      string
        ttype:     saga.task.type enum
        ret:       saga.job.Job / saga.Task
        '''
        return self._adaptor.run_job (cmd, host, ttype=ttype)


    def list (self, ttype=None) :
        '''
        ttype:     saga.task.type enum
        ret:       list [string] / saga.Task
        '''
        return self._adaptor.list (ttype=ttype)


    def get_url (self, ttype=None) :
        '''
        ttype:     saga.task.type enum
        ret:       saga.job.Job / saga.Task
        '''
        return self._adaptor.get_url (ttype=ttype)


    def get_job (self, job_id, ttype=None) :
        '''
        job_id:    string
        ttype:     saga.task.type enum
        ret:       saga.job.Job / saga.Task
        '''
        return self._adaptor.get_job (job_id, ttype=ttype)


    def get_self (self,ttype=None) :
        '''
        ttype:     saga.task.type enum
        ret:       saga.job.Self / saga.Task
        '''
        return self._adaptor.get_self (ttype=ttype)


    jobs = property (list)      # list [saga.job.Job]    # FIXME: dict {string id : saga.job.Job} ?
    self = property (get_self)  # saga.job.Self

