class Command():
    def sshfs(self, server: str):
        print(f"SSHFS connect: {server}")

    def dir(self, directory: str):
        print(f"Open dir: {directory}")
