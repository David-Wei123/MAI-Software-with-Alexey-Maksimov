class TNE:
    def __init__(self):
        self.diesel_engine_status = 'off'
        self.power_status = 'stopped'
        self.robot_status = 'stopped'

    def set_diesel_engine_status(self, status):
        if status in ['on', 'on device', 'off', 'off device']:
            self.diesel_engine_status = 'on' if status.startswith('on') else 'off'
            print('The Diesel engine is now', 'running' if status.startswith('on') else 'stopped')
        else:
            print('Invalid command')

    def set_power_status(self, status):
        if status in ['on', 'on device', 'off', 'off device', 'check', 'check status']:
            if status.startswith('check'):
                print('The Power is currently', self.power_status)
            else:
                self.power_status = 'running' if status.startswith('on') else 'stopped'
                print('The Power is now', self.power_status)
        else:
            print('Invalid command')

    def set_robot_status(self, status):
        if status in ['forward', 'f', 'rotate', 'r', 'stop', 's']:
            self.robot_status = status if len(status) == 1 else 'forward' if status == 'f' else 'rotate' if status == 'r' else 'stop'
            print('The Robot is now', self.robot_status)
        else:
            print('Invalid command')

T = TNE()
operation = input("Please input the operation (choose from Diesel engine, Power switch, and Robot)\n").lower()
if operation in ['diesel engine', 'de']:
    status = input("Please input the status (choose from on device and off device)\n").lower()
    T.set_diesel_engine_status(status)
elif operation in ['power switch', 'ps']:
    status = input("Please input the status (choose from check status, on device, and off device)\n").lower()
    T.set_power_status(status)
elif operation in ['robot', 'r']:
    status = input("Please input the status (choose from forward, rotate, and stop)\n").lower()
    T.set_robot_status(status)
else:
    print('Invalid command')