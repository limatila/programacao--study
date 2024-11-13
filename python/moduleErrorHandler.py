#* Trying to install depedencies on runtime (easy way):
import asyncio

async def installPag():
    import os
    os.system("pip install pyautogui"); #? Never use 'start cmd', as it won't wait for the process.

async def tryImporting():
    try:
        import pyautogui as pag
    except ImportError:
        print("\n ---------------installing Pyautogui.---------------")
        await installPag()
        import pyautogui as pag
    finally:
        print("\n ---------------Pyautogui installed.---------------")
    return pag #So i can use in code, not that it won't be so nice highlighted, for it will become a Var.

#Main execution of code intended
async def mainRaw():
    pag = await tryImporting()
    pag.alert("Sucessfull") #Should be achieved

if __name__ == "__main__":
    asyncio.run(mainRaw())



#* Installing more effectively and adequatelly with Subprocess (hard, better way):
import subprocess as sub