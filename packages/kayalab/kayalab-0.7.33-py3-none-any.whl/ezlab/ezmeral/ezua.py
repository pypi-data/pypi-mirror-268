from ezlab.parameters import *
from ezlab.utils import *


logger = logging.getLogger("ezua")


def precheck():
    """Fabric pre-checks for roles"""

    write_precheck_yaml()

    # Results
    coordinator_ok = False
    compute_ok = False
    storage_ok = False
    proxy_ok = False
    dns_ok = False

    # output marker
    host = "LOCAL"
    role = ""

    for out in execute("./tmp/ezfabricctl pc -i ./tmp/prechecksInput.yaml -s ./tmp/prechecksStatus.txt"):
        if "Running checks for Ezmeral " in out:
            # should use regex but too lazy for it
            # extracting from string '***** Running checks for Ezmeral Unified Analytics role "worker" on host "vm23.kaya.home"'
            hostrole = out.split('role "')[1]
            role = hostrole.split('"')[0]
            host = hostrole.split('"')[2]

        logger.info("[ %s %s ]: %s", role.upper(), host, out)

        if "Additional information for debugging is written to" in out:
            # reset the host/role pair
            host = "LOCAL"
            role = ""

        # Check aggregate results

        if "Coordinator hosts: SUCCESS" in out:
            coordinator_ok = True

        if "Compute hosts: SUCCESS" in out:
            compute_ok = True

        if "Storage hosts: SUCCESS" in out:
            storage_ok = True

        if "Proxy settings: SUCCESS" in out:
            proxy_ok = True

        if "DNS settings: SUCCESS" in out:
            dns_ok = True

    return all([coordinator_ok, compute_ok, storage_ok, proxy_ok, dns_ok])


def install():
    """
    UA orchestrator installation
    """

    write_ezkf_input_yaml()

    result = False

    for out in execute(
        "./tmp/ezfabricctl o init -p ./tmp/ezfab-release.tgz -i ./tmp/ezkf-input.yaml -s ./tmp/ezkf-orch-status.txt --save-kubeconfig ./tmp/mgmt-kubeconfig"
    ):
        # ignore transfer messages, overloading UI
        if "Transferring to " not in out:
            logger.info(out)
            markword = "Save kubeconfig in "
            if markword in out:
                msg = out.split(markword)[1]
                APP_STATUS_CONTAINER.append(("Orchestrator Kubeconfig", msg.replace("./tmp", "/files", 1)))
                status_container.refresh()

    write_hostPoolConfig_yaml()

    for out in execute("./tmp/ezfabricctl ph i -i ./tmp/hostPoolConfig.yaml -c ./tmp/mgmt-kubeconfig -s ./tmp/hostPoolConfigStatus.txt"):
        logger.info(out)

    write_clusterConfig_yaml()

    for out in execute("./tmp/ezfabricctl w i -i ./tmp/clusterConfig.yaml -c ./tmp/mgmt-kubeconfig -s ./tmp/clusterConfigStatus.txt"):
        logger.info(out)

    for out in execute(
        "./tmp/ezfabricctl w g k -n ezlab -i ./tmp/clusterConfig.yaml -c ./tmp/mgmt-kubeconfig -s ./tmp/clusterConfigStatus.txt --save-kubeconfig ./tmp/workload-kubeconfig"
    ):
        logger.info(out)
        markword = "Fetched kubeconfig for "
        if markword in out:
            APP_STATUS_CONTAINER.append(("Workload Kubeconfig", "/files/workload-kubeconfig"))
            status_container.refresh()
            result = True

    return result


def deploy():

    write_ezkf_workloaddeploy_yaml()

    for out in execute("kubectl --kubeconfig=./tmp/workload-kubeconfig apply -f ./tmp/ezkfWorkloadDeploy.yaml"):
        logger.info(out)
        if "ezkfworkloaddeploy.ezkfops.hpe.ezkf-ops.com/ezlab" in out and any(i in out for i in ["created", "configured", "unchanged"]):
            # STATUS="kubectl --kubeconfig=./worker_kubeconfig get ezkfworkloaddeploy/$CLUSTER_NAME -n $CLUSTER_NAME -o json | jq -r '.status.status'"
            logger.info(
                """
                Monitor CR Status with:
                kubectl --kubeconfig=./tmp/workload-kubeconfig get ezkfworkloaddeploy/ezlab -n ezlab -o json | jq '.status.genericaddonsstatus | .[] | select(.installstatus == "INSTALLING")'
                """
            )

    return True


def write_precheck_yaml():
    """
    Write the file for prechecks
    """

    hosts_yaml = ""
    for host in app.storage.general[UA]["workers"].split(","):
        hosts_yaml += f"      - host: {host}\n"

    input = f"""defaultHostCredentials:
  sshUserName: {app.storage.general["config"]["username"]}
  sshPassword: {toB64(app.storage.general["config"]["password"])}
  sshPort: 22
sudoPrefix: ""
prechecks:
  coordinator:
    controlplane:
      - host: {app.storage.general[UA]["orchestrator"]}
  ua:
    controlplane:
      - host: {app.storage.general[UA]["controller"]}
    worker:
{hosts_yaml}"""

    with open("./tmp/prechecksInput.yaml", "wt") as f:
        f.write(input)


