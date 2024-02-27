import serial
import time

# Replace '/dev/ttyS0' with the actual serial port your GSM module is connected to
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

def send_at_command(command, timeout=1):
    ser.write((command + '\r\n').encode())
    time.sleep(timeout)
    response = ser.read(ser.inWaiting()).decode()
    return response

def check_gsm_status():
    response = send_at_command('AT')
    return 'OK' in response

def check_network_registration():
    response = send_at_command('AT+CREG?')
    return '+CREG: 0,1' in response or '+CREG: 0,5' in response

try:
    # Check if the GSM module is ready
    if check_gsm_status():
        print('GSM module is ready.')

        # Check network registration status
        if check_network_registration():
            print('Connected to the GSM network.')
        else:
            print('Not registered on the GSM network. Check SIM card and signal strength.')

    else:
        print('Unable to communicate with the GSM module. Check connections and power.')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    ser.close()