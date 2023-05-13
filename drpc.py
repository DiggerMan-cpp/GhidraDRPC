import pypresence
import time
import ghidra
from ghidra.util.task import TaskMonitor

Discord RPC
client_id = 'tyt id'
RPC = pypresence.Presence(client_id)
RPC.connect()

current_program = ghidra.program.model.listing.ProgramManager.getCurrentProgram()

Discord RPC
RPC.update(
    details="Ghidra Disassembler",
    state="Working on " + current_program.getName(),
    large_image="ghidra_logo",
    large_text="Ghidra",
    small_image="python_logo",
    small_text="Python"
)

task_monitor = TaskMonitor.DUMMY
while not task_monitor.isCancelled():
    if RPC.update_time + 15 < time.time():
        RPC.update(
            details="Ghidra Disassembler",
            state="Working on " + current_program.getName(),
            large_image="ghidra_logo",
            large_text="Ghidra",
            small_image="python_logo",
            small_text="Python"
        )
    time.sleep(15)

Discord RPC
RPC.close()
