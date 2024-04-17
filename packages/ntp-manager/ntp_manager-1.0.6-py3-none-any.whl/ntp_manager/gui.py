import webview
import platform
import fire
import subprocess
from webview.guilib import GUIType

os = platform.system()

class PythonAPI:
    window: webview.Window
    
    def run_cmd(self, cmd):
        res = subprocess.run(cmd, shell=True, capture_output=True)
        return res.stdout.decode('utf-8')
    
    def select_file(self, dialog_type=10, directory='', allow_multiple=False, save_filename='', file_types=()):
        return self.window.create_file_dialog(
            dialog_type=dialog_type, directory=directory, allow_multiple=allow_multiple, 
            save_filename=save_filename, file_types=file_types
        )
    
    def polygonize_ntp(
        self, ntp_path, um_per_pixel=0.65, bin_size=1, 
        verbose=False, ignore_regions=['region3','region4','mark4']
    ):
        from ntp_manager.pa import main as pa_main

        return pa_main(
            ntp_path, um_per_pixel=um_per_pixel, bin_size=bin_size, 
            verbose=verbose, ignore_regions=ignore_regions, return_bytes=True
        )

    def set_title(self, title: str):
        self.window.set_title(title)

    def exec(self, codes):
        return exec(codes, globals(), locals())
    
    def eval(self, codes):
        return eval(codes, globals(), locals())
    

def main(
    debug: bool = False,
    gui: GUIType | None = None,
    url = 'http://10.20.34.150:5173/'
):
    if debug:
        url = 'http://localhost:5173/'
    
    if gui is None:
        if os == 'Linux':
            gui = 'gtk'
        elif os == 'Windows':
            gui = None
        else:
            raise Exception('Unsupported OS')
    
    if debug:
        print(url, gui)

    api = PythonAPI()

    window = webview.create_window('ntp manager', url, js_api=api)
    api.window = window
    webview.start(debug=debug, gui=gui)

if __name__ == '__main__':
    fire.Fire(main)

