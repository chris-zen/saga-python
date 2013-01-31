
import gc
import os
import sys
import time
import saga
import pprint
import cProfile

import subprocess

import threading

def get_mem () :

    pid     = os.getpid()
    process = subprocess.Popen ("ps h -p %s -o rss" % pid,
                                shell=True, stdout=subprocess.PIPE)
    stdout_list = process.communicate ()[0].split('\n')
    return stdout_list[0]
    return 0

jobcount = 0

def workload (url, n_jobs) :

    jd   = saga.job.Description ()
    jd.executable = '/bin/date'
    
    service = saga.job.Service (url)

    for id in range (1, n_jobs+1) :
        tmp_j     = service.create_job (jd)
        tmp_j.run ()
        print "%5d : %s" % (id, tmp_j.id)
      # time.sleep (1)

  # sys.stdout.write ('\n')
    del (service)


def perf (n_jobs, urls) :

    try :

        s = saga.Session ()

        start      = time.time ()
        threads    = []
        n_services = len(urls)

        for url in urls :
            thread = threading.Thread (target=workload, args=[url, n_jobs//n_services])
            thread.start ()
            threads.append (thread)

        for thread in threads :
            thread.join ()

        stop = time.time ()
        print "-----------------------------------------------"
        print "services: %s" % (n_services)
        print "jobs    : %s" % (n_jobs)
        print "time    : %s" % (stop - start)
        print "jobs/sec: %s" % (n_jobs / (stop - start))
        print "memory  : %s" % (get_mem ())
            
    except saga.exceptions.SagaException as e :
        print "Exception: ==========\n%s"  %  e.get_message ()
        print "%s====================="    %  e.get_traceback ()


# cProfile.run('main()', 'test_perf.prof')
# perf (10000, 10*['ssh://merzky@localhost/'] + 10*['ssh://amerzky@cyder.cct.lsu.edu/']+ 10*['ssh://merzky@repex1.tacc.utexas.edu/'])

# perf (    1,  1*['ssh://merzky@localhost/'])
# perf (    1,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])

perf (  10,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
perf (  10,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
perf (  10,  1*['ssh://localhost/'])
perf (  10,  1*['fork://localhost/'])
perf (  10,  1*['gsissh://tg-login.ranger.tacc.teragrid.org/'])

# perf (  100,  1*['ssh://merzky@localhost/'])

# perf (    0,  1*['ssh://merzky@localhost/'])
# perf (    1,  1*['ssh://merzky@localhost/'])
# perf (    2,  1*['ssh://merzky@localhost/'])
# perf (    4,  1*['ssh://merzky@localhost/'])
# perf (    8,  1*['ssh://merzky@localhost/'])
# perf (   16,  1*['ssh://merzky@localhost/'])
# perf (   32,  1*['ssh://merzky@localhost/'])
# perf (   64,  1*['ssh://merzky@localhost/'])
# perf (  128,  1*['ssh://merzky@localhost/'])
# perf (  256,  1*['ssh://merzky@localhost/'])
# perf (  512,  1*['ssh://merzky@localhost/'])
# perf ( 1024,  1*['ssh://merzky@localhost/'])
# perf ( 2048,  1*['ssh://merzky@localhost/'])
# perf ( 4096,  1*['ssh://merzky@localhost/'])
# perf ( 8192,  1*['ssh://merzky@localhost/'])
# perf (16384,  1*['ssh://merzky@localhost/'])
# perf (32768,  1*['ssh://merzky@localhost/'])
# perf (    0,  2*['ssh://merzky@localhost/'])
# perf (    1,  2*['ssh://merzky@localhost/'])
# perf (    2,  2*['ssh://merzky@localhost/'])
# perf (    4,  2*['ssh://merzky@localhost/'])
# perf (    8,  2*['ssh://merzky@localhost/'])
# perf (   16,  2*['ssh://merzky@localhost/'])
# perf (   32,  2*['ssh://merzky@localhost/'])
# perf (   64,  2*['ssh://merzky@localhost/'])
# perf (  128,  2*['ssh://merzky@localhost/'])
# perf (  256,  2*['ssh://merzky@localhost/'])
# perf (  512,  2*['ssh://merzky@localhost/'])
# perf ( 1024,  2*['ssh://merzky@localhost/'])
# perf ( 2048,  2*['ssh://merzky@localhost/'])
# perf ( 4096,  2*['ssh://merzky@localhost/'])
# perf ( 8192,  2*['ssh://merzky@localhost/'])
# perf (16384,  2*['ssh://merzky@localhost/'])
# perf (32768,  2*['ssh://merzky@localhost/'])
# perf (    0,  3*['ssh://merzky@localhost/'])
# perf (    1,  3*['ssh://merzky@localhost/'])
# perf (    2,  3*['ssh://merzky@localhost/'])
# perf (    4,  3*['ssh://merzky@localhost/'])
# perf (    8,  3*['ssh://merzky@localhost/'])
# perf (   16,  3*['ssh://merzky@localhost/'])
# perf (   32,  3*['ssh://merzky@localhost/'])
# perf (   64,  3*['ssh://merzky@localhost/'])
# perf (  128,  3*['ssh://merzky@localhost/'])
# perf (  256,  3*['ssh://merzky@localhost/'])
# perf (  512,  3*['ssh://merzky@localhost/'])
# perf ( 1024,  3*['ssh://merzky@localhost/'])
# perf ( 2048,  3*['ssh://merzky@localhost/'])
# perf ( 4096,  3*['ssh://merzky@localhost/'])
# perf ( 8192,  3*['ssh://merzky@localhost/'])
# perf (16384,  3*['ssh://merzky@localhost/'])
# perf (32768,  3*['ssh://merzky@localhost/'])
# perf (    0,  4*['ssh://merzky@localhost/'])
# perf (    1,  4*['ssh://merzky@localhost/'])
# perf (    2,  4*['ssh://merzky@localhost/'])
# perf (    4,  4*['ssh://merzky@localhost/'])
# perf (    8,  4*['ssh://merzky@localhost/'])
# perf (   16,  4*['ssh://merzky@localhost/'])
# perf (   32,  4*['ssh://merzky@localhost/'])
# perf (   64,  4*['ssh://merzky@localhost/'])
# perf (  128,  4*['ssh://merzky@localhost/'])
# perf (  256,  4*['ssh://merzky@localhost/'])
# perf (  512,  4*['ssh://merzky@localhost/'])
# perf ( 1024,  4*['ssh://merzky@localhost/'])
# perf ( 2048,  4*['ssh://merzky@localhost/'])
# perf ( 4096,  4*['ssh://merzky@localhost/'])
# perf ( 8192,  4*['ssh://merzky@localhost/'])
# perf (16384,  4*['ssh://merzky@localhost/'])
# perf (32768,  4*['ssh://merzky@localhost/'])
# perf (    0,  5*['ssh://merzky@localhost/'])
# perf (    1,  5*['ssh://merzky@localhost/'])
# perf (    2,  5*['ssh://merzky@localhost/'])
# perf (    4,  5*['ssh://merzky@localhost/'])
# perf (    8,  5*['ssh://merzky@localhost/'])
# perf (   16,  5*['ssh://merzky@localhost/'])
# perf (   32,  5*['ssh://merzky@localhost/'])
# perf (   64,  5*['ssh://merzky@localhost/'])
# perf (  128,  5*['ssh://merzky@localhost/'])
# perf (  256,  5*['ssh://merzky@localhost/'])
# perf (  512,  5*['ssh://merzky@localhost/'])
# perf ( 1024,  5*['ssh://merzky@localhost/'])
# perf ( 2048,  5*['ssh://merzky@localhost/'])
# perf ( 4096,  5*['ssh://merzky@localhost/'])
# perf ( 8192,  5*['ssh://merzky@localhost/'])
# perf (16384,  5*['ssh://merzky@localhost/'])
# perf (32768,  5*['ssh://merzky@localhost/'])
# perf (    0,  6*['ssh://merzky@localhost/'])
# perf (    1,  6*['ssh://merzky@localhost/'])
# perf (    2,  6*['ssh://merzky@localhost/'])
# perf (    4,  6*['ssh://merzky@localhost/'])
# perf (    8,  6*['ssh://merzky@localhost/'])
# perf (   16,  6*['ssh://merzky@localhost/'])
# perf (   32,  6*['ssh://merzky@localhost/'])
# perf (   64,  6*['ssh://merzky@localhost/'])
# perf (  128,  6*['ssh://merzky@localhost/'])
# perf (  256,  6*['ssh://merzky@localhost/'])
# perf (  512,  6*['ssh://merzky@localhost/'])
# perf ( 1024,  6*['ssh://merzky@localhost/'])
# perf ( 2048,  6*['ssh://merzky@localhost/'])
# perf ( 4096,  6*['ssh://merzky@localhost/'])
# perf ( 8192,  6*['ssh://merzky@localhost/'])
# perf (16384,  6*['ssh://merzky@localhost/'])
# perf (32768,  6*['ssh://merzky@localhost/'])
# perf (    0,  7*['ssh://merzky@localhost/'])
# perf (    1,  7*['ssh://merzky@localhost/'])
# perf (    2,  7*['ssh://merzky@localhost/'])
# perf (    4,  7*['ssh://merzky@localhost/'])
# perf (    8,  7*['ssh://merzky@localhost/'])
# perf (   16,  7*['ssh://merzky@localhost/'])
# perf (   32,  7*['ssh://merzky@localhost/'])
# perf (   64,  7*['ssh://merzky@localhost/'])
# perf (  128,  7*['ssh://merzky@localhost/'])
# perf (  256,  7*['ssh://merzky@localhost/'])
# perf (  512,  7*['ssh://merzky@localhost/'])
# perf ( 1024,  7*['ssh://merzky@localhost/'])
# perf ( 2048,  7*['ssh://merzky@localhost/'])
# perf ( 4096,  7*['ssh://merzky@localhost/'])
# perf ( 8192,  7*['ssh://merzky@localhost/'])
# perf (16384,  7*['ssh://merzky@localhost/'])
# perf (32768,  7*['ssh://merzky@localhost/'])
# perf (    0,  8*['ssh://merzky@localhost/'])
# perf (    1,  8*['ssh://merzky@localhost/'])
# perf (    2,  8*['ssh://merzky@localhost/'])
# perf (    4,  8*['ssh://merzky@localhost/'])
# perf (    8,  8*['ssh://merzky@localhost/'])
# perf (   16,  8*['ssh://merzky@localhost/'])
# perf (   32,  8*['ssh://merzky@localhost/'])
# perf (   64,  8*['ssh://merzky@localhost/'])
# perf (  128,  8*['ssh://merzky@localhost/'])
# perf (  256,  8*['ssh://merzky@localhost/'])
# perf (  512,  8*['ssh://merzky@localhost/'])
# perf ( 1024,  8*['ssh://merzky@localhost/'])
# perf ( 2048,  8*['ssh://merzky@localhost/'])
# perf ( 4096,  8*['ssh://merzky@localhost/'])
# perf ( 8192,  8*['ssh://merzky@localhost/'])
# perf (16384,  8*['ssh://merzky@localhost/'])
# perf (32768,  8*['ssh://merzky@localhost/'])
# perf (    0,  9*['ssh://merzky@localhost/'])
# perf (    1,  9*['ssh://merzky@localhost/'])
# perf (    2,  9*['ssh://merzky@localhost/'])
# perf (    4,  9*['ssh://merzky@localhost/'])
# perf (    8,  9*['ssh://merzky@localhost/'])
# perf (   16,  9*['ssh://merzky@localhost/'])
# perf (   32,  9*['ssh://merzky@localhost/'])
# perf (   64,  9*['ssh://merzky@localhost/'])
# perf (  128,  9*['ssh://merzky@localhost/'])
# perf (  256,  9*['ssh://merzky@localhost/'])
# perf (  512,  9*['ssh://merzky@localhost/'])
# perf ( 1024,  9*['ssh://merzky@localhost/'])
# perf ( 2048,  9*['ssh://merzky@localhost/'])
# perf ( 4096,  9*['ssh://merzky@localhost/'])
# perf ( 8192,  9*['ssh://merzky@localhost/'])
# perf (16384,  9*['ssh://merzky@localhost/'])
# perf (32768,  9*['ssh://merzky@localhost/'])
# perf (    0, 10*['ssh://merzky@localhost/'])
# perf (    1, 10*['ssh://merzky@localhost/'])
# perf (    2, 10*['ssh://merzky@localhost/'])
# perf (    4, 10*['ssh://merzky@localhost/'])
# perf (    8, 10*['ssh://merzky@localhost/'])
# perf (   16, 10*['ssh://merzky@localhost/'])
# perf (   32, 10*['ssh://merzky@localhost/'])
# perf (   64, 10*['ssh://merzky@localhost/'])
# perf (  128, 10*['ssh://merzky@localhost/'])
# perf (  256, 10*['ssh://merzky@localhost/'])
# perf (  512, 10*['ssh://merzky@localhost/'])
# perf ( 1024, 10*['ssh://merzky@localhost/'])
# perf ( 2048, 10*['ssh://merzky@localhost/'])
# perf ( 4096, 10*['ssh://merzky@localhost/'])
# perf ( 8192, 10*['ssh://merzky@localhost/'])
# perf (16384, 10*['ssh://merzky@localhost/'])
# perf (32768, 10*['ssh://merzky@localhost/'])
# 
# 
# perf (    0,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  1*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  2*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  3*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  4*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  5*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  6*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  7*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  8*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768,  9*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    0, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    1, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    2, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    4, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (    8, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   16, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   32, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (   64, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  128, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  256, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (  512, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 1024, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 2048, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 4096, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf ( 8192, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (16384, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# perf (32768, 10*['ssh://amerzky@cyder.cct.lsu.edu/'])
# 
# 
# perf (    0,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  1*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  2*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  3*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  4*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  5*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  6*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  7*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  8*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768,  9*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    0, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    1, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    2, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    4, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (    8, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   16, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   32, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (   64, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  128, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  256, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (  512, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 1024, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 2048, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 4096, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf ( 8192, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (16384, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# perf (32768, 10*['ssh://merzky@repex1.tacc.utexas.edu/'])
# # 
# # 
# # # vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# # 
