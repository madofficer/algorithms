import usb1


def list_usb_devices():
    with usb1.USBContext() as context:
        print(context.getDeviceList())
        for device in context.getDeviceList():
            print(f"Device {device.getVendorID():#04x}:{device.getProductID():#04x}")
            try:
                manufacturer = device.getManufacturer()
                product = device.getProduct()
                print(f"Manufacturer: {manufacturer}")
                print(f"Product: {product}")
            except usb1.USBError as e:
                print(f"Error usb reading: {e}")

            try:
                serial_number = device.getSerialNumber()
                print(f"Serial num: {serial_number}")
            except usb1.USBError as e:
                print(f"Serial num err: {e}")


if __name__ == "__main__":
    list_usb_devices()