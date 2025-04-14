import os
import psutil
import schedule
import time
from datetime import datetime
import speedtest

LOG_FOLDER = "logs"


def bytes_to_mb(bytes_val):
    return round(bytes_val / (1024 * 1024), 2)


def perform_speedtest():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download()
        upload_speed = st.upload()
        ping = st.results.ping

        return {
            "download": round(download_speed / 1_000_000, 2),
            "upload": round(upload_speed / 1_000_000, 2),
            "ping": round(ping, 2)
        }

    except Exception as e:
        return {
            "error": f"Speedtest failed: {str(e)}"
        }


def generate_report(manual_mode=False):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    date_time_str = f"{date_str}_{time_str}"

    net_io = psutil.net_io_counters()
    mb_sent = bytes_to_mb(net_io.bytes_sent)
    mb_received = bytes_to_mb(net_io.bytes_recv)

    speedtest_result = perform_speedtest()

    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    file_name = f"{LOG_FOLDER}/report_{date_time_str}.txt"

    content = (
        f"📅 {'MANUAL' if manual_mode else 'AUTOMATIC'} Internet Report - {date_str} at {time_str}\n"
        f"{'='*60}\n"
        f"📶 NETWORK USAGE\n"
        f"  - MB Sent   : {mb_sent} MB\n"
        f"  - MB Received  : {mb_received} MB\n"
        f"  - Packets Sent : {net_io.packets_sent}\n"
        f"  - Packets Received: {net_io.packets_recv}\n"
        f"  - Input Errors: {net_io.errin}\n"
        f"  - Output Errors : {net_io.errout}\n"
        f"\n"
        f"🚀 SPEED TEST\n"
    )

    if "error" in speedtest_result:
        content += f"  - ❌ Error: {speedtest_result['error']}\n"
    else:
        content += (
            f"  - Download (↓): {speedtest_result['download']} Mbps\n"
            f"  - Upload   (↑): {speedtest_result['upload']} Mbps\n"
            f"  - Ping         : {speedtest_result['ping']} ms\n"
        )

    content += f"{'='*60}\n"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[✔] Report saved to: {file_name}")

    if manual_mode:
        print("\n" + content)


print("[📡] Monitoring network now...\n")
generate_report(manual_mode=True)

schedule.every().day.at("22:00").do(generate_report)

print("[🕒] Script running... A report will be generated every day at 22:00.\n")

while True:
    schedule.run_pending()
    time.sleep(30)
