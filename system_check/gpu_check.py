import tensorflow as tf

print(tf.__version__)

# Verify GPU availability
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Verify cuDNN usage
print("cuDNN Enabled:", tf.test.is_built_with_cuda() and tf.test.is_built_with_cudnn())
