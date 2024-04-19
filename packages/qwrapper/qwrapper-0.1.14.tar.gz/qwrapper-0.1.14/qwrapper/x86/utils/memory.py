from qemu.qmp import QMPClient
import re




def format_qemu_memory_output(output):
    memory_list = []
    for line in output.strip().split('\n'):
        elements = line.split(' ')[1:]
        memory_list.extend([elem for elem in elements if elem and ':' not in elem])

    # Remove escape characters before returning the memory list.
    memory_list = [elem.replace('\r', '').replace('\n', '') for elem in memory_list]
    memory_list = [re.sub(r'\x1b[^m]*m', '', elem) for elem in memory_list]
    return memory_list


async def read_memory_bytes(startaddress,number_of_bytes):
    qmp = QMPClient('x86')
    con_result = await qmp.connect("/tmp/qmp.socket")


    # Convert startaddress to a string in case it is passed as an integer
    if isinstance(startaddress, int):
        startaddress = hex(startaddress)

    if not startaddress.startswith('0x'):
        startaddress = '0x' + startaddress


    command_line = f'x /{number_of_bytes}bx {startaddress}'
    memory_output = await qmp.execute('human-monitor-command', {'command-line' : command_line})
    memory_list = format_qemu_memory_output(memory_output)


    return memory_list
