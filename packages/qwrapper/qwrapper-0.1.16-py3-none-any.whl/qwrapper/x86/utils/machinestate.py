from qemu.qmp import QMPClient



async def reset_machine():
    # Reset the virtual machine

    pass

async def stop_machine():
    # This stops/pauses the virtual machine execution.
    qmp = QMPClient('x86')
    await qmp.connect('/tmp/qmp.socket')
    res = await qmp.execute("stop")
    print(res)

async def reset_machine():
    qmp = QMPClient('x86')
    await qmp.connect('/tmp/qmp.socket')
    res = await qmp.execute("system_reset")
    print(res)

async def start_machine():
    # This starts/resumes the virtual machine execution
    qmp = QMPClient('x86')
    await qmp.connect('/tmp/qmp.socket')
    res = await qmp.execute("cont")
    pass


async def get_machine_state():
    # Returns the state of the machine ("paused" or "running")
    qmp = QMPClient('x86')
    await qmp.connect('/tmp/qmp.socket')
    res = await qmp.execute('human-monitor-command', {'command-line' : 'info status'})
    if ("running" in res):
        return "running"
    elif ("paused" in res):
        return "paused"
    else: 
        return None