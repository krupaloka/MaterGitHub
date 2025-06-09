import os
import platform

def get_uptime():
    if platform.system() == "Windows":
        # On Windows, use 'net stats srv' and parse the output
        import subprocess
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                return line
        return "Could not determine uptime."
    else:
        # On Unix/Linux/macOS systems, read /proc/uptime or use 'uptime' command
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = uptime_seconds // 3600
                minutes = (uptime_seconds % 3600) // 60
                return f"Uptime: {int(hours)} hours, {int(minutes)} minutes"
        except FileNotFoundError:
            # Fallback for systems without /proc/uptime
            import subprocess
            output = subprocess.check_output("uptime", shell=True, text=True)
            return output.strip()

if __name__ == "__main__":
    print(get_uptime())
