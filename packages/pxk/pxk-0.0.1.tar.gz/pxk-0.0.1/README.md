# Pytest-xdist-kubernetes
  
The pytest-xdist-plugin extends pytest-xdist with new kubernetes pod communication. It is capable of creating Kubernetes deployment using the given namespace and docker image, run tests from pods, and display the result at the end from the terminal.  

## How to Install
In order to use the plugin, >= Python 3.9 is required. Can be installed with the following command:  
```bash
pip install pytest-xdist-kubernetes
```

## How to Use
By giving <code>--tx='pod'</code> as part of the xdist command, it triggers Pytest-xdist-kubernetes plugin.
```bash
pytest {test files to run} -n {number of pods per deployment} --tx='pod'
```
On top of the existing pytest-xdist library, various options have been added to support running tests from kubernetes pods remotely.
```bash
pytest --namespace='custom namspace' --custom_image='custom image' {test files to run} -n {number of pods per deployment} --tx='pod'
```
Logger is included as part of the functions added by the plugin. You can check the progress of the plugin by specifying:
```bash
--log-cli-level INFO
```  
Since the plugin relies on xdist library's task scheduler for distributing tasks, you can specify how you would like to distribute tasks across multiple pods. By default, it evenly distributes test files.  
But if you would like each pod to run all the specified test files:
```bash
pytest {testfiles to run} -n {number of pods per deployment} --tx='pod' --dist=each
```

## Reference
The plugin uses Kubernetes API to create/delete kubernetes deployments.  
https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md