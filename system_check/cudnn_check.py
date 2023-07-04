import tensorflow as tf

physical_devices = tf.config.list_physical_devices()
print("Available Physical Devices:")
for device in physical_devices:
    print(device)