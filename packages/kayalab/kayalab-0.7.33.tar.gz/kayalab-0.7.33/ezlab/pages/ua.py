import logging
from nicegui import app, ui, run

from ezlab.ezmeral.ezua import deploy, install, precheck
from ezlab.parameters import UA
from ezinfra.vms import prepare
from ezlab.utils import get_doc, get_fqdn


logger = logging.getLogger("ezlab.ui.ua")


async def runall_action():
    return await prepare_action() and await precheck_action() and await install_action() and await deploy_action()


async def prepare_action():
    orchestrator = app.storage.general[UA].get("orchestrator", None)
    controller = app.storage.general[UA].get("controller", None)
    workers = app.storage.general[UA].get("workers", None)

    if orchestrator is None or controller is None or workers is None or len(workers.split(",")) < 3:
        logger.warning("You have some hosts missing, make sure you have all roles filled in!")
        logger.debug(
            "Orchestrator: %s, Controller: %s, Workers: %s",
            orchestrator,
            controller,
            workers,
        )

    logger.info("Starting configuration for UA")
    app.storage.user["busy"] = True

    hosts = [orchestrator, controller]
    hosts.extend(workers.split(","))

    completed = 0

    for host in hosts:
        result = await run.io_bound(
            prepare,
            hostname=get_fqdn(host),
            hostip=host,
            settings=dict(app.storage.general["config"]),
            addhosts=[h for h in hosts if h != host],
            add_to_noproxy=f"{orchestrator},{controller},{workers}",
            prepare_for=UA,
            dryrun=app.storage.general["config"]["dryrun"],
        )
        if app.storage.general["config"]["dryrun"]:
            get_doc(result)
            completed += 1
        elif result:
            logger.info("[ %s ] ready: %s", host, result)
            completed += 1
        else:
            ui.notify(f"[{host}] preparation failed!", type="warning")

    app.storage.user["busy"] = False

    return True if completed == len(hosts) else False


async def precheck_action():
    logger.info("Running prechecks for UA")
    app.storage.user["busy"] = True

    result = await run.io_bound(precheck)
    logger.debug("RESULT: %s", result)

    app.storage.user["busy"] = False

    return result


async def install_action():
    logger.info("Starting UA installation")
    app.storage.user["busy"] = True
    result = await run.io_bound(install)

    logger.debug("RESULT: %s", result)

    app.storage.user["busy"] = False

    return result


async def deploy_action():
    logger.info("Deploying UA Applications")
    app.storage.user["busy"] = True
    result = await run.io_bound(deploy)

    logger.debug("RESULT: %s", result)

    app.storage.user["busy"] = False

    return result
