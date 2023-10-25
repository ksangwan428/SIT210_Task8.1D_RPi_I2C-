# Import necessary libraries
import smbus  # Import the smbus library for I2C communication
import time   # Import the time library for sleep function

# Define BH1750 sensor constants
BH1750 = 0x23  # Set the I2C address for the BH1750 light sensor
CONTINUOUS_HIGH_RES_MODE_1 = 0x10  # Set the mode for continuous high-resolution measurements

# Initialize the SMBus (I2C) communication on bus 1
bus = smbus.SMBus(1)  # Initialize I2C communication on bus 1

# Function to read light intensity from the BH1750 sensor
def ReadBH1750(device_address):
    # Read data from I2C interface
    data = bus.read_i2c_block_data(device_address, CONTINUOUS_HIGH_RES_MODE_1)
    # Calculate light intensity in lux based on sensor data format and sensitivity
    result = (data[1] + (256 * data[0])) / 1.2
    return result

# Main program
try:
    # Continuous loop for monitoring light level
    while True:
        # Read light level from the BH1750 sensor
        LightLevel = ReadBH1750(BH1750)
        
        # Determine the light level category and print an appropriate message
        if LightLevel < 5:
            print("Too Dark")  # If light level is very low, it's considered "Too Dark"
        elif LightLevel < 10:
            print("Dark")  # If light level is low, it's considered "Dark"
        elif LightLevel < 20:
            print("Medium")  # If light level is moderate, it's "Medium"
        elif LightLevel < 25:
            print("Bright")  # If light level is high, it's "Bright"
        else:
            print("Too Bright")  # If light level is very high, it's "Too Bright"
        
        # Pause for 1 second before the next reading
        time.sleep(1)
                
except KeyboardInterrupt:
    # Handle keyboard interrupt by cleaning up GPIO 
    GPIO.cleanup()  # Clean up any resources or connections when the program is interrupted by the user

