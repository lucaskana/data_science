import os
import subprocess
import re
import time

####################################################################################
# Kubernetes Commands
####################################################################################

def osexeccmd(command):
    stream = os.popen(command)
    output = stream.readlines()
    return output

def setKubeConfig(kubeconfig):
    os.environ['KUBECONFIG'] = kubeconfig
    print(os.getenv('KUBECONFIG'))

def getcontext():
    command = 'kubectl config get-contexts'
    return osexeccmd(command)

def getcurrentcontext():
    command = 'kubectl config current-context'
    return osexeccmd(command)

def setcontext(context):
    command = 'kubectl config use-context {}'.format(context)
    return osexeccmd(command)

def getnamespaces():
    command = 'kubectl get namespace'
    return osexeccmd(command)

def getpodsbynamespace(namespace):
    command = 'kubectl get pods  -n {}'.format(namespace)
    return osexeccmd(command)

def getdeploymentsbynamespace(namespace):
    command = 'kubectl get deployments -o wide -n {}'.format(namespace)
    return osexeccmd(command)

def getdeployments():
    command = 'kubectl get deployments'
    return osexeccmd(command)

def getservices():
    command = 'kubectl get services'
    return osexeccmd(command)

def getservicesbynamespace(namespace):
    command = 'kubectl get services -n {}'.format(namespace)
    return osexeccmd(command)
    
def getlogsbydeployment(namespace,deployment,time='30m'):
    command = 'kubectl -n {} logs Deployment/{} --all-containers=true --since={}'.format(namespace, deployment,time)
    return osexeccmd(command)

def getlogsbydeploymenttofile(namespace,deployment,logfile='kubernetes.log',time='30m'):
    command = 'kubectl -n {} logs Deployment/{} --all-containers=true --since={} >> {}'\
    .format(namespace, deployment,time,logfile)
    return osexeccmd(command)
