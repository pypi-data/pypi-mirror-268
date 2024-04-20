from qwrapper.qemumachine import QemuMachine
from .utils import registers
from .utils import machinestate
from .utils import debugging
from .utils import memory
from qemu.qmp import QMPClient
import pygdbmi.gdbcontroller as gdbcontroller
import time
import os
import subprocess
import asyncio

class X86Machine(QemuMachine):
        gdbControl = gdbcontroller.GdbController()
        gdbConnected = False
        qemuCmd = []
        QemuProcess = None

        def __init__(self, disk_images, qmpwait=False,):
            super().__init__()

            self.disk_counter = ord('a') # Initial disk value

            if qmpwait == True:
                self.qemuCmd = ['qemu-system-i386', '-display', 'none', '-S', '-s', '-qmp', 'unix:/tmp/qmp.socket,server=on,wait=on']
            if qmpwait == False:
                self.qemuCmd = ['qemu-system-i386', '-display', 'none', '-S', '-s', '-qmp', 'unix:/tmp/qmp.socket,server=on,wait=off']

            for image in disk_images:
                if self.disk_counter > ord('z'):
                    print("Error: Too many disk images")
                    break
                self.qemuCmd.append('-hd' + chr(self.disk_counter))
                self.qemuCmd.append(image)
                self.disk_counter += 1
            

            print("Setting up virtual machine...")
            # Start Qemu with gdb stub and QMP Server. Add the kernel and disk images.
            # Virtual machine starts in "wait" mode. Waits for user to start VM execution.
            self.QemuProcess = subprocess.Popen(self.qemuCmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Wait 2 seconds to allow QEMU to create the socket file
            time.sleep(2) 
        
        def __del__(self):
            self.cleanup()

        def stop(self):
            # Stop/pause the execution of virtual machine
            asyncio.run(machinestate.stop_machine())

        def reset(self):
            # Resets the virtual machine (does not resume execution)
            pass

        def start(self):
            # Start/resume the execution of the virtual machine
            asyncio.run(machinestate.start_machine())
        
        def set_breakpoint(self, symbol):
            status = asyncio.run(debugging.set_breakpoint(self.gdbControl, symbol))

        def get_state(self):
            state = asyncio.run(machinestate.get_machine_state())
            return state

        def cleanup(self):
            print("Shutting down QEMU machine and cleaning up...")
            if not self.QemuProcess is None:
                self.QemuProcess.terminate()
                self.QemuProcess.wait()
            
            # wait for any updates to the file system before checking 
            # and deleting the socket file.
            time.sleep(1)
            if (os.path.exists("/tmp/qmp.socket")):
                os.remove("/tmp/qmp.socket")
            print("QEMU machine has been shut down")
             

        # This function gets all the registers and returns a dictionary containing every register and the corresponding values.
        def get_all_registers(self):
            if self.QemuProcess.poll is None:
                print("QEMU process has not been initialised yet.")
                return None
            regs = asyncio.run(registers.get_all_cpu_registers())
            return regs
        
        def get_register(self, requested_register):
            if self.QemuProcess.poll is None:
                print("QEMU process has not been initialised yet.")
                return None
            register = asyncio.run(registers.get_register(requested_register))
            return register
        
        # Memory functionality

        def read_memory_bytes(self, startaddress, number_of_bytes):
            if self.QemuProcess.poll is None:
                print("QEMU process has not been initialised yet")
                return None
            memory_list = asyncio.run(memory.read_memory_bytes(startaddress, number_of_bytes))
            return memory_list