def write_ezkf_input_yaml():
    """
    Write the file for orchestrator deployment
    """

    input = f"""defaultHostCredentials:
  sshUserName: {app.storage.general["config"]["username"]}
  sshPassword: {toB64(app.storage.general["config"]["password"])}
  sshPort: 22
airgap:
  registryUrl: {app.storage.general[UA].get("registryUrl", "''")}
  registryInsecure: {app.storage.general[UA].get("registryInsecure", "true")}
orchestrator:
  deployTarget: pph
  controlPlane:
    enableHa: false
    externalUrl: ""
  network:
    pods:
      cidrBlocks: 10.224.0.0/16
    serviceDomain: cluster.local
    services:
      cidrBlocks: 10.96.0.0/12
hosts:
  - host: {app.storage.general[UA]["orchestrator"]}
webproxy:
  httpProxy: {app.storage.general["config"].get("proxy", "")}
  httpsProxy: {app.storage.general["config"].get("proxy","")}
  noProxy: {NO_PROXY.format(vm_domain=app.storage.general["config"]["domain"], vm_network=app.storage.general["config"]["cidr"],no_proxy=app.storage.general[UA].get("orchestrator", ""))}
"""
    with open("./tmp/ezkf-input.yaml", "wt") as f:
        f.write(input)


def write_hostPoolConfig_yaml():
    """ """
    workers = app.storage.general[UA]["workers"].split(",")
    input = f"""defaultHostCredentials:
  sshUserName: {app.storage.general["config"]["username"]}
  sshPassword: {toB64(app.storage.general["config"]["password"])}
  sshPort: 22
hosts:
  - host: {app.storage.general[UA]["controller"]}
    labels:
    - role: controlplane
  - host: {workers[0]}
    labels:
    - role: worker
  - host: {workers[1]}
    labels:
    - role: worker
  - host: {workers[2]}
    labels:
    - role: worker

"""
    with open("./tmp/hostPoolConfig.yaml", "wt") as f:
        f.write(input)


def write_clusterConfig_yaml():
    """
    Create cluster configuration for deployment
    """

    input = f"""workload:
  deployTarget: pph
  deployEnv: ezkube
  workloadType: ezua
  clusterName: ezlab
  resources:
    vcpu: 96
  controlPlaneHostLabels:
    role: controlplane
  workerHostLabels:
    role: worker
  dataFabricHostLabels:
    role: worker
  gpuHostLabels:
    role: worker
  clusterLabels: {{}}
  controlplane:
    enableHa: false
    controlPlaneEndpoint: {app.storage.general[UA]["controller"]}
  airgap:
    registryUrl: {app.storage.general[UA].get("registryUrl", "''")}
    registryInsecure: {app.storage.general[UA].get("registryInsecure", "true")}
  network:
    pods:
      cidrBlocks: "10.224.0.0/16"
    serviceDomain: "cluster.local"
    services:
      cidrBlocks: "10.96.0.0/12"

"""

    with open("./tmp/clusterConfig.yaml", "wt") as f:
        f.write(input)


def write_ezkf_workloaddeploy_yaml():
    """
    Write the file for UA apps deployment
    """

    AUTH_DATA = f"""{{
        "admin_user": {{
            "fullname": "Ezmeral Admin",
            "email": "ezadmin@{app.storage.general['config']['domain']}",
            "password": "{app.storage.general['config']['password']}",
            "username": "admin"
        }}
    }}
    """

    input = f"""
apiVersion: v1
data:
  registryCaFile: "{app.storage.general[UA].get("registryCaFile", "")}"
  userName: "{app.storage.general[UA].get("registryUsername", "")}"
  password: "{toB64(app.storage.general[UA].get("registryPassword", ""))}"
kind: Secret
metadata:
  name: airgap
  namespace: ezlab
type: Opaque

---
apiVersion: v1
data:
  internal_auth: {toB64(AUTH_DATA)}
kind: Secret
metadata:
  name: authconfig
  namespace: ezlab
type: Opaque


---
apiVersion: ezkfops.hpe.ezkf-ops.com/v1alpha1
kind: EzkfWorkloadDeploy
metadata:
  name: ezlab
  namespace: ezlab
spec:
  deploytarget: pph
  workloadtype: ezua
  clustername: ezlab
  domainname: ez.{app.storage.general["config"]["domain"]}
  isAirgap: false
  deployallinfra: true
  genericaddons:
    machine: true
    ezkube: true
  proxy:
    httpProxy: {app.storage.general["config"].get("proxy", "")}
    httpsProxy: {app.storage.general["config"].get("proxy", "")}
    noProxy: {NO_PROXY.format(vm_domain=app.storage.general["config"]["domain"], vm_network=app.storage.general["config"]["cidr"],no_proxy=app.storage.general[UA].get("orchestrator", ""))}
  workloadaddons:
    ua_prep: true
    hpecp_agent: true
    oidc: true
    kyverno: true
    monitoring: true
    keycloak: true
    chartmuseum: true
    ezaf_controller: true
  deployallapps: true # always set to true from UA
  authconfig:
    secret_name: "authconfig"
  airgap:
    secret_name: "airgap"
    registryUrl: {app.storage.general[UA].get("registryUrl", "''")}
    registryInsecure: {app.storage.general[UA].get("registryInsecure", "true")}

"""

    with open("./tmp/ezkfWorkloadDeploy.yaml", "wt") as f:
        f.write(input)
