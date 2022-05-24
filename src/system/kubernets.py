import os
import subprocess
import re
import time

####################################################################################
# Setting KUBECONFIG env
####################################################################################

def osexeccmd(command):
    stream = os.popen(command)
    output = stream.readlines()
    for line in output:
        print(line)

def setKubeConfig(configdata):
    kubeconfig = configdata['KUBERNETES']['CONFIG']
    os.environ['KUBECONFIG'] = kubeconfig
    KUBECONFIGENV = os.getenv('KUBECONFIG')
    print(KUBECONFIGENV)

def getcontext(configdata):
    command = '{} config get-contexts'.format(configdata['KUBERNETES']['KUBECTLPATH'])
    osexeccmd(command)

def getcurrentcontext(configdata):
    command = '{} config current-context'.format(configdata['KUBERNETES']['KUBECTLPATH'])
    osexeccmd(command)


def setcontext(configdata,context):
    command = '{} config use-context {}'.format(configdata['KUBERNETES']['KUBECTLPATH'],context)
    osexeccmd(command)

def getnamespaces(configdata):
    command = '{} get namespace'.format(configdata['KUBERNETES']['KUBECTLPATH'])
    osexeccmd(command)

def getpodsbynamespace(configdata,namespace):
    command = '{} get pods  -n {}'.format(configdata['KUBERNETES']['KUBECTLPATH'], namespace)
    osexeccmd(command)

def getlogsbydeployment(configdata,namespace,deployment,time='30m'):
    command = '{} -n {} logs Deployment/{} --all-containers=true --since={} >> {}'\
    .format(configdata['KUBERNETES']['KUBECTLPATH'], namespace, deployment,time,configdata['KUBERNETES']['LOGFILE'])
    print(command)
    osexeccmd(command)

    #webservices
#def getpods(configdata):
#    command = '{} get pods -n {namespace} -l app={app}'.format(configdata['KUBERNETES']['KUBECTLPATH'],namespace=namespace,app=app)
#    osexeccmd(command)

#def getLogsByDeployment():
#    log_ecommerce = '-n {} logs Deployment/{} --all-containers=true --since=5h >> '