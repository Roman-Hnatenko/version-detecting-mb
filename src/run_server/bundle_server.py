from subprocess import Popen


class BundleServer:
    def __init__(self, path: str, main_file: str):
        self.p = Popen(['node', 'src/server.js', path, main_file])

    def __enter__(self):
        return self.p

    def __exit__(self, type, value, traceback):
        self.p.terminate()
        self.p.wait()


if __name__ == '__main__':
    with BundleServer('/home/user/bandles/bandle1', 'slot.html'):
        print('Server started on localhost:3000')

    print('Local server shutdown')
