from __future__ import print_function
import json
import importlib.machinery
import importlib.util

loader = importlib.machinery.SourceFileLoader('WalabotAPI',
                                              'C:/Program Files/Walabot/WalabotSDK/python/WalabotAPI.py')
spec = importlib.util.spec_from_loader(loader.name, loader)
WalabotAPI = importlib.util.module_from_spec(spec)
loader.exec_module(WalabotAPI)
WalabotAPI.Init()
WalabotAPI.SetSettingsFolder()


def start_image_energy_service():
    WalabotAPI.ConnectAny()
    WalabotAPI.SetProfile(WalabotAPI.PROF_SHORT_RANGE_IMAGING)
    WalabotAPI.SetDynamicImageFilter(WalabotAPI.FILTER_TYPE_NONE)
    WalabotAPI.Start()
    filename = 'feed.json'
    while True:
        WalabotAPI.StartCalibration()
        WalabotAPI.Trigger()
        energy = WalabotAPI.GetImageEnergy()
        with open(filename, 'w') as outfile:
            json.dump({'energy': energy}, outfile)


if __name__ == '__main__':
    start_image_energy_service()
